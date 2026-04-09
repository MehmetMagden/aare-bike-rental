from flask import Flask, jsonify

app = Flask(__name__)

# db
bikes =[
    {"id":1, "model": "Scott Sub Active", "status": "available"},
    {"id":2, "model": "Specialized Turbo", "status": "rented"}
]

@app. route('/health')
def health():
    return jsonify({"status": "healty", "service": "Aare Bike Rental"}), 200

@app.route('/bikes')
def get_bikes():
    return jsonify(bikes), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)