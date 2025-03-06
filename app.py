from flask import Flask, render_template, request

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Dynamic user route
@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

# Submit form route
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Get the form data (name and age)
        name = request.form['name']
        age = request.form['age']
        return render_template('submit.html', name=name, age=age)
    return render_template('submit_form.html')

if __name__ == '__main__':
    app.run(debug=True)
