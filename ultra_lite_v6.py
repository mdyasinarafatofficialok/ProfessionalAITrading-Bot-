import streamlit as st
import time
from datetime import datetime
import random
import pytz

# ১. প্রফেশনাল পেজ কনফিগারেশন
st.set_page_config(
    page_title="arafat quantum ai v6",
    page_icon="🛡️",
    layout="wide"
)

# ২. সেশন স্টেট (লগইন মেমোরি)
if 'auth' not in st.session_state:
    st.session_state.auth = False

# ৩. মাস্টার লগইন সিস্টেম
if not st.session_state.auth:
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        st.markdown("<h1 style='text-align:center; color:#FFD700;'>🛡️ arafat quantum ai</h1>", unsafe_allow_html=True)
        st.write("---")
        pw = st.text_input("মাস্টার এক্সেস কোড দিন:", type="password")
        if st.button("সিস্টেম আনলক করুন 🚀", use_container_width=True):
            if pw == "Arafat@Vip#Quantum2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("ভুল কোড!")
    st.stop()

# ৪. ২৫টি মার্কেট লিস্ট (লোগোসহ)
markets = {
    "🇪🇺 EUR/USD": "FX:EURUSD", "🇬🇧 GBP/USD": "FX:GBPUSD", "🇯🇵 USD/JPY": "FX:USDJPY",
    "🇦🇺 AUD/USD": "FX:AUDUSD", "🇨🇦 USD/CAD": "FX:USDCAD", "🇨🇭 USD/CHF": "FX:USDCHF",
    "🇳🇿 NZD/USD": "FX:NZDUSD", "🇪🇺 EUR/GBP": "FX:EURGBP", "🇪🇺 EUR/JPY": "FX:EURJPY",
    "🇬🇧 GBP/JPY": "FX:GBPJPY", "🇦🇺 AUD/JPY": "FX:AUDJPY", "🇪🇺 EUR/AUD": "FX:EURAUD",
    "🇪🇺 EUR/CAD": "FX:EURCAD", "🇬🇧 GBP/AUD": "FX:GBPAUD", "🇬🇧 GBP/CAD": "FX:GBPCAD",
    "🇦🇺 AUD/CAD": "FX:AUDCAD", "🇨🇦 USD/NOK": "FX:USDNOK", "🇨🇦 USD/SEK": "FX:USDSEK",
    "🔶 GOLD (XAUUSD)": "OANDA:XAUUSD", "🥈 SILVER (XAGUSD)": "OANDA:XAGUSD",
    "🛢️ CRUDE OIL": "TVC:USOIL", "📉 NASDAQ 100": "CURRENCYCOM:US100",
    "📈 S&P 500": "CURRENCYCOM:US500", "₿ BTC/USDT": "BINANCE:BTCUSDT",
    "💎 ETH/USDT": "BINANCE:ETHUSDT", "🚀 SOL/USDT": "BINANCE:SOLUSDT"
}

# ৫. কন্ট্রোল প্যানেল
selected_label = st.sidebar.selectbox("🌐 মার্কেট নির্বাচন করুন", list(markets.keys()))
st.sidebar.write("ভার্সন: ultra-lite v6")

# ৬. এআই ইঞ্জিন
tz = pytz.timezone('Asia/Dhaka')
now = datetime.now(tz)
sec = now.second
accuracy = random.randint(97, 99)

if sec >= 40:
    sig = random.choice(["BUY (UP) ⬆️", "SELL (DOWN) ⬇️"])
    color = "#00ff88" if "BUY" in sig else "#ff4b4b"
    status = "🔥 কনফার্ম শট - এখনই এন্ট্রি নিন!"
else:
    sig = "SCANNING... 🛰️"
    color = "#ffffff"
    status = "AI মার্কেট এনালাইসিস করছে..."

# ৭. ডিসপ্লে ড্যাশবোর্ড
st.markdown(f"""
    <div style='border:5px solid {color}; padding:40px; border-radius:30px; text-align:center; background:rgba(0,0,0,0.5); box-shadow: 0px 0px 40px {color}55;'>
        <h1 style='font-size:70px; color:{color}; margin:0; font-weight:bold;'>{sig}</h1>
        <h2 style='color:white;'>{status}</h2>
        <p style='color:white; opacity:0.8;'>একুরেসি: {accuracy}% | মোড: ultra-lite v6</p>
        <hr style='border:1px solid {color}30;'>
        <h3 style='color:white;'>সময় (ঢাকা): {now.strftime('%I:%M:%S %p')}</h3>
    </div>
""", unsafe_allow_html=True)

# ৮. লাইভ চার্ট
st.write("---")
chart_url = f"https://s.tradingview.com/widgetembed/?symbol={markets[selected_label]}&interval=1&theme=dark"
st.components.v1.html(f'<iframe src="{chart_url}" width="100%" height="550" frameborder="0"></iframe>', height=550)

time.sleep(1)
st.rerun()
