import streamlit as st
import random
import urllib.request
import json
import urllib.parse
from bs4 import BeautifulSoup

# Configurazione della pagina
st.set_page_config(page_title="Gaming News Generator", page_icon="🎮", layout="wide")

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

st.title("⚡ GAMING NEWS GENERATOR ⚡")
st.write("Bella bro! Generatore potenziato con estrazione contenuti reali e variabilità infinita degli articoli! 🔥")

# Barra laterale per i controlli di ricerca
with st.sidebar:
    st.header("🎮 Controlli di Ricerca")
    query_utente = st.text_input("Cosa vuoi cercare?", "Brawl Stars")
    cerca_btn = st.button("🔍 Cerca News")

# Funzione di traduzione automatica in italiano
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

# Funzione potenziata per estrarre il vero contenuto dall'interno del sito web
def estrai_contenuto_articolo(url):
    try:
        if not url or url.startswith("#"):
            return ""
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=6) as response:
            html = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            
            # Rimuoviamo elementi inutili come script, menu, footer e pubblicità
            for elem in soup(["script", "style", "nav", "footer", "header", "aside", "form", "iframe"]):
                elem.decompose()
                
            # Cerchiamo prima nei blocchi principali dell'articolo se esistono
            contenitore_principale = soup.find('article') or soup.find('main') or soup.find('div', class_=['content', 'post-content', 'entry-content', 'article-body'])
            
            target_soup = contenitore_principale if contenitore_principale else soup
            paragrafi = target_soup.find_all('p')
            
            testi_utili = []
            for p in paragrafi:
                txt = p.get_text().strip()
                # Filtriamo i paragrafi troppo corti o che sembrano menu/cookie
                if len(txt) > 40 and not any(parola in txt.lower() for parola in ['cookie', 'privacy', 'tutti i diritti', 'rights reserved', 'iscriviti', 'newsletter']):
                    testi_utili.append(txt)
                    
            testo_completo = " ".join(testi_utili)
            
            if len(testo_completo) > 150:
                return traduci_in_italiano(testo_completo[:1200])
            return ""
    except:
        return ""

# Funzione di ricerca web
def cerca_news_profonda(termine):
    try:
        results = []
        url_ricerca = "https://lite.duckduckgo.com/lite/"
        dati_post = urllib.parse.urlencode({'q': f"{termine} gaming news update patch"}).encode('utf-8')
        
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
                
                if len(snippet_base) > 10 and not is_spam:
                    # Estraiamo il contenuto reale approfondito dal sito
                    contenuto_reale = estrai_contenuto_articolo(href)
                    
                    # Se il contenuto estratto è valido e corposo usiamo quello, altrimenti ripieghiamo sulla snippet tradotta
                    descrizione_finale = contenuto_reale if len(contenuto_reale) > 100 else traduci_in_italiano(snippet_base)
                    
                    titolo_it = traduci_in_italiano(titolo)
                    results.append({"titolo": titolo_it, "descrizione": descrizione_finale, "url": href})
                    
                    if len(results) >= 4:
                        break
        return results
    except Exception as e:
        return []

# Gestione dello stato della sessione
if "notizie_reali" not in st.session_state:
    st.session_state.notizie_reali = []

if cerca_btn:
    with st.spinner(f"Scandaglio i server e leggo gli articoli per '{query_utente}'... 🚀"):
        st.session_state.notizie_reali = cerca_news_profonda(query_utente)

# Visualizzazione dei risultati e generazione articoli unici
if st.session_state.notizie_reali:
    st.subheader(f"📰 News approfondite trovate per: '{query_utente}'")
    
    for i, n in enumerate(st.session_state.notizie_reali):
        with st.container():
            st.markdown(f"""
            <div class="news-box">
                <h3>🕹️ {n['titolo']}</h3>
                <p><b>Contenuto estratto:</b> {n['descrizione']}</p>
                <a href="{n['url']}" target="_blank" style="color: #00ff66; font-weight: bold;">🔗 Fonte originale</a>
            </div>
            """, unsafe_allow_html=True)
            
            dettaglio_extra = st.text_input(f"Aggiungi dettagli extra (es. nome skin o collab) per la notizia #{i+1}:", key=f"extra_{i}")
            
            if st.button(f"✨ Genera Articolo Unico #{i+1}", key=f"gen_{i}"):
                intro_list = [
                    f"Yo bro, occhio a questa bomba appena sganciata sul mondo di {query_utente}! 💣🔥",
                    f"Madonna fra! C'è un leak pazzesco che sta sconvolgendo la community in queste ore. 🎮💥",
                    f"Bella raga, mettetevi comodi perché l'ultimo aggiornamento spacca di brutto. 🕹️⚡",
                    f"Gamer, zero giri di parole: ecco cosa bolle in pentola per il nostro gioco preferito! 🏆👾",
                    f"Occhi aperti player! Le ultime novità arrivate dal web cambiano completamente le carte in tavola. 🚀🎯",
                    f"Let's go raga! È spuntata fuori una notizia freschissima che stavamo aspettando tutti. 🌟🔥"
                ]
                
                outro_list = [
                    "Voi che ne pensate? Scrivetelo nei commenti e preparate i controller! 🎮💬",
                    "Preparate le ranked e caricate i pad, ci sarà da divertirsi sul serio! 🚀💯",
                    "Fateci sapere se questa novità vi gasa o se speravate in qualcosa di diverso. GG a tutti! 🏆🔥",
                    "L'hype è alle stelle: non ci resta che aspettare il rilascio ufficiale. Stay tuned! 👾✨",
                    "Condividete l'articolo con la vostra squad e preparatevi alla battaglia! 🛠️⚡",
                    "Questa mossa spacca di brutto: ci becciamo direttamente in game per testarla! 🕹️🚀"
                ]
                
                info_fatti = n['descrizione']
                if dettaglio_extra:
                    info_fatti = f"{info_fatti} Dettagli imperdibili dal campo: {dettaglio_extra}"
                
                corpo_art = f"Entrando subito nei dettagli tecnici e nelle informazioni raccolte, ecco cosa sta succedendo: {info_fatti} Gli sviluppatori non si sono risparmiati questa volta, introducendo modifiche che faranno felici sia i veterani che i nuovi player."
                
                st.markdown(f"""
                <div class="article-box">
                    <h3>📝 ARTICOLO GENERATO IN STILE GAMING (100% UNICO)</h3>
                    <p style="font-size: 18px; line-height: 1.6; color: #00ff66;"><b>{random.choice(intro_list)}</b></p>
                    <p style="font-size: 16px; line-height: 1.6;">{corpo_art}</p>
                    <hr style="border-color: #9400D3;">
                    <p style="font-size: 16px; line-height: 1.6; color: #00ff66;"><b>{random.choice(outro_list)}</b></p>
                    <p style="font-size: 13px; color: #b19cd9; margin-top: 15px;">📌 <i>Titolo di riferimento: {n['titolo']}</i></p>
                </div>
                """, unsafe_allow_html=True)
else:
    if cerca_btn:
        st.warning("Nessuna notizia trovata. Prova a scrivere il nome del gioco.")
    else:
        st.info("👈 Scrivi un gioco nella barra laterale e clicca su 'Cerca News'!")
