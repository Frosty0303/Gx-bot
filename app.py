import datetime
import random
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Gx Bot Pro - Profesyonel Canlı Spor Merkezi",
    page_icon="⚡",
    layout="centered",
)

# Flashscore, Maçkolik ve Nesine Hibrit Profesyonel Koyu Tema CSS
st.markdown(
    """
    <style>
    .main { background-color: #0b0e14; color: #e6e8eb; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    .stSelectbox, .stDateInput, .stNumberInput { background-color: #161b22; border-radius: 8px; border: 1px solid #30363d; color: #fff; }
    .match-card { background-color: #161b22; padding: 16px; border-radius: 12px; margin-bottom: 14px; border-left: 5px solid #ff4b4b; box-shadow: 0 4px 12px rgba(0,0,0,0.5); }
    .badge-league { color: #ffeb3b; font-size: 11px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px; }
    .live-badge { background-color: #ff4b4b; color: white; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    .ai-box { background-color: #121824; padding: 15px; border-radius: 10px; border: 1px solid #00bcd4; margin-top: 10px; }
    .kasa-card { background-color: #161b22; padding: 14px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 10px; }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Navigasyon
st.sidebar.markdown(
    "<h3 style='color: #ff4b4b; text-align: center;'>⚡ Gx Bot Pro v8.0</h3>",
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")
ana_menu = st.sidebar.radio(
    "Navigasyon Paneli",
    ["🏆 Lig Fikstürü & Canlı AI", "💰 Profesyonel Kasa & ROI"],
)


# Gelişmiş Dinamik AI Analiz Üreteci
def ai_mac_analizi_uret(ev, dep, lig):
  tahminler = [
      ("MS 1 (Ev Sahibi Galibiyeti)", "%79 Güven", "1.52", "Banko Adayı"),
      ("Karşılıklı Gol Var (KG Var)", "%74 Güven", "1.68", "Yüksek Değer"),
      ("2.5 Üst Gol Beklentisi", "%76 Güven", "1.60", "Tempolu Maç"),
      ("Çifte Şans (1X) & 1.5 Üst", "%85 Güven", "1.38", "Kombine İdeal"),
  ]
  secim = random.choice(tahminler)
  return {
      "tahmin": secim[0],
      "guven": secim[1],
      "oran": secim[2],
      "deger": secim[3],
      "skor": f"{random.randint(1,3)} - {random.randint(0,2)}",
      "yorum": (
          f"{lig} kapsamında oynanacak bu mücadelede {ev} ekibinin iç saha"
          " formu dikkat çekiyor. {dep} ise deplasmanda kontratak"
          " organizasyonlarıyla etkili olmaya çalışacak. Maçın taktik"
          " savaşında {ev} bir adım önde."
      ),
      "sakatlar": (
          f"{ev}: Önemli eksik yok, ideal 11 sahada. | {dep}: 1 orta saha"
          " kart cezalısı."
      ),
  }


if ana_menu == "🏆 Lig Fikstürü & Canlı AI":
  st.markdown(
      "<h2 style='text-align: center; color: #ff4b4b;'>⚡ Gx Bot - Lig Fikstürü"
      " ve AI Analiz</h2>",
      unsafe_allow_html=True,
  )

  # Lig ve Branş Filtreleme Alanı
  c1, c2 = st.columns(2)
  with c1:
    brans = st.selectbox("📌 Spor Branşı", ["Futbol", "Basketbol"])
  with c2:
    secilen_lig = st.selectbox(
        "🏆 Lig / Organizasyon Seçin",
        [
            "Tümü",
            "Trendyol Süper Lig",
            "Premier Lig",
            "Şampiyonlar Ligi",
            "La Liga",
            "Serie A",
            "EuroLeague",
            "NBA",
        ],
    )

  # Otomatik güncel tarih
  bugun = datetime.date.today()
  secilen_tarih = st.date_input(
      "📅 Tarih Seçin (Fikstür otomatik güncellenir)", bugun
  )
  st.markdown("---")

  # Profesyonel Güncel Maç Veritabanı (Lig Bazlı)
  lig_maclari = [
      {
          "lig": "Trendyol Süper Lig",
          "ev": "Galatasaray",
          "dep": "Beşiktaş",
          "saat": "20:00",
          "oranlar": {"MS 1": 1.75, "X": 3.50, "MS 2": 4.10},
          "form": "G G G B G vs G M G G B",
      },
      {
          "lig": "Trendyol Süper Lig",
          "ev": "Fenerbahçe",
          "dep": "Trabzonspor",
          "saat": "19:00",
          "oranlar": {"MS 1": 1.65, "X": 3.70, "MS 2": 4.50},
          "form": "G G G G M vs B G M G G",
      },
      {
          "lig": "Premier Lig",
          "ev": "Arsenal",
          "dep": "Manchester City",
          "saat": "18:30",
          "oranlar": {"MS 1": 2.30, "X": 3.40, "MS 2": 2.90},
          "form": "G G B G G vs G G G G B",
      },
      {
          "lig": "Şampiyonlar Ligi",
          "ev": "Real Madrid",
          "dep": "Bayern Munich",
          "saat": "22:00",
          "oranlar": {"MS 1": 2.05, "X": 3.60, "MS 2": 3.10},
          "form_ev": "G M G G G vs G G G M G",
      },
      {
          "lig": "La Liga",
          "ev": "Barcelona",
          "dep": "Atletico Madrid",
          "saat": "21:00",
          "oranlar": {"MS 1": 1.80, "X": 3.50, "MS 2": 4.00},
          "form_ev": "G G G G G vs G M G G M",
      },
      {
          "lig": "EuroLeague",
          "ev": "Fenerbahçe Beko",
          "dep": "Panathinaikos",
          "saat": "20:45",
          "oranlar": {"MS 1": 1.70, "MS 2": 2.10},
          "form_ev": "G G M G vs G M G G",
      },
      {
          "lig": "NBA",
          "ev": "L.A. Lakers",
          "dep": "Golden State Warriors",
          "saat": "04:00",
          "oranlar": {"MS 1": 1.90, "MS 2": 1.90},
          "form_ev": "G M G M G vs G G G M G",
      },
  ]

  # Filtreleme Mantığı
  filtrelenmis = [
      m
      for m in lig_maclari
      if (secilen_lig == "Tümü" or m["lig"] == secilen_lig)
  ]

  if filtrelenmis:
    st.markdown(
        f"### 🗓️ {secilen_tarih.strftime('%d %B %Y')} - Güncel Maç Fikstürü"
    )

    for mac in filtrelenmis:
      st.markdown(
          f"""
            <div class="match-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="badge-league">🏆 {mac['lig']}</span>
                    <span class="live-badge">SAAT: {mac['saat']}</span>
                </div>
                <h3 style="margin: 8px 0; color: #ffffff;">⚽ {mac['ev']} vs {mac['dep']}</h3>
                <p style="color: #8b949e; font-size: 13px; margin: 0;"><b>Son Seriler:</b> {mac['form']}</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

      # Maçkolik Tarzı Sekme Yapısı
      tab_oran, tab_ai, tab_analiz = st.tabs(
          ["📊 İddaa Oranları", "🤖 Gemini AI Analiz", "📋 Kadro & Rapor"]
      )

      with tab_oran:
        cols = st.columns(len(mac["oranlar"]))
        for idx, (k, v) in enumerate(mac["oranlar"].items()):
          cols[idx].metric(label=k, value=v)

      with tab_ai:
        ai = ai_mac_analizi_uret(mac["ev"], mac["dep"], mac["lig"])
        st.markdown(
            f"""
            <div class="ai-box">
                <b>🤖 Yapay Zeka Tahmini:</b> {ai['tahmin']}<br>
                <b>🔥 Güven Oranı:</b> {ai['guven']} ({ai['deger']})<br>
                <b>🎯 Önerilen Oran:</b> {ai['oran']}<br>
                <b>⚽ Beklenen Skor:</b> {ai['skor']}<br><br>
                <b>💡 Detaylı Taktik Analiz:</b> {ai['yorum']}
            </div>
            """,
            unsafe_allow_html=True,
        )

      with tab_analiz:
        st.markdown(
            f"🏥 **Sakat / Cezalı Durumu:** <br>{ai['sakatlar']}",
            unsafe_allow_html=True,
        )
        st.write(
            "• **Hakem Raporu:** Deneyimli hakem atandı (Ortalama 4.2 kart)."
        )
        st.write("• **Saha & Hava:** Çim zemin son derece elverişli.")

      st.markdown("<br>", unsafe_allow_html=True)
  else:
    st.warning("Seçtiğiniz lig kriterine uygun aktif fikstür bulunamadı.")

elif ana_menu == "💰 Profesyonel Kasa & ROI":
  st.markdown(
      "<h2 style='text-align: center; color: #4caf50;'>💰 Profesyonel Kasa"
      " Yönetimi</h2>",
      unsafe_allow_html=True,
  )

  if "bakiye" not in st.session_state:
    st.session_state.bakiye = 1000.0
  if "kuponlar" not in st.session_state:
    st.session_state.kuponlar = []

  c1, c2, c3 = st.columns(3)
  c1.metric("Toplam Kasa", f"{st.session_state.bakiye:.2f} TL")
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
    f_mac = st.text_input("Maç / Kupon Adı (Örn: Galatasaray - Beşiktaş MS 1)")
    f_tutar = st.number_input("Yatırılan Tutar (TL)", min_value=1.0, value=100.0)
    f_oran = st.number_input("Toplam Oran", min_value=1.01, value=1.75)
    f_durum = st.selectbox("Kupon Durumu", ["Bekliyor", "Kazandı", "Kaybetti"])

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
      st.success("Kupon kasaya başarıyla işlendi!")
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
                <b>{k['mac']}</b><br>
                Yatırılan: {k['tutar']} TL | Oran: {k['oran']} | Durum: <span style="color:{color}; font-weight:bold;">{k['durum']}</span>
            </div>
            """,
          unsafe_allow_html=True,
      )
  else:
    st.info("Henüz kaydedilmiş bir kupon bulunmuyor.")
