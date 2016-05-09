from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def main():
    return show_personality()
 
@app.route('/personality')
def show_personality():
    return 'You are an amazing person'
 
if __name__ == '__main__':
    app.run()