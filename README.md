# 🚨 IoT-Based Gas Leak Detection and Alert System (ESP32 + MQ-2)

## 👥 Kelompok 16
- Alghifari Rasyid Zola (105222006)  
- Raihan Akira Rahmaputra (105222040)

---

## 📌 Deskripsi Singkat
Sistem ini merupakan alat pendeteksi kebocoran gas berbasis IoT yang menggunakan sensor MQ-2 yang terpasang pada ESP32 dengan pemrograman MicroPython. Ketika sensor mendeteksi gas berbahaya seperti LPG, metana, atau asap dalam jumlah berlebih, sistem akan mengaktifkan buzzer dan LED sebagai peringatan di lokasi.
Sistem ini juga dilengkapi dengan LCD 16x2 yang menampilkan informasi real-time seperti kadar gas yang terdeteksi, nilai ambang batas (threshold), serta kondisi sistem. Jika kadar gas berada di bawah ambang batas, LCD akan menampilkan tulisan "Kondisi Normal". Namun, jika terdeteksi kadar gas melebihi threshold, LCD akan menampilkan peringatan "Gas bocor terdeteksi".
Selain peringatan lokal, sistem juga mengirimkan notifikasi secara real-time ke akun Telegram pengguna, sehingga pengguna tetap mendapatkan peringatan jarak jauh meskipun tidak berada di lokasi.
Sebagai fitur tambahan, sistem ini juga dilengkapi dengan web server sederhana yang dijalankan oleh ESP32. Web server ini dapat diakses melalui alamat IP lokal perangkat ketika terhubung ke jaringan WiFi yang sama. Melalui web interface ini, pengguna dapat memantau data sensor secara real-time menggunakan browser, sehingga memberikan alternatif pemantauan tambahan tanpa perlu berada di depan perangkat secara langsung.
Dengan kombinasi antara peringatan visual melalui LCD, audio-visual lokal dengan buzzer dan LED, notifikasi jarak jauh melalui Internet, serta pemantauan real-time melalui web server lokal, sistem ini dirancang sebagai solusi deteksi dini yang efektif untuk mencegah kebakaran akibat kebocoran gas.

---

## 🎯 Tujuan
- Mendeteksi kebocoran gas secara real-time dengan sensor MQ-2.
- Memberikan peringatan lokal melalui LED dan buzzer.
- Memberikan peringatan visual melalui LCD.
- Mengirim alert message ke Telegram sebagai pengingat jarak jauh.
- Meningkatkan keselamatan rumah tangga/tempat usaha dari risiko kebakaran gas.
- Mendukung penerapan IoT untuk menciptakan lingkungan yang aman dan berkelanjutan.

---

## 🌍 Target SDGs
**SDG 11 – Sustainable Cities and Communities**  
Proyek ini mendukung SDG 11 dengan meningkatkan keamanan lingkungan dari risiko kebocoran gas, menciptakan kota yang lebih aman, tangguh, dan berkelanjutan.

---

## 📦 Daftar Komponen

| No | Komponen                | Gambar                                                                 | Fungsi                                                                 |
|----|-------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| 1  | ESP32                   | ![ESP32](gambar/1.jpg) | Mikrokontroler utama, koneksi WiFi, kontrol sensor & aktuator         |
| 2  | Sensor Gas MQ-2         | ![MQ-2](gambar/2.jpg) | Deteksi gas LPG, metana, asap, dan hidrogen                           |
| 3  | LED                     | ![LED](gambar/3.jpg) | Indikator visual saat gas terdeteksi                                  |
| 4  | Buzzer                  | ![Buzzer](gambar/4.jpg) | Alarm suara sebagai peringatan lokal                                  |
| 5  | Breadboard              | ![Breadboard](gambar/5.jpg) | Media penyambung komponen sementara                                   |
| 6  | Kabel Jumper            | ![Jumper Wire](gambar/6.jpg) | Penghubung antar komponen                                              |
| 7  | Resistor (220–330Ω)     | ![Resistor](gambar/7.jpg) | Pembatas arus ke LED                                                  |
| 8  | LCD Display             | ![LCD](gambar/lcd.jpg) | Menampilkan informasi pada LCD                                        |
| 9  | Kabel Micro USB         | ![USB Cable](gambar/8.jpg) | Koneksi ESP32 ke komputer/laptop                                      |
| 10  | Koneksi WiFi           | ![WiFi](gambar/9.png) | Untuk mengirim pesan ke Telegram                                       |
| 11 | Telegram + Bot API      | ![Telegram](https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg) | Menerima alert melalui bot Telegram                                   |

---

## 📷 Diagram Blok Sistem
![Diagram Blok](gambar/sbd_new.png)
Sistem deteksi kebocoran gas ini mengikuti alur kerja yang terpadu dengan ESP32 sebagai pusat kendali utama yang pada tahap development dan testing prototype ini mendapat catu daya melalui koneksi USB dari laptop untuk menjamin operasional seluruh komponen. Proses dimulai ketika terjadi kebocoran gas di lingkungan. Gas yang bocor ini kemudian terdeteksi oleh sensor MQ-2, yang dirancang khusus untuk mengenali keberadaan gas-gas berbahaya seperti LPG, propana, hidrogen, dan gas mudah terbakar lainnya di udara. Setelah mendeteksi adanya kebocoran gas, sensor MQ-2 mengirimkan data analog pengukuran ke mikrokontroler ESP32.
ESP32 bertindak sebagai otak dari sistem ini, memproses data yang diterima dari sensor dan secara simultan menampilkan status sistem melalui LCD Display 16x2 yang memberikan informasi real-time kepada pengguna di lokasi. Berdasarkan data dari sensor MQ-2, ESP32 kemudian mengeksekusi empat tindakan penting secara terkoordinasi: Pertama, ESP32 memperbarui tampilan status pada LCD Display untuk memberikan informasi visual lokal. Kedua, ESP32 mengaktifkan buzzer untuk memberikan peringatan audible yang dapat didengar di lokasi kejadian. Ketiga, ESP32 mengaktifkan LED sebagai indikator visual untuk memberikan peringatan yang dapat dilihat. Keempat, melalui WiFi Module yang terintegrasi, ESP32 terhubung ke internet dan mengirimkan pesan peringatan kepada pengguna melalui Telegram API, memungkinkan notifikasi cepat dan pemantauan jarak jauh dari situasi berbahaya tersebut.
Sebagai fitur tambahan, ESP32 juga menjalankan web server sederhana yang dapat diakses melalui IP address perangkat di jaringan WiFi lokal, menampilkan data sensor terkini secara real-time untuk monitoring tambahan melalui browser web. Keberadaan komponen-komponen dalam sistem ini memiliki nilai tambah karena berkontribusi pada pencapaian Sustainable Development Goals (SDGs), khususnya dalam aspek peningkatan keamanan, pencegahan kecelakaan, dan pengembangan infrastruktur yang tangguh terhadap bencana terkait kebocoran gas. Dengan arsitektur yang terpusat pada sensor MQ-2 untuk deteksi, ESP32 untuk koordinasi respons dan web server lokal, serta LCD untuk display lokal, sistem ini memberikan mekanisme keamanan yang komprehensif, terintegrasi, dan responsif dengan multiple interface monitoring baik melalui display fisik maupun web interface lokal.

---


## Implementasi Hardware dan Software
### Hardware
![Implementasi Hardware dan Software](gambar/hardware.jpg)
### Software
![Implementasi Hardware dan Software](gambar/web1.jpg)
![Implementasi Hardware dan Software](gambar/web2.jpg)

## Flowchart
![Flowchart](gambar/flowchart.jpeg)

---

## 🛠️ Teknologi
- ESP32 dengan MicroPython
- Sensor MQ-2
- Telegram Bot API
- Buzzer + LED
- LCD
- Breadboard prototyping

---


## 📄 Lisensi
Proyek ini dibuat untuk keperluan akademik. Silakan gunakan, ubah, dan distribusikan dengan menyertakan kredit kepada pembuat asli.

---

## Fitur Utama

- **Sensor MQ2**: Deteksi gas berbahaya (LPG, CO, asap, dll)
- **LCD Display**: Tampilan real-time status dan nilai sensor
- **LED & Buzzer**: Indikator visual dan audio saat gas terdeteksi
- **Web Interface**: Dashboard web untuk monitoring
- **Telegram Bot**: Notifikasi otomatis ke Telegram
- **Enkripsi DES**: Keamanan data sensor menggunakan DES encryption

## Implementasi Enkripsi DES

### Masalah Sebelumnya
- Template HTML terlalu panjang (>8 karakter) untuk DES
- Logs HTML bisa sangat panjang
- Enkripsi yang tidak perlu pada variabel statis

### Solusi yang Diterapkan

#### 1. Fungsi Helper Enkripsi
```python
def encrypt_sensor_data(value, key):
    """Enkripsi data sensor menggunakan DES"""
    value_str = pad_to_8_chars(value)
    encrypted = crypto.des_encrypt(value_str, key)
    return bytes_to_hex(encrypted)

def decrypt_sensor_data(hex_data, key):
    """Dekripsi data sensor dari format hex"""
    encrypted_bytes = bytes.fromhex(hex_data)
    decrypted = crypto.des_decrypt(encrypted_bytes, key)
    return decrypted.strip()
```

#### 2. Padding 8 Karakter
```python
def pad_to_8_chars(text):
    """Pad atau truncate text ke tepat 8 karakter untuk DES"""
    text_str = str(text)
    if len(text_str) >= 8:
        return text_str[:8]  # Truncate jika terlalu panjang
    else:
        return text_str + " " * (8 - len(text_str))  # Pad dengan spasi
```

#### 3. Enkripsi Selektif
- **Yang dienkripsi**: Hanya nilai sensor yang penting (level gas)
- **Yang tidak dienkripsi**: Template HTML, logs, status text, dll
- **Format output**: Hexadecimal untuk kemudahan transmisi

### Contoh Penggunaan

```python
# Enkripsi nilai sensor
gas_level = 1234
encrypted_level = encrypt_sensor_data(gas_level, key)
print(f"Terenkripsi: {encrypted_level}")

# Dekripsi nilai sensor
decrypted_level = decrypt_sensor_data(encrypted_level, key)
print(f"Terdekripsi: {decrypted_level}")
```

### Keuntungan Implementasi Baru

1. **Efisien**: Hanya mengenkripsi data yang benar-benar perlu
2. **Kompatibel**: Mengikuti batasan 8 karakter DES
3. **Handal**: Error handling untuk enkripsi/dekripsi
4. **Praktis**: Format hex untuk kemudahan transmisi
5. **Demo**: Fungsi demo untuk testing

## Hardware Requirements

- ESP32 Development Board
- MQ2 Gas Sensor
- LCD 16x2 dengan interface 4-bit
- LED dan Buzzer
- Kabel jumper

## Pin Configuration

```python
# Sensor MQ2
mq2_analog = ADC(Pin(34))  # Analog pin
mq2_digital = Pin(27, Pin.IN)  # Digital pin

# Output devices
led = Pin(2, Pin.OUT)
buzzer = Pin(4, Pin.OUT)

# LCD pins
lcd_rs = Pin(19, Pin.OUT)
lcd_en = Pin(23, Pin.OUT)
lcd_d4 = Pin(18, Pin.OUT)
lcd_d5 = Pin(5, Pin.OUT)
lcd_d6 = Pin(12, Pin.OUT)
lcd_d7 = Pin(13, Pin.OUT)
```

## Konfigurasi

1. **WiFi**: Update `ssid` dan `password`
2. **Telegram**: Update `bot_token` dan `chat_id`
3. **Enkripsi**: Update `key` untuk DES encryption

## Cara Kerja

1. **Startup**: Kalibrasi sensor selama 30 detik
2. **Monitoring**: Baca sensor setiap 200ms
3. **Alert**: Jika nilai > threshold, aktifkan alarm
4. **Notifikasi**: Kirim pesan Telegram dengan data terenkripsi
5. **Web**: Dashboard real-time di port 80

## Troubleshooting

Lihat file `TROUBLESHOOTING_TELEGRAM.md` untuk masalah umum dengan Telegram bot.

## Keamanan

- Data sensor dienkripsi menggunakan DES
- Key enkripsi dapat dikustomisasi
- Format hex untuk transmisi yang aman
- Error handling untuk mencegah crash


