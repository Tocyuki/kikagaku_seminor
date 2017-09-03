from flask import Flask, render_template
from flaski.database import db_session
from flaski.models import Chart

app = Flask(__name__)

@app.route('/')

def hello():
    # DB からデータを取得
    # View -> Model -> View
    queries = Chart.query
    # View -> Template -> View
    return render_template('index.html', queries=queries)

if __name__ == '__main__':
    app.run(debug=True)
