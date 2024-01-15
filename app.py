from flask import Flask, render_template

app = Flask(__name__)


#def index():
#    return render_template('index.html')
@app.route('/')
@app.route('/home')
def home():
    return render_template('Dashboard.html')
    #return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
