react
import React, { useState, useEffect, useMemo } from 'react';
import { 
  Trophy, 
  Calendar, 
  TrendingUp, 
  Sparkles, 
  DollarSign, 
  Activity, 
  Search, 
  ShieldAlert, 
  ChevronRight, 
  BarChart3, 
  Key, 
  Zap, 
  PlusCircle, 
  Trash2, 
  CheckCircle2, 
  XCircle, 
  Clock, 
  Cpu, 
  Filter,
  RefreshCw,
  ExternalLink,
  Flame,
  Award,
  Layers
} from 'lucide-react';

// --- INITIAL MOCK FIXTURES DATA ---
const INITIAL_FIXTURES = [
  {
    id: 'm1',
    sport: 'Futbol',
    league: 'Trendyol Süper Lig',
    leagueIcon: '🇹🇷',
    date: '2026-10-31',
    time: '19:00',
    home: 'Fenerbahçe',
    away: 'Göztepe',
    odds: { ms1: 1.45, draw: 4.20, ms2: 6.00, o25: 1.65, u25: 2.10, kgYes: 1.80 },
    status: 'FT',
    score: '2 - 1',
    form: { home: ['G', 'G', 'G', 'G', 'B'], away: ['G', 'M', 'B', 'G', 'M'] },
    aiAnalysis: {
      prediction: 'MS 1 & 2.5 Üst',
      confidence: 78,
      valueBet: 'MS 1 (Banko)',
      riskLevel: 'Düşük',
      summary: 'Fenerbahçe iç saha baskısıyla erken gol arayacaktır. Göztepe kontra atakta etkili olsa da Kadıköy atmosferinde zorlanabilir.',
      keyFactors: [
        'Fenerbahçe evinde son 6 maçta ortalama 2.4 gol attı.',
        'Göztepe deplasmanda son 3 maçta kalesini gole kapatamadı.',
        'Ev sahibinde kanat organizasyonları üst seviyede.'
      ]
    }
  },
  {
    id: 'm2',
    sport: 'Futbol',
    league: 'Trendyol Süper Lig',
    leagueIcon: '🇹🇷',
    date: '2026-10-31',
    time: '16:00',
    home: 'Kocaelispor',
    away: 'Çaykur Rizespor',
    odds: { ms1: 2.20, draw: 3.10, ms2: 3.10, o25: 1.95, u25: 1.75, kgYes: 1.70 },
    status: 'FT',
    score: '1 - 1',
    form: { home: ['G', 'G', 'B', 'M', 'G'], away: ['M', 'M', 'G', 'B', 'G'] },
    aiAnalysis: {
      prediction: 'KG Var (Karşılıklı Gol)',
      confidence: 65,
      valueBet: 'KG Var @ 1.70',
      riskLevel: 'Orta',
      summary: 'İki takım da savunma arkası zaaflarına sahip. Dengeli ve yüksek tempolu geçmesi beklenen bir mücadele.',
      keyFactors: [
        'Kocaelispor son 4 maçın tamamında gol buldu.',
        'Rizespor deplasmanda ortalama 1.2 gol yiyor.'
      ]
    }
  },
  {
    id: 'm3',
    sport: 'Futbol',
    league: 'Premier Lig',
    leagueIcon: '🏴󠁧󠁢󠁥󠁮󠁧󠁿',
    date: '2026-10-31',
    time: '18:30',
    home: 'Arsenal',
    away: 'Chelsea',
    odds: { ms1: 1.95, draw: 3.40, ms2: 3.70, o25: 1.70, u25: 2.05, kgYes: 1.62 },
    status: 'FT',
    score: '3 - 1',
    form: { home: ['G', 'G', 'G', 'B', 'G'], away: ['G', 'M', 'G', 'B', 'G'] },
    aiAnalysis: {
      prediction: 'MS 1',
      confidence: 70,
      valueBet: 'Arsenal Kazanır @ 1.95',
      riskLevel: 'Orta-Düşük',
      summary: 'Arsenal duran toplarda ezici üstünlüğe sahip. Chelsea geçiş hücumlarında fırsat bulabilir ancak Arsenal organizasyonu ağır basıyor.',
      keyFactors: [
        'Arsenal iç sahada derbilerde son 5 maçtır kaybetmiyor.',
        'Saka ve Martinelli kanat hattı yüksek form durumunda.'
      ]
    }
  },
  {
    id: 'm4',
    sport: 'Futbol',
    league: 'Şampiyonlar Ligi',
    leagueIcon: '🇪🇺',
    date: '2026-11-03',
    time: '22:00',
    home: 'Real Madrid',
    away: 'Bayern Münih',
    odds: { ms1: 2.10, draw: 3.50, ms2: 3.10, o25: 1.55, u25: 2.30, kgYes: 1.50 },
    status: 'NS',
    score: '- - -',
    form: { home: ['G', 'G', 'M', 'G', 'G'], away: ['G', 'G', 'G', 'M', 'G'] },
    aiAnalysis: {
      prediction: '2.5 Üst & KG Var',
      confidence: 82,
      valueBet: 'Toplam Gol 2.5 Üst @ 1.55',
      riskLevel: 'Düşük',
      summary: 'Devlerin randevusunda hücum hatları ön planda. Vinicius Jr. ve Kane formda, karşılıklı goller ve yüksek skor olasılığı yüksek.',
      keyFactors: [
        'İki takım arasındaki son 5 maçın 4\'ü 2.5 Üst bitti.',
        'Real Madrid Bernabeu\'da Avrupa gecelerinde ekstra iştahlı.'
      ]
    }
  },
  {
    id: 'm5',
    sport: 'Futbol',
    league: 'La Liga',
    leagueIcon: '🇪🇸',
    date: '2026-11-01',
    time: '21:00',
    home: 'Barcelona',
    away: 'Atletico Madrid',
    odds: { ms1: 1.80, draw: 3.60, ms2: 4.10, o25: 1.75, u25: 1.95, kgYes: 1.68 },
    status: 'NS',
    score: '- - -',
    form: { home: ['G', 'G', 'G', 'G', 'G'], away: ['G', 'M', 'G', 'G', 'M'] },
    aiAnalysis: {
      prediction: 'MS 1 (Barcelona)',
      confidence: 68,
      valueBet: 'Barcelona Galibiyeti',
      riskLevel: 'Orta',
      summary: 'Hansi Flick\'in yüksek ön alan baskısı Simeone\'nin katı savunmasını çözebilir. Erken gol maçı kilidinden çıkarır.',
      keyFactors: [
        'Barcelona bu sezon ligde en çok gol beklentisi (xG) üreten takım.',
        'Atletico deplasmanda sık katı kapanma tercih ediyor.'
      ]
    }
  },
  {
    id: 'm6',
    sport: 'Basketbol',
    league: 'EuroLeague',
    leagueIcon: '🏀',
    date: '2026-10-31',
    time: '20:45',
    home: 'Fenerbahçe Beko',
    away: 'Panathinaikos',
    odds: { ms1: 1.75, draw: 14.0, ms2: 2.00, o25: 1.85, u25: 1.85, kgYes: '-' },
    status: 'FT',
    score: '84 - 81',
    form: { home: ['G', 'G', 'M', 'G'], away: ['G', 'M', 'G', 'G'] },
    aiAnalysis: {
      prediction: 'MS 1 (-2.5 Handikap)',
      confidence: 62,
      valueBet: 'Fenerbahçe Beko Kazanır',
      riskLevel: 'Orta',
      summary: 'Ülker Arena\'da müthiş atmosfer beklentisi var. Guard düellosunda Baldwin ve Calathes liderliği belirleyici olur.',
      keyFactors: [
        'FB Beko iç sahada savunma reytinginde EuroLeague ilk 3 sırada.',
        'Panathinaikos deplasman üçlük yüzdesi %34 seviyesinde.'
      ]
    }
  },
  {
    id: 'm7',
    sport: 'Basketbol',
    league: 'NBA',
    leagueIcon: '🇺🇸',
    date: '2026-11-01',
    time: '03:00',
    home: 'L.A. Lakers',
    away: 'Golden State',
    odds: { ms1: 1.85, draw: 15.0, ms2: 1.85, o25: 1.80, u25: 1.90, kgYes: '-' },
    status: 'NS',
    score: '- - -',
    form: { home: ['G', 'M', 'G', 'M', 'G'], away: ['G', 'G', 'G', 'M', 'G'] },
    aiAnalysis: {
      prediction: '225.5 Toplam Sayı Üst',
      confidence: 75,
      valueBet: 'Toplam Sayı 225.5 Üst',
      riskLevel: 'Düşük',
      summary: 'Pace (tempo) istatistikleri yüksek iki ekip. Curry ve Davis aksiyonları yüksek skorlu bir mücadeleye işaret ediyor.',
      keyFactors: [
        'Son 3 karşılamada ortalama 234 sayı atıldı.',
        'İki takımın da fast-break sayıları lig ortalamasının üzerinde.'
      ]
    }
  }
];

export default function App() {
  // --- STATES ---
  const [activeTab, setActiveTab] = useState('matches'); // matches | bankroll | live_ai | settings
  const [apiKey, setApiKey] = useState(() => localStorage.getItem('gx_gemini_api_key') || '');
  const [fixtures, setFixtures] = useState(INITIAL_FIXTURES);
  
  // Filters
  const [selectedSport, setSelectedSport] = useState('Tümü');
  const [selectedLeague, setSelectedLeague] = useState('Tümü');
  const [selectedDate, setSelectedDate] = useState('2026-10-31');
  const [searchQuery, setSearchQuery] = useState('');

  // Selected Match View & Tabs
  const [selectedMatch, setSelectedMatch] = useState(null);
  const [matchDetailTab, setMatchDetailTab] = useState('ai'); // odds | ai | form

  // Live AI Analyzer state
  const [aiCustomHome, setAiCustomHome] = useState('');
  const [aiCustomAway, setAiCustomAway] = useState('');
  const [aiCustomSport, setAiCustomSport] = useState('Futbol');
  const [aiCustomLeague, setAiCustomLeague] = useState('Trendyol Süper Lig');
  const [aiCustomPrompt, setAiCustomPrompt] = useState('');
  const [isAiAnalyzing, setIsAiAnalyzing] = useState(false);
  const [liveAiResult, setLiveAiResult] = useState(null);

  // Bankroll state
  const [bankroll, setBankroll] = useState(() => {
    const saved = localStorage.getItem('gx_bankroll');
    return saved ? JSON.parse(saved) : {
      initialBalance: 1000,
      currentBalance: 1250,
      bets: [
        { id: 1, match: 'Fenerbahçe vs Göztepe', pick: 'MS 1', stake: 100, odds: 1.45, status: 'WON', profit: 45, date: '2026-10-31' },
        { id: 2, match: 'Arsenal vs Chelsea', pick: '2.5 Üst', stake: 150, odds: 1.70, status: 'WON', profit: 105, date: '2026-10-31' },
        { id: 3, match: 'Kocaelispor vs Çaykur Rizespor', pick: 'MS 1', stake: 100, odds: 2.20, status: 'LOST', profit: -100, date: '2026-10-31' }
      ]
    };
  });

  const [newBet, setNewBet] = useState({ match: '', pick: '', stake: 50, odds: 1.80, status: 'PENDING' });

  // Sync settings/bankroll
  useEffect(() => {
    localStorage.setItem('gx_gemini_api_key', apiKey);
  }, [apiKey]);

  useEffect(() => {
    localStorage.setItem('gx_bankroll', JSON.stringify(bankroll));
  }, [bankroll]);

  // Available sports & leagues
  const sports = ['Tümü', 'Futbol', 'Basketbol'];
  const leagues = useMemo(() => {
    if (selectedSport === 'Futbol') {
      return ['Tümü', 'Trendyol Süper Lig', 'Premier Lig', 'Şampiyonlar Ligi', 'La Liga'];
    } else if (selectedSport === 'Basketbol') {
      return ['Tümü', 'EuroLeague', 'NBA'];
    }
    return ['Tümü', 'Trendyol Süper Lig', 'Premier Lig', 'Şampiyonlar Ligi', 'La Liga', 'EuroLeague', 'NBA'];
  }, [selectedSport]);

  // Filtered fixtures
  const filteredFixtures = useMemo(() => {
    return fixtures.filter(m => {
      const matchSport = selectedSport === 'Tümü' || m.sport === selectedSport;
      const matchLeague = selectedLeague === 'Tümü' || m.league === selectedLeague;
      const matchDate = !selectedDate || m.date === selectedDate;
      const matchSearch = searchQuery.trim() === '' || 
        m.home.toLowerCase().includes(searchQuery.toLowerCase()) || 
        m.away.toLowerCase().includes(searchQuery.toLowerCase()) ||
        m.league.toLowerCase().includes(searchQuery.toLowerCase());

      return matchSport && matchLeague && matchDate && matchSearch;
    });
  }, [fixtures, selectedSport, selectedLeague, selectedDate, searchQuery]);

  // --- GEMINI AI CALL FUNCTION ---
  const callGeminiAI = async (promptText) => {
    const targetApiKey = apiKey || '';
    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=${targetApiKey}`;
    
    const systemPrompt = `Sen Maçkolik ve Flashscore standardında çalışan dünya çapında kıdemli bir İddaa / Spor Bahisleri Analiz Asistanısın (Gx Bot).
Kullanıcının sorduğu veya belirttiği maç için detaylı, rasyonel, xG ve taktiksel verilere dayalı Türkçe bir bahis analizi üret.
Yanıtın MUTLAKA geçerli bir JSON nesnesi formatında olsun ve başka markdown açıklaması içermesin. 
JSON Yapısı şöyle olmalıdır:
{
  "matchTitle": "Ev Sahibi vs Deplasman",
  "prediction": "Tavsiye Edilen Bahis (Örn: MS 1, 2.5 Üst, KG Var)",
  "confidence": 75, // (1-100 arası sayı)
  "valueBet": "Değerli Oran Önerisi",
  "riskLevel": "Düşük / Orta / Yüksek",
  "summary": "Maçın taktiksel özeti ve takımların durumları (3-4 cümle)",
  "keyFactors": [
    "Önemli veri veya sakatlık 1",
    "Önemli veri veya son form 2",
    "İstatistiksel detay 3"
  ],
  "oddsAnalysis": "Oranların mantıklılığı ve riske değerliği yorumu"
}`;

    const payload = {
      contents: [{ parts: [{ text: promptText }] }],
      systemInstruction: { parts: [{ text: systemPrompt }] },
      generationConfig: {
        responseMimeType: "application/json"
      }
    };

    try {
      const res = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (!res.ok) {
        throw new Error(`API Hatası: ${res.status}`);
      }

      const result = await res.json();
      const text = result?.candidates?.[0]?.content?.parts?.[0]?.text;
      if (text) {
        return JSON.parse(text);
      } else {
        throw new Error("Yanıt alınamadı.");
      }
    } catch (err) {
      console.warn("Gemini API isteği başarısız oldu, simülasyon yanıtı dönülüyor:", err);
      // Fallback mock response if API key is invalid or call fails
      return {
        matchTitle: promptText,
        prediction: "MS 1 & KG Var",
        confidence: 72,
        valueBet: "MS 1 @ 1.85 (Değerli)",
        riskLevel: "Orta",
        summary: `(Simüle Edilmiş AI Yanıtı) ${promptText} karşılaşmasında ev sahibi takımın son maçlardaki xG (Gol Beklentisi) oranı yüksek. İki takımın da son 5 maçlık serisinde temposu yüksek mücadeleler göze çarpıyor.`,
        keyFactors: [
          "Ev sahibi iç sahada son 4 maçın tamamını kazandı.",
          "Deplasman ekibi son 3 lig maçında kalesinde gol gördü.",
          "Sakatlıktan dönen kilit golcünün kadroda olması bekleniyor."
        ],
        oddsAnalysis: "Açılan 1.85 oran mevcut form durumlarına göre %8-10 oranında değer sunmaktadır."
      };
    }
  };

  // Run Custom AI Analysis
  const handleRunCustomAi = async () => {
    if (!aiCustomHome || !aiCustomAway) return;
    setIsAiAnalyzing(true);
    setLiveAiResult(null);

    const prompt = `Lütfen şu karşılaşmayı analiz et:
Spor: ${aiCustomSport}
Lig: ${aiCustomLeague}
Maç: ${aiCustomHome} vs ${aiCustomAway}
Özel Not/Soru: ${aiCustomPrompt || 'Genel maç tahmini ve değer bahsi çıkar.'}`;

    const res = await callGeminiAI(prompt);
    setLiveAiResult(res);
    setIsAiAnalyzing(false);
  };

  // Run AI Deep Analysis for a specific fixture match card
  const handleMatchDeepAi = async (match) => {
    setIsAiAnalyzing(true);
    const prompt = `${match.league} kapsamında oynanacak ${match.home} - ${match.away} karşılaşması için canlı analiz yap. Ev Sahibi Form: ${match.form.home.join('')}, Deplasman Form: ${match.form.away.join('')}. Oranlar: MS1: ${match.odds.ms1}, X: ${match.odds.draw}, MS2: ${match.odds.ms2}.`;
    
    const res = await callGeminiAI(prompt);
    
    // Update match state
    setFixtures(prev => prev.map(f => {
      if (f.id === match.id) {
        return {
          ...f,
          aiAnalysis: {
            prediction: res.prediction,
            confidence: res.confidence,
            valueBet: res.valueBet,
            riskLevel: res.riskLevel,
            summary: res.summary,
            keyFactors: res.keyFactors
          }
        };
      }
      return f;
    }));

    if (selectedMatch && selectedMatch.id === match.id) {
      setSelectedMatch(prev => ({
        ...prev,
        aiAnalysis: {
          prediction: res.prediction,
          confidence: res.confidence,
          valueBet: res.valueBet,
          riskLevel: res.riskLevel,
          summary: res.summary,
          keyFactors: res.keyFactors
        }
      }));
    }

    setIsAiAnalyzing(false);
  };

  // Bankroll Operations
  const handleAddBet = (e) => {
    e.preventDefault();
    if (!newBet.match || !newBet.pick) return;

    const stake = parseFloat(newBet.stake) || 0;
    const odds = parseFloat(newBet.odds) || 1.0;
    let profit = 0;

    if (newBet.status === 'WON') {
      profit = stake * (odds - 1);
    } else if (newBet.status === 'LOST') {
      profit = -stake;
    }

    const betObj = {
      id: Date.now(),
      match: newBet.match,
      pick: newBet.pick,
      stake,
      odds,
      status: newBet.status,
      profit,
      date: new Date().toISOString().split('T')[0]
    };

    setBankroll(prev => ({
      ...prev,
      currentBalance: prev.currentBalance + profit,
      bets: [betObj, ...prev.bets]
    }));

    setNewBet({ match: '', pick: '', stake: 50, odds: 1.80, status: 'PENDING' });
  };

  const handleDeleteBet = (id) => {
    setBankroll(prev => {
      const betToRemove = prev.bets.find(b => b.id === id);
      const newBets = prev.bets.filter(b => b.id !== id);
      let newBal = prev.currentBalance;
      if (betToRemove) {
        newBal -= betToRemove.profit;
      }
      return {
        ...prev,
        currentBalance: newBal,
        bets: newBets
      };
    });
  };

  // Stats for Bankroll
  const bankrollStats = useMemo(() => {
    const totalBets = bankroll.bets.length;
    const wonBets = bankroll.bets.filter(b => b.status === 'WON').length;
    const lostBets = bankroll.bets.filter(b => b.status === 'LOST').length;
    const pendingBets = bankroll.bets.filter(b => b.status === 'PENDING').length;
    
    const winRate = totalBets - pendingBets > 0 
      ? Math.round((wonBets / (totalBets - pendingBets)) * 100) 
      : 0;

    const netProfit = bankroll.currentBalance - bankroll.initialBalance;
    const totalStaked = bankroll.bets.reduce((acc, b) => acc + b.stake, 0);
    const roi = totalStaked > 0 ? ((netProfit / totalStaked) * 100).toFixed(1) : 0;

    return { totalBets, wonBets, lostBets, pendingBets, winRate, netProfit, roi };
  }, [bankroll]);

  return (
    <div className="min-h-screen bg-[#0d0f14] text-gray-100 font-sans pb-24 select-none">
      
      {/* --- HEADER --- */}
      <header className="sticky top-0 z-40 bg-[#141721]/95 backdrop-blur-md border-b border-[#232736] px-4 py-3 shadow-lg">
        <div className="max-w-md mx-auto flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="bg-gradient-to-tr from-red-600 to-red-500 p-2 rounded-xl text-white shadow-md shadow-red-900/30">
              <Zap className="w-5 h-5" />
            </div>
            <div>
              <h1 className="text-lg font-black tracking-wider text-white flex items-center gap-1.5">
                GX BOT <span className="text-xs bg-red-600/30 text-red-400 border border-red-500/30 px-1.5 py-0.5 rounded font-bold">PRO</span>
              </h1>
              <p className="text-[10px] text-gray-400 font-medium">Maçkolik Mobil Analitik & Yapay Zeka</p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button 
              onClick={() => setActiveTab('settings')}
              className={`p-2 rounded-lg border transition ${apiKey ? 'bg-emerald-950/40 border-emerald-500/40 text-emerald-400' : 'bg-[#1c202d] border-[#2d3345] text-gray-400'}`}
              title="Gemini API Anahtarı"
            >
              <Key className="w-4 h-4" />
            </button>
            <div className="bg-[#1c202d] border border-[#2d3345] px-2.5 py-1 rounded-lg text-xs font-semibold text-emerald-400 flex items-center gap-1">
              <DollarSign className="w-3.5 h-3.5 text-emerald-400" />
              {bankroll.currentBalance.toFixed(0)} TL
            </div>
          </div>
        </div>
      </header>

      {/* --- MAIN CONTAINER --- */}
      <main className="max-w-md mx-auto px-3 pt-3">

        {/* ================= TAB 1: MATCHES & LEAGUES ================= */}
        {activeTab === 'matches' && (
          <div className="space-y-3 animate-fade-in">
            
            {/* SEARCH & FILTERS BAR */}
            <div className="bg-[#141721] p-3 rounded-2xl border border-[#232736] space-y-2.5 shadow-md">
              
              {/* Search Box */}
              <div className="relative">
                <Search className="w-4 h-4 absolute left-3 top-2.5 text-gray-400" />
                <input 
                  type="text"
                  placeholder="Takım veya lig ara..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full bg-[#1b1f2c] border border-[#2d3345] rounded-xl pl-9 pr-3 py-1.5 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-red-500 transition"
                />
                {searchQuery && (
                  <button onClick={() => setSearchQuery('')} className="absolute right-3 top-2 text-xs text-gray-400">✕</button>
                )}
              </div>

              {/* Sport Selector Pills */}
              <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none">
                {sports.map(s => (
                  <button
                    key={s}
                    onClick={() => { setSelectedSport(s); setSelectedLeague('Tümü'); }}
                    className={`px-3 py-1 rounded-lg text-xs font-semibold whitespace-nowrap transition ${
                      selectedSport === s 
                        ? 'bg-red-600 text-white shadow-md shadow-red-900/40' 
                        : 'bg-[#1b1f2c] text-gray-400 hover:bg-[#232838]'
                    }`}
                  >
                    {s}
                  </button>
                ))}
              </div>

              {/* League Selector Horizontal Scroll */}
              <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none border-t border-[#1e2230] pt-2">
                <span className="text-[10px] uppercase font-bold text-gray-500 flex items-center gap-1">
                  <Filter className="w-3 h-3" /> Lig:
                </span>
                {leagues.map(l => (
                  <button
                    key={l}
                    onClick={() => setSelectedLeague(l)}
                    className={`px-2.5 py-1 rounded-md text-[11px] font-medium whitespace-nowrap transition ${
                      selectedLeague === l 
                        ? 'bg-red-600/20 text-red-400 border border-red-500/40' 
                        : 'bg-[#181c28] text-gray-400 hover:text-gray-200'
                    }`}
                  >
                    {l}
                  </button>
                ))}
              </div>

              {/* Date Filter */}
              <div className="flex items-center justify-between border-t border-[#1e2230] pt-2 text-xs">
                <span className="text-gray-400 flex items-center gap-1">
                  <Calendar className="w-3.5 h-3.5 text-red-500" /> Tarih Seçimi:
                </span>
                <input 
                  type="date"
                  value={selectedDate}
                  onChange={(e) => setSelectedDate(e.target.value)}
                  className="bg-[#1b1f2c] border border-[#2d3345] rounded-lg px-2 py-1 text-xs text-gray-200 focus:outline-none focus:border-red-500"
                />
              </div>
            </div>

            {/* MATCHES LIST */}
            <div className="space-y-2.5">
              <div className="flex items-center justify-between px-1">
                <span className="text-xs font-bold text-gray-400 uppercase tracking-wider flex items-center gap-1.5">
                  <Activity className="w-3.5 h-3.5 text-red-500" /> Bülten Maçları ({filteredFixtures.length})
                </span>
                <span className="text-[10px] text-gray-500 font-mono">
                  {selectedDate ? new Date(selectedDate).toLocaleDateString('tr-TR', { day: 'numeric', month: 'long', year: 'numeric' }) : 'Tüm Tarihler'}
                </span>
              </div>

              {filteredFixtures.length === 0 ? (
                <div className="bg-[#141721] p-8 text-center rounded-2xl border border-[#232736]">
                  <ShieldAlert className="w-8 h-8 text-gray-500 mx-auto mb-2" />
                  <p className="text-sm font-semibold text-gray-300">Maç Bulunamadı</p>
                  <p className="text-xs text-gray-500 mt-1">Seçtiğiniz lig veya tarih için aktif bülten maçı görünmüyor.</p>
                  <button 
                    onClick={() => { setSelectedSport('Tümü'); setSelectedLeague('Tümü'); setSelectedDate('2026-10-31'); setSearchQuery(''); }}
                    className="mt-3 text-xs text-red-400 bg-red-950/40 border border-red-500/30 px-3 py-1.5 rounded-lg"
                  >
                    Filtreleri Sıfırla
                  </button>
                </div>
              ) : (
                filteredFixtures.map(match => (
                  <div 
                    key={match.id}
                    onClick={() => { setSelectedMatch(match); setMatchDetailTab('ai'); }}
                    className="bg-[#141721] hover:bg-[#181c28] border border-[#232736] rounded-2xl p-3.5 transition cursor-pointer shadow-md hover:border-red-500/40 relative overflow-hidden group"
                  >
                    {/* Top League Ribbon */}
                    <div className="flex items-center justify-between text-xs mb-2.5 pb-2 border-b border-[#1e2230]">
                      <div className="flex items-center gap-1.5 font-bold text-gray-300">
                        <span>{match.leagueIcon}</span>
                        <span className="text-red-400">{match.league}</span>
                      </div>
                      <div className="flex items-center gap-2">
                        <span className="text-[10px] text-gray-400 font-mono">{match.time}</span>
                        {match.status === 'FT' ? (
                          <span className="bg-gray-800 text-gray-300 text-[10px] font-bold px-1.5 py-0.5 rounded">MS</span>
                        ) : (
                          <span className="bg-emerald-950/60 text-emerald-400 border border-emerald-500/30 text-[10px] font-bold px-1.5 py-0.5 rounded animate-pulse">CANLI/YAKINDA</span>
                        )}
                      </div>
                    </div>

                    {/* Team Matchup & Score */}
                    <div className="grid grid-cols-7 items-center gap-2 my-2">
                      <div className="col-span-3 text-right">
                        <p className="text-sm font-bold text-white group-hover:text-red-400 transition truncate">{match.home}</p>
                        <div className="flex items-center justify-end gap-0.5 mt-1">
                          {match.form.home.map((f, i) => (
                            <span key={i} className={`text-[9px] font-bold px-1 rounded ${f === 'G' ? 'bg-emerald-900/60 text-emerald-300' : f === 'M' ? 'bg-red-900/60 text-red-300' : 'bg-amber-900/60 text-amber-300'}`}>{f}</span>
                          ))}
                        </div>
                      </div>

                      <div className="col-span-1 text-center bg-[#1b1f2c] py-1.5 px-1 rounded-xl border border-[#2d3345]">
                        <span className="text-xs font-black text-white block">{match.score}</span>
                      </div>

                      <div className="col-span-3 text-left">
                        <p className="text-sm font-bold text-white group-hover:text-red-400 transition truncate">{match.away}</p>
                        <div className="flex items-center justify-start gap-0.5 mt-1">
                          {match.form.away.map((f, i) => (
                            <span key={i} className={`text-[9px] font-bold px-1 rounded ${f === 'G' ? 'bg-emerald-900/60 text-emerald-300' : f === 'M' ? 'bg-red-900/60 text-red-300' : 'bg-amber-900/60 text-amber-300'}`}>{f}</span>
                          ))}
                        </div>
                      </div>
                    </div>

                    {/* Quick AI & Odds Footer */}
                    <div className="mt-3 pt-2.5 border-t border-[#1e2230] flex items-center justify-between text-xs">
                      <div className="flex items-center gap-1 text-[#a5b4fc] bg-indigo-950/40 border border-indigo-500/30 px-2 py-1 rounded-lg">
                        <Sparkles className="w-3 h-3 text-indigo-400" />
                        <span className="font-semibold">{match.aiAnalysis.prediction}</span>
                        <span className="text-[10px] opacity-75 font-mono">({match.aiAnalysis.confidence}%)</span>
                      </div>
                      
                      <div className="flex items-center gap-1.5 text-gray-400 font-mono text-[11px]">
                        <span className="bg-[#1c202d] px-1.5 py-0.5 rounded border border-[#2a3042]">1: <strong className="text-white">{match.odds.ms1}</strong></span>
                        <span className="bg-[#1c202d] px-1.5 py-0.5 rounded border border-[#2a3042]">X: <strong className="text-white">{match.odds.draw}</strong></span>
                        <span className="bg-[#1c202d] px-1.5 py-0.5 rounded border border-[#2a3042]">2: <strong className="text-white">{match.odds.ms2}</strong></span>
                      </div>
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>
        )}

        {/* ================= MODAL / DETAILED MATCH VIEW ================= */}
        {selectedMatch && (
          <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-end sm:items-center justify-center p-0 sm:p-4">
            <div className="bg-[#141721] border border-[#2d3345] w-full max-w-md rounded-t-3xl sm:rounded-3xl max-h-[90vh] flex flex-col overflow-hidden animate-slide-up shadow-2xl">
              
              {/* Modal Header */}
              <div className="p-4 bg-[#181c28] border-b border-[#232736] flex items-center justify-between">
                <div>
                  <div className="flex items-center gap-1.5 text-xs text-red-400 font-bold">
                    <span>{selectedMatch.leagueIcon}</span>
                    <span>{selectedMatch.league}</span>
                  </div>
                  <h2 className="text-base font-black text-white mt-0.5">
                    {selectedMatch.home} vs {selectedMatch.away}
                  </h2>
                </div>
                <button 
                  onClick={() => setSelectedMatch(null)}
                  className="bg-[#222736] text-gray-400 hover:text-white p-2 rounded-full text-xs font-bold"
                >
                  ✕
                </button>
              </div>

              {/* Sub-Tabs */}
              <div className="flex border-b border-[#232736] bg-[#10131c]">
                <button 
                  onClick={() => setMatchDetailTab('ai')}
                  className={`flex-1 py-2.5 text-xs font-bold flex items-center justify-center gap-1.5 border-b-2 transition ${matchDetailTab === 'ai' ? 'border-red-500 text-red-400 bg-[#161a26]' : 'border-transparent text-gray-400'}`}
                >
                  <Sparkles className="w-3.5 h-3.5" /> Gx Yapay Zeka
                </button>
                <button 
                  onClick={() => setMatchDetailTab('odds')}
                  className={`flex-1 py-2.5 text-xs font-bold flex items-center justify-center gap-1.5 border-b-2 transition ${matchDetailTab === 'odds' ? 'border-red-500 text-red-400 bg-[#161a26]' : 'border-transparent text-gray-400'}`}
                >
                  <BarChart3 className="w-3.5 h-3.5" /> Oranlar
                </button>
                <button 
                  onClick={() => setMatchDetailTab('form')}
                  className={`flex-1 py-2.5 text-xs font-bold flex items-center justify-center gap-1.5 border-b-2 transition ${matchDetailTab === 'form' ? 'border-red-500 text-red-400 bg-[#161a26]' : 'border-transparent text-gray-400'}`}
                >
                  <TrendingUp className="w-3.5 h-3.5" /> Form & İstatistik
                </button>
              </div>

              {/* Modal Body */}
              <div className="p-4 overflow-y-auto space-y-4">

                {/* --- TAB: AI ANALYSIS --- */}
                {matchDetailTab === 'ai' && (
                  <div className="space-y-3.5">
                    {/* Top Prediction Banner */}
                    <div className="bg-gradient-to-r from-red-950/60 to-indigo-950/60 border border-red-500/30 p-3.5 rounded-2xl flex items-center justify-between">
                      <div>
                        <span className="text-[10px] text-gray-400 uppercase tracking-widest font-bold">Önerilen Tahmin</span>
                        <p className="text-lg font-black text-white">{selectedMatch.aiAnalysis.prediction}</p>
                        <p className="text-xs text-amber-400 mt-0.5">Değer: <strong>{selectedMatch.aiAnalysis.valueBet}</strong></p>
                      </div>
                      <div className="text-right">
                        <span className="text-xs text-gray-400 block">Güven Oranı</span>
                        <span className="text-xl font-black text-emerald-400 font-mono">%{selectedMatch.aiAnalysis.confidence}</span>
                        <span className="text-[9px] bg-red-600/30 text-red-300 border border-red-500/30 px-1.5 py-0.5 rounded font-bold block mt-1">
                          Risk: {selectedMatch.aiAnalysis.riskLevel}
                        </span>
                      </div>
                    </div>

                    {/* Summary */}
                    <div className="bg-[#1a1e2b] p-3.5 rounded-xl border border-[#2d3345] space-y-1.5">
                      <h4 className="text-xs font-bold text-gray-300 flex items-center gap-1.5">
                        <Cpu className="w-4 h-4 text-red-400" /> Yapay Zeka Taktik Değerlendirmesi
                      </h4>
                      <p className="text-xs text-gray-300 leading-relaxed">{selectedMatch.aiAnalysis.summary}</p>
                    </div>

                    {/* Key Factors */}
                    <div className="space-y-1.5">
                      <h4 className="text-xs font-bold text-gray-400 uppercase tracking-wider">Kritik Maç Faktörleri</h4>
                      {selectedMatch.aiAnalysis.keyFactors.map((kf, idx) => (
                        <div key={idx} className="bg-[#181c28] p-2.5 rounded-xl border border-[#232736] text-xs text-gray-200 flex items-start gap-2">
                          <span className="bg-red-500/20 text-red-400 text-[10px] font-bold px-1.5 py-0.5 rounded mt-0.5">{idx + 1}</span>
                          <span>{kf}</span>
                        </div>
                      ))}
                    </div>

                    {/* Refresh Live AI Button */}
                    <button 
                      onClick={() => handleMatchDeepAi(selectedMatch)}
                      disabled={isAiAnalyzing}
                      className="w-full py-2.5 bg-gradient-to-r from-red-600 to-red-500 hover:from-red-500 hover:to-red-400 text-white rounded-xl text-xs font-bold flex items-center justify-center gap-2 shadow-lg shadow-red-900/30 transition disabled:opacity-50"
                    >
                      {isAiAnalyzing ? (
                        <>
                          <RefreshCw className="w-4 h-4 animate-spin text-white" /> Gemini Analiz Ediyor...
                        </>
                      ) : (
                        <>
                          <Sparkles className="w-4 h-4" /> Gemini AI İle Canlı Yeniden Analiz Et
                        </>
                      )}
                    </button>
                  </div>
                )}

                {/* --- TAB: ODDS --- */}
                {matchDetailTab === 'odds' && (
                  <div className="space-y-3">
                    <h4 className="text-xs font-bold text-gray-400 uppercase">Maç Sonu (MS) & Gol Bahisleri</h4>
                    
                    <div className="grid grid-cols-3 gap-2 text-center font-mono">
                      <div className="bg-[#1b1f2c] p-3 rounded-xl border border-[#2d3345]">
                        <span className="text-[10px] text-gray-400 block font-sans">MS 1</span>
                        <span className="text-base font-black text-emerald-400">{selectedMatch.odds.ms1}</span>
                      </div>
                      <div className="bg-[#1b1f2c] p-3 rounded-xl border border-[#2d3345]">
                        <span className="text-[10px] text-gray-400 block font-sans">MS X (Beraberlik)</span>
                        <span className="text-base font-black text-amber-400">{selectedMatch.odds.draw}</span>
                      </div>
                      <div className="bg-[#1b1f2c] p-3 rounded-xl border border-[#2d3345]">
                        <span className="text-[10px] text-gray-400 block font-sans">MS 2</span>
                        <span className="text-base font-black text-red-400">{selectedMatch.odds.ms2}</span>
                      </div>
                    </div>

                    <div className="grid grid-cols-2 gap-2 text-center font-mono">
                      <div className="bg-[#1b1f2c] p-3 rounded-xl border border-[#2d3345]">
                        <span className="text-[10px] text-gray-400 block font-sans">2.5 Gol Üst</span>
                        <span className="text-sm font-bold text-white">{selectedMatch.odds.o25}</span>
                      </div>
                      <div className="bg-[#1b1f2c] p-3 rounded-xl border border-[#2d3345]">
                        <span className="text-[10px] text-gray-400 block font-sans">2.5 Gol Alt</span>
                        <span className="text-sm font-bold text-white">{selectedMatch.odds.u25}</span>
                      </div>
                    </div>

                    {selectedMatch.odds.kgYes !== '-' && (
                      <div className="bg-[#1b1f2c] p-3 rounded-xl border border-[#2d3345] flex items-center justify-between text-xs font-mono">
                        <span className="text-gray-400 font-sans">Karşılıklı Gol Var (KG Var):</span>
                        <span className="text-sm font-bold text-emerald-400">{selectedMatch.odds.kgYes}</span>
                      </div>
                    )}
                  </div>
                )}

                {/* --- TAB: FORM --- */}
                {matchDetailTab === 'form' && (
                  <div className="space-y-3">
                    <div className="bg-[#1b1f2c] p-3.5 rounded-xl border border-[#2d3345]">
                      <h4 className="text-xs font-bold text-white mb-2">{selectedMatch.home} Son 5 Maç</h4>
                      <div className="flex gap-1.5">
                        {selectedMatch.form.home.map((f, i) => (
                          <div key={i} className={`flex-1 text-center py-1.5 rounded text-xs font-bold ${f === 'G' ? 'bg-emerald-950 border border-emerald-500/40 text-emerald-400' : f === 'M' ? 'bg-red-950 border border-red-500/40 text-red-400' : 'bg-amber-950 border border-amber-500/40 text-amber-400'}`}>
                            {f}
                          </div>
                        ))}
                      </div>
                    </div>

                    <div className="bg-[#1b1f2c] p-3.5 rounded-xl border border-[#2d3345]">
                      <h4 className="text-xs font-bold text-white mb-2">{selectedMatch.away} Son 5 Maç</h4>
                      <div className="flex gap-1.5">
                        {selectedMatch.form.away.map((f, i) => (
                          <div key={i} className={`flex-1 text-center py-1.5 rounded text-xs font-bold ${f === 'G' ? 'bg-emerald-950 border border-emerald-500/40 text-emerald-400' : f === 'M' ? 'bg-red-950 border border-red-500/40 text-red-400' : 'bg-amber-950 border border-amber-500/40 text-amber-400'}`}>
                            {f}
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                )}

              </div>

              {/* Modal Footer */}
              <div className="p-3 bg-[#181c28] border-t border-[#232736]">
                <button 
                  onClick={() => {
                    setNewBet({
                      match: `${selectedMatch.home} - ${selectedMatch.away}`,
                      pick: selectedMatch.aiAnalysis.prediction,
                      stake: 100,
                      odds: selectedMatch.odds.ms1 || 1.80,
                      status: 'PENDING'
                    });
                    setSelectedMatch(null);
                    setActiveTab('bankroll');
                  }}
                  className="w-full py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 shadow-lg shadow-emerald-950"
                >
                  <PlusCircle className="w-4 h-4" /> Bu Maçı Kasa Takibine Ekle
                </button>
              </div>

            </div>
          </div>
        )}

        {/* ================= TAB 2: LIVE AI ANALYZER ================= */}
        {activeTab === 'live_ai' && (
          <div className="space-y-3.5 animate-fade-in">
            <div className="bg-[#141721] p-4 rounded-2xl border border-[#232736] space-y-3 shadow-md">
              <div className="flex items-center gap-2">
                <div className="p-2 bg-gradient-to-tr from-indigo-600 to-red-600 rounded-xl text-white">
                  <Sparkles className="w-5 h-5" />
                </div>
                <div>
                  <h2 className="text-sm font-black text-white">Canlı Gemini AI Maç Analiz Motoru</h2>
                  <p className="text-[11px] text-gray-400">İstediğin herhangi iki takımı yaz, anında taktiksel analiz al.</p>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-2 pt-1">
                <div>
                  <label className="text-[10px] text-gray-400 font-bold block mb-1">Spor Branşı</label>
                  <select 
                    value={aiCustomSport}
                    onChange={(e) => setAiCustomSport(e.target.value)}
                    className="w-full bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none"
                  >
                    <option value="Futbol">Futbol</option>
                    <option value="Basketbol">Basketbol</option>
                  </select>
                </div>
                <div>
                  <label className="text-[10px] text-gray-400 font-bold block mb-1">Lig / Kupa</label>
                  <input 
                    type="text"
                    value={aiCustomLeague}
                    onChange={(e) => setAiCustomLeague(e.target.value)}
                    placeholder="Örn: Süper Lig"
                    className="w-full bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none"
                  />
                </div>
              </div>

              <div className="grid grid-cols-2 gap-2">
                <div>
                  <label className="text-[10px] text-gray-400 font-bold block mb-1">Ev Sahibi Takım</label>
                  <input 
                    type="text"
                    placeholder="Örn: Galatasaray"
                    value={aiCustomHome}
                    onChange={(e) => setAiCustomHome(e.target.value)}
                    className="w-full bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none"
                  />
                </div>
                <div>
                  <label className="text-[10px] text-gray-400 font-bold block mb-1">Deplasman Takım</label>
                  <input 
                    type="text"
                    placeholder="Örn: Beşiktaş"
                    value={aiCustomAway}
                    onChange={(e) => setAiCustomAway(e.target.value)}
                    className="w-full bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none"
                  />
                </div>
              </div>

              <div>
                <label className="text-[10px] text-gray-400 font-bold block mb-1">Özel Taktik/Soru Notu (Opsiyonel)</label>
                <input 
                  type="text"
                  placeholder="Örn: Yağmurlu hava ve sakat oyuncular etkiler mi?"
                  value={aiCustomPrompt}
                  onChange={(e) => setAiCustomPrompt(e.target.value)}
                  className="w-full bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none"
                />
              </div>

              <button 
                onClick={handleRunCustomAi}
                disabled={isAiAnalyzing || !aiCustomHome || !aiCustomAway}
                className="w-full py-2.5 bg-gradient-to-r from-red-600 via-indigo-600 to-red-600 bg-size-200 hover:bg-right text-white rounded-xl text-xs font-bold flex items-center justify-center gap-2 shadow-lg shadow-indigo-950 transition disabled:opacity-50"
              >
                {isAiAnalyzing ? (
                  <>
                    <RefreshCw className="w-4 h-4 animate-spin" /> Yapay Zeka Verileri Derliyor...
                  </>
                ) : (
                  <>
                    <Sparkles className="w-4 h-4" /> Gemini AI Analizini Başlat
                  </>
                )}
              </button>
            </div>

            {/* LIVE RESULT CARD */}
            {liveAiResult && (
              <div className="bg-[#141721] border border-indigo-500/30 rounded-2xl p-4 space-y-3 shadow-xl animate-fade-in">
                <div className="flex items-center justify-between border-b border-[#232736] pb-2.5">
                  <span className="text-xs font-bold text-indigo-400 flex items-center gap-1">
                    <Award className="w-4 h-4" /> {liveAiResult.matchTitle || `${aiCustomHome} vs ${aiCustomAway}`}
                  </span>
                  <span className="text-[10px] bg-indigo-950 text-indigo-300 px-2 py-0.5 rounded border border-indigo-500/30 font-mono">
                    Güven: %{liveAiResult.confidence}
                  </span>
                </div>

                <div className="grid grid-cols-2 gap-2 text-center">
                  <div className="bg-[#1b1f2c] p-2.5 rounded-xl border border-[#2d3345]">
                    <span className="text-[10px] text-gray-400 block font-bold">Önerilen Tahmin</span>
                    <span className="text-sm font-black text-emerald-400">{liveAiResult.prediction}</span>
                  </div>
                  <div className="bg-[#1b1f2c] p-2.5 rounded-xl border border-[#2d3345]">
                    <span className="text-[10px] text-gray-400 block font-bold">Değerli Bahis Oranı</span>
                    <span className="text-xs font-bold text-amber-400">{liveAiResult.valueBet}</span>
                  </div>
                </div>

                <div className="bg-[#181c28] p-3 rounded-xl border border-[#232736] text-xs text-gray-300 leading-relaxed">
                  <strong className="text-white block mb-1">Taktiksel Özet:</strong>
                  {liveAiResult.summary}
                </div>

                {liveAiResult.keyFactors && liveAiResult.keyFactors.length > 0 && (
                  <div className="space-y-1">
                    <span className="text-[10px] font-bold text-gray-400 uppercase">Önemli Faktörler</span>
                    {liveAiResult.keyFactors.map((kf, i) => (
                      <div key={i} className="text-xs text-gray-300 bg-[#1b1f2c] px-2.5 py-1.5 rounded-lg border border-[#232736]">
                        • {kf}
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>
        )}

        {/* ================= TAB 3: BANKROLL MANAGEMENT ================= */}
        {activeTab === 'bankroll' && (
          <div className="space-y-3.5 animate-fade-in">
            
            {/* STATS OVERVIEW CARDS */}
            <div className="grid grid-cols-3 gap-2">
              <div className="bg-[#141721] p-3 rounded-2xl border border-[#232736] text-center">
                <span className="text-[10px] text-gray-400 font-semibold block">Mevcut Kasa</span>
                <span className="text-base font-black text-white font-mono mt-0.5 block">{bankroll.currentBalance.toFixed(0)} TL</span>
                <span className={`text-[10px] font-bold ${bankrollStats.netProfit >= 0 ? 'text-emerald-400' : 'text-red-400'}`}>
                  {bankrollStats.netProfit >= 0 ? '+' : ''}{bankrollStats.netProfit.toFixed(0)} TL
                </span>
              </div>

              <div className="bg-[#141721] p-3 rounded-2xl border border-[#232736] text-center">
                <span className="text-[10px] text-gray-400 font-semibold block">Kazanma Oranı</span>
                <span className="text-base font-black text-emerald-400 font-mono mt-0.5 block">%{bankrollStats.winRate}</span>
                <span className="text-[10px] text-gray-500 font-mono">{bankrollStats.wonBets}K / {bankrollStats.lostBets}M</span>
              </div>

              <div className="bg-[#141721] p-3 rounded-2xl border border-[#232736] text-center">
                <span className="text-[10px] text-gray-400 font-semibold block">ROI (Getiri)</span>
                <span className={`text-base font-black font-mono mt-0.5 block ${bankrollStats.roi >= 0 ? 'text-emerald-400' : 'text-red-400'}`}>
                  %{bankrollStats.roi}
                </span>
                <span className="text-[10px] text-gray-500 font-mono">{bankrollStats.totalBets} Kupon</span>
              </div>
            </div>

            {/* ADD BET FORM */}
            <div className="bg-[#141721] p-3.5 rounded-2xl border border-[#232736] space-y-2.5 shadow-md">
              <h3 className="text-xs font-bold text-white flex items-center gap-1.5">
                <PlusCircle className="w-4 h-4 text-emerald-400" /> Yeni Kupon Takibi Ekle
              </h3>
              
              <form onSubmit={handleAddBet} className="space-y-2">
                <input 
                  type="text"
                  placeholder="Maç Adı (Örn: Fenerbahçe - Göztepe)"
                  value={newBet.match}
                  onChange={(e) => setNewBet({ ...newBet, match: e.target.value })}
                  className="w-full bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-3 py-1.5 text-xs text-white placeholder-gray-500 focus:outline-none"
                />

                <div className="grid grid-cols-3 gap-2">
                  <input 
                    type="text"
                    placeholder="Tahmin (Örn: MS 1)"
                    value={newBet.pick}
                    onChange={(e) => setNewBet({ ...newBet, pick: e.target.value })}
                    className="bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none"
                  />
                  <input 
                    type="number"
                    step="0.01"
                    placeholder="Oran"
                    value={newBet.odds}
                    onChange={(e) => setNewBet({ ...newBet, odds: e.target.value })}
                    className="bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none"
                  />
                  <input 
                    type="number"
                    placeholder="Tutar (TL)"
                    value={newBet.stake}
                    onChange={(e) => setNewBet({ ...newBet, stake: e.target.value })}
                    className="bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-2.5 py-1.5 text-xs text-white focus:outline-none"
                  />
                </div>

                <div className="flex items-center gap-2">
                  <select 
                    value={newBet.status}
                    onChange={(e) => setNewBet({ ...newBet, status: e.target.value })}
                    className="bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-3 py-1.5 text-xs text-white focus:outline-none flex-1"
                  >
                    <option value="PENDING">⏳ Bekliyor</option>
                    <option value="WON">✅ Kazandı</option>
                    <option value="LOST">❌ Kaybetti</option>
                  </select>

                  <button 
                    type="submit"
                    className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold shadow-md shadow-emerald-950"
                  >
                    Kaydet
                  </button>
                </div>
              </form>
            </div>

            {/* BETS HISTORY LIST */}
            <div className="space-y-2">
              <span className="text-xs font-bold text-gray-400 uppercase tracking-wider block px-1">
                Geçmiş Kuponlar ({bankroll.bets.length})
              </span>

              {bankroll.bets.map(b => (
                <div key={b.id} className="bg-[#141721] p-3 rounded-2xl border border-[#232736] flex items-center justify-between text-xs">
                  <div>
                    <p className="font-bold text-white">{b.match}</p>
                    <div className="flex items-center gap-2 text-[11px] text-gray-400 mt-0.5">
                      <span className="bg-[#1b1f2c] px-1.5 py-0.5 rounded text-gray-300">{b.pick}</span>
                      <span>Oran: <strong className="text-white">{b.odds}</strong></span>
                      <span>Yatırılan: <strong className="text-white">{b.stake} TL</strong></span>
                    </div>
                  </div>

                  <div className="flex items-center gap-2">
                    <div className="text-right">
                      {b.status === 'WON' && <span className="text-emerald-400 font-bold font-mono">+{b.profit.toFixed(0)} TL</span>}
                      {b.status === 'LOST' && <span className="text-red-400 font-bold font-mono">{b.profit.toFixed(0)} TL</span>}
                      {b.status === 'PENDING' && <span className="text-amber-400 font-bold">Bekliyor</span>}
                    </div>

                    <button 
                      onClick={() => handleDeleteBet(b.id)}
                      className="text-gray-500 hover:text-red-400 p-1"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>
              ))}
            </div>

          </div>
        )}

        {/* ================= TAB 4: SETTINGS ================= */}
        {activeTab === 'settings' && (
          <div className="space-y-3.5 animate-fade-in">
            <div className="bg-[#141721] p-4 rounded-2xl border border-[#232736] space-y-3 shadow-md">
              <div className="flex items-center gap-2">
                <Key className="w-5 h-5 text-red-500" />
                <h3 className="text-sm font-bold text-white">Gemini AI Anahtarı Yapılandırması</h3>
              </div>
              <p className="text-xs text-gray-400 leading-relaxed">
                Canlı ve sınırsız yapay zeka maç analizleri için Google Gemini API Anahtarınızı girebilirsiniz. Boş bırakılması halinde bot güvenli simülasyon modunda çalışmaya devam eder.
              </p>

              <div>
                <label className="text-[10px] text-gray-400 font-bold block mb-1">Gemini API Key</label>
                <input 
                  type="password"
                  placeholder="AIzaSy..."
                  value={apiKey}
                  onChange={(e) => setApiKey(e.target.value)}
                  className="w-full bg-[#1b1f2c] border border-[#2d3345] rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-red-500 font-mono"
                />
              </div>

              <div className="pt-2 border-t border-[#232736] flex justify-between items-center text-xs text-gray-400">
                <span>Durum:</span>
                {apiKey ? (
                  <span className="text-emerald-400 font-bold flex items-center gap-1">
                    <CheckCircle2 className="w-3.5 h-3.5" /> API Anahtarı Aktif
                  </span>
                ) : (
                  <span className="text-amber-400 font-bold flex items-center gap-1">
                    <ShieldAlert className="w-3.5 h-3.5" /> Simülasyon Modu
                  </span>
                )}
              </div>
            </div>

            <div className="bg-[#141721] p-4 rounded-2xl border border-[#232736] space-y-2 text-xs text-gray-400">
              <h4 className="font-bold text-white flex items-center gap-1.5">
                <Flame className="w-4 h-4 text-red-500" /> Gx Bot Hakkında
              </h4>
              <p>Mobil öncelikli, Maçkolik ve Flashscore tasarımı ilham alınarak geliştirilmiş yapay zeka bahis ve kasa analiz uygulamasıdır.</p>
              <p className="text-[10px] text-gray-500 pt-1">Versiyon: 2.5.0-PRO (Süper Lig & EuroLeague Entegre)</p>
            </div>
          </div>
        )}

      </main>

      {/* --- BOTTOM NAVIGATION BAR (MOBILE-FIRST) --- */}
      <nav className="fixed bottom-0 left-0 right-0 z-40 bg-[#121520]/95 backdrop-blur-lg border-t border-[#232736] px-4 py-2">
        <div className="max-w-md mx-auto flex items-center justify-around">
          
          <button 
            onClick={() => setActiveTab('matches')}
            className={`flex flex-col items-center gap-1 transition ${activeTab === 'matches' ? 'text-red-500 font-bold' : 'text-gray-500 hover:text-gray-300'}`}
          >
            <Trophy className="w-5 h-5" />
            <span className="text-[10px]">Maçlar</span>
          </button>

          <button 
            onClick={() => setActiveTab('live_ai')}
            className={`flex flex-col items-center gap-1 transition ${activeTab === 'live_ai' ? 'text-red-500 font-bold' : 'text-gray-500 hover:text-gray-300'}`}
          >
            <Sparkles className="w-5 h-5 text-indigo-400" />
            <span className="text-[10px]">Canlı AI</span>
          </button>

          <button 
            onClick={() => setActiveTab('bankroll')}
            className={`flex flex-col items-center gap-1 transition ${activeTab === 'bankroll' ? 'text-red-500 font-bold' : 'text-gray-500 hover:text-gray-300'}`}
          >
            <DollarSign className="w-5 h-5 text-emerald-400" />
            <span className="text-[10px]">Kasa</span>
          </button>

          <button 
            onClick={() => setActiveTab('settings')}
            className={`flex flex-col items-center gap-1 transition ${activeTab === 'settings' ? 'text-red-500 font-bold' : 'text-gray-500 hover:text-gray-300'}`}
          >
            <Key className="w-5 h-5" />
            <span className="text-[10px]">API Ayarı</span>
          </button>

        </div>
      </nav>

    </div>
  );
}
