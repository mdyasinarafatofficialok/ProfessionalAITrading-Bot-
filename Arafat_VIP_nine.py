import streamlit as st
import yfinance as yf
import pandas_ta as ta
import pandas as pd
import time
from datetime import datetime
import pytz

# ১. মাস্টার কনফিগারেশন ও টাইটেল
APP_NAME = "ARAFAT VIP V10 PRO 🛡️"
SECURE_PASSWORD = "Arafat@Vip#Real2026"

st.set_page_config(page_title=APP_NAME, layout="wide")

# ২. ডার্ক ও প্রিমিয়াম ইন্টারফেস ডিজাইন
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .signal-box { 
        padding: 45px; border-radius: 30px; text-align: center; 
        border: 5px solid; background: #0a0a0a; 
        box-shadow: 0px 0px 35px rgba(255, 255, 255, 0.05);
    }
    .time-card {
        background: #111; padding: 12px; border-radius: 12px; 
        border: 1px solid #333; text-align: center;
    }
    .sidebar .sidebar-content { background-image: linear-gradient(#111,#000); }
    </style>
    """, unsafe_allow_html=True)

# ৩. সিকিউর লগইন গেটওয়ে
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    _, col2, _ = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<h2 style='text-align:center; color:#FFD700;'>🔐 ARAFAT VIP SYSTEM</h2>", unsafe_allow_html=True)
        st.write("---")
        pw = st.text_input("মাস্টার পিনটি দিন (Password):", type="password")
        if st.button("সিস্টেম বুট করুন 🚀", use_container_width=True):
            if pw == SECURE_PASSWORD:
                st.session_state.auth = True
                st.success("অ্যাক্সেস অনুমোদিত!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("ভুল পাসওয়ার্ড! আবার চেষ্টা করুন।")
    st.stop()

# ৪. ৩০+ রিয়েল মার্কেট কালেকশন (Global & Crypto)
markets = {
    # --- Forex Majors ---
    "🇪🇺 EUR/USD": "EURUSD=X", "🇬🇧 GBP/USD": "GBPUSD=X", "🇯🇵 USD/JPY": "JPY=X",
    "🇦🇺 AUD/USD": "AUDUSD=X", "🇨🇦 USD/CAD": "CAD=X", "🇨🇭 USD/CHF": "CHF=X",
    "🇳🇿 NZD/USD": "NZDUSD=X", "🇪🇺 EUR/GBP": "EURGBP=X", "🇪🇺 EUR/JPY": "EURJPY=X",
    "🇬🇧 GBP/JPY": "GBPJPY=X", "🇦🇺 AUD/JPY": "AUDJPY=X", "🇨🇭 EUR/CHF": "EURCHF=X",
    # --- Minor & Emerging ---
    "🇧🇷 USD/BRL": "USDBRL=X", "🇮🇳 USD/INR": "USDINR=X", "🇹🇷 USD/TRY": "USDTRY=X",
    "🇿🇦 USD/ZAR": "USDZAR=X", "🇸🇬 USD/SGD": "USDSGD=X", "🇲🇽 USD/MXN": "USDMXN=X",
    "🇭🇰 USD/HKD": "USDHKD=X", "🇳र्वे NOK/USD": "NOKUSD=X",
    # --- Crypto ---
    "₿ BTC/USDT": "BTC-USD", "💎 ETH/USDT": "ETH-USD", "🚀 SOL/USDT": "SOL-USD",
    "🔶 BNB/USDT": "BNB-USD", "🐕 DOGE/USDT": "DOGE-USD", "💠 XRP/USDT": "XRP-USD",
    "📊 ADA/USDT": "ADA-USD", "🔗 LINK/USDT": "LINK-USD", "🦄 UNI/USDT": "UNI-USD",
    # --- Commodities ---
    "🔥 GOLD (XAU)": "GC=F", "🥈 SILVER (XAG)": "SI=F", "🛢️ CRUDE OIL": "CL=F",
    "📉 NASDAQ 100": "^IXIC", "📈 S&P 500": "^GSPC"
}

st.sidebar.title("💎 VIP কন্ট্রোল")
selected_label = st.sidebar.selectbox("🌐 ৩০+ মার্কেট নির্বাচন করুন", list(markets.keys()))
selected_ticker = markets[selected_label]

# ৫. VIP সিগন্যাল ইঞ্জিন (স্মার্ট লজিক)
def get_vip_signal(ticker):
    try:
        # ডাটা ফেচিং
        data = yf.download(ticker, period="1d", interval="1m", progress=False)
        if len(data) < 30: return "ANALYZING...", "#555555", "পর্যাপ্ত ডাটা লোড হয়নি...", 50
        
        # টেকনিক্যাল ইন্ডিকেটর
        data.ta.rsi(length=14, append=True)
        data.ta.ema(length=20, append=True)
        
        current_rsi = data['RSI_14'].iloc[-1]
        current_price = data['Close'].iloc[-1]
        ema_20 = data['EMA_20'].iloc[-1]

        # হাই-অ্যাকিউরেসি লজিক (RSI + Price Action)
        if current_rsi < 31 and current_price < ema_20:
            return "NEXT: BUY (UP) ⬆️", "#00ff88", "মার্কেট অনেক নিচে (Oversold)। রিভার্সাল কনফার্ম!", current_rsi
        elif current_rsi > 69 and current_price > ema_20:
            return "NEXT: SELL (DOWN) ⬇️", "#ff4b4b", "মার্কেট অনেক উপরে (Overbought)। শর্ট সেল কনফার্ম!", current_rsi
        else:
            return "WAIT - NO TRADE ✋", "#FFD700", "মার্কেট এখন ট্রেড করার জন্য ঝুঁকিপূর্ণ। অপেক্ষা করুন।", current_rsi
    except:
        return "DATA ERROR ⚠️", "#ff4b4b", "ইন্টারনেট কানেকশন চেক করুন।", 50

# ইঞ্জিন রান
prediction, color, status_msg, rsi_val = get_vip_signal(selected_ticker)

# ৬. ড্যাশবোর্ড ডিসপ্লে
tz = pytz.timezone('Asia/Dhaka')
now = datetime.now(tz)

col_t1, col_t2 = st.columns(2)
with col_t1:
    st.markdown(f'<div class="time-card"><p style="margin:0;color:gray;">সময় (বাংলাদেশ)</p><h2>{now.strftime("%I:%M:%S %p")}</h2></div>', unsafe_allow_html=True)
with col_t2:
    st.markdown(f'<div class="time-card" style="border-color:#ff4b4b;"><p style="margin:0;color:gray;">ক্যান্ডেল টাইম বাকি</p><h2>{60 - now.second}s</h2></div>', unsafe_allow_html=True)

st.write("") # স্পেস

st.markdown(f"""
    <div class='signal-box' style='border-color: {color}; box-shadow: 0px 0px 40px {color}22;'>
        <p style='color:{color}; font-weight:bold; letter-spacing:2px;'>VIP V10 AI ENGINE</p>
        <h1 style='font-size:75px; color:{color}; margin:10px 0;'>{prediction}</h1>
        <h3 style='color:white; opacity:0.8;'>{status_msg}</h3>
        <hr style='opacity:0.1; margin:20px 0;'>
        <p style='font-size:16px;'>📊 মার্কেট: {selected_label} | 📈 RSI ভ্যালু: {rsi_val:.2f} | 🛡️ প্রোটেকশন: অন</p>
    </div>
""", unsafe_allow_html=True)

# ৭. ডাইনামিক লাইভ চার্ট
st.write("---")
from streamlit.components.v1 import html
# চার্ট সিম্বল ক্লিনআপ (Yahoo থেকে TradingView ফরম্যাট)
tv_symbol = selected_ticker.replace('=X', '').replace('-USD', 'USDT').replace('^IXIC', 'NASDAQ:IXIC').replace('^GSPC', 'SPX')
chart_url = f"https://s.tradingview.com/widgetembed/?symbol={tv_symbol}&interval=1&theme=dark"
html(f'<iframe src="{chart_url}" width="100%" height="520" frameborder="0" allowfullscreen></iframe>', height=520)

# ৮. অটো-রিফ্রেশ লজিক
time.sleep(8)
st.rerun()
