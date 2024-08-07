from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Здесь можно обработать данные (например, сохранить в базу данных или отправить на email)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


