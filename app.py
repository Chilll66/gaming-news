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
st.write("Bella bro! Scrivi qualsiasi gioco o argomento: l'app pescherà le notizie vere di oggi e ieri dal web per trasformarle in articoli dettagliati, semplici e pieni di emoji! 🔥")

with st.sidebar:
    st.header("🎮 Controlli di Ricerca")
    query_utente = st.text_input("Cosa vuoi cercare?", "Fortnite")
    cerca_btn = st.button("🔍 Cerca News di Oggi")

def cerca_notizie_reali(termine):
    try:
        results = []
        with DDGS() as ddgs:
            for r in ddgs.text(f"{termine} videogame news", max_results=4, timelimit='d'):
                titolo = r.get('title', 'Notizia gaming')
                body = r.get('body', 'Nessun dettaglio disponibile.')
                url = r.get('href', '#')
                results.append({"titolo": titolo, "descrizione": body, "url": url})
        return results
    except Exception as e:
        return []

if "notizie_reali" not in st.session_state:
    st.session_state.notizie_reali = []

if cerca_btn:
    with st.spinner(f"Sto scandagliando il web per trovare le novità di oggi su '{query_utente}'... 🚀"):
        st.session_state.notizie_reali = cerca_notizie_reali(query_utente)

if st.session_state.notizie_reali:
    st.subheader(f"📰 Notizie fresche (Oggi/Ieri) per: '{query_utente}'")
    
    for i, n in enumerate(st.session_state.notizie_reali):
        with st.container():
            st.markdown(f"""
            <div class="news-box">
                <h3>🕹️ {n['titolo']}</h3>
                <p><b>Cosa dice la notizia:</b> {n['descrizione']}</p>
                <a href="{n['url']}" target="_blank" style="color: #00ff66; font-weight: bold;">🔗 Fonte originale</a>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"✨ Genera Articolo Dettagliato #{i+1}", key=f"gen_{i}"):
                # Lista enorme di intro tutte diverse per non ripetersi mai
                intro_list = [
                    "Yo bro, beccati questa bomba freschissima uscita proprio tra ieri e oggi! 💣🔥",
                    "Madonna fra! Guarda cosa è appena successo nel mondo del gaming, notizia caldissima! 🎮💥",
                    "Bella raga, c'è un aggiornamento pazzesco che è uscito in queste ore: facciamo il punto! 🕹️⚡",
                    "Gamer di tutto il mondo, occhi aperti: ecco la novità del giorno spiegata semplice! 🏆👾",
                    "Attiska fra! Questa ti farà saltare dalla sedia, guarda che chicca è appena arrivata! 🚀🔥",
                    "Raga, tenetevi forte perché quello che sta succedendo in queste ore ha dell'incredibile! 🎯💯",
                    "Occhi allo schermo player! Tra ieri e oggi è uscita una news che spacca letteralmente i server! 🌐✨",
                    "Bella zio! Preparati i popcorn e il pad, perché la novità fresca di oggi è pura roba da pro! 🎮👑"
                ]
                
                corpo_art = f"Allora, la situazione nel dettaglio è questa: {n['descrizione']} 🛠️✨ In parole semplici, significa che gli sviluppatori hanno fatto questa mossa per migliorare l'esperienza di gioco e dare ai fan esattamente quello che aspettavano. L'hype è salito alle stelle e la community sta già reagendo alla grande! 🚀 Mettetevi comodi, preparate i pad e godetevi ogni novità di questa chicca! 💯🎮🔥"
                
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
        st.warning("Nessuna notizia trovata per questa ricerca specifica nelle ultime ore. Prova a scrivere un altro gioco o un termine più generale!")
    else:
        st.info("👈 Scrivi un gioco nella barra laterale e clicca su 'Cerca News di Oggi' per trovare le ultime novità reali!")
