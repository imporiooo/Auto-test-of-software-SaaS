from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_code():
    user_code = request.form['user_code']
    with open('user_code.py', 'w') as file:
        file.write(user_code)

    # Запуск тестов
    import test_user_code 
    result = test_user_code.test_add_function()
    return result.stdout.decode()


if __name__ == '__main__':
    app.run(debug=True)
