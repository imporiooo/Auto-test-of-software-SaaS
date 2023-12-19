from flask import Flask, make_response, request, render_template, redirect, url_for, session
import subprocess, sqlite3
from hashlib import sha256

app = Flask(__name__,static_folder="static")

@app.route('/')
def transfer():
    return render_template('mainpage.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')


            # TASK 1



@app.route('/tasks/task1')
def task1():
    if 'username' in session:
        return render_template('task1.html')
    else:
        return redirect(url_for('profileuser'))

@app.route('/tasks/task1/submit', methods=['POST'])
def submit_code1():
    user_code1 = request.form['user_code']
    print(user_code1)
    
    conn = sqlite3.connect('login_database.db')
    cursor = conn.cursor()
         
    
    with open('user_code1.py', 'w') as file:
        file.write(user_code1)

    # Запуск тестов
    result = subprocess.run(['pytest', 'test_user_code1.py'], capture_output=True, text=True)

    # Проверяем результат выполнения тестов
    if result.returncode == 0:
        cursor.execute("""
                UPDATE users SET task1 = ? WHERE username = ?
            """, ('Correct',session["username"]))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')


            # TASK 2
    


@app.route('/tasks/task2', methods=['POST', 'GET'])
def task2():
    if 'username' in session:
        return render_template('task2.html')
    else:
        return redirect(url_for('profileuser'))

@app.route('/tasks/task2/submit', methods=['POST'])
def submit_code2():
    user_code2 = request.form['user_code']
    print(user_code2)

    conn = sqlite3.connect('login_database.db')
    cursor = conn.cursor()


    with open('user_code2.py', 'w') as file:
        file.write(user_code2)

    result = subprocess.run(['pytest', 'test_user_code2.py'], capture_output=True, text=True)

    if result.returncode == 0:
        cursor.execute("""
                UPDATE users SET task2 = ? WHERE username = ?
            """, ('Correct',session["username"]))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')


            # TASK 3
    

    
@app.route('/tasks/task3')
def task3():
    if 'username' in session:
        return render_template('task3.html')
    else:
        return redirect(url_for('profileuser'))

@app.route('/tasks/task3/submit', methods=['POST'])
def submit_code3():
    user_code3 = request.form['user_code']
    print(user_code3)

    conn = sqlite3.connect('login_database.db')
    cursor = conn.cursor()

    
    with open('user_code3.py', 'w') as file:
        file.write(user_code3)

    result = subprocess.run(['pytest', 'test_user_code3.py'], capture_output=True, text=True)

    if result.returncode == 0:
        cursor.execute("""
                UPDATE users SET task3 = ? WHERE username = ?
            """, ('Correct',session["username"]))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

            # TASK 4
    

    
@app.route('/tasks/task4')
def task4():
    if 'username' in session:
        return render_template('task4.html')
    else:
        return redirect(url_for('profileuser'))


@app.route('/tasks/task4/submit', methods=['POST'])
def submit_code4():
    user_code4 = request.form['user_code']
    print(user_code4)
    
    conn = sqlite3.connect('login_database.db')
    cursor = conn.cursor()


    
    with open('user_code4.py', 'w') as file:
        file.write(user_code4)

    result = subprocess.run(['pytest', 'test_user_code4.py'], capture_output=True, text=True)

    if result.returncode == 0:
        cursor.execute("""
                UPDATE users SET task4 = ? WHERE username = ?
            """, ('Correct',session["username"]))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

            # TASK 5
    

    
@app.route('/tasks/task5')
def task5():
    if 'username' in session:
        return render_template('task5.html')
    else:
        return redirect(url_for('profileuser'))

@app.route('/tasks/task5/submit', methods=['POST'])
def submit_code5():
    user_code5 = request.form['user_code']
    print(user_code5)
    
    conn = sqlite3.connect('login_database.db')
    cursor = conn.cursor()


    
    with open('user_code5.py', 'w') as file:
        file.write(user_code5)

    result = subprocess.run(['pytest', 'test_user_code5.py'], capture_output=True, text=True)

    if result.returncode == 0:
        cursor.execute("""
                UPDATE users SET task5 = ? WHERE username = ?
            """, ('Correct',session["username"]))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('correctved.html')
    else:
        return render_template('incorrect.html')

            # PROFILE
    


@app.route("/profile", methods=['GET', 'POST'])
def profileuser():
    if 'username' in session:
        conn = sqlite3.connect('login_database.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT,
                password_hash TEXT,
                task1 TEXT default 'Incorrect',
                task2 TEXT default 'Incorrect',
                task3 TEXT default 'Incorrect',
                task4 TEXT default 'Incorrect',
                task5 TEXT default 'Incorrect'
            )
        """)

        conn.commit()
        cursor.execute('SELECT * FROM users WHERE username=?', (session['username'],))
        output = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('profile.html',data=output)
    else:
        return render_template('profilereg.html')

# Функция для хэширования пароля
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Функция для проверки хэша пароля
def check_password(input_password, stored_password):
    return hash_password(input_password) == stored_password

# Роут для страницы регистрации
@app.route('/profile/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Подключение к базе данных
        conn = sqlite3.connect('login_database.db')
        cursor = conn.cursor()
         
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT,
                password_hash TEXT,
                task1 TEXT default 'Incorrect',
                task2 TEXT default 'Incorrect',
                task3 TEXT default 'Incorrect',
                task4 TEXT default 'Incorrect',
                task5 TEXT default 'Incorrect'
            )
        """)

        conn.commit()

        # Проверка, что пользователь с таким именем еще не зарегистрирован
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        existing_user = cursor.fetchone()

        # Хэшируем пароль
        hashed_password = hash_password(password)

        if existing_user:
            # Пользователь с таким именем уже существует
            conn.close()
            return render_template('register.html', error='Username already exists')


        # Вставка данных в таблицу
        else:
            cursor.execute("""
                INSERT INTO users (username, password_hash)
                VALUES (?, ?)
            """, (username, hashed_password))
            conn.commit()

        # Закрываем соединение
        cursor.close()
        conn.close()
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/profile/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('login_database.db')
        cursor = conn.cursor()

        # Поиск пользователя в базе данных по имени пользователя
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        user = cursor.fetchone()

        if user and check_password(password, user[1]):
            # Авторизация успешна, сохраняем имя пользователя в сессии
            session['username'] = username
            conn.close()
            return redirect(url_for('profileuser'))
        else:
            # Неправильное имя пользователя или пароль
            conn.close()
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


@app.route('/profile/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('profileuser'))

if __name__ == "__main__":
    app.secret_key = 'im in your walls'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
