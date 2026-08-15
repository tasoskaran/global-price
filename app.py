import streamlit as st
import urllib.parse

# 1. ΡΥΘΜΙΣΗ ΣΕΛΙΔΑΣ
st.set_page_config(page_title="Global Price & Duty Finder", page_icon="🛍️", layout="wide")

st.title("🛍️ Global Product Finder & Duty Calculator")
st.write("Αναζητήστε προϊόντα σε δεκάδες καταστήματα παγκοσμίως, εισάγετε τιμές και υπολογίστε το συνολικό κόστος εισαγωγής.")

EXCHANGE_RATES = {"EUR (€)": 1.0, "USD ($)": 0.92, "GBP (£)": 1.17}
DUTY_RATES = {"Ηλεκτρονικά / Gadgets": 0.0, "Ρούχα & Υποδήματα": 12.0, "Αξεσουάρ / Κοσμήματα": 4.0, "Γενικά Εμπορεύματα": 3.5}

# 2. ΑΝΑΖΗΤΗΣΗ ΠΡΟΪΟΝΤΩΝ
st.header("1. Αναζήτηση Προϊόντος")

search_query = st.text_input("Εισάγετε το προϊόν που ψάχνετε:", value="ps5")

if st.button("🔍 Αναζήτηση σε Όλα τα Καταστήματα"):
    q = urllib.parse.quote(search_query)
    
    # Λίστα e-shops με προκαθορισμένες ενδεικτικές τιμές
    st.session_state['live_results'] = [
        # 🇬🇷 Ελλάδα & Κύπρος
        {"store": "Skroutz", "region": "🇬🇷 Ελλάδα", "price": 490.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.skroutz.gr/search?keyphrase={q}"},
        {"store": "BestPrice", "region": "🇬🇷 Ελλάδα", "price": 489.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.bestprice.gr/search?q={q}"},
        {"store": "Public", "region": "🇬🇷 Ελλάδα", "price": 499.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.public.gr/search?q={q}"},
        {"store": "Plaisio", "region": "🇬🇷 Ελλάδα", "price": 499.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.plaisio.gr/search?q={q}"},
        {"store": "Shopflix", "region": "🇬🇷 Ελλάδα", "price": 485.00, "currency": "EUR (€)", "eu": True, "link": f"https://shopflix.gr/search/?q={q}"},
        
        # 🇪🇺 Ευρωπαϊκή Ένωση
        {"store": "Amazon Germany", "region": "🇪🇺 Γερμανία", "price": 499.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.amazon.de/s?k={q}"},
        {"store": "Amazon Spain", "region": "🇪🇺 Ισπανία", "price": 499.99, "currency": "EUR (€)", "eu": True, "link": f"https://www.amazon.es/s?k={q}"},
        {"store": "Amazon Italy", "region": "🇪🇺 Ιταλία", "price": 495.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.amazon.it/s?k={q}"},
        {"store": "Amazon France", "region": "🇪🇺 Γαλλία", "price": 499.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.amazon.fr/s?k={q}"},
        {"store": "Computeruniverse", "region": "🇪🇺 Γερμανία", "price": 490.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.computeruniverse.net/en/search?q={q}"},
        {"store": "Idealo (DE)", "region": "🇪🇺 Γερμανία (Σύγκριση)", "price": 480.00, "currency": "EUR (€)", "eu": True, "link": f"https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q={q}"},
        
        # 🇺🇸 🇬🇧 🇨🇳 Εκτός Ε.Ε.
        {"store": "Google Shopping", "region": "🌐 Παγκόσμιο Search", "price": 450.00, "currency": "USD ($)", "eu": False, "link": f"https://www.google.com/search?tbm=shop&q={q}"},
        {"store": "eBay Worldwide", "region": "🌐 Παγκόσμιο Marketplace", "price": 440.00, "currency": "USD ($)", "eu": False, "link": f"https://www.ebay.com/sch/i.html?_nkw={q}"},
        {"store": "Amazon US", "region": "🇺🇸 ΗΠΑ", "price": 499.00, "currency": "USD ($)", "eu": False, "link": f"https://www.amazon.com/s?k={q}"},
        {"store": "Amazon UK", "region": "🇬🇧 Ηνωμένο Βασίλειο", "price": 430.00, "currency": "GBP (£)", "eu": False, "link": f"https://www.amazon.co.uk/s?k={q}"},
        {"store": "AliExpress", "region": "🇨🇳 Κίνα Direct", "price": 410.00, "currency": "USD ($)", "eu": False, "link": f"https://www.aliexpress.com/wholesale?SearchText={q}"},
        {"store": "Banggood", "region": "🇨🇳 Κίνα", "price": 425.00, "currency": "USD ($)", "eu": False, "link": f"https://www.banggood.com/search/{q}.html"},
        {"store": "Gearbest", "region": "🇨🇳 Κίνα", "price": 430.00, "currency": "USD ($)", "eu": False, "link": f"https://www.gearbest.com/search/?q={q}"},
        {"store": "Newegg", "region": "🇺🇸 ΗΠΑ", "price": 485.00, "currency": "USD ($)", "eu": False, "link": f"https://www.newegg.com/p/pl?d={q}"},
        {"store": "B&H Photo Video", "region": "🇺🇸 ΗΠΑ", "price": 499.00, "currency": "USD ($)", "eu": False, "link": f"https://www.bhphotovideo.com/c/search?Ntt={q}"},
        {"store": "Walmart", "region": "🇺🇸 ΗΠΑ", "price": 490.00, "currency": "USD ($)", "eu": False, "link": f"https://www.walmart.com/search?q={q}"}
    ]

# Εμφάνιση Αποτελεσμάτων σε Λίστα με Στήλη Τιμών
if 'live_results' in st.session_state:
    st.subheader(f"📋 Λίστα Καταστημάτων για: '{search_query}'")
    st.info("💡 Δείτε την τιμή στο κατάστημα, συμπληρώστε την στη στήλη 'Τιμή' και πατήστε 'Υπολογισμός'.")

    # Επικεφαλίδες Στηλών
    h_col1, h_col2, h_col3, h_col4, h_col5 = st.columns([2, 1.5, 1.5, 1.5, 1.2])
    h_col1.markdown("**Κατάστημα**")
    h_col2.markdown("**Περιοχή**")
    h_col3.markdown("**Link**")
    h_col4.markdown("**Τιμή Καταστήματος**")
    h_col5.markdown("**Ενέργεια**")
    st.markdown("---")

    # Γραμμές Καταστημάτων
    for idx, item in enumerate(st.session_state['live_results']):
        col1, col2, col3, col4, col5 = st.columns([2, 1.5, 1.5, 1.5, 1.2])
        
        col1.write(f"🏪 **{item['store']}**")
        col2.write(f"{item['region']}")
        col3.markdown(f"[🔗 Μετάβαση]({item['link']})")
        
        # Πεδίο εισαγωγής τιμής για κάθε κατάστημα
        input_price = col4.number_input(
            label=f"Price_{idx}",
            min_value=0.0,
            value=float(item['price']),
            step=5.0,
            label_visibility="collapsed",
            key=f"price_input_{idx}"
        )
        
        if col5.button("Υπολογισμός", key=f"btn_ext_{idx}"):
            st.session_state['selected_price'] = float(input_price)
            st.session_state['selected_currency'] = item['currency']
            st.session_state['selected_eu'] = item['eu']

# 3. ΥΠΟΛΟΓΙΣΜΟΣ ΔΑΣΜΩΝ & ΦΠΑ
st.markdown("---")
st.header("2. Υπολογισμός Εκτελωνισμού & Τελικής Τιμής")

default_price = st.session_state.get('selected_price', 100.0)
default_currency = st.session_state.get('selected_currency', "USD ($)")
default_eu = st.session_state.get('selected_eu', False)

col_calc1, col_calc2 = st.columns(2)

with col_calc1:
    price = st.number_input("Τιμή Προϊόντος (€/$/£)", min_value=0.0, value=float(default_price), step=5.0)
    currency = st.selectbox("Νόμισμα", list(EXCHANGE_RATES.keys()), index=list(EXCHANGE_RATES.keys()).index(default_currency))
    category = st.selectbox("Κατηγορία Προϊόντος", list(DUTY_RATES.keys()))

with col_calc2:
    shipping = st.number_input("Εκτιμώμενο Κόστος Μεταφορικών (€)", min_value=0.0, value=15.0, step=1.0)
    origin_eu = st.checkbox("Αποστολή εντός Ευρωπαϊκής Ένωσης (Ε.Ε.)", value=default_eu)

# Μαθηματικά
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

st.markdown("### 📊 Αναλυτική Σύνοψη Κόστους")
res1, res2, res3 = st.columns(3)
res1.metric("Αρχική Αξία (EUR)", f"{price_eur:.2f} €")
res2.metric("Δασμοί + ΦΠΑ + Τέλη", f"{(duty_amount + vat_amount + clearance_fee):.2f} €")
res3.metric("Συνολικό Τελικό Κόστος", f"{total_cost:.2f} €")