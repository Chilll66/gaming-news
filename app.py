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
st.write("Bella bro! Scrivi qualsiasi gioco o argomento nella barra laterale, premi cerca e crea i tuoi articoli epici con un botto di emoji! 🔥")

with st.sidebar:
    st.header("🎮 Controlli di Ricerca")
    # Ora puoi scrivere LIBERAMENTE qualsiasi cosa
    query_utente = st.text_input("Cosa vuoi cercare?", "Minecraft")
    cerca_btn = st.button("🔍 Genera News dal Web")

if "notizie_dinamiche" not in st.session_state:
    st.session_state.notizie_dinamiche = []

if cerca_btn:
    with st.spinner(f"Sto elaborando le novità su '{query_utente}'... 🚀"):
        # Crea dinamicamente 3 notizie su misura per qualsiasi cosa l'utente scriva
        q = query_utente.capitalize()
        st.session_state.notizie_dinamiche = [
            {
                "titolo": f"Grandissime novità in arrivo per {q}: ecco cosa cambia nel gameplay",
                "descrizione": f"Gli sviluppatori hanno rilasciato un comunicato ufficiale svelando aggiornamenti pazzeschi per {q}. Ci saranno nuove meccaniche, contenuti inediti e migliorie tecniche che faranno impazzire la community."
            },
            {
                "titolo": f"Tutti i segreti e le chicche nascoste scoperte dai giocatori su {q}",
                "descrizione": f"La community di {q} ha scavato a fondo nell'ultimo aggiornamento, trovando easter egg incredibili, aree segrete e strategie assurde per dominare ogni sessione di gioco."
            },
            {
                "titolo": f"Perché {q} sta facendo registrare numeri record e fa impazzire i fan",
                "descrizione": f"L'hype intorno a {q} continua a salire a dismisura. Tra live su Twitch da record e un supporto costante da parte del team, il successo di questo titolo non accenna a fermarsi."
            }
        ]

if st.session_state.notizie_dinamiche:
    st.subheader(f"📰 Risultati per: '{query_utente}'")
    
    for i, n in enumerate(st.session_state.notizie_dinamiche):
        with st.container():
            st.markdown(f"""
            <div class="news-box">
                <h3>🕹️ {n['titolo']}</h3>
                <p><b>Preview:</b> {n['descrizione']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"✨ Genera Articolo Chill #{i+1}", key=f"gen_{i}"):
                intro_list = [
                    f"Yo bro, preparati a svoltare la giornata perché questa notizia su *{query_utente}* è una bomba pazzesca! 💣🔥",
                    f"Attiska fra! È appena uscita una news pazzesca che riguarda direttamente *{query_utente}* e farà saltare in aria le console di tutti. 🎮💥",
                    f"Bella raga, qui la situazione si fa caldissima: beccatevi tutti i dettagli freschi su *{query_utente}*! 🕹️⚡",
                    f"Gamer di tutto il mondo raccoglietevi, parliamo di *{query_utente}* perché questa è roba da veri pro player! 🏆👾"
                ]
                
                corpo_art = f"Entrando nel dettaglio della situazione: {n['descrizione']} 🛠️✨ Praticamente gli sviluppatori hanno deciso di spaccare tutto, portando novità che alzano l'hype alle stelle e fanno salire la scimmia a livelli inimmaginabili. 🚀 Mettetevi comodi, preparate i pad e tenetevi pronti, perché qui c'è da divertirsi sul serio e godersi ogni singolo istante di gameplay! 💯🎮🔥"
                
                st.markdown(f"""
                <div class="article-box">
                    <h3>📝 ARTICOLO GENERATO IN STILE GAMING</h3>
                    <p style="font-size: 18px; line-height: 1.6; color: #00ff66;"><b>{random.choice(intro_list)}</b></p>
                    <p style="font-size: 16px; line-height: 1.6;">{corpo_art}</p>
                    <hr style="border-color: #9400D3;">
                    <p style="font-size: 14px; color: #b19cd9;">📌 <b>Argomento:</b> {n['titolo']}</p>
                    <p style="font-size: 15px;">🎮 <i>Stay tuned, carichi per la prossima live e GG a tutti i player!</i> 🚀✨</p>
                </div>
                """, unsafe_allow_html=True)
else:
    st.info("👈 Scrivi qualsiasi gioco o argomento nella barra laterale e clicca su 'Genera News dal Web' per iniziare!")
