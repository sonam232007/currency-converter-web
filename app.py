from flask import Flask, render_template, request
from api import convert_currency

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        result=None
    )
@app.route("/convert", methods=["POST"])
def convert():

    amount = float(request.form["amount"])
    from_currency = request.form["from_currency"]
    to_currency = request.form["to_currency"]

    converted, rate = convert_currency(
        amount,
        from_currency,
        to_currency
    )

    print("Amount:", amount)
    print("From:", from_currency)
    print("To:", to_currency)
    print("Converted:", converted)
    print("Rate:", rate)

    return render_template(
        "index.html",
        result=converted,
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency,
        rate=rate
    )

if __name__ == "__main__":
    app.run(debug=True)
