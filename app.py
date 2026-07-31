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
st.write("Bella bro! Qui trovi le news fresche di giochi, uscite, serie TV e aggiornamenti. Niente noie finanziarie, solo hype puro! 🔥")

# Barra laterale per i comandi
with st.sidebar:
    st.header("🎮 Controlli")
    # Filtriamo già la ricerca per evitare fatturati e soldi
    query_base = st.text_input("Cosa cerchiamo?", "nuovi videogiochi uscite DLC trailer")
    cerca_btn = st.button("🔍 Cerca Notizie")

def cerca_notizie(termine):
    try:
        results = []
        # Aggiungiamo termini per scartare finanza/azioni
        query_finale = f"{termine} -azioni -finanza -borsa -ricavi -fatturato"
        with DDGS() as ddgs:
            for r in ddgs.text(query_finale, max_results=6):
                titolo = r.get('title', '')
                body = r.get('body', '')
                url = r.get('href', '')
                # Filtro extra di sicurezza anti-soldi nel titolo
                parole_escluse = ['azioni', 'borsa', 'milioni di euro', 'fatturato', 'utili', 'ricavi']
                if not any(p in titolo.lower() for p in parole_escluse):
                    results.append({"titolo": titolo, "body": body, "url": url})
        return results
    except Exception as e:
        return []

if "notizie" not in st.session_state:
    st.session_state.notizie = []

if cerca_btn:
    with st.spinner("Sto scandagliando il web alla ricerca di hype... 🚀"):
        st.session_state.notizie = cerca_notizie(query_base)

# Sezione griglia a quadrati
if st.session_state.notizie:
    st.subheader("📰 Seleziona la notizia da sbrogliare:")
    
    for i, n in enumerate(st.session_state.notizie):
        with st.container():
            st.markdown(f"""
            <div class="news-box">
                <h3>🕹️ {n['titolo']}</h3>
                <p><b>Preview:</b> {n['body']}</p>
                <a href="{n['url']}" target="_blank" style="color: #00ff66; font-weight: bold;">🔗 Apri fonte originale</a>
            </div>
            """, unsafe_allow_html=True)
            
            # Pulsante unico per ogni quadrato
            if st.button(f"✨ Genera Articolo Chill #{i+1}", key=f"gen_{i}"):
                intro_list = [
                    "Yo bro, preparati a svoltare la giornata perché questa è una bomba pazzesca! 💣🔥",
                    "Attiska fra! È appena uscita una news che farà saltare in aria le vostre console. 🎮💥",
                    "Bella raga, qui la situazione si fa caldissima: beccatevi questa chicca! 🕹️⚡",
                    "Gamer di tutto il mondo raccoglietevi, questa è roba da veri pro player! 🏆👾"
                ]
                
                corpo_list = [
                    f"Analizzando la situa su *{n['titolo']}*, sembra proprio che gli sviluppatori abbiano deciso di spaccare tutto. 🛠️✨ Tra chicche succose ehype alle stelle, c'è da esaltarsi forte. 🚀",
                    f"Mettetevi comodi perché la novità fresca fresca riguarda *{n['titolo']}*. 🎯 Hype a mille e pad alla mano, qui c'è da divertirsi sul serio. 💯🎮",
                    f"Occhi puntati sullo schermo: le ultime news su *{n['titolo']}* promettono scintille. 🔥 Non so voi, ma io sto già sbroccando dalla scimmia! 🐒⚡"
                ]
                
                out_intro = random.choice(intro_list)
                out_corpo = random.choice(corpo_list)
                
                st.markdown(f"""
                <div class="article-box">
                    <h3>📝 ARTICOLO GENERATO IN STILE GAMING</h3>
                    <p style="font-size: 18px; line-height: 1.6;">{out_intro}</p>
                    <p style="font-size: 16px; line-height: 1.6;">{out_corpo}</p>
                    <p><b>Dettagli al volo:</b> {n['body']}</p>
                    <p>🎮 <i>Stay tuned e carichi per la prossima live! GG a tutti!</i> 🚀🔥</p>
                </div>
                """, unsafe_allow_html=True)
else:
    if cerca_btn:
        st.warning("Nessuna news trovata o i filtri anti-finanza sono stati troppi stretti. Prova a cercare un altro gioco!")
