# 🚨 IoT-Based Gas Leak Detection and Alert System (ESP32 + MQ-2)

## 👥 Kelompok 16
- Alghifari Rasyid Zola (105222006)  
- Raihan Akira Rahmaputra (105222040)

---

## 📌 Deskripsi Singkat
Sistem ini merupakan alat pendeteksi kebocoran gas berbasis IoT yang menggunakan sensor MQ-2 yang terpasang pada ESP32 dengan pemrograman MicroPython. Ketika sensor mendeteksi gas berbahaya seperti LPG, metana, atau asap dalam jumlah berlebih, sistem akan mengaktifkan buzzer dan LED sebagai peringatan di lokasi.
Sistem ini juga dilengkapi dengan LCD 16x2 yang menampilkan informasi real-time seperti kadar gas yang terdeteksi, nilai ambang batas (threshold), serta kondisi sistem. Jika kadar gas berada di bawah ambang batas, LCD akan menampilkan tulisan "Kondisi Normal". Namun, jika terdeteksi kadar gas melebihi threshold, LCD akan menampilkan peringatan "Gas bocor terdeteksi".
Selain peringatan lokal, sistem juga mengirimkan notifikasi secara real-time ke akun Telegram pengguna, sehingga pengguna tetap mendapatkan peringatan jarak jauh meskipun tidak berada di lokasi.
Dengan kombinasi antara peringatan visual melalui LCD, audio-visual lokal dengan buzzer dan LED, serta notifikasi jarak jauh melalui Internet, sistem ini dirancang sebagai solusi deteksi dini yang efektif untuk mencegah kebakaran akibat kebocoran gas.

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
![Diagram Blok](gambar/sbd.png)
Sistem deteksi kebocoran gas ini mengikuti alur kerja yang terpadu dengan ESP32 sebagai pusat kendali utama. Proses dimulai ketika terjadi kebocoran gas di lingkungan. Gas yang bocor ini kemudian terdeteksi oleh sensor MQ-2, yang dirancang khusus untuk mengenali keberadaan gas-gas berbahaya seperti LPG, propana, hidrogen, dan gas mudah terbakar lainnya di udara.
Setelah mendeteksi adanya kebocoran gas, sensor MQ-2 mengirimkan data pengukuran ke mikrokontroler ESP32. ESP32 bertindak sebagai otak dari sistem ini, memproses data yang diterima dari sensor. Dalam ESP32 sudah terdapat pesan peringatan (alert message) yang telah didefinisikan sebelumnya, siap untuk dikirimkan ketika kondisi kebocoran gas terdeteksi.
Berdasarkan data dari sensor MQ-2, ESP32 kemudian mengeksekusi empat tindakan penting secara terkoordinasi:
Pertama, ESP32 mengaktifkan buzzer untuk memberikan peringatan audible yang dapat didengar di lokasi kejadian. Kedua, ESP32 juga mengaktifkan LED sebagai indikator visual untuk memberikan peringatan yang dapat dilihat. Ketiga, ESP32 mengirimkan pesan peringatan yang sudah tersedia langsung kepada pengguna melalui Telegram Bot, tanpa perlu membuat pesan baru. Ini memungkinkan notifikasi cepat dan pemantauan jarak jauh dari situasi berbahaya tersebut.
Keberadaan LED dalam sistem ini juga memiliki nilai tambah karena berkontribusi pada pencapaian Sustainable Development Goals (SDGs), khususnya dalam aspek peningkatan keamanan, pencegahan kecelakaan, dan pengembangan infrastruktur yang tangguh terhadap bencana terkait kebocoran gas.
Dengan arsitektur yang terpusat pada sensor MQ-2 untuk deteksi dan ESP32 untuk koordinasi respons, sistem ini memberikan mekanisme keamanan yang komprehensif, terintegrasi, dan responsif. ESP32 dapat langsung menggunakan template pesan yang sudah tersedia untuk komunikasi dengan pengguna melalui Telegram Bot, menghasilkan waktu respons yang lebih cepat dalam situasi darurat.

---
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


