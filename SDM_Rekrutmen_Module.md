
# SDM & REKRUTMEN MODULE - Required by Jury Fashion Garment
## 4 Tugas Juri (Wajib)

### 1. Menyeleksi Kandidat
- Input: CV via app super-infrared.local/sdm, foto KTP, portofolio jahitan
- Process: AI filter skill (jahit lurus, obras), AS7341 spectral test buta warna (operator harus bedain warna-warni cerah chemical), IMX219 foto hasil jahitan, auto scoring 0-100
- Output: Ranking kandidat, simpan di Vultr Managed Database, sandboxed execution
- Ongkos: Tidak perlu hardware tambahan, pakai AS7341 yang ada

### 2. Menjadwalkan Wawancara
- Input: Kandidat lolos >70 score
- Process: Calendar integration Google/Outlook, ESP32-S3 buzzer 95dB reminder 10 menit sebelum, Telegram Bot kirim jadwal + link Meet, Vultr API throwaway instance untuk interview coding test (jika ada)
- Containment: Interview code execution di sandbox Docker on Vultr, secret hygiene no API keys in sandbox
- Output: Jadwal terkonfirmasi, WA ke kandidat

### 3. Mengoordinasikan Orientasi Karyawan Baru
- Checklist App PWA HP:
  - Training Super Guardian device: timbang kain HX711 4067/39, cek warna IMX219/AS7341, safety gas MQ-135, healthy room SHT41+NDIR
  - Safety briefing: LEL gas CH4 1400ppm, CO2 5000ppm danger
  - SOP garment: color standardization, weight & count, QC
- Progress bar 0-100% real-time via MQTT, supervisor monitor via super-infrared.local
- Duration: 3 hari orientasi, auto-reset 90 hari untuk re-training

### 4. Melacak Alur Kerja Karyawan
- Sensor: IMX219 cek produktivitas per stasiun jahit (hitung gerakan), HX711 hitung output kain/jam (misal 4067g/jam = 39 pcs), SHT41 cek kenyamanan ruang, MLX90640 cek overload thermal operator
- Dashboard KPI: Output/hari, defect rate (via IMX219 color check), attendance via thermal, comfort index
- Alert: Jika output turun <80% atau suhu >32C, agent Vultr auto suggest pindah ke ruang teduh, trigger fan, log ke Vultr VM backend
- Business Value: Meningkatkan efisiensi 20%, mengurangi turnover, memenuhi syarat kompetisi lablab Vultr Agent Rush Challenge 2 Future of Work HR track

## File Structure
/04_SDM_Rekrutmen/
  04a_Candidate_Selection/ (CV + AS7341 test)
  04b_Interview_Scheduling/ (calendar + buzzer + Telegram)
  04c_Orientation_New_Employee/ (checklist + training device)
  04d_Workflow_Tracking/ (KPI dashboard + IMX219 + HX711)

## Model Bisnis
Jual System & Teknik SDM Module Rp500K tambahan di atas teknik base Rp1.5-3.5jt = total Rp2-4jt jual putus. Buyer garment dapat system HR lengkap, bukan cuma alat sensor.
