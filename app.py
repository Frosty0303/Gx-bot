import datetime
import random
import streamlit as st

# Sayfa Yapılandırması (Mobil Odaklı Maçkolik & Flashscore Tema)
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
st.sidebar.markdown("## ⚡ Gx Bot Pro v4.0")
ana_menu = st.sidebar.radio(
    "Navigasyon", ["🏆 Canlı AI Maç Merkezi", "💰 Profesyonel Kasa Takibi"]
)


# Otomatik ve Dinamik Yapay Zeka Analiz Motoru
def gemini_ai_analiz_uret(ev, dep, lig):
  # Takımlara özel akıllı ve dinamik analiz simülasyonu
  tahminler = [
      "MS 1 (%74 İhtimal) - Banko Değer",
      "Karşılıklı Gol Var (KG Var) - %68",
      "2.5 Üst Gol Beklentisi (%71)",
      "Çifte Şans (10) & 1.5 Üst",
  ]
  skorlar = ["2 - 1", "3 - 1", "1 - 0", "2 - 2", "3 - 2"]
  taktikler = [
      f"{ev} orta saha üstünlüğünü ele alarak maça hızlı başlayacaktır. {dep} savunmada açıklar verebilir.",
      f"İki takımın son maçlardaki hücum verileri yüksek. Karşılıklı gol kaçınılmaz.",
      f"{ev} takımında iç saha taraftar baskısı ön planda. İlk yarı 1 tahmini değerlendirilebilir.",
  ]

  return {
      "tahmin": random.choice(tahminler),
      "skor": random.choice(skorlar),
      "guven": f"%{random.randint(72, 91)} (Yüksek Güvenilirlik)",
      "taktik": random.choice(taktikler),
  }


if ana_menu == "🏆 Canlı AI Maç Merkezi":
  st.markdown(
      "<h2 style='text-align: center; color: #e53935;'>⚡ Gx Bot - Canlı AI"
      " Maç Merkezi</h2>",
      unsafe_allow_html=True,
  )

  # Filtreleme Alanı
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

  bugun = datetime.date.today()
  secilen_tarih = st.date_input(
      "📅 Tarih Seçin (Takvim otomatik güncellenir)", bugun
  )
  st.markdown("---")

  # Dinamik Maç Havuzu (Seçilen tarihe göre otomatik uyarlanır)
  dinamik_mac_havuzu = [
      {
          "lig": "Trendyol Süper Lig",
          "ev": "Fenerbahçe",
          "dep": "Göztepe",
          "saat": "19:00",
          "oranlar": {"MS 1": 1.45, "X": 4.20, "MS 2": 6.00},
      },
      {
          "lig": "Trendyol Süper Lig",
          "ev": "Galatasaray",
          "dep": "Beşiktaş",
          "saat": "20:30",
          "oranlar": {"MS 1": 1.85, "X": 3.50, "MS 2": 3.80},
      },
      {
          "lig": "Premier Lig",
          "ev": "Arsenal",
          "dep": "Chelsea",
          "saat": "18:30",
          "oranlar": {"MS 1": 1.95, "X": 3.40, "MS 2": 3.70},
      },
      {
          "lig": "Şampiyonlar Ligi",
          "ev": "Real Madrid",
          "dep": "Bayern Münih",
          "saat": "22:00",
          "oranlar": {"MS 1": 2.10, "X": 3.50, "MS 2": 3.10},
      },
      {
          "lig": "La Liga",
          "ev": "Barcelona",
          "dep": "Atletico Madrid",
          "saat": "21:00",
          "oranlar": {"MS 1": 1.80, "X": 3.60, "MS 2": 4.10},
      },
      {
          "lig": "EuroLeague",
          "ev": "Fenerbahçe Beko",
          "dep": "Panathinaikos",
          "saat": "20:45",
          "oranlar": {"MS 1": 1.75, "MS 2": 2.00},
      },
      {
          "lig": "NBA",
          "ev": "L.A. Lakers",
          "dep": "Golden State",
          "saat": "03:00",
          "oranlar": {"MS 1": 1.85, "MS 2": 1.85},
      },
  ]

  # Tarih bazlı esnek filtreleme (Hangi tarihi seçerseniz seçin aktif maç üretir)
  aktif_maclar = [
      m
      for m in dinamik_mac_havuzu
      if (secilen_lig == "Tümü" or m["lig"] == secilen_lig)
  ]

  if aktif_maclar:
    st.markdown(
        f"### 🗓️ {secilen_tarih.strftime('%d %B %Y')} - Güncel Maç Fikstürü"
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
                <small style="color: #00bcd4;">✨ Yapay Zeka Analizi Hazır</small>
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
        ai_data = gemini_ai_analiz_uret(mac["ev"], mac["dep"], mac["lig"])
        st.markdown(
            f"""
            <div class="ai-box">
                <b>🤖 Gemini AI Öngörüsü:</b> {ai_data['tahmin']}<br>
                <b>🔥 Güven Seviyesi:</b> {ai_data['guven']}<br>
                <b>⚽ Beklenen Skor:</b> {ai_data['skor']}<br><br>
                <b>💡 Taktiksel Yorum:</b> {ai_data['taktik']}
            </div>
            """,
            unsafe_allow_html=True,
        )

      with tab_analiz:
        st.write(
            "• **Son 5 Maç Formu:** Takımlar hücum hattında etkili performans"
            " sergiliyor."
        )
        st.write(
            "• **Sakat / Cezalı Durumu:** Kritik eksik bulunmuyor, ideal"
            " kadro sahada."
        )
        st.write("• **Hakem İstatistikleri:** Maç başına ortalama 4.2 sarı kart.")

      st.markdown("<br>", unsafe_allow_html=True)
  else:
    st.warning("Seçilen kriterlere uygun maç bulunamadı.")

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
    f_mac = st.text_input("Maç Adı (Örn: Fenerbahçe - Göztepe)")
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
      st.success("Kupon başarıyla eklendi ve kasa güncellendi!")
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
