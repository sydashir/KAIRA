# 🔄 KAIRA Migration Guide (Old → New)

## Quick Migration Path

If you were using the old KAIRA version, here's how to migrate:

---

## 1. Update Your Command

### Old
```bash
streamlit run app.py
```

### New (Same!)
```bash
streamlit run app.py
```

✅ **No change needed!** The main command is the same.

---

## 2. Update Environment Variables

### Old `.env`
```env
OPENAI_API_KEY=your_key_here
```

### New `.env` (Enhanced)
```env
OPENAI_API_KEY=your_key_here
DEFAULT_MODEL=gpt-4o
DEFAULT_TEMPERATURE=0.8
DEFAULT_MAX_TOKENS=2500
```

**Action**: Add the new optional variables (or keep just the API key - it still works!)

---

## 3. Import Changes (If Using as Library)

### Old Imports
```python
from openai_client import LyricsGenerator
from utils import build_json_payload, format_download_txt

# Usage
generator = LyricsGenerator()
result = generator.generate_lyrics(payload)
```

### New Imports
```python
from core import GPTClient, PromptBuilder, ResponseParser
from utils import build_json_payload, format_download_txt

# Usage
client = GPTClient(model="gpt-4o")
system_prompt = PromptBuilder.get_system_prompt()
user_prompt = PromptBuilder.build_user_prompt(payload)
response = client.generate_lyrics(system_prompt, user_prompt)
parsed = ResponseParser.parse(response)
```

**Benefit**: More control, better error handling, multi-model support

---

## 4. Payload Structure Changes

### Old Payload (Still Works!)
```python
payload = {
    "genre": "Reggaeton",
    "type": "Romantic",
    "vibe": "Sensual",
    "energy": "Medium",
    "language": "Spanish",
    "slang_density": 5,
    "structure": "Default",
    "chanteo": False,
    "bridge": True,
    "phonetics": True,
    "notes": "Beach sunset",
    "lyrics_part": "Full Song"
}
```

### New Payload (Enhanced)
```python
payload = {
    "genre": "Reggaeton",
    "type": "Romantic",
    "vibe": "Sensual",
    "energy": "Medium",
    "language": "Spanish",
    "slang_density": "Medium",  # Now accepts "Low", "Medium", "High"
    
    # NEW: Singer profile
    "singer": {
        "gender": "Female",
        "nationality": "Colombian",
        "vocal_style": "Smooth"
    },
    
    "include_chanteo": False,  # Renamed from "chanteo"
    "include_bridge": True,     # Renamed from "bridge"
    "include_phonetics": True,  # Renamed from "phonetics"
    "structure_override": None,
    "lyrics_part": "Full Song",
    "notes": "Beach sunset, visual scenes",
    "length": "Medium",  # NEW
    
    # NEW: Keyword control
    "keywords": ["playa", "recuerdo"],
    "forbidden_words": []
}
```

**Action**: Update your code to use new field names and add optional new features

---

## 5. Response Structure Changes

### Old Response
```python
{
    "lyrics": "Full lyrics text...",
    "phonetics": "Phonetic guidance...",
    "qa_log": "QA notes..."
}
```

### New Response (Structured)
```python
{
    "lyrics": {
        "verse_1": "8 lines...",
        "chorus": "8 lines...",
        "verse_2": "8 lines...",
        "pre_chorus": "4 lines...",
        "chorus_repeat": "8 lines..."
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
        "slang_used": ["na'", "taba"],
        "structure_notes": "..."
    },
    "metadata": {
        "total_lines": 32,
        "structure": "[verse 1] → [chorus] → ...",
        "slang_density": 2,
        "model_used": "gpt-4o",
        "estimated_duration": "3:15"
    }
}
```

**Benefit**: More structured, easier to parse sections, better metadata

---

## 6. New Features Available

### Multi-Model Support
```python
# Old: Only gpt-4o
generator = LyricsGenerator()

# New: Choose your model
client = GPTClient(model="gpt-4o")         # Best quality
client = GPTClient(model="gpt-4o-mini")    # Faster, cheaper
client = GPTClient(model="gpt-4-turbo")    # High quality
client = GPTClient(model="gpt-4")          # Stable
```

### Singer Profile
```python
payload["singer"] = {
    "gender": "Female",
    "nationality": "Puerto Rican",
    "vocal_style": "Raspy"
}
```

### Keyword Control
```python
payload["keywords"] = ["playa", "noche", "recuerdo"]
payload["forbidden_words"] = ["corazón", "alma"]
```

### Validation
```python
from core import validate_payload

is_valid, errors = validate_payload(payload)
if not is_valid:
    print(f"Errors: {errors}")
```

---

## 7. Configuration Access

### Old (Hardcoded)
Had to edit `app.py` to change genres/types/vibes

### New (Config Files)
```python
from config import GENRES, SONG_TYPES, VIBES, STRUCTURES

# Easy access to all options
print(GENRES)  # ['Latin Pop', 'Reggaeton', ...]
print(SONG_TYPES)  # ['Romantic', 'Heartbreak', ...]
print(VIBES)  # ['Warm', 'Dark', ...]

# Add new genre
# Just edit config/genres.py!
```

---

## 8. Error Handling

### Old
```python
try:
    result = generator.generate_lyrics(payload)
except Exception as e:
    print(f"Error: {e}")
```

### New (Auto-Retry)
```python
# Automatic retry (up to 3 attempts)
response = client.generate_with_retry(
    system_prompt=system_prompt,
    user_prompt=user_prompt,
    max_retries=3
)

# Check for errors
if response.get("metadata", {}).get("error"):
    print(f"Error: {response['metadata']['error_message']}")
```

---

## 9. Backward Compatibility

### ✅ What Still Works

- **Basic payload structure** (old field names still recognized)
- **Simple slang density numbers** (0-10)
- **Environment variable** (just `OPENAI_API_KEY`)
- **Same command** (`streamlit run app.py`)
- **Same download formats** (TXT and JSON)

### ⚠️ What Changed

- **Import paths** (if using as library)
- **Response structure** (now nested JSON)
- **Field names** (some renamed for clarity)
- **File structure** (modular packages)

---

## 10. Breaking Changes (If Any)

### If You Were Importing Directly

**Won't Work**:
```python
from openai_client import LyricsGenerator  # ❌ File removed
from utils import get_system_prompt        # ❌ Moved to core
```

**Use Instead**:
```python
from core import GPTClient, PromptBuilder  # ✅ New location
from core.prompt_builder import PromptBuilder  # ✅ New location
```

### If You Were Using Web UI Only

**No Breaking Changes!** The UI is backward compatible and enhanced.

---

## 11. Step-by-Step Migration

### For Web UI Users (No Code Changes)

1. **Pull latest code**
   ```bash
   git pull origin main
   ```

2. **Update dependencies** (same command)
   ```bash
   pip install -r requirements.txt
   ```

3. **Update .env** (optional - add new variables)
   ```bash
   # Add to your .env:
   DEFAULT_MODEL=gpt-4o
   DEFAULT_TEMPERATURE=0.8
   DEFAULT_MAX_TOKENS=2500
   ```

4. **Run app** (same command!)
   ```bash
   streamlit run app.py
   ```

5. **Enjoy new features!**
   - 13 genres (vs 8)
   - 15 vibes (vs 9)
   - Singer profiles
   - Keyword control
   - Better phonetics

### For Library Users (Programmatic Use)

1. **Update imports**
   ```python
   # Old
   from openai_client import LyricsGenerator
   
   # New
   from core import GPTClient, PromptBuilder, ResponseParser
   ```

2. **Update code structure**
   ```python
   # Old
   generator = LyricsGenerator()
   result = generator.generate_lyrics(payload)
   
   # New
   client = GPTClient(model="gpt-4o")
   system = PromptBuilder.get_system_prompt()
   user = PromptBuilder.build_user_prompt(payload)
   response = client.generate_lyrics(system, user)
   parsed = ResponseParser.parse(response)
   ```

3. **Test thoroughly!**

---

## 12. What You Gain

- ✅ **13 genres** (vs 8) with detailed characteristics
- ✅ **15 vibes** (vs 9) for better mood control
- ✅ **4 AI models** support (vs 1)
- ✅ **Singer profiles** for personalization
- ✅ **Keyword control** (include/forbid words)
- ✅ **Better error handling** with auto-retry
- ✅ **Comprehensive validation**
- ✅ **Modular architecture** (easier to extend)
- ✅ **Complete KAIRA DNA** implementation
- ✅ **Better documentation** (6 guides vs 1)
- ✅ **Production-ready** code quality

---

## 13. Need Help?

### Documentation
- **Quick Start**: `QUICKSTART.md`
- **Full Guide**: `README.md`
- **Architecture**: `PROJECT_STRUCTURE.md`
- **Visual Flow**: `VISUAL_GUIDE.md`
- **This Guide**: `MIGRATION_GUIDE.md`

### Common Issues

**Issue**: "Module not found: openai_client"
- **Fix**: Update imports to use `from core import GPTClient`

**Issue**: "Invalid payload structure"
- **Fix**: Use new field names (`include_chanteo` vs `chanteo`)

**Issue**: "Response format changed"
- **Fix**: Access sections via `response['lyrics']['verse_1']` instead of `response['lyrics']`

---

## 14. Rollback (If Needed)

If you need to temporarily rollback:

```bash
# Checkout old version (if in git)
git checkout <old-commit-hash>

# Or restore old files from backup
```

**Note**: The new version is tested and stable. Rollback should not be needed!

---

## ✅ Migration Checklist

- [ ] Pull latest code / Download new version
- [ ] Update `requirements.txt` dependencies
- [ ] Update `.env` file (add new variables)
- [ ] Update imports (if using as library)
- [ ] Update payload structure (rename fields)
- [ ] Test generation with new UI
- [ ] Review new features (singer profile, keywords)
- [ ] Read documentation (README.md, QUICKSTART.md)
- [ ] Explore new genres/vibes/structures
- [ ] Enjoy better lyrics! 🎉

---

**Migration complete! Welcome to KAIRA 2025 MAINSTREAM! 🎧**
