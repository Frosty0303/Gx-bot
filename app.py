import datetime
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Gx Bot - Profesyonel Bahis & Kasa Paneli",
    page_icon="⚡",
    layout="centered",
)

# Modern ve Şık Tasarım İçin CSS
st.markdown(
    """
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stSelectbox, .stDateInput, .stNumberInput { background-color: #1a1c23; border-radius: 8px; }
    .match-card { background-color: #1e222d; padding: 15px; border-radius: 10px; margin-bottom: 15px; border-left: 4px solid #ff4b4b; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    .kasa-card { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 10px; }
    </style>
""",
    unsafe_allow_html=True,
)

# Başlık
st.markdown(
    "<h2 style='text-align: center; color: #ff4b4b;'>⚡ Gx Bot - Mobil Bahis"
    " Analiz Paneli</h2>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #808495;'>Maçkolik Tarzı Ligler,"
    " Yapay Zeka Tahminleri & Kasa Yönetimi</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Yan Menü / Sayfa Navigasyonu
ana_menu = st.sidebar.radio(
    "📌 Menü", ["📅 Maçlar & Ligler", "💰 Kasa Yönetimi"]
)

if ana_menu == "📅 Maçlar & Ligler":
  brans = st.selectbox("📌 Spor Branşı Seçin:", ["Futbol", "Basketbol"])

  ligler_secenekleri = {
      "Futbol": [
          "Tümü",
          "Trendyol Süper Lig",
          "Trendyol 1. Lig",
          "Premier Lig",
          "Şampiyonlar Ligi",
          "La Liga",
          "Serie A",
      ],
      "Basketbol": [
          "Tümü",
          "EuroLeague",
          "Türkiye Basketbol Süper Ligi",
          "NBA",
      ],
  }

  secilen_lig = st.selectbox("🏆 Lig / Kupa Seçin:", ligler_secenekleri[brans])
  bugun = datetime.date.today()
  secilen_tarih = st.date_input("📅 Tarih Seçin:", bugun)

  st.markdown(
      f"### 🗓️ {secilen_tarih.strftime('%d %B %Y')} - {secilen_lig} Programı"
  )

  kapsamli_maclar = {
      "Futbol": [
          {
              "lig": "Trendyol Süper Lig",
              "tarih": datetime.date(2026, 10, 31),
              "ev": "Fenerbahçe",
              "dep": "Göztepe",
              "saat": "19:00",
              "oranlar": {"MS 1": 1.45, "X": 4.20, "MS 2": 6.00},
              "tahmin": "MS 1 (%72 İhtimal)",
              "deger": "MS 1 (Banko)",
              "form": "Fenerbahçe (G G G G B) - Göztepe (G M B G M)",
          },
          {
              "lig": "Trendyol Süper Lig",
              "tarih": datetime.date(2026, 10, 31),
              "ev": "Kocaelispor",
              "dep": "Çaykur Rizespor",
              "saat": "16:00",
              "oranlar": {"MS 1": 2.20, "X": 3.10, "MS 2": 3.10},
              "tahmin": "KG Var (%58 İhtimal)",
              "deger": "Değer Var",
              "form": "Kocaelispor (G G B M G) - Rizespor (M M G B G)",
          },
          {
              "lig": "Premier Lig",
              "tarih": datetime.date(2026, 10, 31),
              "ev": "Arsenal",
              "dep": "Chelsea",
              "saat": "18:30",
              "oranlar": {"MS 1": 1.95, "X": 3.40, "MS 2": 3.70},
              "tahmin": "2.5 Üst (%65 İhtimal)",
              "deger": "Üst Oran",
              "form": "Arsenal (G G G B G) - Chelsea (G M G B G)",
          },
          {
              "lig": "Şampiyonlar Ligi",
              "tarih": datetime.date(2026, 11, 3),
              "ev": "Real Madrid",
              "dep": "Bayern Münih",
              "saat": "22:00",
              "oranlar": {"MS 1": 2.10, "X": 3.50, "MS 2": 3.10},
              "tahmin": "KG Var (%68 İhtimal)",
              "deger": "Karşılıklı Gol",
              "form": "Real Madrid (G G M G G) - Bayern (G G G M G)",
          },
          {
              "lig": "La Liga",
              "tarih": datetime.date(2026, 11, 1),
              "ev": "Barcelona",
              "dep": "Atletico Madrid",
              "saat": "21:00",
              "oranlar": {"MS 1": 1.80, "X": 3.60, "MS 2": 4.10},
              "tahmin": "MS 1 (%60 İhtimal)",
              "deger": "10 Çifte Şans",
              "form": "Barcelona (G G G G G) - Atletico (G M G G M)",
          },
      ],
      "Basketbol": [
          {
              "lig": "EuroLeague",
              "tarih": datetime.date(2026, 10, 31),
              "ev": "Fenerbahçe Beko",
              "dep": "Panathinaikos",
              "saat": "20:45",
              "oranlar": {"MS 1": 1.75, "MS 2": 2.00},
              "tahmin": "MS 1 (%56 İhtimal)",
              "deger": "Handikaplı MS 1",
              "form": "FB Beko (G G M G) - Panathinaikos (G M G G)",
          },
          {
              "lig": "NBA",
              "tarih": datetime.date(2026, 11, 1),
              "ev": "L.A. Lakers",
              "dep": "Golden State",
              "saat": "03:00",
              "oranlar": {"MS 1": 1.85, "MS 2": 1.85},
              "tahmin": "225.5 Üst (%62 İhtimal)",
              "deger": "Üst Seçeneği",
              "form": "Lakers (G M G M G) - GSW (G G G M G)",
          },
      ],
  }

  brans_maclari = kapsamli_maclar.get(brans, [])
  filtrelenmis_maclar = [
      m
      for m in brans_maclari
      if m["tarih"] == secilen_tarih
      and (secilen_lig == "Tümü" or m["lig"] == secilen_lig)
  ]

  if filtrelenmis_maclar:
    for mac in filtrelenmis_maclar:
      with st.container():
        st.markdown(
            f"""
                <div class="match-card">
                    <span style='color: #ff4b4b; font-size: 12px; font-weight: bold;'>🏆 {mac['lig']}</span>
                    <h4>⚽ {mac['ev']} vs {mac['dep']}</h4>
                    <p><b>Saat:</b> {mac['saat']}</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

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
        f"⚠️ Seçtiğiniz tarihte ({secilen_tarih.strftime('%d %B %Y')}) ve"
        f" kategoride ({secilen_lig}) maç bulunmuyor."
    )

elif ana_menu == "💰 Kasa Yönetimi":
  st.markdown("### 💰 Profesyonel Kasa Takibi")

  if "kasa_bakiye" not in st.session_state:
    st.session_state.kasa_bakiye = 1000.0
  if "kuponlar" not in st.session_state:
    st.session_state.kuponlar = []

  col1, col2 = st.columns(2)
  with col1:
    st.metric(
        label="Mevcut Kasa", value=f"{st.session_state.kasa_bakiye:.2f} TL"
    )
  with col2:
    st.metric(label="Toplam Kupon", value=len(st.session_state.kuponlar))

  st.markdown("---")
  st.subheader("📝 Yeni Kupon Ekle")

  with st.form("kasa_form"):
    mac_adi = st.text_input("Maç / Kupon Adı (Örn: Fenerbahçe - Göztepe)")
    yatirilan = st.number_input("Yاتırilan Tutar (TL)", min_value=1.0, value=50.0)
    oran = st.number_input("Toplam Oran", min_value=1.01, value=1.80)
    durum = st.selectbox("Kupon Durumu", ["Bekliyor", "Kazandı", "Kaybetti"])

    submitted = st.form_submit_button("Kuponu Kaydet")
    if submitted:
      potansiyel_kazanc = yatirilan * oran
      st.session_state.kuponlar.append({
          "mac": mac_adi,
          "yatirilan": yatirilan,
          "oran": oran,
          "kazanc": potansiyel_kazanc,
          "durum": durum,
      })
      if durum == "Kazandı":
        st.session_state.kasa_bakiye += potansiyel_kazanc - yatirilan
      elif durum == "Kaybetti":
        st.session_state.kasa_bakiye -= yatirilan
      st.success("Kupon başarıyla kasaya eklendi!")
      st.rerun()

  st.markdown("---")
  st.subheader("📊 Geçmiş Kuponlar")
  if st.session_state.kuponlar:
    for k in st.session_state.kuponlar:
      renk = (
          "green"
          if k["durum"] == "Kazandı"
          else ("red" if k["durum"] == "Kaybetti" else "orange")
      )
      st.markdown(
          f"""
            <div class="kasa-card">
                <b>{k['mac']}</b><br>
                Yatırılan: {k['yatirilan']} TL | Oran: {k['oran']} | Durum: <span style='color:{renk};'><b>{k['durum']}</b></span>
            </div>
            """,
          unsafe_allow_html=True,
      )
  else:
    st.info("Henüz kaydedilmiş kupon bulunmuyor.")
