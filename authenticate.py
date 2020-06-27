from cryptography.fernet import Fernet
from typing import ByteString, TextIO

#generate key
class Securing:

    def genKey(self):
        '''
        Generates a key and save it into a file
        '''
        key = Fernet.generate_key()
        with open('credential\Key.bin', 'wb') as key_to_file:
            key_to_file.write(key)

    def keyLoading(self) -> ByteString:
        '''
        gen_key() generated file loading
        '''
        return open('credential\Key.bin', 'rb').read()

    def encrypt_data(self, message: str) -> int:
        '''
        encrypting credentials
        '''
        key = keyLoading()
        f = Fernet(key)
        f.encrypt(message)

        return 0

    def decrypt_data(self, filename: TextIO) -> int:
        '''
        decrypting the credential file
        '''
        f = Fernet(key)
        with open(filename, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)

        return 0

