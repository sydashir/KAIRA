# KAIRA MAINSTREAM AI SONGWRITING ENGINE — GITHUB COPILOT PROJECT INSTRUCTIONS

You (Copilot) are assisting in building a production-grade Python + Streamlit web application called “KAIRA MAINSTREAM”. This app generates professional Spanish/Latin Pop/Urban lyrics using a Custom GPT backend powered by OpenAI (GPT-4.x or later).

## CONTEXT:
The songwriting rules, structure, persona, vocabulary, constraints, and QA logic come from these project documents:
- KAIRA 2025 FULL DNA.txt 
- KAIRA 2025 RESUMED DNA.txt
- ASIF BULLET LIST.pdf

These documents define:
- Persona: “MAINSTREAM”
- Genre hierarchy
- Vibe and tone definitions
- Slang rules (1–2 marks/block)
- Strict line counts per section
- Section order defaults (V1 → Chorus → V2/Chanteo → Pre → Chorus)
- Phonetic rules (sinalefa, stressed vowels, closure)
- Hook structure (4+4)
- Revision rules (micro-edits only)
- QA checklist (structure, slang, phonetics, breath, endings, etc.)

## WHAT THIS REPO MUST IMPLEMENT:
A full Python project with:
- `/src/app.py` → Streamlit UI front-end  
- Dropdown menus for:
  - Genre
  - Type
  - Vibe
  - Energy level
  - Language (Spanish / English / Spanglish)
  - Slang density (low/med/high)
  - Section include toggles (chanteo, bridge, phonetic lines)
  - Lyrics part selector (full song / verse only / chorus only / custom)
  - Structure override (optional custom sequence)
- Text inputs for notes (scenes, keywords)
- Function that builds a JSON payload using user selections
- Prompt templating function to inject payload into GPT user-prompt
- GPT backend call using the Custom GPT system prompt (stored in prompts/system_prompt.txt)
- Output handling:
  - Render formatted lyrics
  - Optional phonetic lines under each lyric line
  - Display QA logs & metadata
  - Provide download buttons for TXT / JSON

## PROJECT REQUIREMENTS:
- Python 3.10+
- Streamlit app structured with clear UI sections
- Use OpenAI’s API (responses.create or ChatCompletion)
- Modular code:
  - utils for JSON building
  - postprocessing for QA parsing
  - theme.py for styling
- Ensure GPT output is valid JSON; implement retry logic
- Use .env for OPENAI_API_KEY
- Include example payloads
- Include instructions on how to run locally:
  streamlit run app.py

## DEVELOPMENT STYLE FOR COPILOT:
- Generate clean, documented, production-quality code
- Use functions, avoid bloated inline logic
- Add helpful comments, docstrings, and type hints
- Maintain expandable architecture for future RAG or LoRA integration
- When generating code, prioritize clarity, modularity, and scalability

## WHAT TO GENERATE FIRST:
1. Create folder structure:
   /src
   /prompts
   /docs
   .env.example
   requirements.txt

2. Create `app.py` with:
   - Streamlit UI
   - JSON payload builder
   - Prompt template generator
   - GPT call
   - Output renderer

3. Create `prompts/system_prompt.txt` containing KAIRA’s system prompt.

4. Create utils and postprocessing modules.

Copilot: Use this description as your full understanding of the project. Generate cohesive, high-quality Python code that is aligned with the KAIRA DNA documents and the Streamlit workflow described above.
