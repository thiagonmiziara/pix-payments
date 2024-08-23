import uuid
import qrcode


class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        bank_payment_id = uuid.uuid4()

        hash_payment = f"bank_payment_id_{bank_payment_id}"

        img = qrcode.make(hash_payment)
        img.save(f"static/imgs/qr_code_payment_{hash_payment}.png")

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"static/imgs/qr_code_payment_{hash_payment}.png",
        }
