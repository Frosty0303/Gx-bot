import datetime
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Gx Bot - Bahis Analiz", page_icon="⚡", layout="centered"
)

# Modern ve Şık Tasarım İçin CSS
st.markdown(
    """
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stSelectbox, .stDateInput { background-color: #1a1c23; border-radius: 8px; }
    .match-card { background-color: #1e222d; padding: 15px; border-radius: 10px; margin-bottom: 15px; border-left: 4px solid #ff4b4b; }
    </style>
""",
    unsafe_allow_html=True,
)

# Başlık
st.markdown(
    "<h2 style='text-align: center; color: #ff4b4b;'>⚡ Gx Bot - Kişisel Bahis"
    " & Analiz Paneli</h2>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #808495;'>Futbol ve Basketbol"
    " İstatistik & Tahmin Asistanı</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Branş Seçimi
brans = st.selectbox("📌 Branş Seçin:", ["Futbol", "Basketbol"])

# Tarih Seçici
bugun = datetime.date.today()
secilen_tarih = st.date_input("📅 Maç Tarihi Seçin:", bugun)

st.markdown(f"### 🗓️ {secilen_tarih.strftime('%d %B %Y')} Maç Listesi")

# Örnek Maç Veritabanı (Gelecekte buraya API eklenecek)
maclar = {
    "Futbol": [
        {
            "lig": "Süper Lig",
            "ev": "Galatasaray",
            "dep": "Fenerbahçe",
            "saat": "19:00",
            "oranlar": "2.10 / 3.20 / 2.80",
            "tahmin": "MS 1 (%55 İhtimal)",
            "deger": "MS 1 (Value Var)",
        },
        {
            "lig": "Premier Lig",
            "ev": "Arsenal",
            "dep": "Manchester City",
            "saat": "21:30",
            "oranlar": "2.40 / 3.40 / 2.50",
            "tahmin": "KG Var (%65 İhtimal)",
            "deger": "2.5 Üst",
        },
    ],
    "Basketbol": [
        {
            "lig": "EuroLeague",
            "ev": "Anadolu Efes",
            "dep": "Real Madrid",
            "saat": "20:00",
            "oranlar": "1.70 / 2.10",
            "tahmin": "MS 1 (%60 İhtimal)",
            "deger": "Handikaplı MS 1",
        },
        {
            "lig": "NBA",
            "ev": "L.A. Lakers",
            "dep": "Golden State",
            "saat": "03:00",
            "oranlar": "1.85 / 1.85",
            "tahmin": "225.5 Üst (%58 İhtimal)",
            "deger": "Üst Seçeneği",
        },
    ],
}

# Seçilen branşın maçlarını listeleme
aktif_maclar = maclar.get(brans, [])

for mac in aktif_maclar:
  st.markdown(
      f"""
        <div class="match-card">
            <h4>⚽ {mac['ev']} vs {mac['dep']}</h4>
            <p><b>Lig:</b> {mac['lig']} | <b>Saat:</b> {mac['saat']} | <b>Oranlar:</b> {mac['oranlar']}</p>
            <p style='color: #4CAF50;'><b>Gx Tahmini:</b> {mac['tahmin']}</p>
            <p style='color: #FF9800;'><b>Değerli Oran:</b> {mac['deger']}</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

st.markdown("---")
st.info(
    "💡 İpucu: Tarih değiştirerek ileri veya geri tarihlerdeki simüle edilmiş"
    " maç programlarını inceleyebilirsiniz."
)
