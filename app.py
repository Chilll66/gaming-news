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

# Funzione potenziata per estrarre e riassumere in modo pulito il contenuto senza tagli netti o puntini
def estrai_e_rielabora_articolo(url):
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
                
            contenitore_principale = soup.find('article') or soup.find('main') or soup.find('div', class_=['content', 'post-content', 'entry-content', 'article-body'])
            target_soup = contenitore_principale if contenitore_principale else soup
            paragrafi = target_soup.find_all('p')
            
            testi_utili = []
            for p in paragrafi:
                txt = p.get_text().strip()
                if len(txt) > 50 and not any(parola in txt.lower() for parola in ['cookie', 'privacy', 'tutti i diritti', 'rights reserved', 'iscriviti', 'newsletter']):
                    testi_utili.append(txt)
                    
            if testi_utili:
                # Uniamo i paragrafi in modo logico creando un flusso discorsivo fluido e senza troncamenti
                testo_grezzo = " ".join(testi_utili[:4])
                tradotto = traduci_in_italiano(testo_grezzo)
                
                # Aggiungiamo un tocco di curiosità e ricchezza descrittiva fluida
                sintesi_fluida = f"Analizzando a fondo la situazione, emerge che {tradotto} Tra le curiosità meno conosciute legate a questo argomento, la community ha spesso evidenziato dettagli nascosti e retroscena di sviluppo che arricchiscono l'esperienza di gioco in modo inaspettato."
                return sintesi_fluida
            return ""
    except:
        return ""

# Funzione di ricerca web
def cerca_news_profonda(termine):
    try:
        results = []
        url_ricerca = "https://lite.duckduckgo.com/lite/"
        dati_post = urllib.parse.urlencode({'q': f"{termine} gaming news update patch easter egg"}).encode('utf-8')
        
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
                    contenuto_rielaborato = estrai_e_rielabora_articolo(href)
                    
                    descrizione_finale = contenuto_rielaborato if len(contenuto_rielaborato) > 100 else f"Approfondendo le novità su {termine}, emergono dettagli succosi e curiosità insolite che vale la pena scoprire. {traduci_in_italiano(snippet_base)}"
                    
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
                    f"Yo bro! 🎮🔥 Occhio a questa bomba appena sganciata sul mondo di {query_utente}! 💣✨",
                    f"Attiska fra! 🚀👾 C'è un leak pazzesco e pieno di curiosità nascoste che sta sconvolgendo la community. 🔮💥",
                    f"Bella raga! 🕹️⚡ Mettetevi comodi perché l'ultimo aggiornamento nasconde dettagli assurdi. 🌟🔥",
                    f"Gamer! 🏆👾 Zero giri di parole: ecco cosa bolle in pentola e le chicche segrete del giorno! 🎮🎯",
                    f"Occhi aperti player! 🎯🔥 Le ultime novità arrivate dal web svelano retroscena pazzeschi. 🚀💫",
                    f"Let's go raga! 🌟🔥 È spuntata fuori una notizia freschissima ricca di curiosità imperdibili. 🕹️🎮"
                ]
                
                outro_list = [
                    "Voi che ne pensate di queste chicche? 🎮💬 Scrivetelo nei commenti e preparate i controller! 🚀🔥",
                    "Preparate le ranked e caricate i pad! 🕹️💯 Ci sarà da divertirsi scoprendo ogni segreto nascosto. 🏆✨",
                    "Fateci sapere se questa novità vi gasa o se sapevate già tutto. 👾🔥 GG a tutti raga! 🚀🎮",
                    "L'hype è alle stelle! 🌟💫 Non ci resta che testare tutto in game. Stay tuned e buon gaming! 🕹️🎯",
                    "Condividete l'articolo con la vostra squad! 🛠️⚡ Preparatevi alla battaglia e a caccia di easter egg! 🎮🔥",
                    "Questa mossa spacca di brutto! 🚀👾 Ci becciamo direttamente in game per spolparla fino all'ultimo! 🕹️💯"
                ]
                
                info_fatti = n['descrizione']
                if dettaglio_extra:
                    info_fatti = f"{info_fatti} 💎 Curiosità extra dal campo: {dettaglio_extra}"
                
                corpo_art = f"Entrando subito nei dettagli tecnici e nelle curiosità più stravaganti raccolte in rete, ecco cosa sta succedendo: {info_fatti} 🛠️✨ Gli sviluppatori non si sono risparmiati, inserendo chicche e particolari che faranno impazzire sia i veterani più attenti che i nuovi player in cerca di emozioni forti. 🎮🔥"
                
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
    
