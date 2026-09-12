import json
import random
import string
from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore


# Firebase初期化
cred = credentials.Certificate(
    "firebasejson/serviceAccountKey.json"
)

firebase_admin.initialize_app(cred)

db = firestore.client()


# ランダム6文字
def random_string(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


# MMDD
mmdd = datetime.now().strftime("%m%d")

# ドキュメントID
document_id = random_string(6) + mmdd


# sample.json読み込み
with open("sample.json", "r", encoding="utf-8") as f:
    orders = json.load(f)


# testコレクション
doc_ref = db.collection("test").document(document_id)


# sample.json全体を1ドキュメントに登録
doc_ref.set({
    "orders": orders
})


print("登録完了")
print(f"Document ID: {document_id}")
print(f"注文数: {len(orders)}")