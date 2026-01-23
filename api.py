from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = "galamsey_analysis.db"

def get_all_results():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM analysis_results")
    rows = cursor.fetchall()

    results = []
    for row in rows:
        results.append({
            "id": row["id"],
            "total_sites": row["total_sites"],
            "highest_region": row["highest_region"],
            "highest_region_count": row["highest_region_count"],
            
            "created_at": row["created_at"]
        })

    conn.close()
    return results

@app.route("/results", methods=["GET"])
def results():
    data = get_all_results()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
