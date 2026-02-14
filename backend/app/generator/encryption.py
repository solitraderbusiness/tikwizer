from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64

key = b'\x12\x34\x56\x78\x9A\xBC\xDE\xF0\x11\x22\x33\x44\x55\x66\x77\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF\x00\x12\x34\x56\x78\x9A\xBC\xDE\xF0'


def encrypt_aes(plaintext):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create cipher object and encryptor
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the plaintext to be AES block size compliant
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(iv + ciphertext).decode('utf-8')


def decrypt_aes(encoded_ciphertext):
    ciphertext = base64.b64decode(encoded_ciphertext.encode('utf-8'))

    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]

    # Create cipher object and decryptor
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode('utf-8')


# txt = "dibWFIzVGgNai2/szD5qWsetntIYL20Xn3OSQ6zyHyi/ERcT0UZDwfSYTANvT6/VUyGUrTRwbZCCr7NmbPauS62NP1abm4+rpGENoBIT+kBbjYBjRkcx+hgawn2d7AvZrUlYCo4PAel94OTuOjgMLSeiO1OPRP2vSKTly9tVOAHQB4M2K84YmXlwmmrEBVuIVcIrN8Tisc3JePUyOamNVm+hols6I9BhCunHdS7d0FFTedKz2xtv4VbM4bCM8DtSJWT+54dxeh18zmWXhvv3B8csRX1Xiqo5sdEAiBDk0LI4VeIkPVm6QjotFfgtn4XjoSR2m5Hde2HP2YtDGyUPMKo00lY9iwkSjFWjDP1dTO7UBSpZUPGJyjptW2E6yL67kvZOLFF3aRVJVyROeE4Uizfk74QHGB/40UCx5OFQYpXcKvLvkv9WSTk/mpDS1a+W8MGn5NQAyskKjRenCLHK/BdBkJz2tIqXgkK3k9WnXnqlf4xy3ERZz64+HRDSrgEaHQbDZsdmDqI/PZJYgeGsjOkLTb6NnSvHn1Yj7jJLLjEQG2hJByi5HY4LUQgph+VHAyOpdKkxa8Z9kiP0M1ouK8VkAGIpL/M+HljpZlTI8rEylObdqqGmIZ9I8vbWtXifptvQM4hmcz7/5xpx3MIauBHCXa7K37lXOKmWGokQooT7hjf3dOOcryNYXC2e3r+nb43Q8Rkz9bUg6sTRcAwnd4N/fNTQ/DUMUI+ELPmIFdcI5gvpZ6y5YPOZ46WGIciK/flQBiT7KiwfkITjgAaEyYABlQpm7uoSOqk8xLP5KPn6GqPB7J1SgGQ3vPJksHTv0kRA+cytZp46RonLFqMZCMvBuacrF0fywzKkwUX/BVsR9a54JOUz4Ns65JVooI6jkcPloMW2U40TJH9ED/rh1WdxkcU+F+TNx2HxroQQB77ciVXBPAwNaP4VDjheWi1CnAH2o8yeC0vlKYXGbWwyd3TchQhz5jpLKio++5+oGtPMB0/YA1iJMfeH6wDyI5ZXMtDVm8LXyAjVCVxS+fLC5AlhZygR6393DxVbsUKr/o10Mja5tfDita0qDPg2lLGI"
# print(decrypt_aes(txt))

# def test():
#     # key = os.urandom(32)  # 256-bit key
#     encrypted = encrypt_aes("Hello, World!")
#     print("Encrypted:", encrypted)
#
#     decrypted = decrypt_aes(encrypted)
#     print("Decrypted:", decrypted)
#
# test()
