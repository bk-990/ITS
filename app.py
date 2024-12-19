from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        shape = request.form.get("shape")
        dimension1 = request.form.get("dimension1")
        dimension2 = request.form.get("dimension2")
        
        try:
            dimension1 = float(dimension1)
            if dimension2:
                dimension2 = float(dimension2)
            else:
                dimension2 = None

            # Calculating area based on the shape selected
            if shape == "triangle":
                if dimension2 is None:
                    error = "Please enter both dimensions for a triangle."
                else:
                    result = 0.5 * dimension1 * dimension2
            elif shape == "square":
                result = dimension1 ** 2  # Square only requires one dimension
            elif shape == "rectangle":
                if dimension2 is None:
                    error = "Please enter both dimensions for a rectangle."
                else:
                    result = dimension1 * dimension2
            elif shape == "circle":
                if dimension2 is not None:
                    error = "A circle only requires one dimension (radius)."
                else:
                    result = 3.1416 * (dimension1 ** 2)

        except ValueError:
            error = "Please enter valid numbers for dimensions."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
