# Blueprint — Laundry System

## Problem Statement
Pemilik laundry kecil di Makassar masih mengelola order
secara manual menggunakan kertas atau buku tulis.
Akibatnya: order terselip, antrian tidak jelas, laporan
keuangan tidak ada.

## Solusi
Aplikasi web ringan yang bisa diakses lewat HP.
Simple, cepat, tidak perlu training panjang.

## Fitur (Scope Final)

### 1. Order Masuk
- Input: nama pelanggan, nomor HP, berat (kg), jenis layanan
- Jenis layanan: reguler (3 hari), express (1 hari)
- Output: nomor order otomatis, estimasi selesai
- Opsional: kirim notif ke WA pelanggan

### 2. Status Tracker (FIFO)
- Tampilkan semua order aktif
- Status: Antri → Proses → Selesai → Diambil
- Urutan berdasarkan waktu masuk (yang pertama = yang duluan)
- Filter by status

### 3. Laporan Harian
- Total pemasukan hari ini
- Jumlah order masuk / selesai / pending
- Daftar order yang belum dibayar

## Yang Sengaja Tidak Dibuat
- Login/akun pelanggan (terlalu kompleks)
- Inventory deterjen/pewangi (out of scope)
- Multi-cabang (out of scope)

## Target Pengguna
Pemilik atau karyawan laundry kecil.
Non-technical. Pakai HP Android sehari-hari.

## Sukses Seperti Apa?
Pemilik laundry bisa operasikan sendiri tanpa diajarin
lebih dari 10 menit.
