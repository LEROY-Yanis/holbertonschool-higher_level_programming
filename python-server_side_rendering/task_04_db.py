#!/usr/bin/python3
"""
Flask application for displaying data from JSON, CSV, or SQLite database.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(filepath):
    """Read and return data from a JSON file."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv(filepath):
    """Read and return data from a CSV file."""
    try:
        products = []
        with open(filepath, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id and price to appropriate types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except (FileNotFoundError, ValueError):
        return []


def read_sql(database):
    """Read and return data from a SQLite database."""
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        return products
    except (sqlite3.Error, Exception):
        return []


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL source with optional filtering by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_list = read_json('products.json')
    elif source == 'csv':
        products_list = read_csv('products.csv')
    else:  # sql
        products_list = read_sql('products.db')
    
    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            products_list = [p for p in products_list if p.get('id') == product_id]
            if not products_list:
                return render_template('product_display.html', 
                                     error="Product not found")
        except ValueError:
            return render_template('product_display.html', 
                                 error="Invalid product id")
    
    return render_template('product_display.html', 
                         products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
