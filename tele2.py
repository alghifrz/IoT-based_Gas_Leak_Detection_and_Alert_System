import network
import urequests
from time import sleep

# WiFi Configuration
ssid = 'Tathering'
password = 'kandangjaya'

# Telegram Bot Configuration
bot_token = '7544236703:AAF0H9yCuyiNKH5TNbWpCVSqOG6rQfRvfpw'
chat_id = '5372620879'

# Koneksi ke WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Menghubungkan ke WiFi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            sleep(1)
    print("Terhubung ke WiFi:", wlan.ifconfig())

# Kirim pesan ke Telegram
# Kirim pesan ke Telegram
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = f'chat_id={chat_id}&text={message}'
    
    try:
        response = urequests.post(url, data=payload, headers=headers)
        print("Status code:", response.status_code)
        print("Response text:", response.text)
        response.close()
        print("Pesan terkirim!")
    except Exception as e:
        print("Gagal mengirim:", e)


# Eksekusi
connect_wifi()
send_telegram_message("✅ Bot aktif! Ini pesan uji coba dari ESP32 via MicroPython.")
sleep(5)
send_telegram_message("test 1")
sleep(5)
send_telegram_message("test 2")
sleep(5)
send_telegram_message("test 3")
sleep(5)
send_telegram_message("test 1")

