from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from database import (init_db, create_order, get_all_orders, get_stats,
                      get_laporan, get_status_counts, get_db,
                      mark_paid, delete_order)

app = Flask(__name__, template_folder="templates")

init_db()


BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
         "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]


def tgl_id_length(date_obj):
    return f"{HARI[date_obj.weekday()]}, {date_obj.day} {BULAN[date_obj.month - 1]} {date_obj.year}"


@app.template_filter("tgl_id")
def tgl_id_filter(date_str):
    if not date_str:
        return ""
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return f"{dt.day} {BULAN[dt.month - 1]} {dt.year}"
    except:
        return date_str


@app.route("/")
def dashboard():
    stats = get_stats()
    today = tgl_id_length(datetime.today())
    return render_template("dashboard.html", stats=stats, today=today)


@app.route("/order-baru", methods=["GET", "POST"])
def order_baru():
    error = None
    if request.method == "POST":
        name = request.form.get("customer_name", "").strip()
        phone = request.form.get("customer_phone", "").strip()
        service = request.form.get("service_type", "")

        if not name:
            error = "Nama pelanggan tidak boleh kosong"
        elif service not in ("reguler", "express"):
            error = "Jenis layanan tidak valid"
        else:
            try:
                weight = float(request.form.get("weight_kg", 0))
            except (ValueError, TypeError):
                weight = 0

            if weight <= 0:
                error = "Berat harus lebih dari 0 kg"
            elif weight > 100:
                error = "Berat maksimal 100 kg"

        if not error:
            order_number = create_order(name, phone, weight, service)
            return render_template("order_baru.html", saved=order_number)

        return render_template("order_baru.html", saved=None, error=error)

    return render_template("order_baru.html", saved=None, error=error)


@app.route("/daftar-order")
def daftar_order():
    status = request.args.get("status")
    orders = get_all_orders(status)
    counts = get_status_counts()
    return render_template("daftar_order.html", orders=orders, status_filter=status, counts=counts)


@app.route("/laporan")
def laporan():
    data = get_laporan()
    today = tgl_id_length(datetime.today())
    return render_template("laporan.html", data=data, today=today)


@app.route("/order/<int:order_id>/status", methods=["POST"])
def update_status(order_id):
    status = request.form["status"]
    with get_db() as db:
        db.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
    return redirect(url_for("daftar_order"))


@app.route("/order/<int:order_id>/bayar", methods=["POST"])
def bayar(order_id):
    mark_paid(order_id)
    return redirect(url_for("daftar_order"))


@app.route("/order/<int:order_id>/batalkan", methods=["POST"])
def batalkan(order_id):
    delete_order(order_id)
    return redirect(url_for("daftar_order"))


if __name__ == "__main__":
    app.run(debug=True)
