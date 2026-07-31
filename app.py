import streamlit as st
import random
from duckduckgo_search import DDGS
import urllib.request
import json

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
st.write("Bella bro! Cerchiamo le notizie dell'ultima settimana, tradotte in italiano, pulite dallo spam e pronte per essere trasformate in articoli epici! 🔥")

with st.sidebar:
    st.header("🎮 Controlli di Ricerca")
    query_utente = st.text_input("Cosa vuoi cercare?", "Fortnite skin")
    cerca_btn = st.button("🔍 Cerca News dell'Ultima Settimana")

def traduci_in_italiano(testo):
    try:
        if not testo:
            return ""
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=it&dt=t&q={urllib.parse.quote(testo)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            return "".join([item[0] for item in res[0]])
    except:
        return testo

def cerca_news_settimana(termine):
    try:
        results = []
        with DDGS() as ddgs:
            # Filtro impostato esattamente sull'ultima settimana ('w') per avere news fresche ma senza buchi vuoti
            query_mirata = f"{termine} videogioco news"
            for r in ddgs.text(query_mirata, max_results=8, timelimit='w'):
                titolo = r.get('title', '')
                body = r.get('body', '')
                url = r.get('href', '#')
                
                # Filtro anti-spam per bloccare siti fuffa o pubblicità
                parole_spazzatura = ['spa', 'hot tub', 'hotel', 'mattress', 'finance', 'real estate', 'idromassaggio', 'materasso']
                testo_totale = (titolo + " " + body).lower()
                
                is_spam = any(parola in testo_totale for parola in parole_spazzatura)
                
                if len(body) > 30 and not is_spam:
                    titolo_it = traduci_in_italiano(titolo)
                    body_it = traduci_in_italiano(body)
                    results.append({"titolo": titolo_it, "descrizione": body_it, "url": url})
                    
                    if len(results) >= 4:
                        break
        return results
    except Exception as e:
        return []

if "notizie_reali" not in st.session_state:
    st.session_state.notizie_reali = []

if cerca_btn:
    with st.spinner(f"Cerco le novità dell'ultima settimana su '{query_utente}'... 🚀"):
        st.session_state.notizie_reali = cerca_news_settimana(query_utente)

if st.session_state.notizie_reali:
    st.subheader(f"📰 News dell'ultima settimana per: '{query_utente}'")
    
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
                    "Yo bro, beccati questa news freschissima uscita in questi ultimi giorni! 💣🔥",
                    "Attiska fra! Guarda cosa è appena uscito nel mondo del gaming, andiamo dritti al sodo! 🎮💥",
                    "Bella raga, beccatevi questo aggiornamento caldissimo della settimana: ecco i fatti! 🕹️⚡",
                    "Gamer, zero giri di parole: ecco la novità della settimana spiegata pulita e semplice! 🏆👾"
                ]
                
                info_fatti = n['descrizione']
                if dettaglio_extra:
                    info_fatti = f"{info_fatti} Nello specifico: {dettaglio_extra}"
                
                corpo_art = f"Ecco esattamente cosa dice la notizia, senza fronzoli: {info_fatti} 🛠️✨ In parole povere, questo è tutto quello che sta succedendo sul gioco in questi giorni. Preparate i pad e godetevi la novità! 💯🎮🔥"
                
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
        st.warning("Nessuna notizia trovata per questa ricerca nell'ultima settimana. Prova a scrivere un termine leggermente diverso!")
    else:
        st.info("👈 Scrivi un gioco nella barra laterale e clicca su 'Cerca News dell'Ultima Settimana'!")
