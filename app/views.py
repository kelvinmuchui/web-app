from app import app

@app.route('/')
@app.route('/index')
def index():
    return "You are an amazing person "