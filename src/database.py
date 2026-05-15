import sqlite3
import os
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "laundry.db")

HARGA = {"reguler": 7000, "express": 12000}
DURASI = {"reguler": 3, "express": 1}


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    with get_db() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_number TEXT UNIQUE NOT NULL,
                customer_name TEXT NOT NULL,
                customer_phone TEXT,
                weight_kg REAL NOT NULL,
                service_type TEXT NOT NULL CHECK(service_type IN ('reguler','express')),
                price_per_kg INTEGER NOT NULL,
                total_price INTEGER NOT NULL,
                status TEXT NOT NULL DEFAULT 'antri'
                    CHECK(status IN ('antri','proses','selesai','diambil')),
                estimated_date TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)


def generate_order_number():
    with get_db() as db:
        count = db.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
        return f"LDR-{count + 1:03d}"


def hitung_total(weight_kg, service_type):
    harga = HARGA.get(service_type, 7000)
    return int(weight_kg) * harga


def hitung_estimasi(service_type):
    durasi = DURASI.get(service_type, 3)
    return (datetime.today() + timedelta(days=durasi)).strftime("%Y-%m-%d")


def create_order(customer_name, customer_phone, weight_kg, service_type):
    order_number = generate_order_number()
    total_price = hitung_total(weight_kg, service_type)
    estimated_date = hitung_estimasi(service_type)
    price_per_kg = HARGA[service_type]

    with get_db() as db:
        db.execute("""
            INSERT INTO orders (order_number, customer_name, customer_phone,
                weight_kg, service_type, price_per_kg, total_price,
                estimated_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (order_number, customer_name, customer_phone, weight_kg,
              service_type, price_per_kg, total_price, estimated_date))
        return order_number


def get_all_orders(status=None):
    with get_db() as db:
        if status:
            rows = db.execute(
                "SELECT * FROM orders WHERE status = ? ORDER BY created_at ASC",
                (status,)
            ).fetchall()
        else:
            rows = db.execute(
                "SELECT * FROM orders ORDER BY created_at ASC"
            ).fetchall()
        return [dict(r) for r in rows]


def get_stats():
    with get_db() as db:
        today = datetime.today().strftime("%Y-%m-%d")
        row = db.execute("""
            SELECT
                COUNT(*) AS total_masuk,
                SUM(CASE WHEN status='selesai' THEN 1 ELSE 0 END) AS selesai,
                SUM(CASE WHEN status IN ('antri','proses') THEN 1 ELSE 0 END) AS pending,
                COALESCE(SUM(CASE WHEN status='selesai' THEN total_price ELSE 0 END), 0) AS pemasukan
            FROM orders
            WHERE DATE(created_at) = ?
        """, (today,)).fetchone()
        return dict(row)


def get_laporan():
    today = datetime.today().strftime("%Y-%m-%d")
    with get_db() as db:
        stats = db.execute("""
            SELECT
                COUNT(*) AS total_masuk,
                SUM(CASE WHEN status='selesai' THEN 1 ELSE 0 END) AS selesai,
                SUM(CASE WHEN status IN ('antri','proses') THEN 1 ELSE 0 END) AS pending,
                COALESCE(SUM(CASE WHEN status='selesai' THEN total_price ELSE 0 END), 0) AS pemasukan
            FROM orders
            WHERE DATE(created_at) = ?
        """, (today,)).fetchone()

        belum_diambil = db.execute("""
            SELECT * FROM orders
            WHERE status != 'diambil'
            ORDER BY created_at ASC
        """).fetchall()

        return {
            "stats": dict(stats),
            "belum_diambil": [dict(r) for r in belum_diambil]
        }
