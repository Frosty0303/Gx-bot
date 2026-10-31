import datetime
import streamlit as st

st.set_page_config(
    page_title="Gx Bot - Mobil Bahis Paneli", page_icon="⚡", layout="centered"
)

st.markdown(
    """
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .match-card { background-color: #1e222d; padding: 15px; border-radius: 10px; margin-bottom: 15px; border-left: 4px solid #ff4b4b; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<h2 style='text-align: center; color: #ff4b4b;'>⚡ Gx Bot - Mobil Bahis"
    " Paneli</h2>",
    unsafe_allow_html=True,
)
st.markdown("---")

ana_menu = st.sidebar.radio(
    "📌 Menü", ["📅 Maçlar & Ligler", "💰 Kasa Yönetimi"]
)

if ana_menu == "📅 Maçlar & Ligler":
  brans = st.selectbox("📌 Spor Branşı:", ["Futbol", "Basketbol"])
  lig = st.selectbox(
      "🏆 Lig:",
      [
          "Tümü",
          "Trendyol Süper Lig",
          "Premier Lig",
          "Şampiyonlar Ligi",
          "EuroLeague",
      ],
  )
  tarih = st.date_input("📅 Tarih:", datetime.date.today())

  st.markdown(f"### 🗓️ {tarih.strftime('%d %B %Y')} - {lig} Programı")

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

    tab1, tab2, tab3 = st.tabs(
        ["📊 Oranlar", "🤖 Gx Tahmin", "📈 Form & Analiz"]
    )
    with tab1:
      st.text("• MS 1: 1.45\n• X: 4.20\n• MS 2: 6.00")
    with tab2:
      st.success("**Yapay Zeka Öngörüsü:** MS 1 (%72 İhtimal)")
    with tab3:
      st.info("**Son Maçlar:** Fenerbahçe (G G G G B) - Göztepe (G M B G M)")

elif ana_menu == "💰 Kasa Yönetimi":
  st.markdown("### 💰 Kasa Paneli")
  if "bakiye" not in st.session_state:
    st.session_state.bakiye = 1000.0
  st.metric(label="Mevcut Kasa", value=f"{st.session_state.bakiye:.2f} TL")
  st.info("Kasa yönetimi aktif ve çalışıyor.")
