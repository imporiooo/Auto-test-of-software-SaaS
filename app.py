from flask import Flask, make_response, request, render_template
import subprocess

app = Flask(__name__,static_folder="static")

@app.route('/')
def transfer():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')


            # TASK 1



@app.route('/tasks/task1')
def task1():
    return render_template('task1.html')

@app.route('/tasks/task1/submit', methods=['POST'])
def submit_code1():
    user_code1 = request.form['user_code']
    print(user_code1)

    
    with open('user_code1.py', 'w') as file:
        file.write(user_code1)

    # Запуск тестов
    result = subprocess.run(['pytest', 'test_user_code1.py'], capture_output=True, text=True)

    # Проверяем результат выполнения тестов
    if result.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')


            # TASK 2
    


@app.route('/tasks/task2')
def task2():
    return render_template('task2.html')

@app.route('/tasks/task2/submit', methods=['POST'])
def submit_code2():
    user_code2 = request.form['user_code']
    print(user_code2)

    
    with open('user_code2.py', 'w') as file:
        file.write(user_code2)

    result = subprocess.run(['pytest', 'test_user_code2.py'], capture_output=True, text=True)

    if result.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')


            # TASK 3
    

    
@app.route('/tasks/task3')
def task3():
    return render_template('task3.html')

@app.route('/tasks/task3/submit', methods=['POST'])
def submit_code3():
    user_code3 = request.form['user_code']
    print(user_code3)

    
    with open('user_code3.py', 'w') as file:
        file.write(user_code3)

    result = subprocess.run(['pytest', 'test_user_code3.py'], capture_output=True, text=True)

    if result.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

            # TASK 4
    

    
@app.route('/tasks/task4')
def task4():
    return render_template('task4.html')


@app.route('/tasks/task4/submit', methods=['POST'])
def submit_code4():
    user_code4 = request.form['user_code']
    print(user_code4)

    
    with open('user_code4.py', 'w') as file:
        file.write(user_code4)

    result = subprocess.run(['pytest', 'test_user_code4.py'], capture_output=True, text=True)

    if result.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

            # TASK 5
    

    
@app.route('/tasks/task5')
def task5():
    return render_template('task5.html')

@app.route('/tasks/task5/submit', methods=['POST'])
def submit_code5():
    user_code5 = request.form['user_code']
    print(user_code5)

    
    with open('user_code5.py', 'w') as file:
        file.write(user_code5)

    result = subprocess.run(['pytest', 'test_user_code5.py'], capture_output=True, text=True)

    if result.returncode == 0:
        return render_template('correctved.html')
    else:
        return render_template('incorrect.html')

@app.route("/profile")
def profileuser():
    return render_template('profile.html')

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id), 200, {'Content-Type': 'text/markdown'}

if __name__ == "__main__":
    app.run(debug=True)