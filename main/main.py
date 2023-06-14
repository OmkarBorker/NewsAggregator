from flask import jsonify,request,Blueprint, current_app
import psycopg2
import urllib.parse


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


main_bp = Blueprint('main', __name__)

@main_bp.route('/industries', methods=['GET'])
def get_industries():
    try:
        
        conn = create_db_connection()
        cursor = conn.cursor()

        # Execute query to get list of industries, stocks, and tickers in India
        query = "SELECT industry, stock, ticker FROM stock_industry_mapping"
        cursor.execute(query)
        result = cursor.fetchall()

        cursor.close()
        return {'data': result}
    except Exception as e:
        return {'error': str(e)}

@main_bp.route('/stocks-by-industry', methods=['GET'])
def get_stocks_by_industry():
    try:
        industries = request.args.getlist('industry')

        if not industries:
            return jsonify({'error': 'No industries provided'}), 400

        conn = current_app.config['DB_CONNECTION']
        cursor = conn.cursor()

        # Construct the SQL query to retrieve stocks and tickers for the given industries
        query = "SELECT stock, ticker FROM stock_industry_mapping WHERE industry IN %s"
        cursor.execute(query, (tuple(industries),))  # Pass the industries as a tuple

        result = cursor.fetchall()
        cursor.close()

        return jsonify({'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/news', methods=['GET'])
def get_all_news():
    try:
        conn = create_db_connection()
        cursor = conn.cursor()

        # Execute query to get all news items
        query = "SELECT * FROM news"
        cursor.execute(query)
        result = cursor.fetchall()

        cursor.close()
        return {'data': result}
    except Exception as e:
        return {'error': str(e)}

@main_bp.route('/news/<string:news_id>', methods=['GET'])
def get_news_by_id(news_id):
    try:
        conn = create_db_connection()
        cursor = conn.cursor()
        # Execute query to get news details for the given news ID
        query = " SELECT * FROM news WHERE id = %s::uuid "
        cursor.execute(query, (news_id,))
        result = cursor.fetchone()

        cursor.close()
        return {'data': result}
    except Exception as e:
        return {'error': str(e)}

@main_bp.route('/news-by-ticker', methods=['GET'])
def get_news_by_ticker():
    try:
        tickers = request.args.getlist('ticker')  # Get the list of tickers from the query parameters

        conn = create_db_connection()
        cursor = conn.cursor()

        # Construct the SQL query to retrieve news items for the given tickers
        query = "SELECT * FROM news WHERE ticker IN %s"
        cursor.execute(query, (tuple(tickers),))  # Pass the tickers as a tuple

        result = cursor.fetchall()
        cursor.close()

        return jsonify({'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@main_bp.route('/news-by-industry', methods=['GET'])
def get_news_by_industry():
    try:
        industries = request.args.getlist('industry')

        if not industries:
            return jsonify({'error': 'No industries provided'}), 400

        conn = current_app.config['DB_CONNECTION']
        cursor = conn.cursor()

        # Construct the SQL query to retrieve news items for the given industries
        query = "SELECT * FROM news WHERE industry IN %s"
        cursor.execute(query, (tuple(industries),))  # Pass the industries as a tuple

        result = cursor.fetchall()
        cursor.close()

        return jsonify({'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main_bp.route('/news-by-source', methods=['GET'])
def get_news_by_source():
    try:
        sources = request.args.getlist('source')

        if not sources:
            return jsonify({'error': 'No sources provided'}), 400

        conn = current_app.config['DB_CONNECTION']
        cursor = conn.cursor()

        # Construct the SQL query to retrieve news items for the given sources
        query = "SELECT * FROM news WHERE source IN %s"
        cursor.execute(query, (tuple(sources),))  # Pass the sources as a tuple

        result = cursor.fetchall()
        cursor.close()

        return jsonify({'data': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
