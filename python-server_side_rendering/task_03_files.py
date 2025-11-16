#!/usr/bin/python3
"""
Flask application for displaying data from JSON or CSV files.
"""
from flask import Flask, render_template, request
import json
import csv

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


@app.route('/products')
def products():
    """Display products from JSON or CSV source with optional filtering by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_list = read_json('products.json')
    else:  # csv
        products_list = read_csv('products.csv')
    
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
