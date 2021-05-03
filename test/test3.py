import os
from flask import Flask, session, jsonify

app = Flask(__name__)


@app.route('/adminsetting', methods=['GET', 'POST'])
def adminsetting():
    
    session['a1'] = 'admin'
    return jsonify('ok')

if __name__ == '__main__':
    app.secret_key = b'_5#y2L"fewxfew"'
    app.run(host='0.0.0.0')
