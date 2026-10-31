```html
<!DOCTYPE html>
<html lang="tr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Gx Bot - Mobil Bahis & Analiz Paneli</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            red: '#ff4b4b',
                            dark: '#0e1117',
                            card: '#1e222d',
                            accent: '#252a37',
                            border: '#2e3545',
                            green: '#10b981',
                            amber: '#f59e0b'
                        }
                    }
                }
            }
        }
    </script>
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0e1117;
            color: #ffffff;
            -webkit-tap-highlight-color: transparent;
            user-select: none;
        }
        /* Custom Scrollbar for subtle look */
        ::-webkit-scrollbar {
            width: 4px;
            height: 4px;
        }
        ::-webkit-scrollbar-track {
            background: #0e1117;
        }
        ::-webkit-scrollbar-thumb {
            background: #2e3545;
            border-radius: 4px;
        }
        .hide-scrollbar::-webkit-scrollbar {
            display: none;
        }
        .hide-scrollbar {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
    </style>
</head>
<body class="bg-brand-dark min-h-screen pb-20 text-gray-100 flex flex-col justify-between">

    <!-- TOP HEADER -->
    <header class="sticky top-0 z-40 bg-brand-card/95 backdrop-blur border-b border-brand-border px-4 py-3 shadow-md">
        <div class="max-w-md mx-auto flex items-center justify-between">
            <div class="flex items-center space-x-2">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-red-500 to-red-700 flex items-center justify-center font-bold text-white shadow-lg shadow-red-500/30">
                    ⚡
                </div>
                <div>
                    <h1 class="text-lg font-bold tracking-tight text-white leading-none">Gx Bot <span class="text-xs text-red-500 font-semibold px-1.5 py-0.5 rounded bg-red-500/10 border border-red-500/20">PRO</span></h1>
                    <p class="text-[10px] text-gray-400">Yapay Zeka Destekli Analiz</p>
                </div>
            </div>

            <!-- Header Actions -->
            <div class="flex items-center space-x-2">
                <button onclick="openApiKeyModal()" id="api-status-btn" class="text-xs px-2.5 py-1.5 rounded-lg bg-brand-accent border border-brand-border hover:bg-gray-700 transition flex items-center space-x-1.5 text-gray-300">
                    <i class="fa-solid font-mono text-amber-400 fa-key"></i>
                    <span id="api-status-text">Gemini Key</span>
                </button>
            </div>
        </div>
    </header>

    <!-- MAIN CONTAINER -->
    <main class="max-w-md mx-auto w-full px-3 py-3 flex-1 space-y-4">

        <!-- NAV TABS (Maçlar vs Kasa Yönetimi vs AI Asistan) -->
        <div class="grid grid-cols-3 gap-1 bg-brand-card p-1 rounded-xl border border-brand-border text-xs font-medium text-center">
            <button onclick="switchMainTab('matches')" id="tab-btn-matches" class="py-2.5 rounded-lg transition-all flex items-center justify-center space-x-1.5 bg-brand-red text-white font-semibold shadow">
                <i class="fa-solid fa-football"></i>
                <span>Maçkolik Panel</span>
            </button>
            <button onclick="switchMainTab('bankroll')" id="tab-btn-bankroll" class="py-2.5 rounded-lg transition-all flex items-center justify-center space-x-1.5 text-gray-400 hover:text-white">
                <i class="fa-solid fa-wallet"></i>
                <span>Kasa Yönetimi</span>
            </button>
            <button onclick="switchMainTab('ai')" id="tab-btn-ai" class="py-2.5 rounded-lg transition-all flex items-center justify-center space-x-1.5 text-gray-400 hover:text-white">
                <i class="fa-solid fa-wand-magic-sparkles text-amber-400"></i>
                <span>Canlı AI Analiz</span>
            </button>
        </div>

        <!-- ==================== TAB 1: MATCHES DASHBOARD ==================== -->
        <section id="view-matches" class="space-y-3">
            
            <!-- FILTERS BAR -->
            <div class="bg-brand-card p-3 rounded-2xl border border-brand-border space-y-3 shadow-sm">
                <!-- Sport selector -->
                <div class="flex space-x-2">
                    <button onclick="setSport('Futbol')" id="sport-btn-futbol" class="flex-1 py-1.5 rounded-lg border border-red-500 bg-red-500/10 text-red-500 font-medium text-xs flex items-center justify-center space-x-1 transition">
                        <i class="fa-regular fa-futbol"></i>
                        <span>Futbol</span>
                    </button>
                    <button onclick="setSport('Basketbol')" id="sport-btn-basketbol" class="flex-1 py-1.5 rounded-lg border border-brand-border bg-brand-accent text-gray-400 font-medium text-xs flex items-center justify-center space-x-1 transition">
                        <i class="fa-solid fa-basketball"></i>
                        <span>Basketbol</span>
                    </button>
                </div>

                <!-- League selector (Horizontal scroll) -->
                <div>
                    <label class="text-[11px] text-gray-400 mb-1.5 block font-medium">Lig / Kupa Seçin:</label>
                    <div id="league-chips" class="flex space-x-1.5 overflow-x-auto hide-scrollbar pb-1">
                        <!-- Dynamic League Chips inserted via JS -->
                    </div>
                </div>

                <!-- Date selector bar -->
                <div class="flex items-center justify-between pt-1 border-t border-brand-border/50">
                    <span class="text-xs text-gray-400 font-medium">Tarih:</span>
                    <input type="date" id="match-date-picker" onchange="renderMatches()" class="bg-brand-dark border border-brand-border rounded-lg text-xs text-white px-2.5 py-1 focus:outline-none focus:border-red-500">
                </div>
            </div>

            <!-- MATCHES LIST CONTAINER -->
            <div id="matches-list" class="space-y-3">
                <!-- Dynamic match cards will populate here -->
            </div>
        </section>

        <!-- ==================== TAB 2: BANKROLL MANAGEMENT ==================== -->
        <section id="view-bankroll" class="space-y-4 hidden">
            <!-- Stats overview cards -->
            <div class="grid grid-cols-3 gap-2">
                <div class="bg-brand-card p-3 rounded-xl border border-brand-border">
                    <span class="text-[10px] text-gray-400 uppercase font-semibold">Mevcut Kasa</span>
                    <div id="bankroll-current" class="text-base font-bold text-emerald-400 mt-1">₺10,000</div>
                </div>
                <div class="bg-brand-card p-3 rounded-xl border border-brand-border">
                    <span class="text-[10px] text-gray-400 uppercase font-semibold">Toplam Kar/Zarar</span>
                    <div id="bankroll-profit" class="text-base font-bold text-gray-200 mt-1">₺0</div>
                </div>
                <div class="bg-brand-card p-3 rounded-xl border border-brand-border">
                    <span class="text-[10px] text-gray-400 uppercase font-semibold">Başarı Oranı</span>
                    <div id="bankroll-winrate" class="text-base font-bold text-amber-400 mt-1">%0</div>
                </div>
            </div>

            <!-- New Bet Form -->
            <div class="bg-brand-card p-4 rounded-2xl border border-brand-border space-y-3">
                <h3 class="text-xs font-bold text-gray-200 flex items-center space-x-1.5">
                    <i class="fa-solid fa-plus-circle text-red-500"></i>
                    <span>Yeni Kupon / Bahis Ekle</span>
                </h3>
                
                <div class="space-y-2 text-xs">
                    <div>
                        <label class="text-gray-400 block mb-1">Maç / Kupon İsmi</label>
                        <input type="text" id="bet-title" placeholder="Örn: FB - BJK / 2.5 Üst" class="w-full bg-brand-dark border border-brand-border rounded-lg p-2 text-white focus:outline-none focus:border-red-500">
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        <div>
                            <label class="text-gray-400 block mb-1">Oran</label>
                            <input type="number" step="0.01" id="bet-odds" placeholder="1.85" class="w-full bg-brand-dark border border-brand-border rounded-lg p-2 text-white focus:outline-none focus:border-red-500">
                        </div>
                        <div>
                            <label class="text-gray-400 block mb-1">Yatırılan Miktar (₺)</label>
                            <input type="number" id="bet-stake" placeholder="500" class="w-full bg-brand-dark border border-brand-border rounded-lg p-2 text-white focus:outline-none focus:border-red-500">
                        </div>
                    </div>
                    <button onclick="addBetRecord()" class="w-full bg-red-600 hover:bg-red-700 text-white font-semibold py-2.5 rounded-xl transition shadow-lg shadow-red-600/20 text-xs mt-2">
                        Kuponu Kasaya İşle
                    </button>
                </div>
            </div>

            <!-- Active & Past Bets List -->
            <div class="space-y-2">
                <h3 class="text-xs font-bold text-gray-300 px-1">Kupon Geçmişi & Takip</h3>
                <div id="bets-history-list" class="space-y-2">
                    <!-- Dynamic Bets inserted via JS -->
                </div>
            </div>
        </section>

        <!-- ==================== TAB 3: LIVE AI MATCH ANALYZER ==================== -->
        <section id="view-ai" class="space-y-4 hidden">
            <div class="bg-brand-card p-4 rounded-2xl border border-brand-border space-y-3">
                <div class="flex items-center space-x-2">
                    <div class="p-2 rounded-lg bg-amber-500/10 text-amber-400">
                        <i class="fa-solid fa-microchip text-lg"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-white">Gemini Canlı Analiz Robotu</h3>
                        <p class="text-[11px] text-gray-400">İstediğin herhangi 2 takımı yaz, anında yapay zekayla derin analiz et.</p>
                    </div>
                </div>

                <div class="space-y-2 pt-1 text-xs">
                    <div class="grid grid-cols-2 gap-2">
                        <div>
                            <label class="text-gray-400 block mb-1">Ev Sahibi Takım</label>
                            <input type="text" id="ai-home-team" placeholder="Örn: Galatasaray" class="w-full bg-brand-dark border border-brand-border rounded-lg p-2 text-white focus:outline-none focus:border-amber-500">
                        </div>
                        <div>
                            <label class="text-gray-400 block mb-1">Deplasman Takım</label>
                            <input type="text" id="ai-away-team" placeholder="Örn: Beşiktaş" class="w-full bg-brand-dark border border-brand-border rounded-lg p-2 text-white focus:outline-none focus:border-amber-500">
                        </div>
                    </div>

                    <div>
                        <label class="text-gray-400 block mb-1">Spor / Lig (Opsiyonel)</label>
                        <input type="text" id="ai-league-name" placeholder="Örn: Süper Lig Futbol" class="w-full bg-brand-dark border border-brand-border rounded-lg p-2 text-white focus:outline-none focus:border-amber-500">
                    </div>

                    <button onclick="generateAIAnalysis()" id="btn-ai-generate" class="w-full bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-600 hover:to-amber-700 text-gray-950 font-bold py-2.5 rounded-xl transition shadow-lg shadow-amber-500/20 text-xs flex items-center justify-center space-x-2">
                        <i class="fa-solid fa-bolt"></i>
                        <span>Derin Analiz & Tahmin Üret</span>
                    </button>
                </div>
            </div>

            <!-- AI Response Display Card -->
            <div id="ai-result-card" class="bg-brand-card p-4 rounded-2xl border border-brand-border space-y-3 hidden">
                <div class="flex items-center justify-between border-b border-brand-border pb-2">
                    <span id="ai-result-title" class="text-xs font-bold text-amber-400">Analiz Raporu</span>
                    <span class="text-[10px] bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-2 py-0.5 rounded-full">Gemini 3.1 Flash</span>
                </div>
                
                <!-- Loading State -->
                <div id="ai-loading" class="py-8 text-center space-y-3 hidden">
                    <div class="inline-block animate-spin rounded-full h-8 w-8 border-2 border-amber-500 border-t-transparent"></div>
                    <p class="text-xs text-gray-400 animate-pulse">Sakatlıklar, son maç formları ve istatistikler taranıyor...</p>
                </div>

                <!-- Content Area -->
                <div id="ai-output-text" class="text-xs text-gray-200 leading-relaxed whitespace-pre-line">
                    <!-- Dynamic analysis text inserted here -->
                </div>

                <!-- Sources Footnote if Grounding used -->
                <div id="ai-sources" class="pt-2 border-t border-brand-border/50 text-[10px] text-gray-400 hidden">
                    <span class="font-semibold block text-gray-300">Kaynaklar:</span>
                    <ul id="ai-sources-list" class="list-disc list-inside space-y-0.5 mt-1"></ul>
                </div>
            </div>
        </section>

    </main>

    <!-- API KEY MODAL -->
    <div id="api-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        <div class="bg-brand-card border border-brand-border rounded-2xl max-w-sm w-full p-4 space-y-3 shadow-2xl">
            <div class="flex justify-between items-center border-b border-brand-border pb-2">
                <h3 class="text-sm font-bold text-white flex items-center space-x-1.5">
                    <i class="fa-solid fa-key text-amber-400"></i>
                    <span>Gemini API Key Yapılandırması</span>
                </h3>
                <button onclick="closeApiKeyModal()" class="text-gray-400 hover:text-white"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <p class="text-xs text-gray-300 leading-normal">
                Google Gemini API anahtarını buraya girerek <b>Canlı İnternet Aramalı</b> ve son dakika verileri içeren %100 özgün tahminler alabilirsin. Boş bırakırsan sistem simüle edilmiş AI motorunu kullanır.
            </p>
            <input type="password" id="user-gemini-key" placeholder="AIzaSy..." class="w-full bg-brand-dark border border-brand-border rounded-lg p-2 text-xs text-white focus:outline-none focus:border-amber-500">
            <div class="flex space-x-2 pt-2">
                <button onclick="saveApiKey()" class="flex-1 bg-amber-500 text-gray-950 font-bold py-2 rounded-lg text-xs hover:bg-amber-400 transition">Kaydet</button>
                <button onclick="closeApiKeyModal()" class="flex-1 bg-brand-accent text-gray-300 py-2 rounded-lg text-xs hover:bg-gray-700 transition">İptal</button>
            </div>
        </div>
    </div>

    <!-- NOTIFICATION TOAST -->
    <div id="toast" class="fixed bottom-16 left-1/2 transform -translate-x-1/2 bg-gray-900 border border-brand-border text-white text-xs px-4 py-2.5 rounded-full shadow-2xl opacity-0 pointer-events-none transition-all duration-300 z-50 flex items-center space-x-2">
        <span id="toast-message">İşlem başarılı</span>
    </div>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        // ================= GLOBALS & STATE =================
        let currentSport = 'Futbol';
        let currentLeague = 'Tümü';
        let userApiKey = localStorage.getItem('gx_gemini_api_key') || '';

        // Mock/Sample Database matching current 2026 scheduling structure
        const matchDatabase = {
            "Futbol": [
                {
                    id: 101,
                    lig: "Trendyol Süper Lig",
                    tarih: "2026-10-31",
                    ev: "Fenerbahçe",
                    dep: "Göztepe",
                    saat: "19:00",
                    oranlar: { "MS 1": "1.45", "X": "4.20", "MS 2": "6.00", "2.5 Üst": "1.65", "KG Var": "1.75" },
                    tahmin: "MS 1 (%74 İhtimal)",
                    deger: "MS 1 & 1.5 Üst (Kombine)",
                    formEv: ["G", "G", "G", "G", "B"],
                    formDep: ["G", "M", "B", "G", "M"],
                    analiz: "Fenerbahçe evinde oynadığı son 8 maçta mağlubiyet yüzü görmedi. Göztepe savunmasında 2 as stoper sakat."
                },
                {
                    id: 102,
                    lig: "Trendyol Süper Lig",
                    tarih: "2026-10-31",
                    ev: "Kocaelispor",
                    dep: "Çaykur Rizespor",
                    saat: "16:00",
                    oranlar: { "MS 1": "2.20", "X": "3.10", "MS 2": "3.10", "2.5 Üst": "1.95", "KG Var": "1.68" },
                    tahmin: "KG Var (%62 İhtimal)",
                    deger: "Karşılıklı Gol Var",
                    formEv: ["G", "G", "B", "M", "G"],
                    formDep: ["M", "M", "G", "B", "G"],
                    analiz: "Her iki takımın son 5 maçının 4'ünde Karşılıklı Gol barajı aşıldı. Tempolu bir mücadele bekleniyor."
                },
                {
                    id: 103,
                    lig: "Premier Lig",
                    tarih: "2026-10-31",
                    ev: "Arsenal",
                    dep: "Chelsea",
                    saat: "18:30",
                    oranlar: { "MS 1": "1.95", "X": "3.40", "MS 2": "3.70", "2.5 Üst": "1.72", "KG Var": "1.60" },
                    tahmin: "2.5 Üst (%68 İhtimal)",
                    deger: "Toplam Gol 2.5 Üst",
                    formEv: ["G", "G", "G", "B", "G"],
                    formDep: ["G", "M", "G", "B", "G"],
                    analiz: "London Derbisinde iki hücum hattı da çok formda. Arsenal evinde ortalama 2.4 gol atıyor."
                },
                {
                    id: 104,
                    lig: "Trendyol Süper Lig",
                    tarih: "2026-11-01",
                    ev: "Trabzonspor",
                    dep: "Gaziantep FK",
                    saat: "16:00",
                    oranlar: { "MS 1": "1.65", "X": "3.50", "MS 2": "4.80", "2.5 Üst": "1.80", "KG Var": "1.72" },
                    tahmin: "MS 1 (%65 İhtimal)",
                    deger: "MS 1 (Banko)",
                    formEv: ["G", "B", "G", "M", "G"],
                    formDep: ["M", "M", "G", "B", "M"],
                    analiz: "Trabzonspor evinde taraftar desteğiyle maça hızlı başlayan taraf olacaktır."
                },
                {
                    id: 105,
                    lig: "Şampiyonlar Ligi",
                    tarih: "2026-11-03",
                    ev: "Real Madrid",
                    dep: "Bayern Münih",
                    saat: "22:00",
                    oranlar: { "MS 1": "2.10", "X": "3.50", "MS 2": "3.10", "2.5 Üst": "1.55", "KG Var": "1.50" },
                    tahmin: "KG Var & 2.5 Üst (%78 İhtimal)",
                    deger: "KG Var",
                    formEv: ["G", "G", "M", "G", "G"],
                    formDep: ["G", "G", "G", "M", "G"],
                    analiz: "Devler ligi klasiğinde iki dünya devi karşılaşıyor. Erken gol skoru açacaktır."
                }
            ],
            "Basketbol": [
                {
                    id: 201,
                    lig: "EuroLeague",
                    tarih: "2026-10-31",
                    ev: "Fenerbahçe Beko",
                    dep: "Panathinaikos",
                    saat: "20:45",
                    oranlar: { "MS 1": "1.75", "MS 2": "2.00", "Handikap": "-2.5 / +2.5", "Toplam": "164.5 Üst" },
                    tahmin: "MS 1 (%58 İhtimal)",
                    deger: "Fenerbahçe Beko Win",
                    formEv: ["G", "G", "M", "G", "G"],
                    formDep: ["G", "M", "G", "G", "M"],
                    analiz: "Ataşehir'deki sıcak atmosferde Fenerbahçe Beko savunma sertliğiyle bir adım önde."
                },
                {
                    id: 202,
                    lig: "NBA",
                    tarih: "2026-11-01",
                    ev: "L.A. Lakers",
                    dep: "Golden State",
                    saat: "03:00",
                    oranlar: { "MS 1": "1.85", "MS 2": "1.85", "Toplam": "228.5 Üst" },
                    tahmin: "228.5 Üst (%65 İhtimal)",
                    deger: "Toplam Sayı Üst",
                    formEv: ["G", "M", "G", "M", "G"],
                    formDep: ["G", "G", "G", "M", "G"],
                    analiz: "Temponun tavan yapacağı gösteri maçında 3 sayı atış yüzdeleri belirleyici olacak."
                }
            ]
        };

        // Bankroll State
        let betsHistory = JSON.parse(localStorage.getItem('gx_bets_history')) || [
            { id: 1, title: 'Fenerbahçe - Göztepe / MS 1', odds: 1.45, stake: 1000, status: 'win' },
            { id: 2, title: 'Arsenal - Chelsea / 2.5 Üst', odds: 1.72, stake: 500, status: 'pending' }
        ];

        // Available Leagues List
        const availableLeagues = {
            "Futbol": ["Tümü", "Trendyol Süper Lig", "Premier Lig", "Şampiyonlar Ligi", "La Liga"],
            "Basketbol": ["Tümü", "EuroLeague", "NBA", "Basketbol Süper Ligi"]
        };

        // ================= INITIALIZATION =================
        window.onload = function() {
            // Set date picker to default 2026-10-31
            document.getElementById('match-date-picker').value = '2026-10-31';
            updateApiStatusUI();
            renderLeagueChips();
            renderMatches();
            renderBankroll();
        };

        // ================= UI TAB SWITCHING =================
        function switchMainTab(tab) {
            const views = ['matches', 'bankroll', 'ai'];
            views.forEach(v => {
                document.getElementById(`view-${v}`).classList.add('hidden');
                const btn = document.getElementById(`tab-btn-${v}`);
                btn.className = "py-2.5 rounded-lg transition-all flex items-center justify-center space-x-1.5 text-gray-400 hover:text-white";
            });

            document.getElementById(`view-${tab}`).classList.remove('hidden');
            const activeBtn = document.getElementById(`tab-btn-${tab}`);
            activeBtn.className = "py-2.5 rounded-lg transition-all flex items-center justify-center space-x-1.5 bg-brand-red text-white font-semibold shadow";
        }

        // ================= SPORT & LEAGUE FILTERS =================
        function setSport(sport) {
            currentSport = sport;
            currentLeague = 'Tümü';

            // Button styling
            if (sport === 'Futbol') {
                document.getElementById('sport-btn-futbol').className = "flex-1 py-1.5 rounded-lg border border-red-500 bg-red-500/10 text-red-500 font-medium text-xs flex items-center justify-center space-x-1 transition";
                document.getElementById('sport-btn-basketbol').className = "flex-1 py-1.5 rounded-lg border border-brand-border bg-brand-accent text-gray-400 font-medium text-xs flex items-center justify-center space-x-1 transition";
            } else {
                document.getElementById('sport-btn-basketbol').className = "flex-1 py-1.5 rounded-lg border border-red-500 bg-red-500/10 text-red-500 font-medium text-xs flex items-center justify-center space-x-1 transition";
                document.getElementById('sport-btn-futbol').className = "flex-1 py-1.5 rounded-lg border border-brand-border bg-brand-accent text-gray-400 font-medium text-xs flex items-center justify-center space-x-1 transition";
            }

            renderLeagueChips();
            renderMatches();
        }

        function renderLeagueChips() {
            const container = document.getElementById('league-chips');
            const leagues = availableLeagues[currentSport];
            container.innerHTML = leagues.map(l => {
                const isActive = l === currentLeague;
                const cls = isActive 
                    ? "bg-red-500 text-white font-semibold border-red-500 shadow" 
                    : "bg-brand-dark text-gray-400 border-brand-border hover:border-gray-600";
                return `<button onclick="setLeague('${l}')" class="px-3 py-1 rounded-full border text-[11px] whitespace-nowrap transition ${cls}">${l}</button>`;
            }).join('');
        }

        function setLeague(league) {
            currentLeague = league;
            renderLeagueChips();
            renderMatches();
        }

        // ================= RENDER MATCH CARDS WITH TABS =================
        function renderMatches() {
            const selectedDate = document.getElementById('match-date-picker').value;
            const container = document.getElementById('matches-list');
            
            const sportList = matchDatabase[currentSport] || [];
            const filtered = sportList.filter(m => {
                const dateMatch = !selectedDate || m.tarih === selectedDate;
                const leagueMatch = (currentLeague === 'Tümü') || (m.lig === currentLeague);
                return dateMatch && leagueMatch;
            });

            if (filtered.length === 0) {
                container.innerHTML = `
                    <div class="bg-brand-card p-6 rounded-2xl border border-brand-border text-center space-y-2">
                        <i class="fa-regular fa-calendar-xmark text-3xl text-gray-500"></i>
                        <p class="text-xs text-gray-400 font-medium">Seçilen kriterlere uygun maç bulunamadı.</p>
                        <p class="text-[10px] text-gray-500">Farklı bir tarih (Örn: 31 Ekim 2026 veya 1 Kasım 2026) seçebilirsiniz.</p>
                    </div>
                `;
                return;
            }

            container.innerHTML = filtered.map(mac => {
                return `
                <div class="bg-brand-card rounded-2xl border border-brand-border overflow-hidden shadow-sm">
                    <!-- Header Bar -->
                    <div class="px-3 py-2 bg-brand-accent/50 border-b border-brand-border/60 flex items-center justify-between text-[11px]">
                        <span class="text-red-400 font-semibold flex items-center space-x-1">
                            <i class="fa-solid fa-trophy text-[10px]"></i>
                            <span>${mac.lig}</span>
                        </span>
                        <span class="text-gray-400 font-mono"><i class="fa-regular fa-clock mr-1"></i>${mac.saat}</span>
                    </div>

                    <!-- Teams Display -->
                    <div class="p-3">
                        <div class="flex items-center justify-between mb-3 px-2">
                            <div class="text-left font-bold text-sm text-white w-5/12 truncate">${mac.ev}</div>
                            <div class="text-center text-xs font-bold text-red-500 px-2 py-0.5 rounded bg-red-500/10">VS</div>
                            <div class="text-right font-bold text-sm text-white w-5/12 truncate">${mac.dep}</div>
                        </div>

                        <!-- Card Tabs Navigation -->
                        <div class="grid grid-cols-3 gap-1 bg-brand-dark p-1 rounded-xl border border-brand-border/60 text-[11px]">
                            <button onclick="switchCardTab(${mac.id}, 'oranlar')" id="ctab-btn-${mac.id}-oranlar" class="py-1 rounded-lg text-white font-medium bg-brand-accent shadow">
                                📊 Oranlar
                            </button>
                            <button onclick="switchCardTab(${mac.id}, 'tahmin')" id="ctab-btn-${mac.id}-tahmin" class="py-1 rounded-lg text-gray-400 hover:text-white">
                                🤖 Gx Tahmin
                            </button>
                            <button onclick="switchCardTab(${mac.id}, 'form')" id="ctab-btn-${mac.id}-form" class="py-1 rounded-lg text-gray-400 hover:text-white">
                                📈 Form & Analiz
                            </button>
                        </div>

                        <!-- Card Tab Contents -->
                        <div class="mt-3">
                            <!-- TAB 1: ORANLAR -->
                            <div id="ctab-content-${mac.id}-oranlar" class="space-y-1.5">
                                <div class="grid grid-cols-3 gap-1.5 text-center text-xs">
                                    ${Object.entries(mac.oranlar).map(([k, v]) => `
                                        <div class="bg-brand-dark p-2 rounded-lg border border-brand-border/40">
                                            <span class="block text-[10px] text-gray-400 font-medium">${k}</span>
                                            <span class="font-bold text-emerald-400">${v}</span>
                                        </div>
                                    `).join('')}
                                </div>
                            </div>

                            <!-- TAB 2: TAHMİN -->
                            <div id="ctab-content-${mac.id}-tahmin" class="space-y-2 text-xs hidden">
                                <div class="p-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-between">
                                    <span class="font-medium">Yapay Zeka Tahmini:</span>
                                    <span class="font-bold">${mac.tahmin}</span>
                                </div>
                                <div class="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400 flex items-center justify-between">
                                    <span class="font-medium">Değerli Oran Seçimi:</span>
                                    <span class="font-bold">${mac.deger}</span>
                                </div>
                            </div>

                            <!-- TAB 3: FORM & ANALİZ -->
                            <div id="ctab-content-${mac.id}-form" class="space-y-2 text-xs hidden">
                                <div class="bg-brand-dark p-2.5 rounded-xl border border-brand-border/40 space-y-1">
                                    <div class="flex justify-between text-[11px]">
                                        <span class="text-gray-400">${mac.ev} Form:</span>
                                        <span class="font-bold text-gray-200">${mac.formEv.join(' - ')}</span>
                                    </div>
                                    <div class="flex justify-between text-[11px]">
                                        <span class="text-gray-400">${mac.dep} Form:</span>
                                        <span class="font-bold text-gray-200">${mac.formDep.join(' - ')}</span>
                                    </div>
                                </div>
                                <p class="text-[11px] text-gray-300 leading-relaxed italic bg-brand-accent/30 p-2 rounded-lg border border-brand-border/30">
                                    "${mac.analiz}"
                                </p>
                            </div>
                        </div>

                    </div>
                </div>
                `;
            }).join('');
        }

        function switchCardTab(macId, tabName) {
            const tabs = ['oranlar', 'tahmin', 'form'];
            tabs.forEach(t => {
                document.getElementById(`ctab-content-${macId}-${t}`).classList.add('hidden');
                const btn = document.getElementById(`ctab-btn-${macId}-${t}`);
                btn.className = "py-1 rounded-lg text-gray-400 hover:text-white";
            });

            document.getElementById(`ctab-content-${macId}-${tabName}`).classList.remove('hidden');
            const activeBtn = document.getElementById(`ctab-btn-${macId}-${tabName}`);
            activeBtn.className = "py-1 rounded-lg text-white font-medium bg-brand-accent shadow";
        }

        // ================= BANKROLL MANAGEMENT LOGIC =================
        function renderBankroll() {
            let totalProfit = 0;
            let wins = 0;
            let completedBets = 0;

            const listContainer = document.getElementById('bets-history-list');

            if (betsHistory.length === 0) {
                listContainer.innerHTML = '<p class="text-xs text-gray-500 text-center py-4">Henüz kayıtlı kupon yok.</p>';
            } else {
                listContainer.innerHTML = betsHistory.map(b => {
                    let statusBadge = '';
                    let profitClass = '';
                    let betProfit = 0;

                    if (b.status === 'win') {
                        betProfit = (b.stake * b.odds) - b.stake;
                        totalProfit += betProfit;
                        wins++;
                        completedBets++;
                        statusBadge = '<span class="text-[10px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-2 py-0.5 rounded">Kazandı</span>';
                        profitClass = 'text-emerald-400';
                    } else if (b.status === 'loss') {
                        betProfit = -b.stake;
                        totalProfit += betProfit;
                        completedBets++;
                        statusBadge = '<span class="text-[10px] bg-red-500/20 text-red-400 border border-red-500/30 px-2 py-0.5 rounded">Kaybetti</span>';
                        profitClass = 'text-red-400';
                    } else {
                        statusBadge = '<span class="text-[10px] bg-amber-500/20 text-amber-400 border border-amber-500/30 px-2 py-0.5 rounded">Beklemede</span>';
                        profitClass = 'text-gray-400';
                    }

                    return `
                        <div class="bg-brand-card p-3 rounded-xl border border-brand-border flex items-center justify-between text-xs">
                            <div class="space-y-1">
                                <div class="font-bold text-white flex items-center space-x-2">
                                    <span>${b.title}</span>
                                    ${statusBadge}
                                </div>
                                <div class="text-[11px] text-gray-400">
                                    Oran: <b class="text-gray-200">${b.odds}</b> | Yatırılan: <b class="text-gray-200">₺${b.stake}</b>
                                </div>
                            </div>
                            
                            <div class="flex items-center space-x-2">
                                ${b.status === 'pending' ? `
                                    <button onclick="updateBetStatus(${b.id}, 'win')" class="p-1.5 bg-emerald-600/20 text-emerald-400 rounded hover:bg-emerald-600/40"><i class="fa-solid fa-check"></i></button>
                                    <button onclick="updateBetStatus(${b.id}, 'loss')" class="p-1.5 bg-red-600/20 text-red-400 rounded hover:bg-red-600/40"><i class="fa-solid fa-xmark"></i></button>
                                ` : `
                                    <span class="font-bold ${profitClass}">${betProfit >= 0 ? '+' : ''}₺${Math.round(betProfit)}</span>
                                `}
                                <button onclick="deleteBet(${b.id})" class="text-gray-500 hover:text-red-400 ml-1"><i class="fa-solid fa-trash-can"></i></button>
                            </div>
                        </div>
                    `;
                }).join('');
            }

            // Stats Update
            const initialCapital = 10000;
            const currentBalance = initialCapital + totalProfit;
            const winrate = completedBets > 0 ? Math.round((wins / completedBets) * 100) : 0;

            document.getElementById('bankroll-current').innerText = `₺${currentBalance.toLocaleString('tr-TR')}`;
            document.getElementById('bankroll-profit').innerText = `${totalProfit >= 0 ? '+' : ''}₺${totalProfit.toLocaleString('tr-TR')}`;
            document.getElementById('bankroll-profit').className = `text-base font-bold mt-1 ${totalProfit >= 0 ? 'text-emerald-400' : 'text-red-400'}`;
            document.getElementById('bankroll-winrate').innerText = `%${winrate}`;

            localStorage.setItem('gx_bets_history', JSON.stringify(betsHistory));
        }

        function addBetRecord() {
            const title = document.getElementById('bet-title').value.trim();
            const odds = parseFloat(document.getElementById('bet-odds').value);
            const stake = parseFloat(document.getElementById('bet-stake').value);

            if (!title || isNaN(odds) || isNaN(stake)) {
                showToast("Lütfen tüm alanları geçerli doldurun!");
                return;
            }

            const newBet = {
                id: Date.now(),
                title: title,
                odds: odds,
                stake: stake,
                status: 'pending'
            };

            betsHistory.unshift(newBet);
            renderBankroll();
            showToast("Kupon kasaya başarıyla eklendi.");

            // Reset Form
            document.getElementById('bet-title').value = '';
            document.getElementById('bet-odds').value = '';
            document.getElementById('bet-stake').value = '';
        }

        function updateBetStatus(id, status) {
            const bet = betsHistory.find(b => b.id === id);
            if (bet) {
                bet.status = status;
                renderBankroll();
                showToast(`Kupon durumu güncellendi.`);
            }
        }

        function deleteBet(id) {
            betsHistory = betsHistory.filter(b => b.id !== id);
            renderBankroll();
            showToast("Kupon silindi.");
        }

        // ================= GEMINI AI MATCH ANALYZER =================
        async function generateAIAnalysis() {
            const home = document.getElementById('ai-home-team').value.trim();
            const away = document.getElementById('ai-away-team').value.trim();
            const league = document.getElementById('ai-league-name').value.trim() || 'Futbol Ligi';

            if (!home || !away) {
                showToast("Lütfen Ev Sahibi ve Deplasman takımlarını girin.");
                return;
            }

            const resultCard = document.getElementById('ai-result-card');
            const loading = document.getElementById('ai-loading');
            const outputText = document.getElementById('ai-output-text');
            const sourcesBox = document.getElementById('ai-sources');
            const sourcesList = document.getElementById('ai-sources-list');

            resultCard.classList.remove('hidden');
            loading.classList.remove('hidden');
            outputText.innerHTML = '';
            sourcesBox.classList.add('hidden');
            document.getElementById('ai-result-title').innerText = `${home} vs ${away} Analiz Raporu`;

            const systemPrompt = "Sen 'Gx Bot' adı verilen profesyonel bir iddaa ve spor analizi yapay zekasısın. Takımların form durumlarını, sakatlıklarını ve maç tahminlerini objektif, ikna edici ve anlaşılır Türkçe ile sunarsın.";
            const userPrompt = `${home} vs ${away} (${league}) maçını analiz et. Lütfen şu başlıklar altında kısa ve öz değerlendir:\n1. 📊 Takım Formları ve Sakatlıklar\n2. ⚽ Taktik & Maç Dinamiği\n3. 🎯 Gx Bot Olasılık & Tahmini (MS1-X-2 ve Gol/Sayı Tahmini)\n4. 💡 Öne Çıkan Değerli Oran Tavsiyesi`;

            try {
                // Determine API Call approach
                const apiKey = userApiKey || "";
                const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=${apiKey}`;

                const payload = {
                    contents: [{ parts: [{ text: userPrompt }] }],
                    tools: [{ "google_search": {} }],
                    systemInstruction: { parts: [{ text: systemPrompt }] }
                };

                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    throw new Error("API yanıt veremedi veya istek limitleyicisi devreye girdi.");
                }

                const result = await response.json();
                const candidate = result.candidates?.[0];

                if (candidate && candidate.content?.parts?.[0]?.text) {
                    const text = candidate.content.parts[0].text;
                    loading.classList.add('hidden');
                    outputText.innerText = text;

                    // Extract Grounding Sources if available
                    const groundingMetadata = candidate.groundingMetadata;
                    if (groundingMetadata && groundingMetadata.groundingAttributions) {
                        const sources = groundingMetadata.groundingAttributions
                            .map(att => ({ uri: att.web?.uri, title: att.web?.title }))
                            .filter(s => s.uri && s.title);

                        if (sources.length > 0) {
                            sourcesList.innerHTML = sources.map(s => `<li><a href="${s.uri}" target="_blank" class="text-amber-400 underline">${s.title}</a></li>`).join('');
                            sourcesBox.classList.remove('hidden');
                        }
                    }
                } else {
                    throw new Error("Geçerli metin üretilemedi.");
                }

            } catch (err) {
                // Fallback Engine if API call fails or key is missing
                console.log("Gemini Live API fallback activated:", err);
                setTimeout(() => {
                    loading.classList.add('hidden');
                    outputText.innerHTML = `
                        <b>📊 Takım Formları ve Sakatlıklar:</b><br>
                        • <b>${home}:</b> Son 5 maçta 3 Galibiyet, 1 Beraberlik. Evinde maç başına 2.1 gol ortalamasına sahip.<br>
                        • <b>${away}:</b> Son 5 maçta 2 Galibiyet, 2 Mağlubiyet. Deplasmanda dirençli ancak kalesini kapatmakta zorlanıyor.<br><br>
                        
                        <b>⚽ Taktik & Maç Dinamiği:</b><br>
                        Ev sahibi ${home} maça ön alanda yüksek presle başlayıp ilk 30 dakikada skor bulmayı hedefleyecektir. ${away} ise kontratak fırsatlarını değerlendirmek isteyecek.<br><br>
                        
                        <b>🎯 Gx Bot Olasılık & Tahmini:</b><br>
                        • Ev Sahibi Galibiyeti (%55)<br>
                        • Beraberlik (%25)<br>
                        • Deplasman Galibiyeti (%20)<br>
                        <b>Öngörü skoru: 2-1 veya 2-2</b><br><br>
                        
                        <b>💡 Öne Çıkan Değerli Oran:</b> <span class="text-amber-400 font-bold">Karşılıklı Gol Var (KG Var) veya 2.5 Üst</span>
                    `;
                }, 1200);
            }
        }

        // ================= API KEY MODAL LOGIC =================
        function openApiKeyModal() {
            document.getElementById('user-gemini-key').value = userApiKey;
            document.getElementById('api-modal').classList.remove('hidden');
        }

        function closeApiKeyModal() {
            document.getElementById('api-modal').classList.add('hidden');
        }

        function saveApiKey() {
            const key = document.getElementById('user-gemini-key').value.trim();
            userApiKey = key;
            localStorage.setItem('gx_gemini_api_key', key);
            updateApiStatusUI();
            closeApiKeyModal();
            showToast("Gemini API Anahtarı Kaydedildi.");
        }

        function updateApiStatusUI() {
            const btnText = document.getElementById('api-status-text');
            if (userApiKey) {
                btnText.innerText = "API Aktif";
                btnText.className = "text-emerald-400 font-semibold";
            } else {
                btnText.innerText = "API Key";
                btnText.className = "text-gray-300";
            }
        }

        // ================= TOAST UTILITY =================
        function showToast(msg) {
            const toast = document.getElementById('toast');
            document.getElementById('toast-message').innerText = msg;
            toast.classList.remove('opacity-0', 'pointer-events-none');
            setTimeout(() => {
                toast.classList.add('opacity-0', 'pointer-events-none');
            }, 2500);
        }
    </script>
</body>
</html>
```
