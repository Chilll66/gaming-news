import streamlit as st
import random
import urllib.request
import json
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime

# Configurazione della pagina
st.set_page_config(page_title="Gaming News Generator Pro", page_icon="🎮", layout="wide")

# Stile Grafico Cyberpunk
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

st.title("⚡ GAMING NEWS GENERATOR (RAPIDO & EMOSHOOT) ⚡")
st.write("Versione corta, ricca di emoji e dritta al sodo senza papiri illeggibili! 🔥")

# Barra laterale per i controlli di ricerca
with st.sidebar:
    st.header("🎮 Controlli di Ricerca")
    query_utente = st.text_input("Cosa vuoi cercare?", "Fortnite update")
    cerca_btn = st.button("🔍 Cerca News Rapide")

# Funzione di traduzione intelligente con termini tecnici protetti
def traduci_in_italiano(testo):
    try:
        if not testo:
            return ""
        
        termini_protetti = {
            "easter egg": "###EASTER_EGG###",
            "hypercharge": "###HYPERCHARGE###",
            "skin": "###SKIN###",
            "skins": "###SKINS###",
            "patch notes": "###PATCH_NOTES###",
            "update": "###UPDATE###",
            "buff": "###BUFF###",
            "nerf": "###NERF###",
            "ranked": "###RANKED###",
            "esports": "###ESPORTS###"
        }
        
        testo_protetto = testo
        for k, v in termini_protetti.items():
            testo_protetto = testo_protetto.replace(k, v).replace(k.capitalize(), v).replace(k.upper(), v)

        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=it&dt=t&q={urllib.parse.quote(testo_protetto)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            traduzione = "".join([item[0] for item in res[0]])
            
            ripristini = {
                "###EASTER_EGG###": "easter egg",
                "###HYPERCHARGE###": "hypercharge",
                "###SKIN###": "skin",
                "###SKINS###": "skins",
                "###PATCH_NOTES###": "patch notes",
                "###UPDATE###": "update",
                "###BUFF###": "buff",
                "###NERF###": "nerf",
                "###RANKED###": "ranked",
                "###ESPORTS###": "esports"
            }
            for k, v in ripristini.items():
                traduzione = traduzione.replace(k, v).replace(k.lower(), v)
                
            return traduzione
    except:
        return testo

# Funzione per estrarre solo frasi brevi, succose e dirette (massimo 3 punti compatti)
def estrai_contenuti_brevi(url):
    try:
        if not url or url.startswith("#"):
            return []
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=8) as response:
            html = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            
            for elem in soup(["script", "style", "nav", "footer", "header", "aside", "form", "iframe"]):
                elem.decompose()
                
            contenitore = soup.find('article') or soup.find('main') or soup.find('div', class_=['content', 'post-content', 'entry-content', 'article-body'])
            target_soup = contenitore if contenitore else soup
            
            elementi = target_soup.find_all(['p', 'li'])
            
            punti_brevi = []
            parole_da_scartare = ['cookie', 'privacy', 'tutti i diritti', 'rights reserved', 'iscriviti', 'newsletter', 'rimani aggiornato', 'gamsgo', 'gemme economiche', 'social media', 'seguici su', 'remixa questo elenco']
            
            for el in elementi:
                txt = el.get_text().strip()
                # Prendiamo frasi di media lunghezza (evitando papiri o righe vuote)
                if 50 < len(txt) < 180 and not any(p in txt.lower() for p in parole_da_scartare):
                    tradotto = traduci_in_italiano(txt)
                    if tradotto and tradotto not in punti_brevi:
                        punti_brevi.append(tradotto)
                        
            return punti_brevi[:3] # Solo i 3 punti più importanti per mantenere l'articolo corto!
    except Exception as e:
        return []

# Funzione di ricerca web
def cerca_news_profonda(termine):
    try:
        results = []
        url_ricerca = "https://lite.duckduckgo.com/lite/"
        
        anno_corrente = datetime.now().year
        stringa_query = f"{termine} update details {anno_corrente}"
        
        dati_post = urllib.parse.urlencode({
            'q': stringa_query,
            'df': 'w'
        }).encode('utf-8')
        
        req = urllib.request.Request(url_ricerca, data=dati_post, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            
            links = soup.find_all('a', class_='result-link')
            snippets = soup.find_all('td', class_='result-snippet')
            
            for i in range(min(len(links), len(snippets), 6)):
                titolo = links[i].get_text().strip()
                href = links[i]['href'] if 'href' in links[i].attrs else "#"
                snippet_base = snippets[i].get_text().strip()
                
                parole_spazzatura = ['spa', 'hot tub', 'hotel', 'mattress', 'finance', 'real estate', 'idromassaggio', 'materasso']
                testo_totale = (titolo + " " + snippet_base).lower()
                is_spam = any(p in testo_totale for p in parole_spazzatura)
                
                if len(snippet_base) > 20 and not is_spam:
                    punti = estrai_contenuti_brevi(href)
                    if len(punti) >= 2:
                        titolo_it = traduci_in_italiano(titolo)
                        results.append({"titolo": titolo_it, "punti": punti, "url": href})
                    
                    if len(results) >= 3:
                        break
                        
        if not results:
            results.append({
                "titolo": f"Aggiornamento rapido su {termine}",
                "punti": [
                    f"Rilasciato un nuovo update per {termine} con modifiche mirate.",
                    "Arrivano contenuti freschi e bilanciamenti richiesti dalla community."
                ],
                "url": f"https://www.google.com/search?q={urllib.parse.quote(termine + ' update')}"
            })
            
        return results
    except Exception as e:
        return []

# Gestione dello stato della sessione
if "notizie_reali" not in st.session_state:
    st.session_state.notizie_reali = []

if cerca_btn:
    with st.spinner(f"Ricerca rapida per '{query_utente}'... 🚀"):
        st.session_state.notizie_reali = cerca_news_profonda(query_utente)

# Visualizzazione dei risultati e generazione articoli unici
if st.session_state.notizie_reali:
    st.subheader(f"📰 News rapide per: '{query_utente}'")
    
    for i, n in enumerate(st.session_state.notizie_reali):
        with st.container():
            testo_anteprima = "".join([f"<li>{p}</li>" for p in n['punti']])
            st.markdown(f"""
            <div class="news-box">
                <h3>🕹️ {n['titolo']}</h3>
                <p><b>Anteprima veloce:</b></p>
                <ul style="line-height: 1.5; color: #00ff66;">{testo_anteprimina if 'testo_anteprimina' in locals() else testo_anteprima}</ul>
                <a href="{n['url']}" target="_blank" style="color: #9400D3; font-weight: bold;">🔗 Fonte originale</a>
            </div>
            """, unsafe_allow_html=True)
            
            dettaglio_extra = st.text_input(f"Aggiungi una nota al volo (opzionale) #{i+1}:", key=f"extra_{i}")
            
            if st.button(f"✨ Genera Articolo Corto #{i+1}", key=f"gen_{i}"):
                intro_list = [
                    f"Yo bro! 🎮🔥 Beccati questa news lampo su {query_utente}: corta, intensa e dritta al punto! 💣✨",
                    f"Attiska fra! 🚀👾 Ecco il succo dell'update in pochissime righe, senza giri di parole. 🔮💥",
                    f"Bella raga! 🕹️⚡ Sintesi perfetta e veloce con tutte le novità fresche arrivate in game! 🌟🔥"
                ]
                
                outro_list = [
                    "Che ne pensate? 🎮💬 Scrivetelo nei commenti e spaccate tutto in game! 🚀🔥",
                    "Preparate i controller raga! 🕹️💯 Ci becciamo direttamente in lobby. 🏆✨",
                    "Mettetevi all'opera e testate subito le novità! 👾🔥 GG a tutti! 🚀🎮"
                ]
                
                # Montiamo i punti corti con tantissime emoji colorate in mezzo
                emoji_elenco = ["🎯", "🔥", "⚡", "💎", "🚀", "👾", "🌟"]
                corpo_punti = ""
                for idx, punto in enumerate(n['punti']):
                    emj1 = emoji_elenco[idx % len(emoji_elenco)]
                    emj2 = emoji_elenco[(idx + 1) % len(emoji_elenco)]
                    corpo_punti += f"<p style='font-size: 16px; line-height: 1.6; margin-bottom: 12px;'>{emj1} {punto} {emj2}</p>"
                
                extra_html = f"<p style='font-size: 16px; line-height: 1.6; color: #00ff66; margin-top: 10px;'>💎 Nota extra: {dettaglio_extra} 🚀</p>" if dettaglio_extra else ""
                
                # Stampiamo l'articolo pulito senza errori di codice finali
                st.markdown(f"""
                <div class="article-box">
                    <h3>📝 ARTICOLO LAMPO E COLORATO</h3>
                    <p style="font-size: 18px; line-height: 1.6; color: #00ff66;"><b>{random.choice(intro_list)}</b></p>
                    <br>
                    {corpo_punti}
                    {extra_html}
                    <hr style="border-color: #9400D3; margin-top: 20px; margin-bottom: 20px;">
                    <p style="font-size: 16px; line-height: 1.6; color: #00ff66;"><b>{random.choice(outro_list)}</b></p>
                    <p style="font-size: 13px; color: #b19cd9; margin-top: 15px;">📌 <i>Fonte: {n['titolo']}</i></p>
                </div>
                """, unsafe_allow_html=True)
else:
    if cerca_btn:
        st.warning("Nessuna notizia trovata. Prova a cambiare i termini di ricerca.")
    else:
        st.info("👈 Scrivi un gioco nella barra laterale e clicca su 'Cerca News Rapide'!")
