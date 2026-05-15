# User Flow — Laundry System

## Aktor
- **Operator**: pemilik atau karyawan laundry

---

## Flow 1: Catat Order Baru

Pelanggan datang bawa cucian
        ↓
Operator buka aplikasi → pilih "Order Baru"
        ↓
Input data:
- Nama pelanggan
- Nomor HP
- Berat (kg)
- Jenis: Reguler (3hr) / Express (1hr)
        ↓
Sistem otomatis generate:
- Nomor order (cth: LDR-001)
- Estimasi selesai
- Total harga
        ↓
Operator konfirmasi → Order tersimpan
        ↓
Struk muncul di layar (bisa screenshot/kirim WA)

---

## Flow 2: Pantau Status Order

Operator buka "Daftar Order"
        ↓
Tampil semua order aktif — urut dari yang paling lama
        ↓
Operator tap order → pilih update status:
  Antri → Proses → Selesai → Diambil
        ↓
Status terupdate, urutan otomatis menyesuaikan

---

## Flow 3: Laporan Harian

Operator buka "Laporan"
        ↓
Sistem tampilkan ringkasan hari ini:
- Total pemasukan
- Order masuk / selesai / pending
- Daftar belum bayar
        ↓
Selesai — tidak perlu input apapun,
semua otomatis dari data order

---

## Status Order (FIFO)

[Antri] → [Proses] → [Selesai] → [Diambil]
  ↑
  Urutan berdasarkan waktu masuk.
  Yang pertama masuk = yang pertama diproses.

---

## Prinsip UX
- Semua aksi maksimal 3 tap
- Tidak ada menu yang dalam/tersembunyi
- Bahasa Indonesia semua
- Tombol besar, cocok untuk layar HP

---

## Wireframe (Text Version)

### Halaman 1: Dashboard

+---------------------------+
|  🧺 Laundry System        |
+---------------------------+
|  [+ Order Baru]           |
+---------------------------+
|  HARI INI                 |
|  📦 Order Masuk  : 8      |
|  ✅ Selesai      : 3      |
|  ⏳ Pending      : 5      |
|  💰 Pemasukan    : 85.000 |
+---------------------------+
|  [Daftar Order] [Laporan] |
+---------------------------+

### Halaman 2: Daftar Order
+---------------------------+
|  ← Daftar Order           |
+---------------------------+
|  [Semua][Antri][Proses]   |
|  [Selesai][Diambil]       |
+---------------------------+
|  #LDR-001 | Budi          |
|  2kg Reguler | ANTRI      |
|  Estimasi: 17 Mei         |
+---------------------------+
|  #LDR-002 | Sari          |
|  3kg Express | PROSES     |
|  Estimasi: 16 Mei         |
+---------------------------+

### Halaman 3: Order Baru
+---------------------------+
|  ← Order Baru             |
+---------------------------+
|  Nama Pelanggan           |
|  [........................]|
|                           |
|  Nomor HP                 |
|  [........................]|
|                           |
|  Berat (kg)               |
|  [........................]|
|                           |
|  Jenis Layanan            |
|  ( ) Reguler 3hr - 7rb/kg |
|  ( ) Express 1hr - 12rb/kg|
+---------------------------+
|  Total: Rp 0              |
|  [Simpan Order]           |
+---------------------------+
