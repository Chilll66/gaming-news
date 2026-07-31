import streamlit as st
import random
from duckduckgo_search import DDGS
from deep_translator import GoogleTranslator

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
        border: 2px solid #9400D3;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(148, 0, 211, 0.2);
    }
    .article-box {
        background-color: #12121a;
        border: 2px solid #00ff66;
        padding: 25px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0, 255, 102, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ GAMING NEWS GENERATOR ⚡")
st.write("Bella bro! Cerchiamo ovunque nel mondo le notizie di oggi e ieri, le traduciamo in italiano e le spieghiamo dritte al punto, senza perdite di tempo! 🔥")

with st.sidebar:
    st.header("🎮 Controlli di Ricerca")
    query_utente = st.text_input("Cosa vuoi cercare?", "Fortnite skin update")
    cerca_btn = st.button("🔍 Cerca News Globali")

def traduci_testo(testo):
    try:
        if testo and len(testo) > 2:
            return GoogleTranslator(source='auto', target='it').translate(testo)
    except:
        pass
    return testo

def cerca_news_globali(termine):
    try:
        results = []
        # Cerchiamo su tutto il web globale ma imponiamo il filtro temporale rigoroso sulle ultime 24 ore ('d')
        with DDGS() as ddgs:
            for r in ddgs.text(f"{termine} gaming news", max_results=5, timelimit='d'):
                titolo_raw = r.get('title', '')
                body_raw = r.get('body', '')
                url = r.get('href', '#')
                
                if len(body_raw) > 30:
                    # Traduciamo titolo e corpo direttamente in italiano
                    titolo_it = traduci_testo(titolo_raw)
                    body_it = traduci_testo(body_raw)
                    results.append({"titolo": titolo_it, "descrizione": body_it, "url": url})
        return results
    except Exception as e:
        return []

if "notizie_reali" not in st.session_state:
    st.session_state.notizie_reali = []

if cerca_btn:
    with st.spinner(f"Scandaglio il web mondiale per trovare le ultime novità su '{query_utente}'... 🚀"):
        st.session_state.notizie_reali = cerca_news_globali(query_utente)

if st.session_state.notizie_reali:
    st.subheader(f"📰 News freschissime per: '{query_utente}'")
    
    for i, n in enumerate(st.session_state.notizie_reali):
        with st.container():
            st.markdown(f"""
            <div class="news-box">
                <h3>🕹️ {n['titolo']}</h3>
                <p><b>Contenuto:</b> {n['descrizione']}</p>
                <a href="{n['url']}" target="_blank" style="color: #00ff66; font-weight: bold;">🔗 Fonte originale</a>
            </div>
            """, unsafe_allow_html=True)
            
            dettaglio_extra = st.text_input(f"Aggiungi dettagli extra (es. nome skin o collab) per la notizia #{i+1}:", key=f"extra_{i}")
            
            if st.button(f"✨ Genera Articolo Diretto #{i+1}", key=f"gen_{i}"):
                intro_list = [
                    "Yo bro, beccati questa news freschissima appena tradotta e sganciata dal web! 💣🔥",
                    "Attiska fra! Guarda cosa è appena uscito nel mondo, andiamo dritti al sodo! 🎮💥",
                    "Bella raga, beccatevi questo aggiornamento caldissimo tradotto al volo: ecco i fatti! 🕹️⚡",
                    "Gamer, zero giri di parole: ecco la novità del giorno spiegata pulita e semplice! 🏆👾"
                ]
                
                # Montiamo il testo basandoci ESATTAMENTE sui dati reali della notizia senza riempitivi inutili
                info_fatti = n['descrizione']
                if dettaglio_extra:
                    info_fatti = f"{info_fatti} Nello specifico: {dettaglio_extra}"
                
                corpo_art = f"Ecco esattamente cosa dice la notizia, senza fronzoli: {info_fatti} 🛠️✨ In parole povere, questo è tutto quello che sta succedendo in questo momento sul gioco. Preparate i pad e godetevi la novità! 💯🎮🔥"
                
                st.markdown(f"""
                <div class="article-box">
                    <h3>📝 ARTICOLO GENERATO IN STILE GAMING</h3>
                    <p style="font-size: 18px; line-height: 1.6; color: #00ff66;"><b>{random.choice(intro_list)}</b></p>
                    <p style="font-size: 16px; line-height: 1.6;">{corpo_art}</p>
                    <hr style="border-color: #9400D3;">
                    <p style="font-size: 14px; color: #b19cd9;">📌 <b>Titolo originale:</b> {n['titolo']}</p>
                    <p style="font-size: 15px;">🎮 <i>Stay tuned e GG a tutti!</i> 🚀✨</p>
                </div>
                """, unsafe_allow_html=True)
else:
    if cerca_btn:
        st.warning("Nessuna notizia trovata nelle ultime ore per questa ricerca. Prova a cambiare parole chiave o a scrivere il nome del gioco in inglese!")
    else:
        st.info("👈 Scrivi un gioco nella barra laterale e clicca su 'Cerca News Globali'!")
