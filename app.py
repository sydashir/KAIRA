"""
Spanish/Latin Pop/Urban Lyrics Generator - Streamlit App
"""
import streamlit as st
from dotenv import load_dotenv
from openai_client import LyricsGenerator
from utils import build_json_payload, format_download_txt, format_download_json

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="KAIRA - Spanish/Latin Lyrics Generator",
    page_icon="🎵",
    layout="wide"
)

# Title and description
st.title("🎵 KAIRA - Spanish/Latin Lyrics Generator")
st.markdown("""
Generate authentic Spanish/Latin Pop and Urban lyrics using AI.
Configure your preferences below and click **Generate Lyrics** to create your custom lyrics.
""")

# Sidebar for configuration
st.sidebar.header("Configuration")

# Genre selection
genre = st.sidebar.selectbox(
    "Genre",
    [
        "Reggaeton",
        "Dembow",
        "Trap Latino",
        "Bachata Urbana",
        "Latin Pop",
        "Cumbia Urbana",
        "Salsa Urbana",
        "Corridos Tumbados"
    ],
    help="Select the music genre"
)

# Type selection
song_type = st.sidebar.selectbox(
    "Type",
    [
        "Love Song",
        "Party Anthem",
        "Heartbreak",
        "Success/Flex",
        "Storytelling",
        "Romantic",
        "Perreo",
        "Social Commentary"
    ],
    help="Select the type of song"
)

# Vibe selection
vibe = st.sidebar.selectbox(
    "Vibe",
    [
        "Romantic",
        "Energetic",
        "Melancholic",
        "Aggressive",
        "Sensual",
        "Playful",
        "Dark",
        "Uplifting",
        "Chill"
    ],
    help="Select the emotional vibe"
)

# Energy selection
energy = st.sidebar.selectbox(
    "Energy",
    [
        "Low (Chill)",
        "Medium-Low",
        "Medium",
        "Medium-High",
        "High (Hype)"
    ],
    help="Select the energy level"
)

# Language selection
language = st.sidebar.selectbox(
    "Language",
    [
        "Spanish (Spain)",
        "Spanish (Latin America)",
        "Spanish/English Mix (Spanglish)",
        "Primarily English with Spanish phrases",
        "Regional (Caribbean)",
        "Regional (Mexico)",
        "Regional (South America)"
    ],
    help="Select the language and dialect"
)

# Slang density slider
slang_density = st.sidebar.slider(
    "Slang Density",
    min_value=0,
    max_value=10,
    value=5,
    help="0 = Formal, 10 = Heavy street slang"
)

# Structure selection
structure = st.sidebar.selectbox(
    "Structure",
    [
        "Intro - Verse - Chorus - Verse - Chorus - Bridge - Chorus",
        "Verse - Chorus - Verse - Chorus - Bridge - Chorus",
        "Intro - Verse - Pre-Chorus - Chorus - Verse - Pre-Chorus - Chorus",
        "Verse - Chorus - Verse - Chorus",
        "Freestyle (No specific structure)",
        "Custom"
    ],
    help="Select the song structure"
)

# Toggles
st.sidebar.subheader("Additional Elements")
chanteo = st.sidebar.checkbox(
    "Include Chanteo",
    value=False,
    help="Add catchy repetitive hooks/chants"
)

bridge = st.sidebar.checkbox(
    "Include Bridge",
    value=True,
    help="Include a bridge section"
)

phonetics = st.sidebar.checkbox(
    "Include Phonetics",
    value=False,
    help="Include pronunciation guidance for difficult phrases"
)

# Lyrics part selection
lyrics_part = st.sidebar.selectbox(
    "Lyrics Part",
    [
        "Complete Song",
        "Intro",
        "Verse 1",
        "Verse 2",
        "Verse 3",
        "Pre-Chorus",
        "Chorus",
        "Bridge",
        "Outro",
        "Chanteo Section"
    ],
    help="Select which part of the lyrics to generate"
)

# Notes input
notes = st.sidebar.text_area(
    "Additional Notes",
    placeholder="Add any specific requests, themes, or details...",
    help="Provide additional context or specific requirements"
)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Generation Controls")
    
    # Generate button
    if st.button("🎤 Generate Lyrics", type="primary", use_container_width=True):
        # Build payload
        payload = build_json_payload(
            genre=genre,
            song_type=song_type,
            vibe=vibe,
            energy=energy,
            language=language,
            slang_density=slang_density,
            structure=structure,
            chanteo=chanteo,
            bridge=bridge,
            phonetics=phonetics,
            notes=notes,
            lyrics_part=lyrics_part
        )
        
        # Store payload in session state
        st.session_state.payload = payload
        
        # Generate lyrics
        with st.spinner("Generating lyrics... 🎵"):
            try:
                generator = LyricsGenerator()
                result = generator.generate_lyrics(payload)
                
                # Store results in session state
                st.session_state.lyrics = result.get("lyrics", "")
                st.session_state.phonetics = result.get("phonetics", "")
                st.session_state.qa_log = result.get("qa_log", "")
                st.session_state.generated = True
                
                st.success("Lyrics generated successfully! 🎉")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.session_state.generated = False

with col2:
    st.subheader("Current Settings")
    if 'payload' in st.session_state:
        st.json(st.session_state.payload)

# Display results
if st.session_state.get('generated', False):
    st.divider()
    
    # Create tabs for different outputs
    tab1, tab2, tab3 = st.tabs(["📝 Lyrics", "🗣️ Phonetics", "📊 QA Log"])
    
    with tab1:
        st.subheader("Generated Lyrics")
        if st.session_state.lyrics:
            st.text_area(
                "Lyrics",
                value=st.session_state.lyrics,
                height=400,
                key="lyrics_display"
            )
        else:
            st.warning("No lyrics generated.")
    
    with tab2:
        st.subheader("Phonetics Guide")
        if st.session_state.phonetics:
            st.text_area(
                "Phonetics",
                value=st.session_state.phonetics,
                height=400,
                key="phonetics_display"
            )
        else:
            st.info("No phonetics generated. Enable 'Include Phonetics' to get pronunciation guidance.")
    
    with tab3:
        st.subheader("Quality Assurance Log")
        if st.session_state.qa_log:
            st.text_area(
                "QA Log",
                value=st.session_state.qa_log,
                height=400,
                key="qa_log_display"
            )
        else:
            st.info("No QA log available.")
    
    # Download section
    st.divider()
    st.subheader("📥 Download Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # TXT download
        txt_content = format_download_txt(
            st.session_state.lyrics,
            st.session_state.phonetics,
            st.session_state.qa_log,
            st.session_state.payload
        )
        st.download_button(
            label="Download as TXT",
            data=txt_content,
            file_name="lyrics.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    with col2:
        # JSON download
        json_content = format_download_json(
            st.session_state.lyrics,
            st.session_state.phonetics,
            st.session_state.qa_log,
            st.session_state.payload
        )
        st.download_button(
            label="Download as JSON",
            data=json_content,
            file_name="lyrics.json",
            mime="application/json",
            use_container_width=True
        )

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>KAIRA - Spanish/Latin Lyrics Generator</p>
    <p>Powered by OpenAI GPT-4 | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
