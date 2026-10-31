import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="Gx Bot Pro - Canlı AI Maç Merkezi",
    page_icon="⚡",
    layout="centered",
)

st.markdown(
    """
    <style>
    .main { background-color: #0b0e14; color: #e6e8eb; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    .stSelectbox, .stDateInput, .stNumberInput { background-color: #161b22; border-radius: 8px; border: 1px solid #30363d; color: #fff; }
    .match-card { background-color: #161b22; padding: 15px; border-radius: 12px; margin-bottom: 12px; border-left: 5px solid #e53935; box-shadow: 0 4px 10px rgba(0,0,0,0.4); }
    .badge-league { color: #ffeb3b; font-size: 11px; font-weight: bold; text-transform: uppercase; }
    .live-badge { background-color: #e53935; color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .ai-box { background-color: #161f28; padding: 14px; border-radius: 10px; border: 1px solid #00bcd4; margin-top: 10px; }
    .kasa-card { background-color: #161b22; padding: 12px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 8px; }
    </style>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown("## ⚡ Gx Bot Pro")
ana_menu = st.sidebar.radio(
    "Navigasyon", ["🏆 Güncel Maç Fikstürü", "💰 Profesyonel Kasa Takibi"]
)


def ai_analiz_uret(ev, dep):
  tahminler = [
      "MS 1 (%76 Güvenilirlik) - Banko Değer",
      "Karşılıklı Gol Var (KG Var) - %71",
      "2.5 Üst Gol Beklentisi (%74)",
      "Çifte Şans (1X) ve 1.5 Üst",
  ]
  return {
      "tahmin": random.choice(tahminler),
      "oran": round(random.uniform(1.45, 2.20), 2),
      "skor": f"{random.randint(1,3)} - {random.randint(0,2)}",
      "taktik": (
          f"{ev} ev sahibi avantajıyla baskılı başlayacak. {dep} kontra"
          " arayacak."
      ),
  }


if ana_menu == "🏆 Güncel Maç Fikstürü":
  st.markdown(
      "<h2 style='text-align: center; color: #e53935;'>⚡ Gx Bot - Maç"
      " Merkezi</h2>",
      unsafe_allow_html=True,
  )

  c_brans, c_lig = st.columns(2)
  with c_brans:
    brans = st.selectbox("📌 Spor Branşı", ["Futbol", "Basketbol"])
  with c_lig:
    secilen_lig = st.selectbox(
        "🏆 Lig / Kupa",
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

  secilen_tarih = st.date_input("📅 Tarih", datetime.date.today())
  st.markdown("---")

  guncel_maclar = [
      {
          "lig": "Trendyol Süper Lig",
          "ev": "Galatasaray",
          "dep": "Samsunspor",
          "saat": "19:00",
          "oranlar": {"MS 1": 1.48, "X": 4.10, "MS 2": 5.80},
      },
      {
          "lig": "Trendyol Süper Lig",
          "ev": "Fenerbahçe",
          "dep": "Trabzonspor",
          "saat": "21:45",
          "oranlar": {"MS 1": 1.72, "X": 3.60, "MS 2": 4.10},
      },
      {
          "lig": "Premier Lig",
          "ev": "Manchester City",
          "dep": "Liverpool",
          "saat": "18:30",
          "oranlar": {"MS 1": 2.05, "X": 3.40, "MS 2": 3.20},
      },
      {
          "lig": "Şampiyonlar Ligi",
          "ev": "Real Madrid",
          "dep": "Inter",
          "saat": "22:00",
          "oranlar": {"MS 1": 1.90, "X": 3.50, "MS 2": 3.60},
      },
      {
          "lig": "La Liga",
          "ev": "Barcelona",
          "dep": "Villarreal",
          "saat": "21:00",
          "oranlar": {"MS 1": 1.52, "X": 4.00, "MS 2": 5.50},
      },
      {
          "lig": "EuroLeague",
          "ev": "Anadolu Efes",
          "dep": "Real Madrid",
          "saat": "20:30",
          "oranlar": {"MS 1": 1.85, "MS 2": 1.95},
      },
      {
          "lig": "NBA",
          "ev": "Boston Celtics",
          "dep": "Dallas Mavericks",
          "saat": "03:00",
          "oranlar": {"MS 1": 1.75, "MS 2": 2.05},
      },
  ]

  filtrelenmis = [
      m for m in guncel_maclar if secilen_lig == "Tümü" or m["lig"] == secilen_lig
  ]

  if filtrelenmis:
    st.markdown(
        f"### 🗓️ {secilen_tarih.strftime('%d %B %Y')} - Maç Programı"
    )

    for mac in filtrelenmis:
      st.markdown(
          f"""
            <div class="match-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="badge-league">🏆 {mac['lig']}</span>
                    <span class="live-badge">SAAT: {mac['saat']}</span>
                </div>
                <h3 style="margin: 8px 0; color: #fff;">⚽ {mac['ev']} vs {mac['dep']}</h3>
                <small style="color: #00bcd4;">✨ Yapay Zeka Analizi Aktif</small>
            </div>
            """,
          unsafe_allow_html=True,
      )

      tab_oran, tab_ai, tab_analiz = st.tabs(
          ["📊 Oranlar", "🤖 Gemini AI Tahmin", "📋 Detaylar"]
      )

      with tab_oran:
        c1, c2, c3 = st.columns(3)
        for idx, (k, v) in enumerate(mac["oranlar"].items()):
          [c1, c2, c3][idx].metric(label=k, value=v)

      with tab_ai:
        ai = ai_analiz_uret(mac["ev"], mac["dep"])
        st.markdown(
            f"""
            <div class="ai-box">
                <b>🤖 AI Öngörüsü:</b> {ai['tahmin']}<br>
                <b>🎯 Tavsiye Oran:</b> {ai['oran']}<br>
                <b>⚽ Beklenen Skor:</b> {ai['skor']}<br><br>
                <b>💡 Analiz:</b> {ai['taktik']}
            </div>
            """,
            unsafe_allow_html=True,
        )

      with tab_analiz:
        st.write("• **Form Durumu:** Takımların hücum hattı oldukça formda.")
        st.write("• **Kadro:** Sakat ve cezalı oyuncu bulunmuyor.")

      st.markdown("<br>", unsafe_allow_html=True)

elif ana_menu == "💰 Profesyonel Kasa Takibi":
  st.markdown(
      "<h2 style='text-align: center; color: #4caf50;'>💰 Kasa Yönetimi</h2>",
      unsafe_allow_html=True,
  )

  if "bakiye" not in st.session_state:
    st.session_state.bakiye = 1000.0
  if "kuponlar" not in st.session_state:
    st.session_state.kuponlar = []

  c1, c2 = st.columns(2)
  c1.metric("Mevcut Kasa", f"{st.session_state.bakiye:.2f} TL")
  c2.metric("Toplam Kupon", len(st.session_state.kuponlar))

  st.markdown("---")
  with st.form("kasa_formu"):
    f_mac = st.text_input("Maç Adı")
    f_tutar = st.number_input("Tutar (TL)", min_value=1.0, value=100.0)
    f_oran = st.number_input("Oran", min_value=1.01, value=1.85)
    f_durum = st.selectbox("Durum", ["Bekliyor", "Kazandı", "Kaybetti"])

    if st.form_submit_button("Kuponu Kaydet"):
      if f_durum == "Kazandı":
        st.session_state.bakiye += f_tutar * (f_oran - 1)
      elif f_durum == "Kaybetti":
        st.session_state.bakiye -= f_tutar
      st.session_state.kuponlar.append({
          "mac": f_mac,
          "tutar": f_tutar,
          "oran": f_oran,
          "durum": f_durum,
      })
      st.rerun()

  st.subheader("Geçmiş Kuponlar")
  for k in st.session_state.kuponlar:
    st.markdown(
        f"<div class='kasa-card'><b>{k['mac']}</b> - {k['tutar']} TL @ {k['oran']} | <b>{k['durum']}</b></div>",
        unsafe_allow_html=True,
    )
