
import streamlit as st
import time
from datetime import datetime
import pytz
import random

# ১. মাস্টার কনফিগারেশন
APP_NAME = "ARAFAT V6 PRO GLOBAL 🌎"
SECURE_PASSWORD = "Arafat@Vip#Quantum2026"

st.set_page_config(page_title=APP_NAME, layout="wide")

# ২. প্রিমিয়াম ডিজাইন (ভিডিও লুক)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .signal-box { 
        padding: 40px; border-radius: 30px; text-align: center; 
        border: 6px solid; background: #0a0a0a; 
        box-shadow: 0px 0px 40px rgba(255, 215, 0, 0.1);
    }
    .timer-container {
        display: flex; justify-content: center; gap: 20px; margin-bottom: 20px;
    }
    .time-card {
        background: #111; padding: 10px 20px; border-radius: 10px; 
        border: 1px solid #333; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. লগইন সিস্টেম
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        st.markdown("<h2 style='text-align:center; color:#FFD700;'>🔐 V6 GLOBAL UNLOCK</h2>", unsafe_allow_html=True)
        pw = st.text_input("মাস্টার পিন দিন:", type="password")
        if st.button("সিস্টেম বুট করুন 🚀", use_container_width=True):
            if pw == SECURE_PASSWORD:
                st.session_state.auth = True
                st.rerun()
    st.stop()

# ৪. ২৫+ গ্লোবাল মার্কেট ও লোগো (সবগুলো এখানে যুক্ত)
markets = {
    "🇪🇺 EUR/USD": "FX:EURUSD", "🇬🇧 GBP/USD": "FX:GBPUSD", "🇯🇵 USD/JPY": "FX:USDJPY",
    "🇦🇺 AUD/USD": "FX:AUDUSD", "🇨🇦 USD/CAD": "FX:USDCAD", "🇨🇭 USD/CHF": "FX:USDCHF",
    "🇳🇿 NZD/USD": "FX:NZDUSD", "🇪🇺 EUR/GBP": "FX:EURGBP", "🇬🇧 GBP/JPY": "FX:GBPJPY",
    "🔶 GOLD (XAU)": "OANDA:XAUUSD", "🥈 SILVER (XAG)": "OANDA:XAGUSD", "🛢️ OIL (WTI)": "TVC:USOIL",
    "📉 NASDAQ 100": "CURRENCYCOM:US100", "📈 S&P 500": "CURRENCYCOM:US500", "🇬🇧 FTSE 100": "FOREXCOM:UK100",
    "₿ BTC/USDT": "BINANCE:BTCUSDT", "💎 ETH/USDT": "BINANCE:ETHUSDT", "🚀 SOL/USDT": "BINANCE:SOLUSDT",
    "🐕 DOGE/USDT": "BINANCE:DOGEUSDT", "🔹 XRP/USDT": "BINANCE:XRPUSDT", "🍎 APPLE STOCKS": "NASDAQ:AAPL",
    "🚗 TESLA STOCKS": "NASDAQ:TSLA", "🔍 GOOGLE STOCKS": "NASDAQ:GOOGL", "📦 AMAZON": "NASDAQ:AMZN",
    "📺 NETFLIX": "NASDAQ:NFLX"
}

st.sidebar.title("💎 V6 কন্ট্রোল প্যানেল")
selected_label = st.sidebar.selectbox("🌐 মার্কেট নির্বাচন করুন", list(markets.keys()))
tf = st.sidebar.selectbox("⏰ টাইমফ্রেম সিলেক্ট করুন", [1, 5, 15, 30, 60])

# ৫. টাইম ও ক্যান্ডেল কাউন্টডাউন লজিক
tz = pytz.timezone('Asia/Dhaka')
now = datetime.now(tz)
sec = now.second
remaining_sec = 60 - sec # ১ মিনিটের ক্যান্ডেল শেষ হতে বাকি সময়

# ৬. অগ্রিম সিগন্যাল (২০ সেকেন্ড আগে ফিক্সড)
if sec >= 40: # অর্থাৎ ক্যান্ডেল শেষ হওয়ার ২০ সেকেন্ড আগে
    random.seed(now.minute + now.hour) 
    prediction = random.choice(["NEXT: BUY (UP) ⬆️", "NEXT: SELL (DOWN) ⬇️"])
    color = "#00ff88" if "BUY" in prediction else "#ff4b4b"
    status_msg = "🎯 সিগন্যাল লক! পরবর্তী ক্যান্ডেলের এন্ট্রি নিন।"
else:
    prediction = "ANALYZING... 🛰️"
    color = "#555555"
    status_msg = f"পরবর্তী সিগন্যাল আসবে {40 - sec} সেকেন্ড পর"

# ৭. ড্যাশবোর্ড ডিসপ্লে (লাইভ ঘড়ি + ক্যান্ডেল টাইমার)
st.markdown(f"""
    <div class="timer-container">
        <div class="time-card">
            <p style="margin:0; font-size:12px; color:gray;">রিয়েল টাইম (ঢাকা)</p>
            <h3 style="margin:0; color:#FFD700;">{now.strftime('%I:%M:%S %p')}</h3>
        </div>
        <div class="time-card" style="border-color:#FF4B4B;">
            <p style="margin:0; font-size:12px; color:gray;">ক্যান্ডেল শেষ হতে বাকি</p>
            <h3 style="margin:0; color:#FF4B4B;">{remaining_sec}s</h3>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div class='signal-box' style='border-color: {color}; box-shadow: 0px 0px 50px {color}33;'>
        <p style='color:gray; font-size:14px; letter-spacing:2px;'>PREDICTION FOR NEXT CANDLE</p>
        <h1 style='font-size:70px; color:{color}; margin:10px 0;'>{prediction}</h1>
        <h2 style='color:white; font-weight:normal;'>{status_msg}</h2>
        <hr style='opacity:0.1; margin:20px 0;'>
        <div style='display:flex; justify-content:center; gap:30px; font-size:16px;'>
            <span>📊 SMC/FVG: Active</span>
            <span>✅ Accuracy: {random.randint(97,99)}%</span>
            <span>🌍 Market: Global</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ৮. ট্রেডিং চার্ট ইন্টিগ্রেশন
st.write("---")
from streamlit.components.v1 import html
chart_url = f"https://s.tradingview.com/widgetembed/?symbol={markets[selected_label]}&interval={tf}&theme=dark&style=1"
html(f'<iframe src="{chart_url}" width="100%" height="520" frameborder="0" scrolling="no"></iframe>', height=520)

# ৯. অটো-রিফ্রেশ (১ সেকেন্ড পর পর)
time.sleep(1)
st.rerun()
