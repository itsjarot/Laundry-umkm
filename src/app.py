from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from database import init_db, create_order, get_all_orders, get_stats, get_laporan, get_db

app = Flask(__name__, template_folder="templates")

init_db()


@app.route("/")
def dashboard():
    stats = get_stats()
    return render_template("dashboard.html", stats=stats)


@app.route("/order-baru", methods=["GET", "POST"])
def order_baru():
    if request.method == "POST":
        name = request.form["customer_name"].strip()
        phone = request.form.get("customer_phone", "").strip()
        weight = float(request.form["weight_kg"])
        service = request.form["service_type"]

        order_number = create_order(name, phone, weight, service)
        return render_template("order_baru.html", saved=order_number)

    return render_template("order_baru.html", saved=None)


@app.route("/daftar-order")
def daftar_order():
    status = request.args.get("status")
    orders = get_all_orders(status)
    return render_template("daftar_order.html", orders=orders, status_filter=status)


@app.route("/laporan")
def laporan():
    data = get_laporan()
    today = datetime.today().strftime("%A, %d %B %Y")
    return render_template("laporan.html", data=data, today=today)


@app.route("/order/<int:order_id>/status", methods=["POST"])
def update_status(order_id):
    status = request.form["status"]
    with get_db() as db:
        db.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
    return redirect(url_for("daftar_order"))


if __name__ == "__main__":
    app.run(debug=True)
