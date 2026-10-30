import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(page_title="Gx Bot - İddaa & Analiz", page_icon="⚽🏀", layout="wide")

# Özel CSS ile Görünümü Güzelleştirme
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #FF4B4B;
        text-align: center;
        font-weight: 700;
    }
    .sub-header {
        text-align: center;
        color: #808495;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Başlık Kısmı
st.markdown('<p class="main-header">⚡ Gx Bot - Kişisel Bahis & Analiz Paneli</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Futbol ve Basketbol İstatistik & Tahmin Asistanı</p>', unsafe_allow_html=True)

# Yan Menü (Sidebar)
st.sidebar.title("Navigasyon")
secim = st.sidebar.radio("Gitmek İstediğin Yer:", ["Günün Bülteni & Maçlar", "Oran Analizi", "Kupon Oluşturucu"])

if secim == "Günün Bülteni & Maçlar":
    st.subheader("📅 Günün Öne Çıkan Maçları")
    brans = st.selectbox("Branş Seçin:", ["Futbol", "Basketbol"])
    
    if brans == "Futbol":
        st.info("⚽ Futbol Maçları Listeleniyor...")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("### Galatasaray - Fenerbahçe")
            st.caption("Süper Lig | Oranlar: 2.10 / 3.20 / 2.80")
        with col2:
            st.markdown("### Gx Tahmini")
            st.success("MS 1 (%55 İhtimal)")
        with col3:
            st.markdown("### Değerli Oran")
            st.warning("MS 1 (Value Var)")
    else:
        st.info("🏀 Basketbol Maçları Listeleniyor...")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("### Anadolu Efes - Real Madrid")
            st.caption("EuroLeague | Oranlar: 1.70 / 14.00 / 2.10")
        with col2:
            st.markdown("### Gx Tahmini")
            st.success("Üst (165.5) (%62 İhtimal)")
        with col3:
            st.markdown("### Değerli Oran")
            st.info("Maç Sonu 2")

elif secim == "Oran Analizi":
    st.subheader("📊 Oran & Değer Analiz Aracı")
    oran_giris = st.number_input("Maç Oranını Girin:", min_value=1.01, max_value=50.0, value=1.85)
    tahmini_olasilik = st.slider("Senin Tahmini Olasılığın (%):", 1, 100, 60)
    
    hesaplanan_oran = 100 / tahmini_olasilik
    if oran_giris > hesaplanan_oran:
        st.success(f"✅ **Değerli Oran (Value Bet)!** (İdeal Oran en az: {hesaplanan_oran:.2f})")
    else:
        st.error("❌ Bu oranda değer yok, risk/kazanç oranı düşük.")

elif secim == "Kupon Oluşturucu":
    st.subheader("📝 Kişisel Kupon Taslağı")
    st.info("Henüz kupona maç eklenmedi.")
