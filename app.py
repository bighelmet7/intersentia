from intersentia import create_app
from flask import render_template

app = create_app()

@app.route('/ping/')
def ping():
    return 'Pong'

# INFO: Code snippet: http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
