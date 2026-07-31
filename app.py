import streamlit as st
import random

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
st.write("Bella bro! Scegli una categoria, seleziona la news e guarda come viene trasformata in un articolo epico e ricco di dettagli! 🔥")

archivio_notizie = {
    "GTA VI": [
        {
            "titolo": "GTA VI: Nuovi dettagli sulla fisica e sulla mappa svelati dai leak", 
            "descrizione": "Rockstar ha implementato un sistema di intelligenza artificiale avanzato per i NPC, rendendo la città incredibilmente viva. La mappa, ambientata a Leonida, offrirà zone rurali immense e una fisica dei veicoli completamente ridisegnata per simulare ogni singolo impatto."
        },
        {
            "titolo": "L'attesa per GTA VI fa impazzire la community: ecco cosa sappiamo sui veicoli", 
            "descrizione": "I fan hanno analizzato ogni singolo frame del trailer scoprendo oltre 50 tipi di veicoli inediti, con una personalizzazione estetica e meccanica mai vista prima nella storia della saga di Rockstar."
        }
    ],
    "Brawl Stars": [
        {
            "titolo": "Brawl Stars: Arriva il nuovo aggiornamento con brawler inediti e modalità folli", 
            "descrizione": "Supercell ha introdotto due nuovi brawler leggendari dotati di abilità uniche che stravolgeranno il meta competitivo. In più, è stata aggiunta una modalità a tempo limitato con mappe create interamente dalla community."
        },
        {
            "titolo": "Le migliori strategie per dominare la nuova stagione competitiva di Brawl Stars", 
            "descrizione": "Con l'ultimo bilanciamento delle statistiche, i personaggi di supporto sono diventati fondamentali. Gli esperti consigliano composizioni mirate al controllo della mappa per scalare i ranghi senza sforzo."
        }
    ],
    "Uscite e Trailer": [
        {
            "titolo": "Annunciato a sorpresa un nuovo RPG d'azione che promette grafica fotorealistica", 
            "descrizione": "Sviluppato con Unreal Engine 5, questo titolo vanta un sistema di combattimento dinamico all'arma bianca e una storia immersiva dove ogni scelta del giocatore cambia radicalmente il corso degli eventi."
        },
        {
            "titolo": "Nuovo trailer mozzafiato per il kolossal videoludico in arrivo questo inverno", 
            "descrizione": "Il filmato mostra sequenze di gameplay mozzafiato, esplorazione spaziale senza interruzioni di caricamento e boss fight colossali che richiedono una cooperazione totale tra i membri del team."
        }
    ],
    "Serie TV e Film": [
        {
            "titolo": "Rilasciato il primo trailer ufficiale della serie TV basata sul celebre videogioco", 
            "descrizione": "Il video mostra un'ambientazione post-apocalittica curata nei minimi dettagli, con costumi fedelissimi e un'atmosfera cupa che ha fatto subito esaltare i fan storici del franchise."
        },
        {
            "titolo": "Confermato il cast stellare per il film tratto dalla saga videoludica action", 
            "descrizione": "Gli attori principali si stanno già sottoponendo a mesi di allenamento fisico intenso per girare le scene d'azione senza controfigure, promettendo uno spettacolo degno delle sale cinematografiche."
        }
    ]
}

with st.sidebar:
    st.header("🎮 Controlli")
    categoria = st.selectbox("Scegli categoria:", list(archivio_notizie.keys()))
    cerca_btn = st.button("🔍 Carica Notizie")

if "notizie_correnti" not in st.session_state:
    st.session_state.notizie_correnti = []

if cerca_btn:
    with st.spinner("Caricamento notizie in corso... 🚀"):
        st.session_state.notizie_correnti = archivio_notizie.get(categoria, [])

if st.session_state.notizie_correnti:
    st.subheader(f"📰 Notizie fresche per: {categoria}")
    
    for i, n in enumerate(st.session_state.notizie_correnti):
        with st.container():
            st.markdown(f"""
            <div class="news-box">
                <h3>🕹️ {n['titolo']}</h3>
                <p><b>Preview:</b> {n['descrizione']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"✨ Genera Articolo Chill #{i+1}", key=f"gen_{i}"):
                # Intro sempre diverse
                intro_list = [
                    f"Yo bro, preparati a svoltare la giornata perché questa notizia su *{n['titolo']}* è una bomba pazzesca! 💣🔥",
                    f"Attiska fra! È appena uscita una news pazzesca che riguarda direttamente *{n['titolo']}* e farà saltare in aria le console di tutti. 🎮💥",
                    f"Bella raga, qui la situazione si fa caldissima: beccatevi tutti i dettagli freschi su *{n['titolo']}*! 🕹️⚡",
                    f"Gamer di tutto il mondo raccoglietevi, parliamo di *{n['titolo']}* perché questa è roba da veri pro player! 🏆👾"
                ]
                
                # Corpo che riassume ed elabora specificamente la notizia
                corpo_art = f"Entrando nel dettaglio della situazione: {n['descrizione']} 🛠️✨ Praticamente gli sviluppatori hanno deciso di spaccare tutto, portando novità che alzano l'hype alle stelle e fanno salire la scimmia a livelli inimmaginabili. 🚀 Mettetevi comodi, preparate i pad e tenetevi pronti, perché qui c'è da divertirsi sul serio e godersi ogni singolo istante di gameplay! 💯🎮🔥"
                
                st.markdown(f"""
                <div class="article-box">
                    <h3>📝 ARTICOLO GENERATO IN STILE GAMING</h3>
                    <p style="font-size: 18px; line-height: 1.6; color: #00ff66;"><b>{random.choice(intro_list)}</b></p>
                    <p style="font-size: 16px; line-height: 1.6;">{corpo_art}</p>
                    <hr style="border-color: #9400D3;">
                    <p style="font-size: 14px; color: #b19cd9;">📌 <b>Notizia originale di riferimento:</b> {n['titolo']}</p>
                    <p style="font-size: 15px;">🎮 <i>Stay tuned, carichi per la prossima live e GG a tutti i player!</i> 🚀✨</p>
                </div>
                """, unsafe_allow_html=True)
else:
    st.info("👈 Clicca su 'Carica Notizie' nella barra laterale per visualizzare le ultime novità pronte da elaborare!")
