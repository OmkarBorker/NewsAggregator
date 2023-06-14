import csv
from flask import Blueprint, request, current_app, jsonify
import psycopg2

# Database connection details
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'omkarborker1'

# Establish a connection to the PostgreSQL database
def create_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn


data_bp = Blueprint('data', __name__)

@data_bp.route('/', methods=['GET'])
def test_db_connection():
    try:
        conn = create_db_connection()
        conn.close()
        return jsonify({'message': 'Connected to the PostgreSQL database successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@data_bp.route('/push-stock-industry-mapping', methods=['POST'])
def push_stock_industry_mapping():
    try:
        conn = create_db_connection()
        cursor = conn.cursor()
        cursor.execute('TRUNCATE TABLE stock_industry_mapping;')

        with open('stock_industry_mapping.csv', 'r') as file:
            csv_data = csv.reader(file)
            next(csv_data)  # Skip header row

            for row in csv_data:
                query = 'INSERT INTO stock_industry_mapping (id, ticker, stock, industry) VALUES (%s, %s, %s, %s);'
                cursor.execute(query, row)

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Data inserted into stock_industry_mapping table successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@data_bp.route('/push-news', methods=['POST'])
def push_news():
    try:
        conn = create_db_connection()
        cursor = conn.cursor()
        cursor.execute('TRUNCATE TABLE news;')

        with open('news.csv', 'r') as file:
            csv_data = csv.reader(file)
            next(csv_data)  # Skip header row

            for row in csv_data:
                if row[7] == '':
                    row[7] = None
                query = 'INSERT INTO news (id, title, link, summary, published, source, org, mapped_stock_id,ticker, stock, industry ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
                cursor.execute(query, row)

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Data inserted into news table successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
