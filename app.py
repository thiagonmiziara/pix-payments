from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/payments/pix", methods=["POST"])
def create_payment_pix():
    return jsonify({"message": "The payment has been created"})


# webhook
@app.route("/payments/pix/confirmation", methods=["POST"])
def pix_confirmation():
    return jsonify({"message": "The payment has been confirmed"})


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_page(payment_id):
    return "Pagamento PIX"


if __name__ == "__main__":
    app.run(debug=True)
