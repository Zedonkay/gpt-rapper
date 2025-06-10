# GPT-Rapper 🎤

A fun Python application that generates rap lyrics using GPT-3.5 and converts them to speech using ElevenLabs' text-to-speech technology. The voice selection is dynamic and adapts to the content of your rap!

## Features

- 🤖 AI-powered rap generation using GPT-3.5
- 🎵 Dynamic voice selection based on the rap's content
- 🔊 High-quality text-to-speech conversion using ElevenLabs
- 💾 Saves generated raps as MP3 files
- 🎨 Beautiful command-line interface using Rich

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- ElevenLabs API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/gpt-rapper.git
cd gpt-rapper
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

## Usage

1. Run the script:
```bash
python gpt_rapper.py
```

2. Enter your prompt when asked. For example:
   - "rap about a young girl's dreams"
   - "rap about an old man's wisdom"
   - "rap about an energetic party"

3. The script will:
   - Generate rap lyrics based on your prompt
   - Select an appropriate voice based on the content
   - Convert the lyrics to speech
   - Save the audio file in the `raps` directory

4. To exit, type 'quit', 'exit', or 'q'

## Voice Selection

The application automatically selects voices based on the content of your prompt. It looks for keywords related to:
- Gender (female/male)
- Age (young/old)
- Energy level (energetic/calm)
- Style (professional/casual)

## License

MIT License - feel free to use this project for your own purposes!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 