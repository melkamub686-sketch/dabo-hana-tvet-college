from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'dabo_hana_tvet_secure_key_2026'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def admin_login():
    data = request.json
    if data.get('email') == 'melkamub686@gmail.com' and data.get('password') == '178010MnF@#$':
        session['admin'] = True
        return jsonify({"success": True, "message": "Login Successful"})
    return jsonify({"success": False, "message": "Invalid Admin Credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)