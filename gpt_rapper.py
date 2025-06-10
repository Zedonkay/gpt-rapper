import os
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from elevenlabs.client import ElevenLabs
from elevenlabs import save
import time

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize ElevenLabs client
el_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Initialize Rich console for pretty output
console = Console()

def select_voice(prompt: str) -> str:
    """Select an appropriate voice based on the prompt."""
    try:
        # Get all available voices
        voices = el_client.voices.search()
        
        # Default voice ID (Antoni) in case we can't find a better match
        default_voice_id = "EXAVITQu4vr4xnSDxMaL"
        
        # Keywords that might indicate the type of voice needed
        voice_keywords = {
            "female": ["woman", "girl", "female", "lady", "sister"],
            "male": ["man", "boy", "male", "guy", "brother"],
            "young": ["young", "teen", "kid", "child", "youth"],
            "old": ["old", "elder", "senior", "aged", "veteran"],
            "energetic": ["energetic", "excited", "lively", "dynamic", "powerful"],
            "calm": ["calm", "peaceful", "gentle", "soft", "smooth"],
            "professional": ["professional", "business", "formal", "corporate", "official"]
        }
        
        # Analyze prompt for voice characteristics
        prompt_lower = prompt.lower()
        voice_characteristics = []
        
        for category, keywords in voice_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                voice_characteristics.append(category)
        
        # If no specific characteristics found, return default voice
        if not voice_characteristics:
            return default_voice_id
        
        # Search for voices matching the characteristics
        for voice in voices.voices:
            voice_name = voice.name.lower()
            voice_description = (voice.description or "").lower()
            
            # Check if voice matches any of the characteristics
            if any(char in voice_name or char in voice_description for char in voice_characteristics):
                return voice.voice_id
        
        return default_voice_id
    except Exception as e:
        console.print(f"[bold yellow]Warning: Could not select voice based on prompt: {str(e)}[/bold yellow]")
        return "EXAVITQu4vr4xnSDxMaL"  # Return default voice on error

def generate_rap(prompt: str) -> str:
    """Generate rap lyrics using OpenAI's GPT model."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a talented rapper. 
                Generate creative and engaging rap lyrics based on the given prompt.
                Make it rhyme and maintain a good flow. Keep it clean and family-friendly.
                Format the output with line breaks for better readability.
                Keep the rap relatively short (4-8 lines) for better audio generation."""},
                {"role": "user", "content": f"Write a rap about: {prompt}"}
            ],
            temperature=0.8,
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating rap: {str(e)}"

def generate_audio(text: str, prompt: str, output_file: str) -> bool:
    """Generate audio from text using ElevenLabs."""
    try:
        # Select appropriate voice based on the prompt
        voice_id = select_voice(prompt)
        
        audio = el_client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id="eleven_monolingual_v1",
            output_format="mp3_44100_128"
        )
        save(audio, output_file)
        return True
    except Exception as e:
        console.print(f"[bold red]Error generating audio: {str(e)}[/bold red]")
        return False

def main():
    console.print(Panel.fit(
        "[bold magenta]🎤 Welcome to GPT-Rapper! 🎤[/bold magenta]\n"
        "I'll generate some fresh rhymes and turn them into audio for you!",
        title="GPT-Rapper",
        border_style="magenta"
    ))

    # Create output directory if it doesn't exist
    os.makedirs("raps", exist_ok=True)

    while True:
        prompt = Prompt.ask("\n[bold cyan]What would you like me to rap about?[/bold cyan]")
        
        if prompt.lower() in ['quit', 'exit', 'q']:
            console.print("\n[bold yellow]Thanks for jamming with GPT-Rapper! Peace out! ✌️[/bold yellow]")
            break

        console.print("\n[bold green]Generating your rap...[/bold green]")
        rap = generate_rap(prompt)
        
        console.print(Panel(
            rap,
            title="[bold magenta]Your Rap[/bold magenta]",
            border_style="green"
        ))

        # Generate audio
        console.print("\n[bold green]Converting to audio...[/bold green]")
        timestamp = int(time.time())
        output_file = f"raps/rap_{timestamp}.mp3"
        
        if generate_audio(rap, prompt, output_file):
            console.print(f"\n[bold green]🎵 Audio saved to: {output_file}[/bold green]")
        else:
            console.print("\n[bold red]Failed to generate audio. Please check your ElevenLabs API key.[/bold red]")

if __name__ == "__main__":
    main() 