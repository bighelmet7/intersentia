from intersentia import create_app

app = create_app()

@app.route('/ping/')
def ping():
    return 'Pong'

if __name__ == '__main__':
    app.run()
