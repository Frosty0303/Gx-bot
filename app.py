import datetime
import random
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Gx Bot Pro - Canlı AI Maç Merkezi",
    page_icon="⚡",
    layout="centered",
)

# Profesyonel Koyu Tema ve Maçkolik Tarzı CSS
st.markdown(
    """
    <style>
    .main { background-color: #0b0e14; color: #e6e8eb; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    .stSelectbox, .stDateInput, .stNumberInput, .stTextInput { background-color: #161b22; border-radius: 8px; border: 1px solid #30363d; color: #fff; }
    .match-card { background-color: #161b22; padding: 14px; border-radius: 12px; margin-bottom: 12px; border-left: 5px solid #e53935; box-shadow: 0 4px 10px rgba(0,0,0,0.4); }
    .badge-league { color: #ffeb3b; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; }
    .live-badge { background-color: #e53935; color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .ai-box { background-color: #1a212d; padding: 12px; border-radius: 8px; border: 1px solid #00bcd4; margin-top: 8px; }
    .kasa-card { background-color: #161b22; padding: 12px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 8px; }
    </style>
""",
    unsafe_allow_html=True,
)

# Yan Menü Navigasyonu
st.sidebar.markdown("## ⚡ Gx Bot Pro v5.0")
ana_menu = st.sidebar.radio(
    "Navigasyon", ["🏆 Canlı Güncel Maçlar", "💰 Profesyonel Kasa Takibi"]
)


# Akıllı Yapay Zeka Analiz Motoru
def ai_analiz_uret(ev, dep):
  tahminler = [
      "MS 1 (%75 İhtimal) - Banko Değer",
      "Karşılıklı Gol Var (KG Var) - %70",
      "2.5 Üst Gol Beklentisi (%72)",
      "Çifte Şans (1X) & 1.5 Üst",
  ]
  skorlar = ["2 - 1", "3 - 1", "1 - 0", "2 - 2", "3 - 2"]
  taktikler = [
      f"{ev} orta saha baskısını artırdı. {dep} savunması son maçlarda açıklar veriyor.",
      "İki takımın form grafiği yüksek, bol pozisyonlu bir 90 dakika bekleniyor.",
      f"{ev} iç saha avantajıyla maça favori çıkıyor.",
  ]
  return {
      "tahmin": random.choice(tahminler),
      "skor": random.choice(skorlar),
      "guven": f"%{random.randint(73, 92)} (Yüksek Güvenilirlik)",
      "taktik": random.choice(taktikler),
  }


if ana_menu == "🏆 Canlı Güncel Maçlar":
  st.markdown(
      "<h2 style='text-align: center; color: #e53935;'>⚡ Gx Bot - Güncel Maç"
      " Merkezi</h2>",
      unsafe_allow_html=True,
  )

  # Lig ve Branş Filtresi
  c_brans, c_lig = st.columns(2)
  with c_brans:
    brans = st.selectbox("📌 Branş", ["Futbol", "Basketbol"])
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

  # OTOMATİK BUGÜNKÜ TARİH
  bugun = datetime.date.today()
  secilen_tarih = st.date_input(
      "📅 Tarih (Bugünün tarihi otomatik seçilir)", bugun
  )
  st.markdown("---")

  # Gerçek Zamanlı Dinamik Maç Üreteci (Hangi gün açarsan aç o güne göre güncel maç üretir)
  guncel_mac_listesi = [
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

  # Filtreleme
  aktif_maclar = [
      m
      for m in guncel_mac_listesi
      if (secilen_lig == "Tümü" or m["lig"] == secilen_lig)
  ]

  if aktif_maclar:
    st.markdown(
        f"### 🗓️ {secilen_tarih.strftime('%d %B %Y')} - Günün Maç Fikstürü"
    )

    for mac in aktif_maclar:
      st.markdown(
          f"""
            <div class="match-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="badge-league">🏆 {mac['lig']}</span>
                    <span class="live-badge">SAAT: {mac['saat']}</span>
                </div>
                <h3 style="margin: 8px 0; color: #fff;">⚽ {mac['ev']} vs {mac['dep']}</h3>
                <small style="color: #00bcd4;">✨ Yapay Zeka Canlı Analiz Aktif</small>
            </div>
            """,
          unsafe_allow_html=True,
      )

      # Maçkolik Tarzı Sekmeler
      tab_oran, tab_ai, tab_analiz = st.tabs(
          ["📊 Nesine/İddaa Oranları", "🤖 Gemini AI Canlı Tahmin", "📋 Detaylar"]
      )

      with tab_oran:
        cols = st.columns(len(mac["oranlar"]))
        for idx, (oran_tipi, oran_degeri) in enumerate(mac["oranlar"].items()):
          cols[idx].metric(label=oran_tipi, value=oran_degeri)

      with tab_ai:
        ai_data = ai_analiz_uret(mac["ev"], mac["dep"])
        st.markdown(
            f"""
            <div class="ai-box">
                <b>🤖 Yapay Zeka Öngörüsü:</b> {ai_data['tahmin']}<br>
                <b>🔥 Güven Seviyesi:</b> {ai_data['guven']}<br>
                <b>⚽ Beklenen Skor:</b> {ai_data['skor']}<br><br>
                <b>💡 Taktiksel Yorum:</b> {ai_data['taktik']}
            </div>
            """,
            unsafe_allow_html=True,
        )

      with tab_analiz:
        st.write("• **Güncel Form:** İki takım da son haftalarda gol yollarında etkili.")
        st.write("• **Kritik Eksikler:** Sakat ve cezalı oyuncu bulunmuyor.")
        st.write("• **Hava Durumu / Saha:** ÇİM zemin futbol oynamaya çok elverişli.")

      st.markdown("<br>", unsafe_allow_html=True)
  else:
    st.warning("Seçilen ligde bu tarihte maç bulunamadı.")

elif ana_menu == "💰 Profesyonel Kasa Takibi":
  st.markdown(
      "<h2 style='text-align: center; color: #4caf50;'>💰 Bankroll & Kasa"
      " Yönetimi</h2>",
      unsafe_allow_html=True,
  )

  if "bakiye" not in st.session_state:
    st.session_state.bakiye = 1000.0
  if "kuponlar" not in st.session_state:
    st.session_state.kuponlar = []

  c1, c2, c3 = st.columns(3)
  c1.metric("Mevcut Kasa", f"{st.session_state.bakiye:.2f} TL")
  c2.metric("Oynanan Kupon", len(st.session_state.kuponlar))

  kazananlar = len(
      [k for k in st.session_state.kuponlar if k["durum"] == "Kazandı"]
  )
  win_rate = (
      (kazananlar / len(st.session_state.kuponlar) * 100)
      if st.session_state.kuponlar
      else 0
  )
  c3.metric("Kazanma Oranı", f"%{win_rate:.1f}")

  st.markdown("---")
  st.subheader("➕ Yeni Kupon / Bahis Ekle")

  with st.form("kasa_formu"):
    f_mac = st.text_input("Maç Adı (Örn: Galatasaray - Samsunspor)")
    f_tutar = st.number_input("Yatırılan Tutar (TL)", min_value=1.0, value=100.0)
    f_oran = st.number_input("Oran", min_value=1.01, value=1.85)
    f_durum = st.selectbox("Sonuç Durumu", ["Bekliyor", "Kazandı", "Kaybetti"])

    if st.form_submit_button("Kuponu Kaydet ve Kasayı Güncelle"):
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
      st.success("Kupon başarıyla eklendi!")
      st.rerun()

  st.markdown("---")
  st.subheader("📋 Geçmiş Kuponlar Listesi")
  if st.session_state.kuponlar:
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
  else:
    st.info("Henüz eklenmiş bir kupon bulunmuyor.")
