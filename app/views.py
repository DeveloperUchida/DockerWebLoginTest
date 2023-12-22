from flask import Flask, request, render_template

app = Flask(__name__)

# 検証用DB
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def home():
    return "Welcome to the Home Page!!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ユーザーの存在をチェックする
        if username in users and users[username] == password:
            # ログイン成功時メッセージ表示
            return 'Login successful!!'
        else:
            # ログイン失敗時の処理
            return 'Login failed. Please check your username and password.'

    # GETリクエストが来たときは、login.htmlを表示
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
    