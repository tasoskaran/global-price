import streamlit as st
import urllib.parse

# 1. ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ
st.set_page_config(page_title="Global Price & Duty Finder", page_icon="⚡", layout="wide")

# 2. CUSTOM TECH / DARK CSS STYLING
st.markdown("""
    <style>
    /* Γενικό υπόβαθρο και γραμματοσειρές */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Segoe UI', Roboto, monospace;
    }
    
    /* Κεφαλίδες με Neon Glow */
    h1, h2, h3 {
        color: #58a6ff !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 10px rgba(88, 166, 255, 0.3);
    }
    
    /* Πεδία εισαγωγής κειμένου & αριθμών */
    .stTextInput > div > div > input, .stNumberInput > div > div > input {
        background-color: #161b22 !important;
        color: #3fb950 !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
        font-family: 'Courier New', Courier, monospace;
    }
    .stTextInput > div > div > input:focus, .stNumberInput > div > div > input:focus {
        border-color: #58a6ff !important;
        box-shadow: 0 0 8px rgba(88, 166, 255, 0.5) !important;
    }

    /* Κουμπιά με Neon Hover Effect */
    .stButton > button {
        background: linear-gradient(135deg, #1f6beb 0%, #1158c7 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 10px rgba(31, 107, 235, 0.4);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #388bfd 0%, #1f6beb 100%) !important;
        box-shadow: 0 0 18px rgba(56, 139, 253, 0.8) !important;
        transform: translateY(-1px);
    }

    /* Metrics / Κάρτες αποτελεσμάτων */
    [data-testid="stMetricValue"] {
        font-family: 'Courier New', Courier, monospace !important;
        color: #3fb950 !important;
        font-size: 1.8rem !important;
        text-shadow: 0 0 8px rgba(63, 185, 80, 0.4);
    }
    [data-testid="stMetricLabel"] {
        color: #8b949e !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Διαχωριστικές γραμμές */
    hr {
        border-color: #30363d !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ GLOBAL PRICE & DUTY TERMINAL")
st.caption("SYSTEM STATUS: ONLINE // ENTER SEARCH PARAMETERS")

EXCHANGE_RATES = {"EUR (€)": 1.0, "USD ($)": 0.92, "GBP (£)": 1.17}
DUTY_RATES = {"Ηλεκτρονικά / Gadgets": 0.0, "Ρούχα & Υποδήματα": 12.0, "Αξεσουάρ / Κοσμήματα": 4.0, "Γενικά Εμπορεύματα": 3.5}

# 3. ΑΝΑΖΗΤΗΣΗ ΠΡΟΪΟΝΤΩΝ
st.header("01 // SEARCH STORES")

search_query = st.text_input("QUERY TARGET:", value="ps5")

if st.button("🔍 RUN GLOBAL SEARCH"):
    q = urllib.parse.quote(search_query)
    
    st.session_state['live_results'] = [
        # 🇬🇷 Ελλάδα
        {"store": "Skroutz", "region": "🇬🇷 GR", "price": 490.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.skroutz.gr/search?keyphrase={q}"},
        {"store": "BestPrice", "region": "🇬🇷 GR", "price": 489.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.bestprice.gr/search?q={q}"},
        {"store": "Public", "region": "🇬🇷 GR", "price": 499.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.public.gr/search?q={q}"},
        {"store": "Plaisio", "region": "🇬🇷 GR", "price": 499.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.plaisio.gr/search?q={q}"},
        {"store": "Shopflix", "region": "🇬🇷 GR", "price": 485.00, "currency": "EUR (€)", "eu": True, "link": f"https://shopflix.gr/search/?q={q}"},
        
        # 🇪🇺 Ε.Ε.
        {"store": "Amazon DE", "region": "🇪🇺 DE", "price": 499.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.amazon.de/s?k={q}"},
        {"store": "Amazon ES", "region": "🇪🇺 ES", "price": 499.99, "currency": "EUR (€)", "eu": True, "link": f"https://www.amazon.es/s?k={q}"},
        {"store": "Amazon IT", "region": "🇪🇺 IT", "price": 495.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.amazon.it/s?k={q}"},
        {"store": "Amazon FR", "region": "🇪🇺 FR", "price": 499.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.amazon.fr/s?k={q}"},
        {"store": "Computeruniverse", "region": "🇪🇺 DE", "price": 490.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.computeruniverse.net/en/search?q={q}"},
        {"store": "Idealo", "region": "🇪🇺 DE", "price": 480.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q={q}"},
        
        # 🌐 Εκτός Ε.Ε.
        {"store": "Google Shopping", "region": "🌐 GLOBAL", "price": 450.00, "currency": "USD ($)", "eu": False, "link": f"https://www.google.com/search?tbm=shop&q={q}"},
        {"store": "eBay Global", "region": "🌐 GLOBAL", "price": 440.00, "currency": "USD ($)", "eu": False, "link": f"https://www.ebay.com/sch/i.html?_nkw={q}"},
        {"store": "Amazon US", "region": "🇺🇸 US", "price": 499.00, "currency": "USD ($)", "eu": False, "link": f"https://www.amazon.com/s?k={q}"},
        {"store": "Amazon UK", "region": "🇬🇧 UK", "price": 430.00, "currency": "GBP (£)", "eu": False, "link": f"https://www.amazon.co.uk/s?k={q}"},
        {"store": "AliExpress", "region": "🇨🇳 CN", "price": 410.00, "currency": "USD ($)", "eu": False, "link": f"https://www.aliexpress.com/wholesale?SearchText={q}"},
        {"store": "Banggood", "region": "🇨🇳 CN", "price": 425.00, "currency": "USD ($)", "eu": False, "link": f"https://www.banggood.com/search/{q}.html"},
        {"store": "Newegg", "region": "🇺🇸 US", "price": 485.00, "currency": "USD ($)", "eu": False, "link": f"https://www.newegg.com/p/pl?d={q}"}
    ]

# Εμφάνιση Λίστας Αποτελεσμάτων
if 'live_results' in st.session_state:
    st.subheader(f"DATA MATRIX FOR: '{search_query.upper()}'")

    h_col1, h_col2, h_col3, h_col4, h_col5 = st.columns([2, 1.2, 1.5, 1.5, 1.2])
    h_col1.markdown("**STORE**")
    h_col2.markdown("**REGION**")
    h_col3.markdown("**TARGET LINK**")
    h_col4.markdown("**PRICE INPUT**")
    h_col5.markdown("**ACTION**")
    st.markdown("---")

    for idx, item in enumerate(st.session_state['live_results']):
        col1, col2, col3, col4, col5 = st.columns([2, 1.2, 1.5, 1.5, 1.2])
        
        col1.write(f"🖥️ **{item['store']}**")
        col2.write(f"`{item['region']}`")
        col3.markdown(f"[🔗 OPEN SITE]({item['link']})")
        
        input_price = col4.number_input(
            label=f"Price_{idx}",
            min_value=0.0,
            value=float(item['price']),
            step=5.0,
            label_visibility="collapsed",
            key=f"price_input_{idx}"
        )
        
        if col5.button("SELECT", key=f"btn_ext_{idx}"):
            st.session_state['selected_price'] = float(input_price)
            st.session_state['selected_currency'] = item['currency']
            st.session_state['selected_eu'] = item['eu']

# 4. ΥΠΟΛΟΓΙΣΜΟΣ ΔΑΣΜΩΝ & ΦΠΑ
st.markdown("---")
st.header("02 // DUTY & VAT CALCULATOR")

default_price = st.session_state.get('selected_price', 100.0)
default_currency = st.session_state.get('selected_currency', "USD ($)")
default_eu = st.session_state.get('selected_eu', False)

col_calc1, col_calc2 = st.columns(2)

with col_calc1:
    price = st.number_input("PRODUCT PRICE", min_value=0.0, value=float(default_price), step=5.0)
    currency = st.selectbox("CURRENCY", list(EXCHANGE_RATES.keys()), index=list(EXCHANGE_RATES.keys()).index(default_currency))
    category = st.selectbox("CATEGORY", list(DUTY_RATES.keys()))

with col_calc2:
    shipping = st.number_input("SHIPPING COST (€)", min_value=0.0, value=15.0, step=1.0)
    origin_eu = st.checkbox("EU ORIGIN (NO CUSTOMS DUTY)", value=default_eu)

# Μαθηματικοί Υπολογισμοί
rate = EXCHANGE_RATES[currency]
price_eur = price * rate
shipping_eur = shipping
cif_value = price_eur + shipping_eur

duty_percent = 0.0 if origin_eu else DUTY_RATES[category]
vat_percent = 24.0

duty_amount = (cif_value * (duty_percent / 100.0)) if (not origin_eu and cif_value > 150) else 0.0
vat_amount = 0.0 if origin_eu else ((cif_value + duty_amount) * (vat_percent / 100.0))
clearance_fee = 15.0 if (not origin_eu and cif_value > 150) else (5.0 if not origin_eu else 0.0)
total_cost = cif_value + duty_amount + vat_amount + clearance_fee

st.markdown("### 📊 FINANCIAL SUMMARY")
res1, res2, res3 = st.columns(3)
res1.metric("BASE VALUE (EUR)", f"{price_eur:.2f} €")
res2.metric("DUTIES + VAT + FEES", f"{(duty_amount + vat_amount + clearance_fee):.2f} €")
res3.metric("TOTAL ESTIMATED COST", f"{total_cost:.2f} €")
