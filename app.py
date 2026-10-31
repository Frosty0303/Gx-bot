import datetime
import streamlit as st

st.set_page_config(
    page_title="Gx Bot - Mobil Analiz", page_icon="⚡", layout="centered"
)

st.markdown(
    """
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stSelectbox, .stDateInput, .stNumberInput { background-color: #1a1c23; border-radius: 8px; }
    .match-card { background-color: #1e222d; padding: 15px; border-radius: 10px; margin-bottom: 15px; border-left: 4px solid #ff4b4b; }
    .kasa-card { background-color: #161b22; padding: 12px; border-radius: 8px; border: 1px solid #30363d; margin-bottom: 8px; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h2 style='text-align: center; color: #ff4b4b;'>⚡ Gx Bot Mobil</h2>",
    unsafe_allow_html=True,
)
st.markdown("---")

ana_menu = st.sidebar.radio(
    "📌 Menü", ["📅 Maçlar & Ligler", "💰 Kasa Yönetimi"]
)

if ana_menu == "📅 Maçlar & Ligler":
  brans = st.selectbox("📌 Spor Branşı:", ["Futbol", "Basketbol"])
  lig = st.selectbox(
      "🏆 Lig / Kupa:",
      [
          "Tümü",
          "Trendyol Süper Lig",
          "Premier Lig",
          "Şampiyonlar Ligi",
          "EuroLeague",
          "NBA",
      ],
  )
  tarih = st.date_input("📅 Tarih:", datetime.date.today())

  st.markdown(f"### 🗓️ {tarih.strftime('%d %B %Y')} Programı")

  with st.container():
    st.markdown(
        """
        <div class="match-card">
            <span style='color: #ff4b4b; font-size: 12px; font-weight: bold;'>🏆 Trendyol Süper Lig</span>
            <h4>⚽ Fenerbahçe vs Göztepe</h4>
            <p><b>Saat:</b> 19:00</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    t1, t2, t3 = st.tabs(["📊 Oranlar", "🤖 Gx Tahmin", "📈 Form"])
    with t1:
      st.write("• MS 1: 1.45 | X: 4.20 | MS 2: 6.00")
      st.write("• 2.5 Üst: 1.65 | 2.5 Alt: 2.10")
    with t2:
      st.success("Yapay Zeka Öngörüsü: MS 1 (%72 İhtimal)")
      st.warning("Öne Çıkan Değer: MS 1 (Banko)")
    with t3:
      st.info("Form: Fenerbahçe (G-G-G-G-B) - Göztepe (G-M-B-G-M)")

elif ana_menu == "💰 Kasa Yönetimi":
  st.markdown("### 💰 Kasa Takip Paneli")

  if "bakiye" not in st.session_state:
    st.session_state.bakiye = 1000.0
  if "kuponlar" not in st.session_state:
    st.session_state.kuponlar = []

  st.metric(label="Mevcut Kasa", value=f"{st.session_state.bakiye:.2f} TL")

  with st.form("kasa_form"):
    mac_adi = st.text_input("Maç / Kupon Adı")
    yatirilan = st.number_input("Tutar (TL)", min_value=1.0, value=50.0)
    oran = st.number_input("Oran", min_value=1.01, value=1.80)
    durum = st.selectbox("Durum", ["Bekliyor", "Kazandı", "Kaybetti"])

    if st.form_submit_button("Kuponu Kaydet"):
      if durum == "Kazandı":
        st.session_state.bakiye += yatirilan * (oran - 1)
      elif durum == "Kaybetti":
        st.session_state.bakiye -= yatirilan

      st.session_state.kuponlar.append(
          {"mac": mac_adi, "tutar": yatirilan, "oran": oran, "durum": durum}
      )
      st.success("Kasa Güncellendi!")
      st.rerun()

  st.markdown("---")
  st.subheader("Geçmiş Kuponlar")
  for k in st.session_state.kuponlar:
    st.markdown(
        f"<div class='kasa-card'><b>{k['mac']}</b> - {k['tutar']} TL @ {k['oran']} | <b>{k['durum']}</b></div>",
        unsafe_allow_html=True,
    )
