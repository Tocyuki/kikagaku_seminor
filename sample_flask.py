from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello():
    # return 'こんにちわ！'
    title = "ようこそ"
    message = "MTVデザインパターンでWebアプリを作成"
    name = '香西'
    return render_template(
        'index.html',
        message=message,
        title=title,
        name=name
        )

if __name__ == '__main__':
    app.run(debug=True)
