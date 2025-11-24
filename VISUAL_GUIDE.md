# 🎧 KAIRA 2025 MAINSTREAM — Visual Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT WEB UI                          │
│  ┌────────────┐  ┌──────────────┐  ┌────────────────────┐  │
│  │  Sidebar   │  │ Main Content │  │   Output Tabs      │  │
│  │ Config     │  │ Notes/Keys   │  │ Lyrics/Phonetics   │  │
│  └────┬───────┘  └──────┬───────┘  └──────┬─────────────┘  │
└───────┼──────────────────┼──────────────────┼────────────────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    ┌──────▼──────┐
                    │   PAYLOAD   │ (JSON)
                    │   BUILDER   │
                    └──────┬──────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
     ┌────▼─────┐    ┌─────▼────┐    ┌─────▼────┐
     │ Validate │    │  Prompt  │    │  System  │
     │ Payload  │    │ Builder  │    │  Prompt  │
     └────┬─────┘    └─────┬────┘    └─────┬────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
                    ┌──────▼──────────┐
                    │   GPT CLIENT    │
                    │  (Multi-Model)  │
                    │ ┌─────────────┐ │
                    │ │  Retry      │ │
                    │ │  Logic      │ │
                    │ └─────────────┘ │
                    └──────┬──────────┘
                           │
                    ┌──────▼──────────┐
                    │  OpenAI GPT-4+  │
                    │   API Call      │
                    └──────┬──────────┘
                           │
                    ┌──────▼──────────┐
                    │   JSON          │
                    │  RESPONSE       │
                    └──────┬──────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
     ┌────▼─────┐    ┌─────▼────┐    ┌─────▼────┐
     │ Response │    │ Validate │    │  Format  │
     │  Parser  │    │ Response │    │ Display  │
     └────┬─────┘    └─────┬────┘    └─────┬────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
                    ┌──────▼──────────┐
                    │  DISPLAY OUTPUT │
                    │ ┌─────────────┐ │
                    │ │ Lyrics      │ │
                    │ │ Phonetics   │ │
                    │ │ QA Log      │ │
                    │ │ Metadata    │ │
                    │ └─────────────┘ │
                    └──────┬──────────┘
                           │
                    ┌──────▼──────────┐
                    │   DOWNLOAD      │
                    │  TXT  |  JSON   │
                    └─────────────────┘
```

---

## Configuration Flow

```
USER SELECTS
├── 🎼 Genre (13 options)
│   └── Latin Pop, Reggaeton, Latin Trap, Urban, Afro-Latin...
│
├── 🎭 Type (12 options)
│   └── Romantic, Heartbreak, Party, Empowerment...
│
├── 🌈 Vibe (15 options)
│   └── Warm, Dark, Cinematic, Intimate, Energetic...
│
├── ⚡ Energy (5 levels)
│   └── Low → Medium-Low → Medium → Medium-High → High
│
├── 🗣️ Language (3 options)
│   └── Spanish, English, Spanglish
│
├── 💬 Slang Density (3 levels)
│   └── Low (0-3), Medium (4-6), High (7-10)
│
├── 🎤 Singer Profile (optional)
│   ├── Gender
│   ├── Nationality
│   └── Vocal Style
│
├── 🎹 Structure (9 templates)
│   ├── Mainstream Default (KAIRA DNA)
│   ├── Classic Pop
│   ├── Urban Simple
│   ├── Trap Flow
│   ├── Bachata Classic
│   ├── Reggaeton Party
│   ├── Ballad
│   ├── Freestyle
│   └── Custom
│
├── ✅ Optional Elements
│   ├── Include Chanteo
│   ├── Include Bridge
│   └── Include Phonetics
│
├── 📝 Lyrics Part
│   └── Full Song, Verse Only, Chorus Only, Custom...
│
└── ✍️ Creative Direction
    ├── Notes (scenes, themes, emotions)
    ├── Keywords (words to include)
    └── Forbidden Words (words to avoid)
```

---

## KAIRA DNA Structure

```
MAINSTREAM DEFAULT STRUCTURE:
┌─────────────────────────────────────┐
│  [VERSE 1] - 8 lines                │
│  • Sets the scene                   │
│  • Conversational, cinematic tone   │
│  • Visual storytelling              │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│  [CHORUS] - 8 lines (4+4)           │
│  • Hook (4 lines)                   │
│  • Echo/Answer (4 lines)            │
│  • Catchy, repeatable, emotional    │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│  [VERSE 2 / CHANTEO] - 8 lines     │
│  • Continues story OR               │
│  • Flow-driven rhythmic section     │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│  [PRE-CHORUS] - 4 lines             │
│  • Builds tension                   │
│  • Energy rises melodically         │
│  • Anticipation to hook             │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│  [CHORUS] - 8 lines (repeat)        │
│  • Same or light variation          │
└─────────────────────────────────────┘

OPTIONAL SECTIONS (when requested):
┌─────────────────────────────────────┐
│  [BRIDGE] - 4-6 lines               │
│  • Emotional twist or closure       │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  [CHANTEO] - 8, 12, or 16 lines    │
│  • Between singing and rapping      │
│  • Flow-driven rhythmic phrasing    │
└─────────────────────────────────────┘
```

---

## Phonetic Rhythm System

```
SPANISH SUNG PHONETICS (not syllable counting)

1. SINALEFA (Vowel Fusion)
   "te hablo" → "tea-blo" (fuses to one beat)
   "mi alma" → "mial-ma" (fuses to one beat)

2. STRESSED VOWELS (Extended Beats)
   "café" → ca-FÉ (final é extends)
   "pasó" → pa-SÓ (final ó extends)

3. STRONG BEATS
   Fall on meaning words:
   ✅ Verbs, Nouns (voy, casa, amor)
   ❌ Fillers (y, de, que, para)

4. NATURAL BREATHING
   Every 1-2 lines = breath point
   Write like a voice, not a paragraph

5. RHYTHMIC CONTRAST
   Long lines + Short lines = Movement
   Example:
   "Baby, qué más" (short, punchy)
   "Hace rato no sé na' de ti" (longer, flowing)

6. GROOVE OVER MATH
   Rhythmic feel > exact syllable count
   Contrast matters more than total
```

---

## Output Structure

```
JSON RESPONSE FORMAT:

{
  "lyrics": {
    "intro": "...",           // Optional, 2-4 lines
    "verse_1": "...",         // Required, 8 lines
    "pre_chorus": "...",      // Optional, 4 lines
    "chorus": "...",          // Required, 8 lines (4+4)
    "verse_2": "...",         // 8 lines OR chanteo
    "chanteo": "...",         // Optional, 8/12/16 lines
    "chorus_repeat": "...",   // 8 lines (repeat/variation)
    "bridge": "...",          // Optional, 4-6 lines
    "outro": "..."            // Optional, 4-6 lines
  },
  
  "phonetics": {
    "difficult_phrases": [
      {
        "phrase": "te apetece a ti",
        "phonetic": "tea-pe-té-sea-tí",
        "note": "Sinalefa: 'te' + 'apetece'"
      }
    ],
    "rhythm_notes": "Strong beats on 'apetece' and 'ti'..."
  },
  
  "qa_log": {
    "creative_choices": "Used beach sunset imagery...",
    "cultural_references": "Caribbean slang: 'taba', 'pa''...",
    "slang_used": ["taba", "pa'", "na'", "toy'"],
    "structure_notes": "8-line verses for breathing room...",
    "revision_notes": "..."
  },
  
  "metadata": {
    "total_lines": 32,
    "structure": "[verse 1] → [chorus] → ...",
    "slang_density": 2,
    "language": "Spanish (Latin America)",
    "model_used": "gpt-4o",
    "estimated_duration": "3:15",
    "tokens_used": 1524
  }
}
```

---

## Model Comparison

```
┌────────────────┬──────────┬───────┬─────────┬────────────┐
│ Model          │ Quality  │ Speed │ Cost    │ Best For   │
├────────────────┼──────────┼───────┼─────────┼────────────┤
│ GPT-4o         │ ⭐⭐⭐⭐⭐ │ Fast  │ Medium  │ Production │
│ GPT-4o-mini    │ ⭐⭐⭐⭐   │ Faster│ Low     │ Testing    │
│ GPT-4-turbo    │ ⭐⭐⭐⭐⭐ │ Medium│ High    │ Quality    │
│ GPT-4          │ ⭐⭐⭐⭐   │ Slow  │ Highest │ Stable     │
└────────────────┴──────────┴───────┴─────────┴────────────┘

RECOMMENDATION:
• Production: GPT-4o (best balance)
• rapid iteration: GPT-4o-mini (fast + cheap)
• Maximum quality: GPT-4-turbo
• Stable/tested: GPT-4
```

---

## Workflow Examples

### Example 1: Romantic Reggaeton
```
INPUT:
  Genre: Reggaeton
  Type: Romantic
  Vibe: Sensual
  Energy: Medium
  Language: Spanish
  Slang: Medium (4-6)
  Notes: "Beach sunset, bittersweet memories"
  
PROCESS:
  1. Build payload
  2. Validate required fields
  3. Generate system + user prompts
  4. Call GPT-4o API
  5. Parse JSON response
  6. Validate structure
  7. Format for display
  
OUTPUT:
  ✅ 32-line song
  ✅ Structure: [V1][C][V2][PC][C]
  ✅ Slang density: 2 marks
  ✅ Phonetics included
  ✅ QA log: "Caribbean vibes, visual imagery..."
```

### Example 2: High-Energy Trap
```
INPUT:
  Genre: Latin Trap
  Type: Party
  Vibe: Aggressive
  Energy: High
  Language: Spanglish
  Slang: High (7-10)
  Include Chanteo: ✅
  
OUTPUT:
  ✅ 48-line song (with chanteo)
  ✅ Heavy slang: "toy'", "bellaqueo", "perreo"
  ✅ English phrases mixed in
  ✅ Chanteo: 16 lines of flow
```

---

## File Organization

```
kaira/
│
├── 📱 APP FILES
│   ├── app_new.py              (Main Streamlit UI)
│   ├── app.py                  (Original - legacy)
│   └── openai_client.py        (Legacy client)
│
├── ⚙️ CONFIG/ (Dropdown Options)
│   ├── __init__.py
│   ├── genres.py               (13 genres)
│   ├── types.py                (12 types)
│   ├── vibes.py                (15 vibes)
│   └── structures.py           (9 structures)
│
├── 🧠 CORE/ (Engine)
│   ├── __init__.py
│   ├── gpt_client.py           (Multi-model GPT)
│   ├── prompt_builder.py       (KAIRA DNA prompts)
│   ├── response_parser.py      (JSON parsing)
│   └── validator.py            (Validation logic)
│
├── 🛠️ UTILS/ (Helpers)
│   ├── __init__.py
│   ├── formatters.py           (TXT/JSON download)
│   └── helpers.py              (Payload builder)
│
├── 📚 DATA/ (Specs)
│   ├── KAIRA 2025 FULL DNA.txt
│   ├── KAIRA 2025 RESUMED DNA.txt
│   └── ASIF BULLET LIST.pdf
│
├── 📖 DOCS/
│   ├── README_NEW.md           (Comprehensive guide)
│   ├── QUICKSTART_NEW.md       (5-min setup)
│   ├── PROJECT_STRUCTURE.md    (Architecture)
│   ├── IMPLEMENTATION_SUMMARY.md
│   └── VISUAL_GUIDE.md         (This file)
│
└── 🔧 CONFIG FILES
    ├── .env                    (API keys - NOT committed)
    ├── .env.example            (Template)
    ├── requirements_new.txt    (Dependencies)
    └── .gitignore
```

---

## Success Criteria Checklist

### ✅ KAIRA Quality Lyrics:
- [ ] Singable (not just readable)
- [ ] Natural rhythm (breathable phrases)
- [ ] Current Spanish (2025 Gen-Z tone)
- [ ] Subtle slang (credible, not forced)
- [ ] Catchy chorus (hook+echo pattern)
- [ ] Visual scenes (movie in words)
- [ ] Emotional honesty (no melodrama)
- [ ] Structure compliance (KAIRA DNA)

### ✅ Technical Quality:
- [ ] Valid JSON response
- [ ] Correct line counts
- [ ] Phonetics (if enabled)
- [ ] QA log included
- [ ] Metadata complete
- [ ] Download works (TXT & JSON)

---

## Quick Reference Commands

```bash
# Install
pip install -r requirements_new.txt

# Configure
cp .env.example .env
# Edit .env with your OPENAI_API_KEY

# Run
streamlit run app_new.py

# Access
http://localhost:8501
```

---

## Support & Resources

📖 Full Docs: `README_NEW.md`  
🚀 Quick Start: `QUICKSTART_NEW.md`  
🏗️ Architecture: `PROJECT_STRUCTURE.md`  
📊 Implementation: `IMPLEMENTATION_SUMMARY.md`  
🎧 DNA Specs: `data/KAIRA 2025 FULL DNA.txt`

---

**KAIRA 2025 MAINSTREAM — Professional songwriting at the speed of inspiration** 🎧🎵
