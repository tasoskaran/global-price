import streamlit as st
import urllib.parse
import requests

# 1. ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ
st.set_page_config(page_title="Global Price & Duty Terminal", page_icon="⚡", layout="wide")

# 2. CUSTOM TECH / DARK CSS STYLING
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Segoe UI', Roboto, monospace;
    }
    h1, h2, h3 {
        color: #58a6ff !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 10px rgba(88, 166, 255, 0.3);
    }
    .stTextInput > div > div > input, .stNumberInput > div > div > input {
        background-color: #161b22 !important;
        color: #3fb950 !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton > button {
        background: linear-gradient(135deg, #1f6beb 0%, #1158c7 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: bold !important;
        box-shadow: 0 0 10px rgba(31, 107, 235, 0.4);
    }
    .stButton > button:hover {
        box-shadow: 0 0 18px rgba(56, 139, 253, 0.8) !important;
    }
    [data-testid="stMetricValue"] {
        font-family: 'Courier New', Courier, monospace !important;
        color: #3fb950 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ GLOBAL PRICE & DUTY TERMINAL")
st.caption("SYSTEM STATUS: ONLINE // ENTER SEARCH PARAMETERS")

# Βάλτε το SerpAPI Key σας στα Streamlit Secrets ή απευθείας στη μεταβλητή
SERPAPI_KEY = st.secrets.get("SERPAPI_KEY", "ΤΟ_SERPAPI_KEY_ΣΟΥ")

EXCHANGE_RATES = {"EUR (€)": 1.0, "USD ($)": 0.92, "GBP (£)": 1.17}
DUTY_RATES = {"Ηλεκτρονικά / Gadgets": 0.0, "Ρούχα & Υποδήματα": 12.0, "Αξεσουάρ / Κοσμήματα": 4.0, "Γενικά Εμπορεύματα": 3.5}

# 3. ΑΝΑΖΗΤΗΣΗ ΠΡΟΪΟΝΤΩΝ
st.header("01 // SEARCH STORES")

search_query = st.text_input("QUERY TARGET:", value="ps5")

def get_live_prices(query):
    """Κλήση στο SerpAPI για λήψη πραγματικών χαμηλότερων τιμών ανά κατάστημα"""
    stores_data = {
        "Skroutz": {"region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": f"https://www.skroutz.gr/search?keyphrase={urllib.parse.quote(query)}", "price": None},
        "BestPrice": {"region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": f"https://www.bestprice.gr/search?q={urllib.parse.quote(query)}", "price": None},
        "Amazon DE": {"region": "🇪🇺 DE", "currency": "EUR (€)", "eu": True, "link": f"https://www.amazon.de/s?k={urllib.parse.quote(query)}", "price": None},
        "Amazon US": {"region": "🇺🇸 US", "currency": "USD ($)", "eu": False, "link": f"https://www.amazon.com/s?k={urllib.parse.quote(query)}", "price": None},
        "eBay Global": {"region": "🌐 GLOBAL", "currency": "USD ($)", "eu": False, "link": f"https://www.ebay.com/sch/i.html?_nkw={urllib.parse.quote(query)}", "price": None},
        "AliExpress": {"region": "🇨🇳 CN", "currency": "USD ($)", "eu": False, "link": f"https://www.aliexpress.com/wholesale?SearchText={urllib.parse.quote(query)}", "price": None},
    }
    
    if SERPAPI_KEY and SERPAPI_KEY != "ΤΟ_SERPAPI_KEY_ΣΟΥ":
        try:
            url = f"https://serpapi.com/search.json?engine=google_shopping&q={urllib.parse.quote(query)}&api_key={SERPAPI_KEY}"
            resp = requests.get(url, timeout=10).json()
            results = resp.get("shopping_results", [])
            
            # Εντοπισμός χαμηλότερης τιμής ανά κατάστημα
            for item in results:
                merchant = item.get("source", "")
                extracted_price = item.get("extracted_price")
                if merchant and extracted_price:
                    for store_name in stores_data:
                        if store_name.lower() in merchant.lower() and stores_data[store_name]["price"] is None:
                            stores_data[store_name]["price"] = float(extracted_price)
        except Exception:
            pass

    return stores_data

if st.button("🔍 RUN GLOBAL SEARCH"):
    with st.spinner("FETCHING LIVE PRICES..."):
        st.session_state['live_results'] = get_live_prices(search_query)

# Εμφάνιση Λίστας Αποτελεσμάτων
if 'live_results' in st.session_state:
    st.subheader(f"DATA MATRIX FOR: '{search_query.upper()}'")

    h_col1, h_col2, h_col3, h_col4, h_col5 = st.columns([2, 1.2, 1.5, 1.5, 1.2])
    h_col1.markdown("**STORE**")
    h_col2.markdown("**REGION**")
    h_col3.markdown("**TARGET LINK**")
    h_col4.markdown("**LOWEST PRICE**")
    h_col5.markdown("**ACTION**")
    st.markdown("---")

    for idx, (store_name, data) in enumerate(st.session_state['live_results'].items()):
        col1, col2, col3, col4, col5 = st.columns([2, 1.2, 1.5, 1.5, 1.2])
        
        col1.write(f"🖥️ **{store_name}**")
        col2.write(f"`{data['region']}`")
        col3.markdown(f"[🔗 OPEN SITE]({data['link']})")
        
        # Αν υπάρχει τιμή εμφανίζεται, αλλιώς εμφανίζεται παύλα (-)
        if data['price'] is not None:
            price_display = f"{data['price']:.2f} {data['currency']}"
            col4.markdown(f"**`{price_display}`**")
        else:
            col4.markdown("**`-`**")
        
        if col5.button("SELECT", key=f"btn_ext_{idx}"):
            if data['price'] is not None:
                st.session_state['selected_price'] = float(data['price'])
            st.session_state['selected_currency'] = data['currency']
            st.session_state['selected_eu'] = data['eu']

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
