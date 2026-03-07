from flask import Flask, render_template, request
from controller.calculator_controller import CalculatorController

app = Flask(__name__)
controller = CalculatorController()


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        a = float(request.form["num1"])
        b = float(request.form["num2"])
        operation = request.form["operation"]

        result = controller.calculate(operation, a, b)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)