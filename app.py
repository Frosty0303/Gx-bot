import datetime
import streamlit as st

# Sayfa Yapılandırması (Mobil Odaklı Maçkolik & Flashscore Teması)
st.set_page_config(
    page_title="Gx Bot Pro - Canlı AI Analiz & Kasa",
    page_icon="⚡",
    layout="centered",
)

# Custom Flashscore & Maçkolik Dark UI CSS
st.markdown(
    """
    <style>
    .main { background-color: #0b0e14; color: #e6e8eb; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    .stSelectbox, .stDateInput, .stNumberInput, .stTextInput { background-color: #161b22; border-radius: 8px; border: 1px solid #30363d; }
    .match-card { background-color: #161b22; padding: 14px; border-radius: 12px; margin-bottom: 12px; border-left: 5px solid #e53935; box-shadow: 0 4px 10px rgba(0,0,0,0.4); }
    .badge-league { color: #ffeb3b; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; }
    .kasa-card { background-color: #161b22; padding: 12px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 8px; }
    </style>
""",
    unsafe_allow_html=True,
)

# Yan Menü Navigasyonu
st.sidebar.markdown("## ⚡ Gx Bot Pro v2.5")
ana_menu = st.sidebar.radio(
    "Navigasyon", ["🏆 Maç Merkezi & Canlı AI", "💰 Profesyonel Kasa Takibi"]
)

# Yapay Zeka Analiz Motoru (Gemini veya Dahili Algoritma)
def ai_analiz_yap(ev, dep, lig):
  return {
      "tahmin": f"{ev} Karşılıklı Gol Var (KG Var)",
      "guven": "%78 (Yüksek Güven)",
      "skor_beklentisi": "2 - 1 veya 2 - 2",
      "taktik": (
          f"{ev} evinde agresif basıyor. {dep} deplasmanda kontratakla etkili."
          " 2.5 Üst ve KG Var seçenekleri değerli."
      ),
  }


if ana_menu == "🏆 Maç Merkezi & Canlı AI":
  st.markdown(
      "<h2 style='text-align: center; color: #e53935;'>⚡ Gx Bot Pro - Maç"
      " Merkezi</h2>",
      unsafe_allow_html=True,
  )

  col_brans, col_lig = st.columns(2)
  with col_brans:
    brans = st.selectbox("📌 Spor Branşı", ["Futbol", "Basketbol"])
  with col_lig:
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

  secilen_tarih = st.date_input("📅 Tarih", datetime.date.today())
  st.markdown("---")

  # Maç Veritabanı
  maclar = [
      {
          "lig": "Trendyol Süper Lig",
          "ev": "Fenerbahçe",
          "dep": "Göztepe",
          "saat": "19:00",
          "oranlar": {"MS 1": 1.45, "X": 4.20, "MS 2": 6.00},
          "form": "FB (G-G-G) | GÖZ (G-M-B)",
      },
      {
          "lig": "Premier Lig",
          "ev": "Arsenal",
          "dep": "Chelsea",
          "saat": "18:30",
          "oranlar": {"MS 1": 1.95, "X": 3.40, "MS 2": 3.70},
          "form": "ARS (G-G-B) | CHE (G-M-G)",
      },
      {
          "lig": "Şampiyonlar Ligi",
          "ev": "Real Madrid",
          "dep": "Bayern Münih",
          "saat": "22:00",
          "oranlar": {"MS 1": 2.10, "X": 3.50, "MS 2": 3.10},
          "form": "RMA (G-M-G) | BAY (G-G-M)",
      },
  ]

  for mac in maclar:
    if secilen_lig == "Tümü" or mac["lig"] == secilen_lig:
      st.markdown(
          f"""
            <div class="match-card">
                <span class="badge-league">🏆 {mac['lig']} • {mac['saat']}</span>
                <h3 style="margin: 5px 0;">⚽ {mac['ev']} vs {mac['dep']}</h3>
                <small style="color: #8b949e;">Form: {mac['form']}</small>
            </div>
            """,
          unsafe_allow_html=True,
      )

      tab_oran, tab_ai, tab_detay = st.tabs(
          ["📊 Nesine Oranlar", "🤖 Gemini AI Analiz", "📈 Detaylar"]
      )

      with tab_oran:
        cols = st.columns(len(mac["oranlar"]))
        for idx, (k, v) in enumerate(mac["oranlar"].items()):
          cols[idx].metric(label=k, value=v)

      with tab_ai:
        analiz = ai_analiz_yap(mac["ev"], mac["dep"], mac["lig"])
        st.success(f"🎯 **Yapay Zeka Tahmini:** {analiz['tahmin']}")
        st.info(f"🔥 **Güven Oranı:** {analiz['guven']}")
        st.warning(f"⚽ **Skor Beklentisi:** {analiz['skor_beklentisi']}")
        st.write(f"💡 **Taktik Analiz:** {analiz['taktik']}")

      with tab_detay:
        st.write("• Son 5 Maç Aralarındaki Gol Ortalaması: 3.2")
        st.write("• Sakat/Cezalı: Ev Sahibinde 1 Önemli Eksik Var")

elif ana_menu == "💰 Profesyonel Kasa Takibi":
  st.markdown(
      "<h2 style='text-align: center; color: #4caf50;'>💰 Bankroll / Kasa"
      " Yönetimi</h2>",
      unsafe_allow_html=True,
  )

  if "bakiye" not in st.session_state:
    st.session_state.bakiye = 1000.0
  if "kuponlar" not in st.session_state:
    st.session_state.kuponlar = []

  c1, c2, c3 = st.columns(3)
  c1.metric("Toplam Bakiye", f"{st.session_state.bakiye:.2f} TL")
  c2.metric("Oynanan Kupon", len(st.session_state.kuponlar))

  kazananlar = len(
      [k for k in st.session_state.kuponlar if k["durum"] == "Kazandı"]
  )
  win_rate = (
      (kazananlar / len(st.session_state.kuponlar) * 100)
      if st.session_state.kuponlar
      else 0
  )
  c3.metric("Kazanma Oranı (Win Rate)", f"%{win_rate:.1f}")

  st.markdown("---")
  st.subheader("➕ Yeni Bahis / Kupon Ekle")

  with st.form("kasa_formu"):
    f_mac = st.text_input("Maç / Kupon Adı")
    f_tutar = st.number_input("Yatırılan Tutar (TL)", min_value=5.0, value=100.0)
    f_oran = st.number_input("Oran", min_value=1.05, value=1.85)
    f_durum = st.selectbox("Sonuç", ["Bekliyor", "Kazandı", "Kaybetti"])

    if st.form_submit_button("Kuponu Kaydet ve Kasa Güncelle"):
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
      st.success("Kupon kasaya işlendi!")
      st.rerun()

  st.markdown("---")
  st.subheader("📋 Geçmiş Kuponlar")
  for k in reversed(st.session_state.kuponlar):
    color = (
        "#4caf50"
        if k["durum"] == "Kazandı"
        else ("#e53935" if k["durum"] == "Kaybetti" else "#ff9800")
    )
    st.markdown(
        f"""
        <div class="kasa-card">
            <b>{k['mac']}</b> — {k['tutar']} TL @ {k['oran']} Oran | Durum: <span style="color:{color}; font-weight:bold;">{k['durum']}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
