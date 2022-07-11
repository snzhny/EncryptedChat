try:
    from cryptography.fernet import Fernet
    from random import randint
    import base64
except ModuleNotFoundError:
    from subprocess import call

    modules = ["cryptography", "Fernet", "fernet", "base64"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    # base64 encryption
    def encryptFile(path : str, key : int) -> bytes:
        with open(path, 'rb') as file:
            file_encode_b64 = base64.b64encode(file.read())
        keyraw = '{:032b}'.format(key)
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
        encrypted = fernet.encrypt(file_encode_b64)
        # print(encrypted) # это мы отправляем челу
        return encrypted

    # base64 decryption
    def decryptFile(encrypted, key):
        keyraw = '{:032b}'.format(int(key))
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf-8')))
        decrypted = fernet.decrypt(encrypted)

        with open("D:\\de.txt", 'wb') as file:
            file.write(base64.b64decode(decrypted))

        return f'file on D:\\de.txt'

    # шифровка текста
    def encryptText(text : str, key : int) -> bytes :
        keyraw = '{:032b}'.format(key)
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
        encrypted = fernet.encrypt(text.encode('utf-8'))
        return encrypted

    def decryptText(encrypted : bytes, key : int) -> str:
        keyraw = '{:032b}'.format(key)
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
        encrypted = fernet.decrypt(encrypted).decode()
        return encrypted
