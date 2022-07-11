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
        keyraw = '{:032b}'.format(key)
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
        with open(path, 'rb') as file:
            encrypted = fernet.encrypt(file.read())
        return encrypted

    # base64 decryption
    def decryptFile(encrypted : bytes, key : int) -> None:
        keyraw = '{:032b}'.format(int(key))
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf-8')))
        decrypted = fernet.decrypt(encrypted)
        with open("D:\\de.jpg", 'wb') as file:
            file.write(decrypted)

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
