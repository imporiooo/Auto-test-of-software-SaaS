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
    result1 = subprocess.run(['pytest', 'test_user_code1.py'], capture_output=True, text=True)

    # Проверяем результат выполнения тестов
    if result1.returncode == 0:
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

    result2 = subprocess.run(['pytest', 'test_user_code2.py'], capture_output=True, text=True)

    if result2.returncode == 0:
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

    result2 = subprocess.run(['pytest', 'test_user_code3.py'], capture_output=True, text=True)

    if result2.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

            # TASK 4
    

    
@app.route('/tasks/task4', methods=['GET', 'POST'])
def task4():
    if request.method == 'POST': 
        text4 = request.form.get('textarea')
        with open('task3.py', 'w') as f:
            f.write(text4)
    return render_template('task4.html')


            # TASK 5
    

    
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