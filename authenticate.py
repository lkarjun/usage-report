from cryptography.fernet import Fernet
from typing import Union, TextIO

#generate key
class Securing:

    def genKey(self):
        '''
        Generates a key and save it into a file
        '''
        key = Fernet.generate_key()
        with open('credential\Key.bin', 'wb') as key_to_file:
            key_to_file.write(key)

    def keyLoading(self) -> Union[bytes, str]:
        '''
        gen_key() generated file loading
        '''
        return open('credential\Key.bin', 'rb').read()

    def encrypt_data(self, message: str) -> int:
        '''
        encrypting credentials
        '''
        key = self.keyLoading()
        f = Fernet(key)
        f.encrypt(message.encode())

        return 0

    def decrypt_data(self, filename: str) -> int:
        '''
        decrypting the credential file
        '''
        key = self.keyLoading()
        f = Fernet(key)
        with open(filename, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)

        return 0

class FileManage(Securing):

    fileName = 'cred.bin'

    def add_data(self):
        '''it will write essential data from user, its important for email procsessing'''

        receiver_mail = str(input('Please Enter Receiver Mail Address: '))
        sending_mail = str(input('Please Enter Sender Mail Address: '))
        sending_mail_password = str(input(f'Enter Password {sending_mail} : '))

        with open('credential\cred.bin', 'w') as file:
             file.write(f'password: {sending_mail_password}\n')
             file.write(f'sender_mail: {sending_mail}\n')
             file.write(f'receiver_mail: {receiver_mail}\n')