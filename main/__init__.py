import psycopg2
from flask import Flask
from flask_cors import CORS

# Database connection details
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'omkarborker1'

def create_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

def create_app():
    app = Flask(__name__)
    
    from main import main_bp
    from data import data_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(data_bp)
    
    conn = create_db_connection()
    app.config['DB_CONNECTION'] = conn
    
    return app

