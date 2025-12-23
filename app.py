from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        class_name = request.form['class']
        password = request.form['password']
        print(name, email, class_name, password)  
        return redirect(url_for('home'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
