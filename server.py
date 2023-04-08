from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def render_boxes():
    return render_template("index.html")

@app.route('/play/<int:num>')          
def rndr_multboxes(num):
    return render_template("multi.html", num=num)

@app.route('/play/<int:num>/<string:color>')          
def rndr_multcolor(num, color):
    return render_template("multi_color.html", num=num, color=color)


if __name__=="__main__":
    app.run(debug=True)