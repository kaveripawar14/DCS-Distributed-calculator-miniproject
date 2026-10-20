
from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

history = []


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["num1"])
            b = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = a + b

            elif operation == "subtract":
                result = a - b

            elif operation == "multiply":
                result = a * b

            elif operation == "divide":
                if b == 0:
                    raise ValueError("Cannot divide by zero.")
                result = a / b

            else:
                raise ValueError("Invalid operation.")

            history.insert(0, {
                "num1": a,
                "num2": b,
                "operation": operation,
                "result": result,
                "time": datetime.now().strftime("%H:%M:%S")
            })

            del history[10:]

        except (ValueError, TypeError) as e:
            error = str(e) or "Please enter valid numbers."

    return render_template(
        "index.html",
        result=result,
        error=error,
        history=history
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
