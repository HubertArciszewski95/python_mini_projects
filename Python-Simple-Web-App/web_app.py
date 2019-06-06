from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def my_form():
    value = request.form.get("input")
    if request.method == 'POST':
        with open("user_data.txt", "a") as file:
            file.write(value + "\n")

    return render_template("my_form.html")


if __name__ == '__main__':
    app.run(debug=True)

