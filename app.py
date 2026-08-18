import streamlit as st
import urllib.parse

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

EXCHANGE_RATES = {"EUR (€)": 1.0, "USD ($)": 0.92, "GBP (£)": 1.17}
DUTY_RATES = {"Ηλεκτρονικά / Gadgets": 0.0, "Ρούχα & Υποδήματα": 12.0, "Αξεσουάρ / Κοσμήματα": 4.0, "Γενικά Εμπορεύματα": 3.5}

# 3. ΑΝΑΖΗΤΗΣΗ ΠΡΟΪΟΝΤΩΝ
st.header("01 // SEARCH STORES")

search_query = st.text_input("QUERY TARGET:", value="ps5")

def make_link(store_type, q, domain=""):
    quoted = urllib.parse.quote(q)
    if store_type == "skroutz": return f"https://www.skroutz.gr/search?keyphrase={quoted}"
    if store_type == "bestprice": return f"https://www.bestprice.gr/search?q={quoted}"
    if store_type == "public": return f"https://www.public.gr/search?q={quoted}"
    if store_type == "plaisio": return f"https://www.plaisio.gr/search?q={quoted}"
    if store_type == "shopflix": return f"https://shopflix.gr/search/?q={quoted}"
    if store_type == "kotsovolos": return f"https://www.kotsovolos.gr/site/search.jsp?q={quoted}"
    if store_type == "e-shop": return f"https://www.e-shop.gr/search_main.phtml?table=PER&q={quoted}"
    if store_type == "germanos": return f"https://www.germanos.gr/search?q={quoted}"
    
    if store_type == "amazon": return f"https://www.amazon.{domain}/s?k={quoted}"
    if store_type == "ebay": return f"https://www.ebay.{domain}/sch/i.html?_nkw={quoted}"
    if store_type == "google_shopping": return f"https://www.google.com/search?tbm=shop&q={quoted}"
    if store_type == "idealo": return f"https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q={quoted}"
    if store_type == "computeruniverse": return f"https://www.computeruniverse.net/en/search?q={quoted}"
    if store_type == "caseking": return f"https://www.caseking.de/search?sSearch={quoted}"
    if store_type == "fnac": return f"https://www.fnac.com/ia1/search?query={quoted}"
    if store_type == "otto": return f"https://www.otto.de/suche/{quoted}/"
    if store_type == "cdiscount": return f"https://www.cdiscount.com/search/10/{quoted}.html"
    
    if store_type == "aliexpress": return f"https://www.aliexpress.com/wholesale?SearchText={quoted}"
    if store_type == "banggood": return f"https://www.banggood.com/search/{quoted}.html"
    if store_type == "dhgate": return f"https://www.dhgate.com/wholesale/search.do?act=search&sus=&searchkey={quoted}"
    if store_type == "walmart": return f"https://www.walmart.com/search?q={quoted}"
    if store_type == "target": return f"https://www.target.com/s?searchTerm={quoted}"
    if store_type == "bestbuy": return f"https://www.bestbuy.com/site/searchpage.jsp?st={quoted}"
    if store_type == "newegg": return f"https://www.newegg.com/p/pl?d={quoted}"
    if store_type == "bhphoto": return f"https://www.bhphotovideo.com/c/search?Ntt={quoted}"
    
    # Fallback search via Google
    return f"https://www.google.com/search?q=site:{domain}+{quoted}"

if st.button("🔍 RUN EXTENDED GLOBAL SEARCH"):
    q = search_query
    
    st.session_state['all_results'] = [
        # --- ΕΛΛΑΔΑ (🇬🇷) ---
        {"store": "Skroutz", "region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": make_link("skroutz", q)},
        {"store": "BestPrice", "region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": make_link("bestprice", q)},
        {"store": "Public", "region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": make_link("public", q)},
        {"store": "Plaisio", "region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": make_link("plaisio", q)},
        {"store": "Shopflix", "region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": make_link("shopflix", q)},
        {"store": "Kotsovolos", "region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": make_link("kotsovolos", q)},
        {"store": "E-Shop.gr", "region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": make_link("e-shop", q)},
        {"store": "Germanos", "region": "🇬🇷 GR", "currency": "EUR (€)", "eu": True, "link": make_link("germanos", q)},
        
        # --- ΕΥΡΩΠΑΪΚΗ ΕΝΩΣΗ (🇪🇺) ---
        {"store": "Amazon DE", "region": "🇪🇺 DE", "currency": "EUR (€)", "eu": True, "link": make_link("amazon", q, "de")},
        {"store": "Amazon ES", "region": "🇪🇺 ES", "currency": "EUR (€)", "eu": True, "link": make_link("amazon", q, "es")},
        {"store": "Amazon IT", "region": "🇪🇺 IT", "currency": "EUR (€)", "eu": True, "link": make_link("amazon", q, "it")},
        {"store": "Amazon FR", "region": "🇪🇺 FR", "currency": "EUR (€)", "eu": True, "link": make_link("amazon", q, "fr")},
        {"store": "Amazon NL", "region": "🇪🇺 NL", "currency": "EUR (€)", "eu": True, "link": make_link("amazon", q, "nl")},
        {"store": "Idealo DE", "region": "🇪🇺 DE", "currency": "EUR (€)", "eu": True, "link": make_link("idealo", q)},
        {"store": "Computeruniverse", "region": "🇪🇺 DE", "currency": "EUR (€)", "eu": True, "link": make_link("computeruniverse", q)},
        {"store": "Caseking DE", "region": "🇪🇺 DE", "currency": "EUR (€)", "eu": True, "link": make_link("caseking", q)},
        {"store": "Fnac FR", "region": "🇪🇺 FR", "currency": "EUR (€)", "eu": True, "link": make_link("fnac", q)},
        {"store": "Otto DE", "region": "🇪🇺 DE", "currency": "EUR (€)", "eu": True, "link": make_link("otto", q)},
        {"store": "Cdiscount FR", "region": "🇪🇺 FR", "currency": "EUR (€)", "eu": True, "link": make_link("cdiscount", q)},

        # --- ΕΚΤΟΣ Ε.Ε. (🇺🇸 / 🇬🇧 / 🇨🇳 / GLOBAL) ---
        {"store": "Google Shopping", "region": "🌐 GLOBAL", "currency": "USD ($)", "eu": False, "link": make_link("google_shopping", q)},
        {"store": "eBay Global", "region": "🌐 GLOBAL", "currency": "USD ($)", "eu": False, "link": make_link("ebay", q, "com")},
        {"store": "eBay UK", "region": "🇬🇧 UK", "currency": "GBP (£)", "eu": False, "link": make_link("ebay", q, "co.uk")},
        {"store": "Amazon US", "region": "🇺🇸 US", "currency": "USD ($)", "eu": False, "link": make_link("amazon", q, "com")},
        {"store": "Amazon UK", "region": "🇬🇧 UK", "currency": "GBP (£)", "eu": False, "link": make_link("amazon", q, "co.uk")},
        {"store": "AliExpress", "region": "🇨🇳 CN", "currency": "USD ($)", "eu": False, "link": make_link("aliexpress", q)},
        {"store": "Banggood", "region": "🇨🇳 CN", "currency": "USD ($)", "eu": False, "link": make_link("banggood", q)},
        {"store": "DHgate", "region": "🇨🇳 CN", "currency": "USD ($)", "eu": False, "link": make_link("dhgate", q)},
        {"store": "Walmart US", "region": "🇺🇸 US", "currency": "USD ($)", "eu": False, "link": make_link("walmart", q)},
        {"store": "Target US", "region": "🇺🇸 US", "currency": "USD ($)", "eu": False, "link": make_link("target", q)},
        {"store": "Best Buy US", "region": "🇺🇸 US", "currency": "USD ($)", "eu": False, "link": make_link("bestbuy", q)},
        {"store": "Newegg US", "region": "🇺🇸 US", "currency": "USD ($)", "eu": False, "link": make_link("newegg", q)},
        {"store": "B&H Photo US", "region": "🇺🇸 US", "currency": "USD ($)", "eu": False, "link": make_link("bhphoto", q)}
    ]

# Εμφάνιση Αποτελεσμάτων σε Tabs για εύκολη πλοήγηση
if 'all_results' in st.session_state:
    st.subheader(f"DATA MATRIX FOR: '{search_query.upper()}' ({len(st.session_state['all_results'])} STORES FOUND)")

    tab_gr, tab_eu, tab_global = st.tabs(["🇬🇷 ΕΛΛΑΔΑ (8)", "🇪🇺 ΕΥΡΩΠΗ (11)", "🌐 GLOBAL / USA / CHINA (13)"])

    def display_store_table(results_subset, key_prefix):
        h_col1, h_col2, h_col3, h_col4, h_col5 = st.columns([2, 1.2, 1.5, 1.5, 1.2])
        h_col1.markdown("**STORE**")
        h_col2.markdown("**REGION**")
        h_col3.markdown("**TARGET LINK**")
        h_col4.markdown("**ENTER PRICE**")
        h_col5.markdown("**ACTION**")
        st.markdown("---")

        for idx, item in enumerate(results_subset):
            col1, col2, col3, col4, col5 = st.columns([2, 1.2, 1.5, 1.5, 1.2])
            
            col1.write(f"🖥️ **{item['store']}**")
            col2.write(f"`{item['region']}`")
            col3.markdown(f"[🔗 OPEN SITE]({item['link']})")
            
            user_price = col4.number_input(
                label=f"Price_{key_prefix}_{idx}",
                min_value=0.0,
                value=0.0,
                step=5.0,
                label_visibility="collapsed",
                key=f"price_input_{key_prefix}_{idx}"
            )
            
            if col5.button("SELECT", key=f"btn_{key_prefix}_{idx}"):
                st.session_state['selected_price'] = float(user_price)
                st.session_state['selected_currency'] = item['currency']
                st.session_state['selected_eu'] = item['eu']

    with tab_gr:
        gr_items = [x for x in st.session_state['all_results'] if x['region'].startswith("🇬🇷")]
        display_store_table(gr_items, "gr")

    with tab_eu:
        eu_items = [x for x in st.session_state['all_results'] if x['region'].startswith("🇪🇺")]
        display_store_table(eu_items, "eu")

    with tab_global:
        global_items = [x for x in st.session_state['all_results'] if not x['region'].startswith("🇬🇷") and not x['region'].startswith("🇪🇺")]
        display_store_table(global_items, "global")

# 4. ΥΠΟΛΟΓΙΣΜΟΣ ΔΑΣΜΩΝ & ΦΠΑ
st.markdown("---")
st.header("02 // DUTY & VAT CALCULATOR")

default_price = st.session_state.get('selected_price', 0.0)
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
