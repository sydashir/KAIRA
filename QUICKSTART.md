# Quick Start Guide

Get started with KAIRA in 5 minutes! 🚀

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Set Up OpenAI API Key

1. Get your OpenAI API key from https://platform.openai.com/api-keys
2. Create a `.env` file:
   ```bash
   cp .env.example .env
   ```
3. Edit `.env` and add your API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

## Step 3: Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Step 4: Generate Your First Lyrics

### Simple Example - Party Reggaeton:

1. **Left Sidebar** - Configure your lyrics:
   - Genre: `Reggaeton`
   - Type: `Party Anthem`
   - Vibe: `Energetic`
   - Energy: `High (Hype)`
   - Language: `Spanish (Latin America)`
   - Slang Density: `7`
   - Leave other settings as default

2. **Optional**: Add notes:
   ```
   Need high-energy party vibes for summer
   ```

3. **Click** the red "🎤 Generate Lyrics" button

4. **View** your generated lyrics in the tabs:
   - 📝 Lyrics - Your generated content
   - 🗣️ Phonetics - Pronunciation guide
   - 📊 QA Log - Creative insights

5. **Download** your lyrics:
   - Click "Download as TXT" for plain text
   - Click "Download as JSON" for structured data

## What's Next?

- Check out [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) for more detailed examples
- Read the full [README.md](README.md) for all features
- Experiment with different configurations!

## Troubleshooting

**Problem**: "OpenAI API key not found"
- **Solution**: Make sure you created the `.env` file with your API key

**Problem**: Generation takes too long
- **Solution**: Check your internet connection and OpenAI API status

**Problem**: Lyrics don't match my expectations
- **Solution**: Be more specific in the "Additional Notes" field and adjust slang density

## Tips for Great Results

1. 🎯 **Be specific** - Add details in the Notes field
2. 🎚️ **Adjust slang** - Use slider to control language formality
3. 🎭 **Match energy to genre** - High energy for party tracks, lower for ballads
4. 🗣️ **Enable phonetics** - If you need pronunciation help
5. 🎵 **Start with chorus** - Generate the hook first, then build around it

Enjoy creating! 🎵
