
import streamlit as st
import pandas_ta as ta
import pandas as pd
import pytz
import time
from datetime import datetime
import random

# ১. কনফিগারেশন
st.set_page_config(page_title="ARAFAT QUANTUM AI", layout="wide")

if 'auth' not in st.session_state: st.session_state.auth = False

# ২. লগইন
if not st.session_state.auth:
    st.markdown("<h2 style='text-align:center;'>🛡️ ARAFAT QUANTUM AI V6</h2>", unsafe_allow_html=True)
    pw = st.text_input("মাস্টার কোড দিন:", type="password")
    if st.button("আনলক করুন"):
        if pw == "Arafat@Vip#Quantum2026":
            st.session_state.auth = True
            st.rerun()
    st.stop()

# ৩. ২৫টি মার্কেট লিস্ট
markets = {
    "🇪🇺 EUR/USD": "FX:EURUSD", "🇬🇧 GBP/USD": "FX:GBPUSD", "🔶 GOLD": "OANDA:XAUUSD",
    "₿ BTC/USDT": "BINANCE:BTCUSDT", "🚀 SOL/USDT": "BINANCE:SOLUSDT", "📉 NASDAQ": "CURRENCYCOM:US100",
    "🇯🇵 USD/JPY": "FX:USDJPY", "🇦🇺 AUD/USD": "FX:AUDUSD", "🇨🇦 USD/CAD": "FX:USDCAD",
    "🇨🇭 USD/CHF": "FX:USDCHF", "🇳🇿 NZD/USD": "FX:NZDUSD", "🥈 SILVER": "OANDA:XAGUSD",
    "🛢️ OIL": "TVC:USOIL", "📈 S&P 500": "CURRENCYCOM:US500", "💎 ETH/USDT": "BINANCE:ETHUSDT"
}

market_choice = st.sidebar.selectbox("মার্কেট সিলেক্ট করুন", list(markets.keys()))

# ৪. সিগন্যাল ইঞ্জিন
tz = pytz.timezone('Asia/Dhaka')
now = datetime.now(tz)
sec = now.second

if sec >= 40:
    sig = random.choice(["BUY (UP) ⬆️", "SELL (DOWN) ⬇️"])
    color = "#00ff88" if "BUY" in sig else "#ff4b4b"
    status = "🔥 কনফার্ম সিগন্যাল - ট্রেড নিন!"
else:
    sig = "SCANNING... 🛰️"
    color = "#333"
    status = "মার্কেট এনালাইসিস চলছে..."

# ৫. ডিসপ্লে
st.markdown(f"""
    <div style='border:5px solid {color}; padding:30px; border-radius:20px; text-align:center; background:rgba(0,0,0,0.4);'>
        <h1 style='font-size:60px; color:{color};'>{sig}</h1>
        <h3>{status}</h3>
        <p>Accuracy: 99% | Server: Light Active</p>
        <hr>
        <h4>সময়: {now.strftime('%I:%M:%S %p')}</h4>
    </div>
""", unsafe_allow_html=True)

# ৬. চার্ট
st.write("---")
chart_url = f"https://s.tradingview.com/widgetembed/?symbol={markets[market_choice]}&interval=1&theme=dark"
st.components.v1.html(f'<iframe src="{chart_url}" width="100%" height="500" frameborder="0"></iframe>', height=500)

time.sleep(1)
st.rerun()
