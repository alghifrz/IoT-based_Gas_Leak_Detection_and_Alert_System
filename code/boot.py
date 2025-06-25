from machine import Pin, ADC
import network
from time import sleep
import time
import gc
import web  # Import web module

# Konfigurasi WiFi dan Telegram
ssid = 'Tathering'
password = 'kandangjaya'
bot_token = '7544236703:AAF0H9yCuyiNKH5TNbWpCVSqOG6rQfRvfpw'
chat_id = '5312626621'

# DES encryption key (8 karakter)
DES_KEY = "Sliterin"

print("=== STARTING GAS DETECTOR DEBUG VERSION ===")

# Setup hardware pins
mq2_analog = ADC(Pin(34))
mq2_analog.atten(ADC.ATTN_11DB)
led = Pin(2, Pin.OUT)
buzzer = Pin(4, Pin.OUT)

# LCD pins
lcd_rs = Pin(19, Pin.OUT)
lcd_en = Pin(23, Pin.OUT)
lcd_d4 = Pin(18, Pin.OUT)
lcd_d5 = Pin(5, Pin.OUT)
lcd_d6 = Pin(12, Pin.OUT)
lcd_d7 = Pin(13, Pin.OUT)

# Global variables
gas_alert_log = []
gas_detected = False
ref_avg = 0
threshold = 0
current_analog_val = 0
web_server_enabled = False
server = None
telegram_alert_sent = False  # Flag untuk mencegah multiple alerts

# LCD class (sama seperti sebelumnya, tidak diubah)
class LCD:
    def __init__(self, rs, en, d4, d5, d6, d7):
        self.rs = rs
        self.en = en
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7
        for pin in [rs, en, d4, d5, d6, d7]:
            pin.off()
        sleep(0.1)
        self.init_lcd()

    def pulse_enable(self):
        self.en.on()
        sleep(0.001)
        self.en.off()
        sleep(0.001)

    def send_byte(self, byte, rs_mode):
        self.rs.value(rs_mode)
        self.d4.value((byte >> 4) & 1)
        self.d5.value((byte >> 5) & 1)
        self.d6.value((byte >> 6) & 1)
        self.d7.value((byte >> 7) & 1)
        self.pulse_enable()
        self.d4.value(byte & 1)
        self.d5.value((byte >> 1) & 1)
        self.d6.value((byte >> 2) & 1)
        self.d7.value((byte >> 3) & 1)
        self.pulse_enable()
        sleep(0.001)

    def init_lcd(self):
        sleep(0.05)
        self.send_byte(0x28, 0)
        sleep(0.005)
        self.send_byte(0x0C, 0)
        sleep(0.005)
        self.send_byte(0x06, 0)
        sleep(0.005)
        self.clear()

    def clear(self):
        self.send_byte(0x01, 0)
        sleep(0.002)

    def home(self):
        self.send_byte(0x02, 0)
        sleep(0.002)

    def set_cursor(self, row, col):
        addr = 0x80 if row == 0 else 0xC0
        addr += col
        self.send_byte(addr, 0)

    def write_string(self, string):
        for char in string:
            self.send_byte(ord(char), 1)

    def display_status(self, gas_detected, gas_level, threshold):
        self.clear()
        self.write_string("GAS DETECTED!" if gas_detected else "Status: NORMAL")
        self.set_cursor(1, 0)
        gas_str = f"Gas:{gas_level} T:{threshold}"
        self.write_string(gas_str)


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Menghubungkan ke WiFi...")
        wlan.connect(ssid, password)
        timeout = 20
        while not wlan.isconnected() and timeout > 0:
            sleep(1)
            timeout -= 1
            print(".", end="")
        if not wlan.isconnected():
            print("\n❌ GAGAL TERHUBUNG KE WIFI!")
            return None
    ip = wlan.ifconfig()[0]
    print(f"\n✅ WiFi terhubung: {ip}")
    return ip


def test_telegram_simple():
    try:
        import urequests
        url = f'https://api.telegram.org/bot{bot_token}/getMe'
        response = urequests.get(url, timeout=10)
        if response.status_code == 200:
            response.close()
            send_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            data = {'chat_id': chat_id, 'text': '=== Gas Leak Detector Active ==='}
            response = urequests.post(send_url, json=data, timeout=10)
            response.close()
            return response.status_code == 200
        else:
            response.close()
            return False
    except Exception as e:
        print(f"Telegram test failed: {e}")
        return False


def send_telegram_alert(gas_level, threshold, ref_avg):
    """Send simple gas detection alert to Telegram (no encryption, clean format)"""
    try:
        import urequests
        import gc
        gc.collect()  # Minimize RAM usage before HTTPS request
        send_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        message = (
            "Gas Leak Detected!\n"
            f"Gas Level: {int(gas_level)}\n"
            f"Threshold: {int(threshold)}\n"
            f"Reference: {int(ref_avg)}"
        )
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = urequests.post(send_url, json=data, timeout=10)
        if response.status_code == 200:
            print("Telegram alert sent successfully")
            response.close()
            return True
        else:
            print(f"Failed to send Telegram alert: {response.status_code}")
            response.close()
            return False
    except Exception as e:
        print(f"Error sending Telegram alert: {e}")
        return False


# === SETUP AWAL ===
print("🚀 Initializing...")
try:
    lcd = LCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7)
    lcd.display_status(False, 0, 0)
except Exception as e:
    print(f"LCD init failed: {e}")
    lcd = None

ip_address = connect_wifi()
if not ip_address:
    if lcd:
        lcd.clear()
        lcd.write_string("No WiFi")
        lcd.set_cursor(1, 0)
        lcd.write_string("Check connection")

telegram_ok = False
if ip_address:
    telegram_ok = test_telegram_simple()

if ip_address:
    server, web_server_enabled = web.setup_web_server()
    if web_server_enabled:
        print(f"🌐 Web aktif: http://{ip_address}")

print("Kalibrasi sensor...")
if lcd:
    lcd.clear()
    lcd.write_string("Calibrating...")
    lcd.set_cursor(1, 0)
    lcd.write_string("Please wait...")

ref_vals = []
for i in range(10):
    val = mq2_analog.read()
    ref_vals.append(val)
    print(f"Calibration {i+1}/10: {val}")
    if lcd:
        lcd.set_cursor(1, 0)
        lcd.write_string(f"Cal {i+1}/10: {val}   ")
    sleep(0.1)

ref_avg = sum(ref_vals) / len(ref_vals)
threshold = ref_avg + 500
print(f"✅ Kalibrasi selesai - Ref: {int(ref_avg)}, Threshold: {int(threshold)}")

if lcd:
    lcd.clear()
    lcd.write_string("Calibration done!")
    lcd.set_cursor(1, 0)
    lcd.write_string(f"T:{int(threshold)}")
    sleep(2)

# === MAIN LOOP ===
print("🔄 Starting main loop...")
last_print = 0
last_lcd_update = 0

try:
    while True:
        current_time = time.time()
        current_analog_val = mq2_analog.read()

        if current_analog_val > threshold:
            if not gas_detected:
                gas_detected = True
                led.on()  # LED nyala terus
                buzzer.on()  # Buzzer nyala terus
                log_entry = f"{web.get_timestamp()} - Gas: {int(current_analog_val)}"
                gas_alert_log.append(log_entry)
                print(f"🚨 GAS DETECTED! Level: {int(current_analog_val)}")
                if lcd:
                    lcd.display_status(True, int(current_analog_val), int(threshold))

        else:
            if gas_detected:
                gas_detected = False
                led.off()  # LED mati
                buzzer.off()  # Buzzer mati
                telegram_alert_sent = False  # Reset flag untuk alert berikutnya
                print("✅ Gas level normal")
                if lcd:
                    lcd.display_status(False, int(current_analog_val), int(threshold))

        if current_time - last_lcd_update > 2:
            if lcd:
                lcd.display_status(gas_detected, int(current_analog_val), int(threshold))
            last_lcd_update = current_time

        if current_time - last_print > 5:
            print(f"Status: {'ALERT' if gas_detected else 'NORMAL'} | Gas: {int(current_analog_val)} | Threshold: {int(threshold)}")
            last_print = current_time

        if web_server_enabled and server:
            try:
                client, addr = server.accept()
                print(f"Web client: {addr}")
                web.handle_web_request(client, gas_detected, current_analog_val, threshold, ref_avg, gas_alert_log)
            except OSError:
                pass
            except Exception as e:
                print(f"Web error: {e}")

        if gas_detected and not telegram_alert_sent:
            telegram_alert_sent = send_telegram_alert(current_analog_val, threshold, ref_avg)

        gc.collect()
        sleep(0.1)  # Delay normal

except KeyboardInterrupt:
    print("\n🛑 Stopped by user")
except Exception as e:
    print(f"❌ Main loop error: {e}")
finally:
    if server:
        server.close()
    led.off()
    buzzer.off()
    if lcd:
        lcd.clear()
        lcd.write_string("System stopped")
    print("System shutdown complete")



