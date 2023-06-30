from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)


@app.route('/api/current-time')
def current_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = "Automate All The Things"
    return jsonify({'time': current_time, 'message': message})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

