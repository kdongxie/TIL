from flask import Flask,render_template
app = Flask(__name__)
import random

@app.route("/")
def hello():
    return "Main Page"

@app.route("/mulcam")
def mulcam():
    return "Mulcam Page"

@app.route("/greeting/<string:name>")
def greeting(name):
    return f'반갑습니다 {name} 님!'

# path variable
@app.route("/cube/<int:num>")
def cube(num):
    result = num ** 3
    return str(result) # f'{result}'를사용해도 된다


@app.route("/lunch/<int:people>")
def lunch(people):
    menu = ["짜장면","탕수육","짬뽕","피자","햄버거","냉면","회","국수","돈까스"]
    select = [random.choice(menu) for i in range(people)]
    return str(select)

@app.route('/html')
def html():
    multiple_string = '''
        <h1>This is h1 tag </h1>
        <p> This is p tag </p>  
    '''
    return multiple_string

# template variable: html에 변수를 넘겨주는 형식
@app.route('/html_file')
def html_file():
    return render_template('html_file.html')

@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html',your_name=name)


@app.route('/menu_list')
def menu_list():
    menu = ["짜장면", "탕수육", "짬뽕", "피자", "햄버거", "냉면", "회", "국수", "돈까스"]
    return render_template("menu_list.html",menu_list=menu)

@app.route('/boot')
def boot():
    return render_template("bootstrap.html")


if __name__ == "__main__":
    app.run(debug=True)