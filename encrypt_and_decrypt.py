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
    # base64 encryption
    def encryption(path, key):
        with open(path, 'rb') as file:
            file_encode_b64 = base64.b64encode(file.read())

        keyraw = '{:032b}'.format(key_a)
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
        encrypted = fernet.encrypt(file_encode_b64)
        # print(encrypted) # это мы отправляем челу
        return encrypted

    # base64 decryption
    def decryption(decrypted):
        keyraw = '{:032b}'.format(key_b)
        fernet = Fernet(base64.urlsafe_b64encode(bytes(keyraw, encoding='utf8')))
        decrypted = fernet.decrypt(encrypted)

        with open("a.png", 'wb') as file:
            file.write(base64.b64decode(decrypted))

    #шифровка текста
    def encryptText(key):
        message=input()
        message_bytes=message.encode('utf-8')#в utf-8 введённое сообщение
        encoded_data=base64.b64encode(message_bytes)#перевод в base64
        enc_message=''
        for i in encoded_data:#цикл для шифрования каждой буквы
            enc_message+=chr(i+key)#создание закодированной строки
        print(enc_message)
        return enc_message

    #расшифровка текста
    def decryptText(key,enc_message):
        decr_message=''
        for i in enc_message:
            decr_message+=chr(ord(i)-key)#дешифровка строки
        decr_message_base64=base64.b64decode(decr_message)#перевод из base64
        message=decr_message_base64.decode('utf-8')#перевод из utf-8
        print(message)
    

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
    encrypted = ''
