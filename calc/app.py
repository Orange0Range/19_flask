# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)
print(app)

@app.route('/')
def say_hello():
    """Return simple "Hello" Greeting."""

    html = "<html><body><h1>Hey</h1></body></html>"
    return html

@app.route('/add')
def addPage():
    a = request.args.get('a')
    b = request.args.get('b')
    
    return f"<body>{add(int(a),int(b))}</body>"

@app.route('/sub')
def subPage():
    a = request.args.get('a')
    b = request.args.get('b')
    
    return f"<body>{sub(int(a),int(b))}</body>"

@app.route('/mult')
def multPage():
    a = request.args.get('a')
    b = request.args.get('b')
    
    return f"<body>{mult(int(a),int(b))}</body>"

@app.route('/div')
def divPage():
    a = request.args.get('a')
    b = request.args.get('b')
    
    return f"<body>{div(int(a),int(b))}</body>"

calc = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

@app.route('/math/<op>')
def mathPage(op):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return f"<body>{calc[op](a,b)}</body>"