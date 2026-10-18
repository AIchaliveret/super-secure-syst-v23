SUPER SECURE SYST v3.0 - AMD ACT III - THE BEST F-21 HMDS Uparrow
🛡️ SUPER SECURE SPACE GUARDIAN - SIMULATOR TEORI UNTUK JUDGING DIGITHOOK
⚠️ INI SIMULATOR TEORI 01-02-03 BUAT JUDGING PAK - YANG AKTUAL ROBOTIK NDIR 4 PLUS THERMAL PLUS CCTV LAGI KITA RAKIT DI RUANG TEDUH - POWER WAJIB KABEL DATA WIFI/KABEL LAN ESP32 OTAK PLUS KONEKSI INCLUDE

KENAPA DI RUANG TEDUH, NGGAK DI README SUPER SECURE KITA AJA DI GITHUB?
Karena 2 tempat ini beda fungsi sis, biar juri dan sponsor gak salah paham:

1. GITHUB super-secure-syst-v23.streamlit.app INI = SIMULATOR TEORI UNTUK JURI (DIGITHOOK)

Isinya: HMDS-35 85% TRANSP, Fused Thermal+RGB, HUD 612°C White Hot - DATA SIMULASI UI
Fungsinya: Buat belajar teori 01 THEORY, 02 OBSERVATION 30s DETECT / 270s STANDBY, 03 OPINION AI
Data gas CO2 852ppm, HC %LEL di dashboard ini adalah SIMULASI UNTUK DEMO CARA KERJA DASHBOARD, BUKAN DATA SENSOR NDIR AKTUAL
Aman hukum, tidak klaim bisa cium BBM/LPG/Ethanol 45°C beneran
2. RUANG TEDUH = LAB AKTUAL ROBOTIK (OFFLINE, BUKAN DI GITHUB)

Isinya: ESP32-S3 + NDIR 4 Channel BENERAN (3.33um BBM/LPG/Ethanol, 4.26um CO2, 4.64um CO, 3.91um Ref) + SHT41 + KE-25 O2 + MLX90640 Thermal 32x24 + IMX219 CCTV + Pompa 350mL
Fungsinya: Uji coba beneran 24 jam nonstop, baca voltase asli, kalibrasi ethanol 45°C, test LPG bocor
Kenapa di ruang teduh? Karena butuh listrik kabel terus, butuh gas beneran buat test, butuh 90 hari log - gak bisa di cloud
Ini yang nanti dipasang di Mall, Plaza, Bioskop, Gedung DPR, Polri/TNI - POWER WAJIB KABEL, DATA BISA WIFI/KABEL LAN (ESP32 OTAK + KONEKSI INCLUDE DI DALAM CHIP)
Jadi kalau juri tanya: "Ini alatnya mana?" Jawab: "Yang di GitHub ini simulator teorinya Pak, yang aktualnya lagi dirakit di ruang teduh lab kami."

ARSITEKTUR AKTUAL (RUANG TEDUH)
HIDUNG ASLI NDIR 4 (butuh kabel power 12V)
   ↓
OTAK + KONEKSI ROBOT ESP32-S3 (WiFi include di chip, tapi power tetap kabel - lebih stabil)
   ↓
MATA Thermal Spectral MLX90640 + CCTV IMX219 (power kabel, data WiFi atau kabel LAN)
   ↓
MONITOR APP AKTUAL ROBOTIK PY (di laptop/Raspberry Pi di ruang teduh - baca Serial COM3/MQTT, BUKAN random)
Sekarang jamannya WiFi serba wireless nirkabel, CCTV saja terhubung hanya dengan WiFi walau mesti ada kelistrikan yang terus memberi power. Betul, tapi untuk enterprise mall/plaza/DPR, kabel LAN lebih efektif karena WiFi bisa putus - alarm gak jalan. Makanya kita pakai kabel untuk koneksitasnya juga.
DEPLOY
Untuk Juri: app.py (simulator teori) -> Streamlit Cloud super-secure-syst-v23.streamlit.app
Untuk Lab Aktual: esp32_ndir_actual.ino + app_aktual_robotik.py -> ESP32 di ruang teduh + laptop lokal
TEAM
Mister Ali Ang, Mister Sandy, Mister Budi, Even Garden - Ruang Teduh Jakarta

STATUS
✅ FINAL JURI DIGITHOOK - 01 THEORY 02 OBSERVATION 03 OPINION - SIMULATOR AMAN HUKUM
🔧 AKTUAL ROBOTIK DALAM PENGEMBANGAN 90 HARI DI RUANG TEDUH

Catatan Hukum: Repo ini tidak mengklaim sebagai alat deteksi kebakaran aktual. Data gas adalah simulasi UI untuk judging. Alat aktual robotik dikembangkan terpisah dengan kalibrasi lab.

