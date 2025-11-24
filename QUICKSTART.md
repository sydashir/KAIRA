# 🚀 KAIRA 2025 QUICKSTART

Get your KAIRA MAINSTREAM songwriting assistant running in 5 minutes!

---

## Step 1: Install Dependencies

```bash
pip install -r requirements_new.txt
```

---

## Step 2: Set Up OpenAI API Key

1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

2. Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

3. Edit `.env` and add your key:
   ```env
   OPENAI_API_KEY=sk-your-actual-api-key-here
   DEFAULT_MODEL=gpt-4o
   DEFAULT_TEMPERATURE=0.8
   DEFAULT_MAX_TOKENS=2500
   ```

---

## Step 3: Run the Application

```bash
streamlit run app_new.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## Step 4: Generate Your First Lyrics

### Example 1: Romantic Reggaeton

**Configure (Left Sidebar):**
- Model: `gpt-4o`
- Genre: `Reggaeton`
- Type: `Romantic`
- Vibe: `Sensual`
- Energy: `Medium`
- Language: `Spanish`
- Slang Density: `Medium (4-6)`

**Add Notes:**
```
Beach sunset, bittersweet memories after breakup,
visual scenes, not melodramatic, Caribbean vibes
```

**Keywords:**
```
playa, atardecer, recuerdo, mirada
```

**Click "🎤 Generate Lyrics"**

---

### Example 2: High-Energy Party Trap

**Configure:**
- Genre: `Latin Trap`
- Type: `Party`
- Vibe: `Energetic`
- Energy: `High`
- Language: `Spanglish`
- Slang Density: `High (7-10)`
- ✅ Include Chanteo

**Notes:**
```
Club energy, neon lights, heavy bass,
Puerto Rican street slang, party anthem
```

**Click "🎤 Generate Lyrics"**

---

## Step 5: Review Output

### Tabs Available:

1. **📝 Lyrics**
   - Complete formatted lyrics
   - Sections labeled: [VERSE 1], [CHORUS], etc.
   - Ready for studio use

2. **🗣️ Phonetics** (if enabled)
   - Difficult phrase breakdowns
   - Sinalefa markings
   - Rhythm notes

3. **📊 QA Log**
   - Creative choices explained
   - Cultural references
   - Slang usage notes

4. **ℹ️ Metadata**
   - Structure validation
   - Line counts
   - Model info
   - Estimated duration

---

## Step 6: Download

- **📄 Download as TXT**: Clean format for printing/studio
- **📋 Download as JSON**: Complete structured data with metadata

---

## 🎯 Quick Tips

### For Best Results:

1. **Be Specific**: "Beach sunset, red dress, nostalgic" > "Make it emotional"
2. **Match Energy**: High for Reggaeton/Dembow, Medium for Bachata
3. **Use Slang Wisely**: Low (0-3) for radio, High (7-10) for underground
4. **Enable Phonetics**: Especially for non-native Spanish speakers
5. **Try Different Models**: GPT-4o for quality, GPT-4o-mini for speed

### Genre-Energy Pairings:

| Genre | Typical Energy | Common Vibe |
|-------|---------------|-------------|
| Reggaeton | High | Energetic, Sensual |
| Bachata Urbana | Medium | Romantic, Melancholic |
| Latin Trap | Medium-High | Aggressive, Dark |
| Latin Pop | Medium | Warm, Hopeful |
| Dembow | High | Playful, Energetic |

---

## 🎼 Understanding KAIRA Structure

### Default MAINSTREAM Structure:
```
[verse 1] → [chorus] → [verse 2] → [pre-chorus] → [chorus]
```

### Line Counts:
- **Verse**: 8 lines (sets the scene)
- **Pre-Chorus**: 4 lines (builds tension)
- **Chorus**: 8 lines (4+4 hook+echo)
- **Chanteo**: 8-16 lines (flow-driven, optional)
- **Bridge**: 4-6 lines (emotional twist, optional)

---

## 🔧 Troubleshooting

**Problem**: API Key Error
- **Solution**: Check `.env` file has correct `OPENAI_API_KEY`

**Problem**: Generation is slow
- **Solution**: Switch to `gpt-4o-mini` model

**Problem**: Lyrics not matching expectations
- **Solution**: 
  - Be more specific in Notes field
  - Add relevant Keywords
  - Adjust Slang Density
  - Try regenerating with same settings (AI variation)

---

## 📖 Next Steps

- Read full [README_NEW.md](README_NEW.md) for comprehensive guide
- Check [KAIRA DNA documents](data/) for specs
- Experiment with different configurations
- Try revision workflow (generate → refine → regenerate)

---

## 🎵 Success Criteria

Your lyrics are KAIRA-quality when:
- ✅ They sound singable (not just readable)
- ✅ Rhythm feels natural (breathable phrases)
- ✅ Spanish sounds current (2025 Gen-Z tone)
- ✅ Slang is subtle and credible
- ✅ Chorus is catchy (hook+echo pattern)
- ✅ Scenes are visual (movie in words)

---

## 🎤 Example Output Preview

```
[VERSE 1]
Baby, qué más
Hace rato no sé na' de ti
Taba con alguien, pero ya estoy free
Pa' revivir lo que fue, si te apetece a ti

Sigo pensando en tu voz
Y en la última vez que te vi
No sé si fue el vino o el adiós
Pero aún me vibra tu hoodie en mí

[CHORUS]
Si antes te hubiera conocido
No habría final, solo destino
Tú y yo mirando el mismo ruido
La playa hablándonos al oído
```

---

**Ready to create? Run `streamlit run app_new.py` now! 🎧**
