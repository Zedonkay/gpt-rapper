# GPT-Rapper Quick Start Guide 🚀

Get up and running with GPT-Rapper v2.0 in under 5 minutes!

## Prerequisites

- Python 3.8+ (3.12 recommended)
- OpenAI API key
- ElevenLabs API key

## ⚡ Quick Setup (5 minutes)

### 1. Clone and Setup
```bash
git clone https://github.com/Zedonkay/gpt-rapper.git
cd gpt-rapper
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Install ffmpeg (macOS)
```bash
brew install ffmpeg
```

### 3. Add API Keys
Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

### 4. Run!
```bash
python3 gpt_rapper.py
```

## 🎤 Your First Rap

1. **Enter a prompt** like:
   - "A motivational rap about achieving your dreams"
   - "A fun party rap about dancing"
   - "A dark rap about overcoming challenges"

2. **Wait for generation** (about 30-60 seconds)

3. **Find your song** in the `raps/` folder!

## 🎵 What You'll Get

- **Complete song structure** (intro, verses, chorus, outro)
- **Professional voice** selected based on your content
- **Background beats** matching the mood
- **High-quality MP3** ready to play

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'pydub'"
```bash
rm -rf venv
python3.12 -m venv venv  # Use Python 3.12
source venv/bin/activate
pip install -r requirements.txt
```

### "ffmpeg not found"
```bash
# macOS
brew install ffmpeg

# Ubuntu
sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/
```

### API Key Errors
- Check your `.env` file exists
- Verify API keys are correct
- Ensure you have credits in your accounts

## 🎯 Example Prompts

| Style | Prompt Example |
|-------|----------------|
| **Motivational** | "A powerful rap about never giving up on your dreams" |
| **Party** | "An energetic rap about dancing all night long" |
| **Dark** | "A intense rap about overcoming life's toughest challenges" |
| **Love** | "A smooth rap about finding true love" |
| **Success** | "A confident rap about achieving greatness" |

## 📁 File Structure
```
gpt-rapper/
├── gpt_rapper.py      # Main app
├── requirements.txt   # Dependencies
├── .env              # Your API keys
└── raps/             # Generated songs
    └── rap_*.mp3     # Your rap files
```

## 🚀 Advanced Usage

### Custom Voice Selection
The AI automatically selects voices based on your prompt, but you can influence it:
- Use words like "female", "male", "young", "old", "energetic", "calm"
- Example: "A young female rapper singing about empowerment"

### Batch Generation
Run the script multiple times to create different versions:
```bash
python3 gpt_rapper.py  # First song
python3 gpt_rapper.py  # Second song
# Each creates a unique file with timestamp
```

## 🎧 Audio Quality

- **Format**: MP3 (320kbps)
- **Duration**: 1-3 minutes typically
- **Quality**: Professional-grade mixing
- **Compatibility**: Works with all music players

## 💡 Tips

1. **Be specific** in your prompts for better results
2. **Experiment** with different styles and moods
3. **Check the raps folder** for all your generated songs
4. **Use descriptive words** to influence voice selection
5. **Keep prompts under 100 words** for optimal results

## 🆘 Need Help?

- Check the [full README](README.md) for detailed documentation
- Review the [CHANGELOG](CHANGELOG.md) for version updates
- Open an issue on GitHub for bugs or feature requests

---

**🎤 Ready to create your first hit? Run `python3 gpt_rapper.py` and let the AI do the rest! 🎵** 