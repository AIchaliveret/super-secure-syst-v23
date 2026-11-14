# UPDATE WAJIB - Super Secure Syst v23

## MODE: HYBRID - 1 LIVE + 5 CALIBRATED SIMULATION
Engineering decision karena keterbatasan hardware di hackathon.
Bukan bohong, ini jujur di dashboard + di kode.

## Arsitektur
[ESP32] -> 1 Sensor Real (DHT22 SHT31 / MQ-135)
        -> 5 Sensor Virtual (model kalibrasi)

1. Makanan - Kesegaran (NIR simulasi)
2. Makanan - Kematangan (NIR simulasi)
3. Ruangan - Bio Aerosol / Partikel (simulasi)
4. Ruangan - Cahaya / Infrared (simulasi)
5. Bio - Detak / Suhu Tubuh (simulasi pola)

## File Baru
- esp32_hybrid.ino = kode ESP32 + DEMO_MODE + Watchdog + Fallback
- api_connector.py = game Tron baca data sensor
- game_config.json = config Tron

## Cara Demo Aman
1. Set DEMO_MODE true
2. Upload ke ESP32
3. Buka Serial Monitor, cek MODE: SIMULASI
4. Buka dashboard, cek angka naik-turun halus
5. Rekam video 90 detik SEKARANG sebagai cadangan
