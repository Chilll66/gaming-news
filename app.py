import streamlit as st

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
st.write("Bella bro! Qui trovi le tue notizie fresche fresche in stile chill & gaming.")

with st.sidebar:
    st.header("🎮 Controlli")
    if st.button("🔍 Cerca Nuove Notizie"):
        st.success("Ricerca avviata nel web!")

st.subheader("📰 Notizie pronte da elaborare")
st.markdown("""
<div class="news-box">
    <h3>Uscita epica in arrivo per il nuovo RPG</h3>
    <p><b>Fonte:</b> Web Gaming</p>
    <p><i>Anteprima:</i> Annunciata la data ufficiale...</p>
</div>
""", unsafe_allow_html=True)

if st.button("✨ Genera Testo Notizia (Stile Chill)"):
    st.info("Yo bro, beccati questa: sembra proprio che gli sviluppatori abbiano spaccato stavolta, preparate i pad!")
