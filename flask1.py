from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/')
def transfer():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/tasks/task1')
def task1():
    return render_template('task1.html')

@app.route('/tasks/task2')
def task2():
    return render_template('task2.html')

@app.route("/profile")
def profileuser():
    return render_template('profile.html')

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id), 200, {'Content-Type': 'text/markdown'}

if __name__ == "__main__":
    app.run(debug=True)