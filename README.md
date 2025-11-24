# KAIRA 2025 — MAINSTREAM Songwriting Assistant 🎧

## Professional Bilingual Lyrics Generator for Latin Pop & Urban Music

KAIRA MAINSTREAM is a state-of-the-art songwriting assistant powered by GPT-4+ that generates authentic, singable, emotionally believable lyrics for Latin Pop and Urban music genres (Reggaeton, Latin Trap, Bachata Urbana, and more).

Based on the KAIRA DNA specifications, this system writes like a real human songwriter from the 2017-2025 post-Despacito era.

---

## 🎯 What Makes KAIRA Different

- **Not a Chatbot**: A professional songwriting system, not a generic text generator
- **MAINSTREAM Persona**: Hybrid voice blending global pop melody, urban groove, and natural Latin songwriter tone
- **Phonetic Rhythm**: Follows Spanish sung phonetics (sinalefa, stressed vowels, natural breath patterns)
- **Visual Storytelling**: Creates movie-like scenes in words, not abstract poetry
- **Cultural Authenticity**: Modern Spanish with subtle, credible 2025 Gen-Z slang
- **Revision Stable**: Maintains rhythm, tone, and structure through multiple edits

---

## ✨ Features

### 🎼 Comprehensive Configuration

- **13 Genres**: Latin Pop, Reggaeton, Latin Trap, Urban, Afro-Latin, Pop Balada, Cumbia Urbana, Bachata Urbana, Dembow, Corridos Tumbados, Salsa Urbana, Perreo, Tropical Pop
- **12 Song Types**: Romantic, Heartbreak, Party, Empowerment, Seduction, Nostalgia, Storytelling, Social Commentary, Success/Flex, Perreo, Love Song, Party Anthem
- **15 Vibes**: Warm, Dark, Cinematic, Intimate, Energetic, Sensual, Melancholic, Hopeful, Playful, Aggressive, Uplifting, Chill, Mysterious, Confident, Dreamy
- **5 Energy Levels**: Low, Medium-Low, Medium, Medium-High, High
- **3 Languages**: Spanish, English, Spanglish
- **Slang Density Control**: Low (0-3), Medium (4-6), High (7-10)

### 🎤 Singer Profile

- Gender specification
- Nationality for regional flavor
- Vocal style preferences

### 🎵 Structure Templates

- **Mainstream Default** (KAIRA DNA): `[verse 1] → [chorus] → [verse 2] → [pre-chorus] → [chorus]`
- Classic Pop, Urban Simple, Trap Flow, Bachata Classic, Reggaeton Party
- Ballad, Freestyle, and Custom structures

### 📏 Line Count Specifications

Based on KAIRA DNA:
- **Verse**: 8 lines (conversational, cinematic tone)
- **Pre-Chorus**: 4 lines (builds tension)
- **Chorus**: 8 lines (4+4 hook+echo pattern)
- **Chanteo**: 8, 12, or 16 lines (flow-driven rhythmic phrasing)
- **Bridge**: 4-6 lines (emotional twist, only when requested)

### 🗣️ Phonetic Support

- Detailed phonetic breakdowns for difficult phrases
- Sinalefa markings (vowel fusion: "te hablo" → "tea-blo")
- Stress pattern explanations
- Rhythm notes for natural singing

### 📊 Quality Assurance

- **QA Log**: Explains creative choices, cultural references, slang usage
- **Metadata**: Structure validation, line counts, estimated duration
- **Error Handling**: Automatic retry with correction prompts

### 💾 Export Options

- **TXT Format**: Clean, readable format for studio sessions
- **JSON Format**: Complete structured data with metadata

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/kaira.git
   cd kaira
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements_new.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

4. **Run the application**:
   ```bash
   streamlit run app_new.py
   ```

The app will open in your browser at `http://localhost:8501`

---

## 📖 How to Use

### Basic Workflow

1. **Select AI Model**: Choose GPT-4o (recommended), GPT-4o-mini, or GPT-4-turbo

2. **Configure Core Parameters**:
   - Genre: Latin Pop, Reggaeton, etc.
   - Type: Romantic, Heartbreak, Party, etc.
   - Vibe: Warm, Dark, Energetic, etc.
   - Energy Level: Low to High
   - Language: Spanish, English, or Spanglish
   - Slang Density: How much street slang to use

3. **Add Singer Profile** (Optional):
   - Gender, nationality, vocal style
   - Helps tailor lyrics to specific artists

4. **Choose Structure**:
   - Use Mainstream Default or select a preset
   - Enable Chanteo for flow-driven sections
   - Enable Bridge for emotional twist
   - Enable Phonetics for pronunciation help

5. **Provide Creative Direction**:
   - Notes: Scenes, themes, emotions, requirements
   - Keywords: Words to include in lyrics
   - Forbidden Words: Words to avoid

6. **Generate**:
   - Click "Generate Lyrics"
   - Review in tabs: Lyrics, Phonetics, QA Log, Metadata
   - Download as TXT or JSON

### Example Configuration

**Romantic Reggaeton Ballad:**
```
Genre: Reggaeton
Type: Romantic
Vibe: Sensual
Energy: Medium
Language: Spanish
Slang: Medium
Singer: Female, Colombian
Notes: "Beach sunset, bittersweet memories, visual scenes"
Keywords: playa, recuerdo, mirada
```

---

## 🎧 KAIRA DNA Principles

### Fixed Structure (Default)

```
[verse 1] → [chorus] → [verse 2 / chanteo] → [pre-chorus] → [chorus]
```

**Never starts with pre-chorus.** This structure is optimized for Latin Pop/Urban radio play.

### Phonetic Rhythm Rules

- **Count by sound, not spelling**: Spanish vowels fuse (sinalefa)
- **Stressed vowels extend**: Words ending in "-é", "-ó" count as full beats
- **Strong beats**: Fall on meaning words (verbs/nouns), not fillers
- **Natural breathing**: Every 1-2 lines, like real singing
- **Groove over math**: Rhythmic contrast matters more than exact syllable counts

### Language Style

- **Conversational Spanish**: Spoken-but-singable, 2025 Gen-Z tone
- **Visual imagery**: Real-world objects (car, club, phone, skin, night)
- **Honest emotion**: Desire, nostalgia, guilt, empowerment — never melodrama
- **Precision slang**: Max 1-2 slang marks per block, always credible
- **Repetition allowed**: For rhythm or emotional echo

### Revision Protocol

When editing, KAIRA preserves:
- Original rhythm and flow
- Tone & lexical field (same word family)
- Structure (same order/line count)
- Persona (Mainstream voice)

Allowed: Tighten imagery, improve pacing, swap lines
Not allowed: Reset tone, rewrite from scratch, flatten rhythm

---

## 🗂️ Project Structure

```
kaira/
├── app_new.py                  # Enhanced Streamlit application
├── config/
│   ├── genres.py              # Genre definitions
│   ├── types.py               # Song types
│   ├── vibes.py               # Vibe options
│   └── structures.py          # Song structure templates
├── core/
│   ├── gpt_client.py          # GPT API integration
│   ├── prompt_builder.py      # Prompt templating
│   ├── response_parser.py     # Response parsing
│   └── validator.py           # Validation logic
├── utils/
│   ├── formatters.py          # TXT/JSON formatting
│   └── helpers.py             # Helper functions
├── data/
│   ├── KAIRA 2025 FULL DNA.txt
│   └── KAIRA 2025 RESUMED DNA.txt
├── .env                       # Environment variables
├── requirements_new.txt       # Python dependencies
└── README_NEW.md             # This file
```

---

## 🤖 Supported AI Models

### Current

- **GPT-4o** (Recommended): Latest multimodal model, excellent creative writing
- **GPT-4o-mini**: Faster, more affordable, good for experimentation
- **GPT-4-turbo**: High-quality, reliable generation
- **GPT-4**: Original GPT-4, stable and tested

### Future

- Automatic support for GPT-5+ when released
- Code is model-agnostic and forward-compatible

---

## ⚙️ Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
DEFAULT_MODEL=gpt-4o
DEFAULT_TEMPERATURE=0.8
DEFAULT_MAX_TOKENS=2500
```

---

## 💡 Tips for Best Results

### Genre-Specific

- **Reggaeton/Dembow**: High energy, Medium-High slang, Spanglish friendly
- **Bachata Urbana**: Medium energy, Medium-Low slang, romantic vibes
- **Latin Trap**: Medium-High energy, High slang, aggressive/dark vibes
- **Latin Pop**: Medium energy, Low slang, warm/hopeful vibes

### Notes Field Best Practices

**Good:**
```
Visual scenes, beach sunset, red dress flowing in wind,
nostalgic but not sad, subtle desire, Caribbean vibes
```

**Avoid:**
```
Make it good and emotional
```

### Slang Density Guide

- **Low (0-3)**: Formal, mainstream radio-friendly
- **Medium (4-6)**: Balanced, authentic but accessible
- **High (7-10)**: Heavy street slang, underground feel

### Model Selection

- **GPT-4o**: Production-ready lyrics, best quality
- **GPT-4o-mini**: Rapid iteration, testing ideas
- **GPT-4-turbo**: Balanced quality and speed

---

## 📊 Output Format

### JSON Structure

```json
{
  "lyrics": {
    "verse_1": "...",
    "chorus": "...",
    "verse_2": "...",
    "pre_chorus": "...",
    "chorus_repeat": "..."
  },
  "phonetics": {
    "difficult_phrases": [
      {
        "phrase": "te apetece a ti",
        "phonetic": "tea-pe-té-sea-tí",
        "note": "Sinalefa between 'te' and 'apetece'"
      }
    ],
    "rhythm_notes": "..."
  },
  "qa_log": {
    "creative_choices": "...",
    "cultural_references": "...",
    "slang_used": ["na'", "taba", "free"]
  },
  "metadata": {
    "total_lines": 32,
    "structure": "...",
    "model_used": "gpt-4o"
  }
}
```

---

## 🛠️ Troubleshooting

**Issue**: "OpenAI API key not found"
- **Solution**: Create `.env` file with `OPENAI_API_KEY=your_key`

**Issue**: Generation timeout
- **Solution**: Switch to GPT-4o-mini for faster responses

**Issue**: Lyrics don't match expected quality
- **Solution**: 
  - Be more specific in Notes field
  - Adjust slang density
  - Try different model (GPT-4o recommended)
  - Add keywords for specific vocabulary

**Issue**: JSON parsing error
- **Solution**: Automatic retry enabled; if persistent, check API status

---

## 🎓 Learn More

### KAIRA DNA Documents

- `data/KAIRA 2025 FULL DNA.txt`: Complete specifications
- `data/KAIRA 2025 RESUMED DNA.txt`: Quick reference

### Key Concepts

- **Sinalefa**: Vowel fusion in Spanish singing
- **Hook + Echo**: 4+4 chorus pattern
- **Phonetic Rhythm**: Sound-based beats, not syllable math
- **Visual Storytelling**: Scenes over abstractions
- **Revision Stability**: Same voice through edits

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Test thoroughly
4. Submit a pull request

---

## 📄 License

MIT License - See LICENSE file

---

## 🙏 Acknowledgments

- Based on KAIRA DNA specifications
- Powered by OpenAI GPT-4+
- Built with Streamlit

---

## 📧 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check existing documentation
- Review KAIRA DNA files

---

## 🎵 Example Use Cases

### Songwriters
1. Generate chorus first to establish hook
2. Build verses around theme
3. Use revision for polish
4. Export JSON for project archival

### Producers
1. Match lyrics to beat energy
2. Use phonetics to verify singability
3. Adjust slang for target market
4. Download TXT for studio sessions

### Artists
1. Specify your nationality for regional flavor
2. Set vocal style preferences
3. Use keywords for personal topics
4. Review QA log for cultural context

---

**Built with ❤️ for Latin Music Creators**

*KAIRA 2025 — Professional songwriting at the speed of inspiration*
