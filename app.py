import streamlit as st
import urllib.request
import json
import urllib.parse

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

# Funzione per cercare notizie usando le API pubbliche di DuckDuckGo
def cerca_notizie(termine):
    try:
        url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(termine)}&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            risultati = []
            for item in data.get('RelatedTopics', []):
                if 'Text' in item and 'FirstURL' in item:
                    risultati.append({"titolo": item['Text'], "url": item['FirstURL']})
            return risultati
    except Exception as e:
        return []

# Gestione della ricerca
if "notizie_trovate" not in st.session_state:
    st.session_state.notizie_trovate = []

if cerca_btn:
    with st.spinner("Sto scandagliando il web per te..."):
        st.session_state.notizie_trovate = cerca_notizie(query)

# Mostra i risultati se ci sono
if st.session_state.notizie_trovate:
    st.subheader("📰 Notizie trovate nel web (Seleziona la tua preferita)")
    
    scelte = [n["titolo"] for n in st.session_state.notizie_trovate]
    notizia_scelta = st.selectbox("Scegli una notizia dalla lista:", scelte)
    
    if st.button("✨ Genera Testo Notizia (Stile Chill)"):
        st.markdown("---")
        st.subheader("📝 Articolo Generato:")
        st.success(f"**Yo bro, beccati questa:**\n\Abbiamo analizzato la notizia selezionata: *\"{notizia_scelta}\"*. Sembra proprio che ci siano grosse novità in arrivo nel mondo del gaming. Preparate i pad perché qui la situazione si fa interessante!" )
else:
    if cerca_btn:
        st.warning("Nessun risultato immediato trovato, prova a cambiare termine di ricerca nella barra laterale!") gli sviluppatori abbiano spaccato stavolta, preparate i pad!")
