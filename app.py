import streamlit as st
import random
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
st.write("Bella bro! Scrivi qualsiasi gioco o argomento: l'app pescherà i dettagli specifici di oggi e ieri dal web (collaborazioni, skin, aggiornamenti) e li trasformerà in articoli epici, semplici e pieni di emoji! 🔥")

with st.sidebar:
    st.header("🎮 Controlli di Ricerca")
    query_utente = st.text_input("Cosa vuoi cercare?", "Fortnite skin")
    cerca_btn = st.button("🔍 Cerca News Dettagliate")

def cerca_notizie_specifiche(termine):
    try:
        results = []
        with DDGS() as ddgs:
            # Cerchiamo con termini specifici per catturare dettagli, skin e collaborazioni
            for r in ddgs.text(f"{termine} dettagli skin collaborazione aggiornamento", max_results=4, timelimit='d'):
                titolo = r.get('title', 'Notizia gaming')
                body = r.get('body', 'Nessun dettaglio specifico disponibile.')
                url = r.get('href', '#')
                results.append({"titolo": titolo, "descrizione": body, "url": url})
        return results
    except Exception as e:
        return []

if "notizie_reali" not in st.session_state:
    st.session_state.notizie_reali = []

if cerca_btn:
    with st.spinner(f"Sto analizzando a fondo il web per trovare tutti i dettagli su '{query_utente}'... 🚀"):
        st.session_state.notizie_reali = cerca_notizie_specifiche(query_utente)

if st.session_state.notizie_reali:
    st.subheader(f"📰 Notizie specifiche e dettagliate per: '{query_utente}'")
    
    for i, n in enumerate(st.session_state.notizie_reali):
        with st.container():
            st.markdown(f"""
            <div class="news-box">
                <h3>🕹️ {n['titolo']}</h3>
                <p><b>Contenuto specifico:</b> {n['descrizione']}</p>
                <a href="{n['url']}" target="_blank" style="color: #00ff66; font-weight: bold;">🔗 Fonte originale completa</a>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"✨ Genera Articolo Dettagliato #{i+1}", key=f"gen_{i}"):
                intro_list = [
                    "Yo bro, beccati questa bomba freschissima con tutti i dettagli precisi usciti in queste ore! 💣🔥",
                    "Madonna fra! Guarda che roba assurda è appena stata svelata nel mondo del gaming, entriamo subito nel vivo! 🎮💥",
                    "Bella raga, ci sono novità pazzesche e super specifiche: ecco esattamente cosa sta succedendo! 🕹️⚡",
                    "Gamer di tutto il mondo, occhi aperti: ecco il report completo e dettagliato della notizia del giorno! 🏆👾",
                    "Attiska fra! Questa è una chicca imperdibile, beccati tutti i retroscena e le novità svelate! 🚀🔥",
                    "Raga, tenetevi forte perché abbiamo tutti i dettagli succosi di questa news appena sfornata! 🎯💯"
                ]
                
                # Articolo strutturato per sviscerare specificamente cosa dice la notizia (collaborazioni, skin, contenuti)
                corpo_art = f"Entriamo subito nei dettagli di quello che sta succedendo: {n['descrizione']} 🛠️✨ In parole molto semplici e dirette, la notizia ci svela esattamente tutti i retroscena, i contenuti e le particolarità di questa novità. Che si tratti di una skin pazzesca, di una collaborazione inaspettata o di un aggiornamento del gameplay, la community ha già iniziato a esaltarsi forte. L'hype è alle stelle e i fan non vedono l'ora di mettere le mani su tutto questo ben di dio! 🚀 Mettetevi comodi, preparate i pad e godetevi ogni singolo dettaglio di questa chicca! 💯🎮🔥"
                
                st.markdown(f"""
                <div class="article-box">
                    <h3>📝 ARTICOLO GENERATO IN STILE GAMING</h3>
                    <p style="font-size: 18px; line-height: 1.6; color: #00ff66;"><b>{random.choice(intro_list)}</b></p>
                    <p style="font-size: 16px; line-height: 1.6;">{corpo_art}</p>
                    <hr style="border-color: #9400D3;">
                    <p style="font-size: 14px; color: #b19cd9;">📌 <b>Notizia originale:</b> {n['titolo']}</p>
                    <p style="font-size: 15px;">🎮 <i>Stay tuned, carichi per la prossima live e GG a tutti!</i> 🚀✨</p>
                </div>
                """, unsafe_allow_html=True)
else:
    if cerca_btn:
        st.warning("Nessuna notizia specifica trovata nelle ultime ore per questa ricerca. Prova a scrivere il nome del gioco insieme a 'skin', 'aggiornamento' o 'collaborazione'!")
    else:
        st.info("👈 Scrivi un gioco o un evento nella barra laterale (es. *Fortnite skin* o *Brawl Stars aggiornamento*) e clicca su 'Cerca News Dettagliate'!")
