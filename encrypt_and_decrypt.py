#!/usr/bin/python3

try:
    from cryptography.fernet import Fernet
    from random import randint
    import base64
except ModuleNotFoundError:
    from subprocess import call

    modules = ["cryptography", "Fernet", "fernet", "base64"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    # # base64 encryption
    # def encryption(path, key):
    #     with open(path, 'rb') as file:
    #         file_encode_b64 = base64.b64encode(file.read())
    #     keyraw = '{:032b}'.format(key_a)
    #     fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
    #     encrypted = fernet.encrypt(file_encode_b64)
    #     print(encrypted) # это мы отправляем челу
    #     # return encrypted
    #
    # # base64 decryption
    # def decryption(decrypted):
    #     keyraw = '{:032b}'.format(key_b)
    #     fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
    #     decrypted = fernet.decrypt(encrypted)
    #
    #     with open("a.png", 'wb') as file:
    #         file.write(base64.b64decode(decrypted))

    # шифровка текста
    def encryptText(text, key):
        keyraw = '{:032b}'.format(key)
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
        encrypted = fernet.encrypt(text.encode())
        return encrypted

    def decryptText(encrypted, key):
        keyraw = '{:032b}'.format(key)
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
        encrypted = fernet.decrypt(encrypted).decode("utf-8")
        return encrypted

    # g = randint(1, 10)
    # p = randint(1, 10)
    #
    # # A
    # a = randint(1, 10)
    # ga = (g ** a) % p
    #
    # # B
    # b = randint(1, 10)
    # gb = (g ** b) % p
    #
    # # KEYS
    # key_a = gb ** a % p
    # key_b = ga ** b % p

    #
    # file_encode_b64 = intoBase64()
    # encrypted = encrypt(key_a, file_encode_b64)
    # decrypted = decrypt(key_b, encrypted)
    # fromBase64(decrypted)
