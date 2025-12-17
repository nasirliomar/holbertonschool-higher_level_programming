#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_products_json(path="products.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
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

    # Normalize types (keep it simple for template rendering)
    normalized = []
    for p in products:
        normalized.append({
            "id": int(p["id"]) if str(p.get("id", "")).isdigit() else p.get("id"),
            "name": p.get("name"),
            "category": p.get("category"),
            "price": float(p["price"]) if p.get("price") not in (None, "") else p.get("price"),
        })
    return normalized


def normalize_products(products):
    """Ensure each product has consistent keys/types for template."""
    normalized = []
    for p in products:
        try:
            pid = p.get("id")
            if isinstance(pid, str) and pid.isdigit():
                pid = int(pid)
            name = p.get("name")
            category = p.get("category")
            price = p.get("price")
            if isinstance(price, str):
                try:
                    price = float(price)
                except ValueError:
                    pass
            normalized.append({"id": pid, "name": name, "category": category, "price": price})
        except AttributeError:
            continue
    return normalized


@app.route("/products")
def products():
    source = request.args.get("source", "")
    id_param = request.args.get("id")

    error = None
    products_list = []

    if source == "json":
        products_list = normalize_products(read_products_json())
    elif source == "csv":
        products_list = normalize_products(read_products_csv())
    else:
        error = "Wrong source"
        return render_template("product_display.html", products=[], error=error)

    # Optional filtering by id
    if id_param is not None:
        try:
            wanted_id = int(id_param)
        except ValueError:
            wanted_id = None

        if wanted_id is None:
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
