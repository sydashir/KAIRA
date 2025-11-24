# KAIRA 2025 - Enhanced Project Structure

## Overview
KAIRA is a professional bilingual songwriting assistant for Mainstream Latin Pop & Urban music, powered by GPT-4+ models.

## Folder Structure

```
kaira/
├── app.py                          # Main Streamlit application (NEW - Enhanced UI)
├── config/
│   ├── __init__.py
│   ├── genres.py                   # Genre definitions and configurations
│   ├── types.py                    # Song types (romantic, heartbreak, party, etc.)
│   ├── vibes.py                    # Vibe options (warm, dark, cinematic, etc.)
│   └── structures.py               # Song structure templates
├── core/
│   ├── __init__.py
│   ├── prompt_builder.py           # Converts UI selections to GPT prompts
│   ├── gpt_client.py              # GPT API integration (GPT-4+)
│   ├── response_parser.py         # Parse and validate GPT responses
│   └── validator.py               # JSON validation and error handling
├── utils/
│   ├── __init__.py
│   ├── formatters.py              # Output formatting (TXT, JSON)
│   └── helpers.py                 # Helper functions
├── data/
│   ├── KAIRA 2025 FULL DNA.txt
│   ├── KAIRA 2025 RESUMED DNA.txt
│   └── ASIF BULLET LIST.pdf
├── .env                           # Environment variables (API keys)
├── .env.example
├── requirements.txt
├── README.md
└── QUICKSTART.md
```

## Key Components

### 1. Enhanced Streamlit UI (`app.py`)
- **Genre Selector**: Latin Pop, Reggaeton, Latin Trap, Urban, Afro-Latin, Pop Balada, etc.
- **Type Selector**: Romantic, Heartbreak, Party, Empowerment, Seduction, Nostalgia
- **Vibe Selector**: Warm, Dark, Cinematic, Intimate, Energetic, Sensual, Melancholic, Hopeful
- **Energy Level**: Low, Medium, High
- **Singer Profile**: Gender, nationality, vocal style
- **Language**: Spanish, English, Spanglish
- **Slang Density**: Low (0-3), Medium (4-6), High (7-10)
- **Structure Override**: Custom structure option
- **Lyrics Part**: Full song, Verse only, Chorus only, Custom sections
- **Additional Options**:
  - Include Chanteo (checkbox)
  - Include Bridge (checkbox)
  - Include Phonetic Lines (checkbox)
- **Notes Field**: Free-text for scenes, objects, keywords, forbidden words
- **Length Selector**: Short, Medium, Long

### 2. Prompt Builder (`core/prompt_builder.py`)
- Converts UI selections into structured JSON payload
- Embeds KAIRA MAINSTREAM system prompt
- Implements phonetic rhythm rules
- Enforces fixed structure: [verse 1] → [chorus] → [verse 2/chanteo] → [pre-chorus] → [chorus]

### 3. GPT Client (`core/gpt_client.py`)
- Supports GPT-4 Turbo, GPT-4o, and future models
- Structured JSON output mode
- Error handling and retry logic
- Temperature and token controls

### 4. Response Parser (`core/response_parser.py`)
- Validates GPT responses
- Extracts lyrics, phonetics, QA log, metadata
- Handles malformed JSON with retry mechanism

### 5. Output Rendering
- Formatted lyrics display
- Phonetic lines (PHON:) when enabled
- QA Log with creative insights
- Metadata display
- Download buttons (TXT and JSON formats)

## Configuration Files

### `config/genres.py`
Defines all supported genres from KAIRA DNA:
- Latin Pop
- Reggaeton
- Latin Trap
- Urban
- Afro-Latin
- Pop Balada
- Cumbia Urbana
- Bachata Urbana
- Dembow
- Corridos Tumbados
- Salsa Urbana

### `config/types.py`
Song types:
- Romantic
- Heartbreak
- Party
- Empowerment
- Seduction
- Nostalgia
- Storytelling
- Social Commentary
- Success/Flex
- Perreo

### `config/vibes.py`
Emotional vibes:
- Warm
- Dark
- Cinematic
- Intimate
- Energetic
- Sensual
- Melancholic
- Hopeful
- Playful
- Aggressive
- Uplifting
- Chill

## API Models Supported

1. **GPT-4 Turbo** (`gpt-4-turbo-preview`)
2. **GPT-4o** (`gpt-4o`)
3. **GPT-4o-mini** (`gpt-4o-mini`) - Free tier option
4. Future: GPT-5+ when available

## Environment Variables

```
OPENAI_API_KEY=your_api_key_here
DEFAULT_MODEL=gpt-4o
DEFAULT_TEMPERATURE=0.8
DEFAULT_MAX_TOKENS=2500
```

## JSON Payload Structure

```json
{
  "genre": "Reggaeton",
  "type": "Romantic",
  "vibe": "Sensual",
  "energy": "Medium",
  "singer": {
    "gender": "Female",
    "nationality": "Colombian",
    "vocal_style": "Smooth"
  },
  "language": "Spanish",
  "slang_density": "Medium",
  "include_chanteo": true,
  "include_bridge": false,
  "include_phonetics": true,
  "structure_override": null,
  "lyrics_part": "Full Song",
  "notes": "Visual scenes, beach sunset, emotional but not melodramatic",
  "length": "Medium",
  "forbidden_words": [],
  "keywords": ["playa", "atardecer", "recuerdos"]
}
```

## Output Structure

```json
{
  "lyrics": {
    "verse_1": "...",
    "chorus": "...",
    "verse_2": "...",
    "pre_chorus": "...",
    "chorus_repeat": "...",
    "bridge": "..."
  },
  "phonetics": {
    "difficult_phrases": [
      {
        "phrase": "te apetece a ti",
        "phonetic": "tea-pe-té-sea-tí",
        "note": "Sinalefa between 'te' and 'apetece'"
      }
    ]
  },
  "qa_log": {
    "creative_choices": "...",
    "cultural_references": "...",
    "slang_used": ["na'", "taba", "free"],
    "revision_notes": "..."
  },
  "metadata": {
    "total_lines": 32,
    "structure": "[verse 1] → [chorus] → [verse 2] → [pre-chorus] → [chorus]",
    "slang_density": 2,
    "language": "Spanish (Latin America)",
    "model_used": "gpt-4o"
  }
}
```

## Development Phases

### Phase 1 (Current)
- ✅ Build modular Streamlit UI
- ✅ Implement prompt templating system
- ✅ GPT-4+ integration
- ✅ Structured JSON output
- ✅ Error handling and retry logic
- ✅ Download functionality

### Phase 2 (Future)
- Regional tone controls (+7% Mexico, +5% Colombia)
- Advanced slang/melodic energy parameters
- Multi-language support expansion
- Voice synthesis integration
- Revision history tracking
- Collaborative editing

## Quality Standards

1. **Human-sounding**: Lyrics must sound like 2017-2025 Latin songwriter
2. **Phonetically singable**: Natural breath patterns, stress on meaning words
3. **Structurally consistent**: Fixed order unless overridden
4. **Revision stable**: 3-5 edits without tone/rhythm drift
5. **Culturally authentic**: Believable slang, modern Spanish
6. **Production-ready**: Clean code, error handling, typed Python
