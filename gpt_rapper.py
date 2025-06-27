import os
import json
import time
import random
from typing import Dict, List, Tuple
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from elevenlabs.client import ElevenLabs
from elevenlabs import save
import requests
from pydub import AudioSegment
from pydub.effects import speedup

# Load environment variables
load_dotenv()

# Initialize clients
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
el_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Initialize Rich console for pretty output
console = Console()

class RapSongGenerator:
    def __init__(self):
        self.console = Console()
        
    def analyze_prompt(self, prompt: str) -> Dict:
        """Analyze prompt to determine rap style, mood, and musical characteristics."""
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": """You are a music analysis expert. Analyze the given prompt and return a JSON object with the following structure:
                    {
                        "style": "trap/boom-bap/conscious/party/emotional",
                        "mood": "aggressive/calm/energetic/melancholic/confident",
                        "tempo": "slow/medium/fast",
                        "voice_gender": "male/female/any",
                        "voice_age": "young/adult/elderly/any",
                        "voice_energy": "low/medium/high",
                        "beat_style": "trap/boom-bap/jazz/synth/rock",
                        "key_emotions": ["emotion1", "emotion2"],
                        "themes": ["theme1", "theme2"]
                    }
                    Be specific and creative in your analysis."""},
                    {"role": "user", "content": f"Analyze this rap prompt: {prompt}"}
                ],
                temperature=0.7,
                max_tokens=300
            )
            
            analysis = json.loads(response.choices[0].message.content)
            return analysis
        except Exception as e:
            self.console.print(f"[bold red]Error analyzing prompt: {str(e)}[/bold red]")
            # Return default analysis
            return {
                "style": "conscious",
                "mood": "confident",
                "tempo": "medium",
                "voice_gender": "any",
                "voice_age": "any",
                "voice_energy": "medium",
                "beat_style": "boom-bap",
                "key_emotions": ["confident"],
                "themes": ["life"]
            }

    def generate_rap_lyrics(self, prompt: str, analysis: Dict) -> str:
        """Generate structured rap lyrics based on prompt and analysis."""
        try:
            style_instructions = {
                "trap": "Use trap-style lyrics with heavy bass references, money, success themes, and repetitive hooks",
                "boom-bap": "Use boom-bap style with conscious lyrics, social commentary, and complex wordplay",
                "conscious": "Focus on deep, meaningful lyrics with social awareness and personal growth",
                "party": "Create upbeat, fun lyrics perfect for parties and celebrations",
                "emotional": "Write emotional, heartfelt lyrics with personal stories and feelings"
            }
            
            style_guide = style_instructions.get(analysis["style"], "Write engaging rap lyrics")
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"""You are a talented rapper. Create a structured rap song with:
                    - Intro (2-4 lines)
                    - Verse 1 (8-12 lines)
                    - Chorus (4-6 lines)
                    - Verse 2 (8-12 lines)
                    - Outro (2-4 lines)
                    
                    Style: {style_guide}
                    Mood: {analysis['mood']}
                    Themes: {', '.join(analysis['themes'])}
                    
                    Make it rhyme well, maintain good flow, and keep it engaging. Format with clear section markers."""},
                    {"role": "user", "content": f"Write a rap about: {prompt}"}
                ],
                temperature=0.8,
                max_tokens=500
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating rap: {str(e)}"

    def select_voice(self, analysis: Dict) -> str:
        """Select the most appropriate voice based on analysis."""
        try:
            voices = el_client.voices.search()
            
            # Voice selection criteria based on analysis
            criteria = {
                "gender": analysis.get("voice_gender", "any"),
                "age": analysis.get("voice_age", "any"),
                "energy": analysis.get("voice_energy", "medium")
            }
            
            # Score each voice based on criteria
            voice_scores = []
            for voice in voices.voices:
                score = 0
                voice_name = voice.name.lower()
                voice_desc = (voice.description or "").lower()
                
                # Gender matching
                if criteria["gender"] != "any":
                    if criteria["gender"] == "male" and any(word in voice_name for word in ["male", "man", "guy", "dude"]):
                        score += 3
                    elif criteria["gender"] == "female" and any(word in voice_name for word in ["female", "woman", "girl", "lady"]):
                        score += 3
                
                # Age matching
                if criteria["age"] != "any":
                    if criteria["age"] == "young" and any(word in voice_name for word in ["young", "teen", "kid"]):
                        score += 2
                    elif criteria["age"] == "elderly" and any(word in voice_name for word in ["old", "elder", "senior"]):
                        score += 2
                
                # Energy matching
                if criteria["energy"] == "high" and any(word in voice_name for word in ["energetic", "powerful", "dynamic"]):
                    score += 2
                elif criteria["energy"] == "low" and any(word in voice_name for word in ["calm", "gentle", "soft"]):
                    score += 2
                
                voice_scores.append((voice.voice_id, score))
            
            # Return voice with highest score, or default
            if voice_scores:
                best_voice = max(voice_scores, key=lambda x: x[1])
                if best_voice[1] > 0:
                    return best_voice[0]
            
            return "EXAVITQu4vr4xnSDxMaL"  # Default voice
            
        except Exception as e:
            self.console.print(f"[bold yellow]Warning: Could not select voice: {str(e)}[/bold yellow]")
            return "EXAVITQu4vr4xnSDxMaL"

    def generate_background_beat(self, analysis: Dict, output_file: str) -> bool:
        """Generate a background beat using a music generation API."""
        try:
            # For now, we'll create a simple beat using pydub
            # In a real implementation, you'd use a music generation API like Mubert, AIVA, or similar
            
            # Create a simple drum pattern
            sample_rate = 44100
            duration = 3000  # 3 seconds
            
            # Create kick drum
            kick = AudioSegment.silent(duration=100)
            kick = kick + 20  # Add some volume
            
            # Create snare
            snare = AudioSegment.silent(duration=100)
            snare = snare + 15
            
            # Create hi-hat
            hihat = AudioSegment.silent(duration=50)
            hihat = hihat + 10
            
            # Build the beat pattern
            beat = AudioSegment.empty()
            
            # 4/4 time signature
            for i in range(8):  # 8 beats
                # Kick on 1 and 3
                if i % 2 == 0:
                    beat += kick
                else:
                    beat += AudioSegment.silent(duration=100)
                
                # Snare on 2 and 4
                if i % 2 == 1:
                    beat += snare
                else:
                    beat += AudioSegment.silent(duration=100)
                
                # Hi-hats on every beat
                beat += hihat + hihat
            
            # Loop the beat to match the rap duration
            final_beat = beat * 10  # Repeat 10 times for ~30 seconds
            
            # Adjust tempo based on analysis
            if analysis["tempo"] == "fast":
                final_beat = speedup(final_beat, playback_speed=1.2)
            elif analysis["tempo"] == "slow":
                final_beat = speedup(final_beat, playback_speed=0.8)
            
            final_beat.export(output_file, format="mp3")
            return True
            
        except Exception as e:
            self.console.print(f"[bold red]Error generating beat: {str(e)}[/bold red]")
            return False

    def generate_vocals(self, lyrics: str, voice_id: str, output_file: str) -> bool:
        """Generate vocals from lyrics using ElevenLabs."""
        try:
            audio = el_client.text_to_speech.convert(
                text=lyrics,
                voice_id=voice_id,
                model_id="eleven_monolingual_v1",
                output_format="mp3_44100_128"
            )
            save(audio, output_file)
            return True
        except Exception as e:
            self.console.print(f"[bold red]Error generating vocals: {str(e)}[/bold red]")
            return False

    def mix_audio(self, vocals_file: str, beat_file: str, output_file: str) -> bool:
        """Mix vocals with background beat."""
        try:
            # Load audio files
            vocals = AudioSegment.from_mp3(vocals_file)
            beat = AudioSegment.from_mp3(beat_file)
            
            # Extend beat if it's shorter than vocals
            if len(beat) < len(vocals):
                beat = beat * (len(vocals) // len(beat) + 1)
            
            # Trim beat to match vocals length
            beat = beat[:len(vocals)]
            
            # Adjust volumes
            vocals = vocals + 5  # Increase vocals volume
            beat = beat - 10     # Lower beat volume
            
            # Mix the tracks
            mixed = vocals.overlay(beat)
            
            # Export final mix
            mixed.export(output_file, format="mp3")
            return True
            
        except Exception as e:
            self.console.print(f"[bold red]Error mixing audio: {str(e)}[/bold red]")
            return False

    def create_rap_song(self, prompt: str) -> Tuple[str, str]:
        """Create a complete rap song from prompt."""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:
            
            # Step 1: Analyze prompt
            task1 = progress.add_task("Analyzing prompt...", total=None)
            analysis = self.analyze_prompt(prompt)
            progress.update(task1, description="✅ Prompt analyzed")
            
            # Step 2: Generate lyrics
            task2 = progress.add_task("Generating rap lyrics...", total=None)
            lyrics = self.generate_rap_lyrics(prompt, analysis)
            progress.update(task2, description="✅ Lyrics generated")
            
            # Step 3: Select voice
            task3 = progress.add_task("Selecting voice...", total=None)
            voice_id = self.select_voice(analysis)
            progress.update(task3, description="✅ Voice selected")
            
            # Step 4: Generate background beat
            task4 = progress.add_task("Creating background beat...", total=None)
            timestamp = int(time.time())
            beat_file = f"raps/beat_{timestamp}.mp3"
            beat_success = self.generate_background_beat(analysis, beat_file)
            progress.update(task4, description="✅ Background beat created" if beat_success else "⚠️ Beat creation failed")
            
            # Step 5: Generate vocals
            task5 = progress.add_task("Generating vocals...", total=None)
            vocals_file = f"raps/vocals_{timestamp}.mp3"
            vocals_success = self.generate_vocals(lyrics, voice_id, vocals_file)
            progress.update(task5, description="✅ Vocals generated" if vocals_success else "⚠️ Vocals generation failed")
            
            # Step 6: Mix audio
            task6 = progress.add_task("Mixing audio...", total=None)
            final_file = f"raps/rap_song_{timestamp}.mp3"
            mix_success = False
            
            if beat_success and vocals_success:
                mix_success = self.mix_audio(vocals_file, beat_file, final_file)
                progress.update(task6, description="✅ Audio mixed" if mix_success else "⚠️ Mixing failed")
            else:
                progress.update(task6, description="⚠️ Skipped mixing - missing components")
            
            # Clean up temporary files
            try:
                if os.path.exists(beat_file):
                    os.remove(beat_file)
                if os.path.exists(vocals_file):
                    os.remove(vocals_file)
            except:
                pass
            
            return lyrics, final_file if mix_success else vocals_file

def main():
    console.print(Panel.fit(
        "[bold magenta]🎤 Welcome to GPT-Rapper! 🎤[/bold magenta]\n"
        "I'll create complete rap songs with beats and vocals just for you!",
        title="GPT-Rapper v2.0",
        border_style="magenta"
    ))

    # Create output directory
    os.makedirs("raps", exist_ok=True)
    
    generator = RapSongGenerator()

    while True:
        prompt = Prompt.ask("\n[bold cyan]What would you like me to rap about?[/bold cyan]")
        
        if prompt.lower() in ['quit', 'exit', 'q']:
            console.print("\n[bold yellow]Thanks for jamming with GPT-Rapper! Peace out! ✌️[/bold yellow]")
            break

        try:
            lyrics, audio_file = generator.create_rap_song(prompt)
            
            console.print(Panel(
                lyrics,
                title="[bold magenta]Your Rap Lyrics[/bold magenta]",
                border_style="green"
            ))

            console.print(f"\n[bold green]🎵 Complete rap song saved to: {audio_file}[/bold green]")
            
        except Exception as e:
            console.print(f"\n[bold red]Error creating rap song: {str(e)}[/bold red]")

if __name__ == "__main__":
    main() 