from flask import Flask, make_response, request, render_template
import subprocess

app = Flask(__name__,static_folder="static")

@app.route('/')
def transfer():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/tasks/task1')
def task1():
    return render_template('task1.html')

@app.route('/submit', methods=['POST'])
def submit_code():
    user_code = request.form['user_code']
    print(user_code)

    
    with open('user_code.py', 'w') as file:
        file.write(user_code)

    # Запуск тестов
    result = subprocess.run(['pytest', 'test_user_code.py'], capture_output=True, text=True)

    # Проверяем результат выполнения тестов
    if result.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

@app.route('/tasks/task2', methods=['GET', 'POST'])
def task2():
    if request.method == 'POST': 
        text2 = request.form.get('textarea')
        with open('task2.py', 'w') as f:
            f.write(text2)
    return render_template('task2.html')

@app.route('/tasks/task3', methods=['GET', 'POST'])
def task3():
    if request.method == 'POST': 
        text3 = request.form.get('textarea')
        with open('task3.py', 'w') as f:
            f.write(text3)
    return render_template('task3.html')

@app.route('/tasks/task4', methods=['GET', 'POST'])
def task4():
    if request.method == 'POST': 
        text4 = request.form.get('textarea')
        with open('task3.py', 'w') as f:
            f.write(text4)
    return render_template('task4.html')

@app.route('/tasks/task5', methods=['GET', 'POST'])
def task5():
    if request.method == 'POST': 
        text5 = request.form.get('textarea')
        with open('task5.py', 'w') as f:
            f.write(text5)
    return render_template('task5.html')

@app.route("/profile")
def profileuser():
    return render_template('profile.html')

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id), 200, {'Content-Type': 'text/markdown'}

if __name__ == "__main__":
    app.run(debug=True)