from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

# DSA鍵ペアの生成
key = DSA.generate(2048)

# 公開鍵の取得
public_key = key.publickey()

# 署名するメッセージ
message = b'flag'

# メッセージのハッシュ
h = SHA256.new(message)

# 署名の生成
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(h)

print("生成された署名:", signature)

# 署名の検証
verifier = DSS.new(public_key, 'fips-186-3')

try:
    verifier.verify(h, signature)
    print("署名が有効です")
except ValueError:
    print("署名が無効です")

# 公開鍵のエクスポート
public_key_pem = public_key.export_key()
print("公開鍵 (PEM形式):")
print(public_key_pem.decode())

# 署名を受け取って検証するコード
def verify_signature(public_key_pem, message, signature):
    public_key = DSA.import_key(public_key_pem)
    verifier = DSS.new(public_key, 'fips-186-3')
    h = SHA256.new(message)
    try:
        verifier.verify(h, signature)
        print("署名が有効です")
    except ValueError:
        print("署名が無効です")

# 署名の検証をテスト
verify_signature(public_key_pem, b'flag', signature)
