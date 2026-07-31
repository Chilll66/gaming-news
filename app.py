import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Gaming News Generator", page_icon="🎮", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #0b0b0e;
        color: #e0e0e0;
    }
    h1, h2, h3 {
        color: #00ff66 !important;
        text-shadow: 0 0 10px rgba(0, 255, 102, 0.5);
    }
    .stButton>button {
        background-color: #9400D3;
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        box-shadow: 0 0 10px rgba(148, 0, 211, 0.6);
    }
    .news-box {
        background-color: #15151c;
        border: 1px solid #9400D3;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ GAMING NEWS GENERATOR ⚡")
st.write("Bella bro! Cerca le ultime notizie dal web, seleziona quella che ti interessa e genera l'articolo in stile chill & gaming.")

# Barra laterale per i comandi di ricerca
with st.sidebar:
    st.header("🎮 Controlli di Ricerca")
    query = st.text_input("Cosa vuoi cercare?", "videogiochi ultime uscite")
    cerca_btn = st.button("🔍 Cerca sul Web")

# Funzione di ricerca robusta con DuckDuckGo
def cerca_notizie_web(termine):
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(termine, max_results=5):
                results.append({"titolo": r.get('title'), "url": r.get('href'), "body": r.get('body')})
        return results
    except Exception as e:
        return []

if "notizie_trovate" not in st.session_state:
    st.session_state.notizie_trovate = []

if cerca_btn:
    with st.spinner("Sto scandagliando il web per te..."):
        st.session_state.notizie_trovate = cerca_notizie_web(query)

# Mostra i risultati
if st.session_state.notizie_trovate:
    st.subheader("📰 Notizie trovate nel web (Seleziona la tua preferita)")
    
    scelte = {n["titolo"]: n for n in st.session_state.notizie_trovate}
    titolo_scelto = st.selectbox("Scegli una notizia dalla lista:", list(scelte.keys()))
    notizia_scelta = scelte[titolo_scelto]
    
    st.markdown(f"""
    <div class="news-box">
        <p><b>Anteprima:</b> {notizia_scelta['body']}</p>
        <p><a href="{notizia_scelta['url']}" target="_blank">🔗 Leggi la fonte originale</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✨ Genera Testo Notizia (Stile Chill)"):
        st.markdown("---")
        st.subheader("📝 Articolo Generato:")
        st.success(f"**Yo bro, beccati questa:**\n\nAbbiamo analizzato la notizia *\"{titolo_scelto}\"*. Sembra proprio che gli sviluppatori abbiano spaccato stavolta, preparate i pad perché la scimmia è salita altissima!")
else:
    if cerca_btn:
        st.warning("Nessun risultato trovato, prova a cambiare termine di ricerca nella barra laterale!")
