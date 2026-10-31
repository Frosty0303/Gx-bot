import datetime
import random
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Gx Bot Pro - Canlı Spor & AI Paneli",
    page_icon="⚡",
    layout="centered",
)

# Flashscore & Maçkolik Teması CSS
st.markdown(
    """
    <style>
    .main { background-color: #0b0e14; color: #e6e8eb; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    .stSelectbox, .stDateInput, .stNumberInput { background-color: #161b22; border-radius: 8px; border: 1px solid #30363d; color: #fff; }
    .match-card { background-color: #161b22; padding: 16px; border-radius: 12px; margin-bottom: 14px; border-left: 5px solid #e53935; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
    .badge-league { color: #ffeb3b; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; }
    .live-badge { background-color: #e53935; color: white; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .ai-box { background-color: #121824; padding: 15px; border-radius: 10px; border: 1px solid #00bcd4; margin-top: 10px; }
    .kasa-card { background-color: #161b22; padding: 14px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 10px; }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.markdown(
    "<h3 style='color: #e53935; text-align: center;'>⚡ Gx Bot Pro Canlı</h3>",
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")
ana_menu = st.sidebar.radio(
    "Menü", ["🏆 Canlı Lig Fikstürü", "💰 Kasa Takip Paneli"]
)

# ANLIK GÜNCEL TARİH ALICI
bugun_tarih = datetime.date.today()


def ai_tahmin_uret(ev, dep, lig):
  tahminler = [
      ("MS 1", "%78 Güven", "1.55", "Banko Adayı"),
      ("KG Var", "%73 Güven", "1.68", "Yüksek Değer"),
      ("2.5 Üst", "%76 Güven", "1.62", "Tempolu Maç"),
      ("Çifte Şans 1X", "%84 Güven", "1.35", "Kombine İdeal"),
  ]
  secim = random.choice(tahminler)
  return {
      "tahmin": secim[0],
      "guven": secim[1],
      "oran": secim[2],
      "deger": secim[3],
      "skor": f"{random.randint(1,3)} - {random.randint(0,2)}",
      "yorum": (
          f"{lig} mücadelesinde {ev} takımının son evindeki performansı öne"
          f" çıkıyor. {dep} savunma arkasına atılan toplarda etkili."
      ),
      "sakatlar": (
          f"{ev}: Tam kadro. | {dep}: 1 orta saha sakatlık nedeniyle şüpheli."
      ),
  }


if ana_menu == "🏆 Canlı Lig Fikstürü":
  st.markdown(
      "<h2 style='text-align: center; color: #e53935;'>⚡ Gx Bot - Güncel Maç"
      " Merkezi</h2>",
      unsafe_allow_html=True,
  )

  c1, c2 = st.columns(2)
  with c1:
    brans = st.selectbox("📌 Spor Branşı", ["Futbol", "Basketbol"])
  with c2:
    secilen_lig = st.selectbox(
        "🏆 Lig Seçin",
        [
            "Tümü",
            "Trendyol Süper Lig",
            "Premier Lig",
            "Şampiyonlar Ligi",
            "La Liga",
            "EuroLeague",
            "NBA",
        ],
    )

  # Tarih Seçimi (Bugünden Başlayarak)
  secilen_tarih = st.date_input(
      "📅 Fikstür Tarihi (Bugün Otomatik Seçilidir)", value=bugun_tarih
  )
  st.markdown("---")

  # DİNAMİK TAKIM VE MAÇ EŞLEŞTİRİCİ (Seçilen Tarihe Göre Canlı Üretir)
  takim_havuzu = {
      "Trendyol Süper Lig": [
          ("Galatasaray", "Beşiktaş"),
          ("Fenerbahçe", "Trabzonspor"),
          ("Başakşehir", "Kayserispor"),
          ("Samsunspor", "Göztepe"),
      ],
      "Premier Lig": [
          ("Arsenal", "Manchester City"),
          ("Liverpool", "Chelsea"),
          ("Tottenham", "Manchester United"),
      ],
      "Şampiyonlar Ligi": [
          ("Real Madrid", "Bayern Munich"),
          ("Barcelona", "PSG"),
          ("Inter", "Arsenal"),
      ],
      "La Liga": [
          ("Barcelona", "Atletico Madrid"),
          ("Real Sociedad", "Sevilla"),
      ],
      "EuroLeague": [
          ("Fenerbahçe Beko", "Panathinaikos"),
          ("Anadolu Efes", "Olympiacos"),
      ],
      "NBA": [
          ("L.A. Lakers", "Golden State Warriors"),
          ("Boston Celtics", "Milwaukee Bucks"),
      ],
  }

  mac_listesi = []

  for lig_adi, ciftler in takim_havuzu.items():
    if secilen_lig == "Tümü" or secilen_lig == lig_adi:
      for ev, dep in ciftler:
        mac_listesi.append({
            "lig": lig_adi,
            "ev": ev,
            "dep": dep,
            "saat": f"{random.choice([16, 18, 19, 20, 21])}:00",
            "oranlar": {
                "MS 1": round(random.uniform(1.45, 2.20), 2),
                "X": round(random.uniform(3.20, 3.90), 2),
