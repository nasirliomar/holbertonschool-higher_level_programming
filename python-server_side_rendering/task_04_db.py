#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def normalize_products(products):
    """Ensure each product has consistent keys/types for template."""
    normalized = []
    for p in products:
        if not isinstance(p, dict):
            continue
        pid = p.get("id")
        if isinstance(pid, str) and pid.isdigit():
            pid = int(pid)

        price = p.get("price")
        if isinstance(price, str):
            try:
                price = float(price)
            except ValueError:
                pass

        normalized.append({
            "id": pid,
            "name": p.get("name"),
            "category": p.get("category"),
            "price": price,
        })
    return normalized


def read_products_json(path="products.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return normalize_products(data)
    except (OSError, json.JSONDecodeError):
        pass
    return []


def read_products_csv(path="products.csv"):
    products = []
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
    except OSError:
        return []

    # Normalize CSV rows
    normalized = []
    for p in products:
        pid_raw = p.get("id")
        pid = int(pid_raw) if isinstance(pid_raw, str) and pid_raw.isdigit() else pid_raw

        price_raw = p.get("price")
        try:
            price = float(price_raw) if price_raw not in (None, "") else price_raw
        except ValueError:
            price = price_raw

        normalized.append({
            "id": pid,
            "name": p.get("name"),
            "category": p.get("category"),
            "price": price,
        })
    return normalized


def read_products_sql(db_path="products.db"):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT id, name, category, price FROM Products")
        rows = cur.fetchall()
        conn.close()

        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3],
            })
        return normalize_products(products)
    except sqlite3.Error:
        return None  # signal DB error


@app.route("/products")
def products():
    source = request.args.get("source", "")
    id_param = request.args.get("id")
    error = None

    if source == "json":
        products_list = read_products_json()
    elif source == "csv":
        products_list = read_products_csv()
    elif source == "sql":
        products_list = read_products_sql()
        if products_list is None:
            error = "Database error"
            return render_template("product_display.html", products=[], error=error)
    else:
        error = "Wrong source"
        return render_template("product_display.html", products=[], error=error)

    # Optional filter by id
    if id_param is not None:
        try:
            wanted_id = int(id_param)
        except ValueError:
            error = "Product not found"
            return render_template("product_display.html", products=[], error=error)

        filtered = [p for p in products_list if p.get("id") == wanted_id]
        if not filtered:
            error = "Product not found"
            return render_template("product_display.html", products=[], error=error)
        products_list = filtered

    return render_template("product_display.html", products=products_list, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
