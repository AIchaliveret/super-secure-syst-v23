
# RUANG TEDUH MODULE - Fashion Garment Market Control
## Konsep
Ruang teduh = shaded rest area + QC area untuk garment & obsidian altarum. Teduh = tidak panas, tidak silau, nyaman untuk cek warna kain & batu mulia.

## Spec
- Sensor: MLX90640 Thermal 32x24 Rp1.07jt cek heat stress operator, SHT41 humidity, NDIR CO2, IMX219 8MP cek warna fabric under teduh lighting (biar warna-warni cerah akurat).
- Kondisi Ideal: Suhu 24-28C, Humidity 50-65%, CO2 <800ppm, Lux 500-750 (cek via AS7341).
- Agent Logic: Jika suhu >32C atau CO2 >1000ppm di ruang jahit, agent Vultr RAG auto pindah operator ke ruang teduh, trigger fan, kirim WA supervisor. Log via Vultr VM backend.
- Fungsi: Meningkatkan akurasi color standardization (AS7341 11-channel 350-1000nm), mengurangi cacat garment 15%, meningkatkan produktivitas, tempat istirahat bio healthy.
- Integrasi: Bagian dari Fashion Garment Market Control System, folder /05_Market_Control_Fashion_Garment/Ruang_Teduh/
- Ongkos: Sama dengan Healthy Room, tambah tenda/kain teduh Rp50K.
- Kenapa wajib di kompetisi lablab? Menunjukkan Future of Work - employee wellbeing, bukan cuma alat. Vultr Challenge 2 butuh workflow tracking.
