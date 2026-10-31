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

st.markdown(f"### 🗓️ {secilen_tarih.strftime('%d %B %Y')} Maç Listesi & Detaylar")

# Güncel Maç Veritabanı ve Detay Sekmeleri İçeriği
guncel_maclar = {
    "Futbol": {
        datetime.date(2026, 10, 31): [
            {
                "lig": "Süper Lig",
                "ev": "Erzurumspor FK",
                "dep": "Çorum FK",
                "saat": "13:30",
                "oranlar": {"MS 1": 1.90, "X": 3.30, "MS 2": 3.80},
                "tahmin": "MS 1 (%52 İhtimal)",
                "deger": "Alt Seçeneği",
                "form": (
                    "Erzurumspor (G B M G G) - Çorum FK (M G B M G)"
                ),
            },
            {
                "lig": "Süper Lig",
                "ev": "Kocaelispor",
                "dep": "Çaykur Rizespor",
                "saat": "16:00",
                "oranlar": {"MS 1": 2.20, "X": 3.10, "MS 2": 3.10},
                "tahmin": "KG Var (%58 İhtimal)",
                "deger": "Değer Var",
                "form": (
                    "Kocaelispor (G G B M G) - Rizespor (M M G B G)"
                ),
            },
            {
                "lig": "Süper Lig",
                "ev": "Fenerbahçe",
                "dep": "Göztepe",
                "saat": "19:00",
                "oranlar": {"MS 1": 1.45, "X": 4.20, "MS 2": 6.00},
                "tahmin": "MS 1 (%72 İhtimal)",
                "deger": "MS 1 (Banko)",
                "form": "Fenerbahçe (G G G G B) - Göztepe (G M B G M)",
            },
        ],
        datetime.date(2026, 11, 1): [
            {
                "lig": "Süper Lig",
                "ev": "Trabzonspor",
                "dep": "Gaziantep FK",
                "saat": "16:00",
                "oranlar": {"MS 1": 1.65, "X": 3.50, "MS 2": 4.80},
                "tahmin": "MS 1 (%62 İhtimal)",
                "deger": "2.5 Üst",
                "form": (
                    "Trabzonspor (G B G M G) - Gaziantep (M M G B M)"
                ),
            },
            {
                "lig": "Süper Lig",
                "ev": "Kasımpaşa",
                "dep": "Beşiktaş",
                "saat": "19:00",
                "oranlar": {"MS 1": 3.10, "X": 3.30, "MS 2": 2.15},
                "tahmin": "MS 2 (%54 İhtimal)",
                "deger": "KG Var",
                "form": (
                    "Kasımpaşa (M G B G M) - Beşiktaş (G G M G G)"
                ),
            },
        ],
    },
    "Basketbol": {
        datetime.date(2026, 10, 31): [
            {
                "lig": "EuroLeague",
                "ev": "Fenerbahçe Beko",
                "dep": "Panathinaikos",
                "saat": "20:45",
                "oranlar": {"MS 1": 1.75, "MS 2": 2.00},
                "tahmin": "MS 1 (%56 İhtimal)",
                "deger": "Handikaplı MS 1",
                "form": "FB Beko (G G M G) - Panathinaikos (G M G G)",
            },
            {
                "lig": "EuroLeague",
                "ev": "Anadolu Efes",
                "dep": "Real Madrid",
                "saat": "21:30",
                "oranlar": {"MS 1": 2.10, "MS 2": 1.70},
                "tahmin": "Üst (%60 İhtimal)",
                "deger": "162.5 Üst",
                "form": "Anadolu Efes (M G G B) - Real Madrid (G G G M)",
            },
        ]
    },
}

brans_dict = guncel_maclar.get(brans, {})
aktif_maclar = brans_dict.get(secilen_tarih, [])

if aktif_maclar:
  for mac in aktif_maclar:
    # Her maç için şık bir kapsayıcı ve sekmeler (Maçkolik tarzı)
    with st.container():
      st.markdown(
          f"""
            <div class="match-card">
                <h4>⚽ {mac['ev']} vs {mac['dep']}</h4>
                <p><b>Lig:</b> {mac['lig']} &nbsp;|&nbsp; <b>Saat:</b> {mac['saat']}</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

      # Maç İçi Sekmeler (Oranlar, Tahmin, Form)
      tab1, tab2, tab3 = st.tabs(
          ["📊 Oranlar", "🤖 Gx Tahmin", "📈 Form & Analiz"]
      )

      with tab1:
        st.write("Bahis Oranları:")
        for oran_adi, oran_degeri in mac["oranlar"].items():
          st.text(f"• {oran_adi}: {oran_degeri}")

      with tab2:
        st.success(f"**Yapay Zeka Öngörüsü:** {mac['tahmin']}")
        st.warning(f"**Öne Çıkan Değer:** {mac['deger']}")

      with tab3:
        st.info(f"**Son Maç Serileri:** {mac['form']}")

      st.markdown("---")
else:
  st.warning(
      "⚠️ Seçtiğiniz tarih için maç bulunmuyor. (İpucu: 31 Ekim 2026 veya 1"
      " Kasım 2026 tarihlerini seçebilirsiniz)."
  )

st.info("💡 Adım 1 tamamlandı: Maçkolik tarzı sekmeli yapı entegre edildi!")
