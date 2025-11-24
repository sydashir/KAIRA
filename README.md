# KAIRA - Spanish/Latin Lyrics Generator 🎵

A powerful Streamlit application that generates authentic Spanish/Latin Pop and Urban lyrics using OpenAI's GPT-4. Perfect for creating reggaeton, dembow, trap latino, bachata urbana, and other Latin urban music genres.

## Features

- 🎤 **Multiple Genre Support**: Reggaeton, Dembow, Trap Latino, Bachata Urbana, Latin Pop, and more
- 🎭 **Customizable Parameters**: Control genre, type, vibe, energy, language, and slang density
- 🎼 **Flexible Structure**: Choose from predefined song structures or go freestyle
- 🗣️ **Phonetic Guidance**: Optional pronunciation help for difficult phrases
- 📊 **QA Logs**: Get insights into the creative decisions behind your lyrics
- 💾 **Export Options**: Download your lyrics as TXT or JSON files
- 🌍 **Multiple Spanish Dialects**: Support for various regional variations

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sydashir/KAIRA.git
cd KAIRA
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Generator

1. **Configure Your Lyrics** (in the sidebar):
   - **Genre**: Select from Reggaeton, Dembow, Trap Latino, etc.
   - **Type**: Choose the song type (Love Song, Party Anthem, etc.)
   - **Vibe**: Set the emotional tone (Romantic, Energetic, etc.)
   - **Energy**: Select energy level from Low (Chill) to High (Hype)
   - **Language**: Pick your preferred Spanish dialect or Spanglish
   - **Slang Density**: Adjust from 0 (formal) to 10 (heavy street slang)
   - **Structure**: Select your song structure
   - **Additional Elements**: 
     - Enable Chanteo for catchy repetitive hooks
     - Include Bridge section
     - Add Phonetics for pronunciation guidance
   - **Lyrics Part**: Generate complete song or specific sections
   - **Notes**: Add any additional requirements or themes

2. **Generate**: Click the "Generate Lyrics" button

3. **Review**: View your generated lyrics in three tabs:
   - **Lyrics**: The main lyrical content
   - **Phonetics**: Pronunciation guidance (if enabled)
   - **QA Log**: Creative insights and cultural references

4. **Download**: Save your lyrics as TXT or JSON format

## Project Structure

```
KAIRA/
├── app.py              # Main Streamlit application
├── openai_client.py    # OpenAI API integration
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Configuration Options

### Genres
- Reggaeton
- Dembow
- Trap Latino
- Bachata Urbana
- Latin Pop
- Cumbia Urbana
- Salsa Urbana
- Corridos Tumbados

### Song Types
- Love Song
- Party Anthem
- Heartbreak
- Success/Flex
- Storytelling
- Romantic
- Perreo
- Social Commentary

### Vibes
- Romantic, Energetic, Melancholic, Aggressive, Sensual, Playful, Dark, Uplifting, Chill

### Languages
- Spanish (Spain)
- Spanish (Latin America)
- Spanglish
- Regional variations (Caribbean, Mexico, South America)

## Modular Architecture

The application is built with modularity in mind:

- **`app.py`**: UI layer with Streamlit components
- **`openai_client.py`**: Handles all OpenAI API interactions
- **`utils.py`**: Contains utility functions for:
  - JSON payload building
  - Response parsing
  - Download formatting
  - System prompt management

## API Key Security

- Never commit your `.env` file
- Use environment variables for API keys
- The `.env.example` file is provided as a template

## Requirements

- streamlit>=1.28.0
- openai>=1.3.0
- python-dotenv>=1.0.0

## Troubleshooting

**Issue**: "OpenAI API key not found"
- **Solution**: Make sure you've created a `.env` file with your `OPENAI_API_KEY`

**Issue**: Generation takes too long
- **Solution**: Check your internet connection and OpenAI API status

**Issue**: Lyrics not culturally accurate
- **Solution**: Adjust the slang density, provide more specific notes, or try different genre combinations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

Built with ❤️ using Streamlit and OpenAI GPT-4
