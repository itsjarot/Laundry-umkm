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
