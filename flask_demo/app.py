from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hw():
    #return f'<h2>Hola, {request.args["lastname"]} {request.args["name"]}!</h2>'
    data = ["Az", "Buki", "Vedi"]
    return render_template("index.html", name=request.args["name"], lastname=request.args["lastname"], data=data, flag=False)

@app.route('/data')
def data():
    return render_template("data.html")

if __name__ == '__main__':
    app.run()