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
st.write("Bella bro! Scegli una categoria, trova le news e genera i tuoi articoli in stile chill & gaming con un botto di emoji! 🔥")

# Database di notizie di gaming pronte all'uso e sempre aggiornate nello stile
archivio_notizie = {
    "GTA VI": [
        {"titolo": "GTA VI: Nuovi dettagli sulla fisica e sulla mappa svelati dai leak", "body": "Rockstar ha fatto di nuovo centro: la mappa pare sia la più viva e dettagliata mai creata, con interazioni assurde."},
        {"titolo": "L'attesa per GTA VI fa impazzire la community: ecco cosa sappiamo sui veicoli", "body": "Personalizzazione estrema e modelli di guida rinnovati per il titolo più atteso del decennio."}
    ],
    "Brawl Stars": [
        {"titolo": "Brawl Stars: Arriva il nuovo aggiornamento con brawler inediti e modalità folli", "body": "Supercell ha annunciato modifiche al bilanciamento e una valanga di ricompense per tutti i player."},
        {"titolo": "Le migliori strategie per dominare la nuova stagione competitiva di Brawl Stars", "body": "Ecco i brawler più forti del momento da usare assolutamente per salire di grado in fretta."}
    ],
    "Uscite e Trailer": [
        {"titolo": "Annunciato a sorpresa un nuovo RPG d'azione che promette grafica fotorealistica", "body": "Un team indipendente ha svelato un trailer epico che sta già facendo sbavare tutti gli amanti del genere."},
        {"titolo": "Nuovo trailer mozzafiato per il kolossal videoludico in arrivo questo inverno", "body": "Combattimenti frenetici, lore profonda e colonna sonora spaziale: preparate i portafogli."}
    ],
    "Serie TV e Film": [
        {"titolo": "Rilasciato il primo trailer ufficiale della serie TV basata sul celebre videogioco", "body": "I fan sono in estasi: la cura dei dettagli scenografici sembra perfetta e fedele al capolavoro originale."},
        {"titolo": "Confermato il cast stellare per il film tratto dalla saga videoludica action", "body": "Le riprese sono ufficialmente iniziate e la direzione promette un'azione senza sosta sul grande schermo."}
    ]
}

with st.sidebar:
    st.header("🎮 Controlli")
    categoria = st.selectbox("Scegli categoria:", ["GTA VI", "Brawl Stars", "Uscite e Trailer", "Serie TV e Film"])
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
                <p><b>Preview:</b> {n['body']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"✨ Genera Articolo Chill #{i+1}", key=f"gen_{i}"):
                intro_list = [
                    "Yo bro, preparati a svoltare la giornata perché questa è una bomba pazzesca! 💣🔥",
                    "Attiska fra! È appena uscita una news che farà saltare in aria le vostre console. 🎮💥",
                    "Bella raga, qui la situazione si fa caldissima: beccatevi questa chicca! 🕹️⚡",
                    "Gamer di tutto il mondo raccoglietevi, questa è roba da veri pro player! 🏆👾"
                ]
                
                corpo_list = [
                    f"Analizzando la situa su *{n['titolo']}*, sembra proprio che gli sviluppatori abbiano deciso di spaccare tutto. 🛠️✨ Tra chicche succose e hype alle stelle, c'è da esaltarsi forte. 🚀",
                    f"Mettetevi comodi perché la novità fresca fresca spacca di brutto. 🎯 Hype a mille e pad alla mano, qui c'è da divertirsi sul serio. 💯🎮",
                    f"Occhi puntati sullo schermo: le ultime novità promettono scintille. 🔥 Non so voi, ma io sto già sbroccando dalla scimmia! 🐒⚡"
                ]
                
                st.markdown(f"""
                <div class="article-box">
                    <h3>📝 ARTICOLO GENERATO IN STILE GAMING</h3>
                    <p style="font-size: 18px; line-height: 1.6;">{random.choice(intro_list)}</p>
                    <p style="font-size: 16px; line-height: 1.6;">{random.choice(corpo_list)}</p>
                    <p><b>Dettagli chiave:</b> {n['body']}</p>
                    <p>🎮 <i>Stay tuned e carichi per la prossima live! GG a tutti!</i> 🚀🔥</p>
                </div>
                """, unsafe_allow_html=True)
else:
    st.info("👈 Clicca su 'Carica Notizie' nella barra laterale per visualizzare le ultime novità pronte da elaborare!")
