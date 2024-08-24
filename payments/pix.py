import uuid
import qrcode


class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        bank_payment_id = str(uuid.uuid4())

        hash_payment = f"bank_payment_id_{bank_payment_id}"

        img = qrcode.make(hash_payment)
        img.save(f"{base_dir}static/img/qr_code_{bank_payment_id}.png")

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"qr_code_{bank_payment_id}",
        }
