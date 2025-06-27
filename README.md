# GPT-Rapper v2.0 🎤🎵

A revolutionary Python application that generates complete rap songs using GPT-3.5 and converts them to speech using ElevenLabs' text-to-speech technology. Now with **dynamic voice selection**, **background beats**, and **complete song structure**!

## ✨ New in v2.0

- 🎵 **Complete Song Generation**: Creates structured rap songs with intro, verses, chorus, and outro
- 🎤 **Dynamic Voice Selection**: AI-powered voice matching based on your prompt's content and mood
- 🎧 **Background Beats**: Automatically generates and mixes background music
- 🎚️ **Audio Mixing**: Professional-quality audio mixing with vocals and beats
- 🎨 **Smart Prompt Analysis**: Analyzes your prompt to determine style, mood, and musical characteristics
- 📊 **Progress Tracking**: Beautiful progress indicators for each generation step

## Features

- 🤖 **AI-powered rap generation** using GPT-3.5 with structured song format
- 🎵 **Dynamic voice selection** based on content analysis (gender, age, energy level)
- 🔊 **High-quality text-to-speech** conversion using ElevenLabs
- 🎧 **Background beat generation** and audio mixing
- 💾 **Saves generated songs** as MP3 files in organized folders
- 🎨 **Beautiful command-line interface** using Rich
- 🎚️ **Professional audio processing** with pydub and ffmpeg

## Prerequisites

- Python 3.8 or higher (Python 3.12 recommended)
- OpenAI API key
- ElevenLabs API key
- ffmpeg (automatically installed via Homebrew on macOS)

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Zedonkay/gpt-rapper.git
cd gpt-rapper
```

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up your API keys:**
Create a `.env` file in the project root:
```env
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# ElevenLabs API Key
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

## Usage

1. **Activate your virtual environment:**
```bash
source venv/bin/activate
```

2. **Run the application:**
```bash
python3 gpt_rapper.py
```

3. **Enter your prompt:**
The AI will analyze your prompt and create a complete rap song with:
- Appropriate voice selection based on content
- Background beats matching the mood
- Structured song format (intro, verses, chorus, outro)
- Professional audio mixing

## Example Prompts

- **"A motivational rap about achieving your dreams"**
- **"A dark and intense rap about overcoming challenges"**
- **"A fun and energetic rap about partying with friends"**
- **"A smooth and laid-back rap about love and relationships"**
- **"An aggressive rap about competition and success"**

## How It Works

### 1. **Prompt Analysis**
The AI analyzes your prompt to determine:
- Rap style and mood
- Voice characteristics (gender, age, energy)
- Musical tempo and style
- Content themes and emotions

### 2. **Song Generation**
Creates a complete rap song with:
- **Intro** (2-4 lines): Sets the mood and introduces the theme
- **Verse 1** (8-12 lines): Develops the main story or message
- **Chorus** (4-6 lines): Catchy, memorable hook
- **Verse 2** (8-12 lines): Continues or contrasts with verse 1
- **Outro** (2-4 lines): Wraps up the song

### 3. **Voice Selection**
Intelligently selects the best voice based on:
- **Gender matching**: Male/female voices based on content
- **Age appropriateness**: Young/adult/elderly voices
- **Energy level**: Low/medium/high energy voices
- **Style compatibility**: Voice characteristics that match the rap style

### 4. **Audio Generation**
- Generates vocals using ElevenLabs TTS
- Creates background beats using AI music generation
- Mixes vocals and beats professionally
- Applies audio effects and mastering

## File Structure

```
gpt-rapper/
├── gpt_rapper.py          # Main application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .env                  # API keys (create this)
├── .gitignore           # Git ignore rules
└── raps/                # Generated songs (auto-created)
    ├── rap_2024_01_15_14_30_22.mp3
    ├── rap_2024_01_15_14_35_45.mp3
    └── ...
```

## API Keys Setup

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Go to API keys section
4. Create a new API key
5. Add to your `.env` file

### ElevenLabs API Key
1. Visit [ElevenLabs](https://elevenlabs.io/)
2. Sign up or log in
3. Go to your profile settings
4. Find your API key
5. Add to your `.env` file

## Dependencies

- **openai**: GPT-3.5 integration for rap generation
- **elevenlabs**: High-quality text-to-speech conversion
- **pydub**: Audio processing and mixing
- **rich**: Beautiful command-line interface
- **python-dotenv**: Environment variable management
- **requests**: HTTP requests for API calls
- **numpy**: Numerical operations for audio processing
- **ffmpeg-python**: Audio format conversion

## Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'pydub'"**
   - Make sure you're using Python 3.12 or lower
   - Reinstall the virtual environment: `rm -rf venv && python3.12 -m venv venv`

2. **"ffmpeg not found"**
   - On macOS: `brew install ffmpeg`
   - On Ubuntu: `sudo apt install ffmpeg`
   - On Windows: Download from [ffmpeg.org](https://ffmpeg.org/)

3. **API Key Errors**
   - Check your `.env` file exists and has correct API keys
   - Verify your API keys are valid and have sufficient credits

4. **Audio Generation Fails**
   - Check your ElevenLabs API key and credits
   - Ensure you have a stable internet connection

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **OpenAI** for GPT-3.5 API
- **ElevenLabs** for high-quality text-to-speech
- **Rich** for beautiful terminal interfaces
- **pydub** for audio processing capabilities

---

**🎤 Ready to create your next hit? Run `python3 gpt_rapper.py` and let the AI do the rest! 🎵** 