import os import mysql.connector 
from flask import Flask, jsonify, request, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(file))
FRONTEND_DIR = os.path.abspath(
os.path.join(BASE_DIR, "..", "frontend")
)

app = Flask(name)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306))
    )

@app.route("/path:filename")
def home(filename):
    return send_from_directory(FRONTEND_DIR, filename)

@app.route("/equipment")
def get_equipment():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("""
            SELECT e.equipment_id, e.equipment_name,
                   c.category_name, e.quantity, e.status
            FROM Equipment e
            LEFT JOIN Category c
            ON e.category_id = c.category_id
        """)

        result = cursor.fetchall()
        cursor.close()
        db.close()

        return jsonify(result)

    except Exception as error:
        return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)