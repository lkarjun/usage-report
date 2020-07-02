from cryptography.fernet import Fernet
from typing import Union

fileName = 'credential\cred.bin'
keyName = 'credential\Key.bin'

class Securing:

    def genKey(self):
        '''
        Generates a key and save it into a file
        '''
        key = Fernet.generate_key()
        with open(keyName, 'wb') as key_to_file:
            key_to_file.write(key)

    def keyLoading(self) -> Union[bytes, str]:
        '''
        gen_key() generated file loading
        '''
        return open(keyName, 'rb').read()

    def encrypt_data(self) -> int:
        '''
        encrypting credentials
        '''
        key = self.keyLoading()
        f = Fernet(key)    
        with open(fileName, 'rb') as file:
            file_data = file.read()
        
        encrypted_data = f.encrypt(file_data)
        print(encrypted_data)

        with open(fileName, 'wb') as file:
            file.write(encrypted_data)

        return 0

    def decrypt_data(self) -> int:
        '''
        decrypting the credential file
        '''
        key = self.keyLoading()
        f = Fernet(key)
        with open(fileName, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)
        
        with open(fileName, 'wb') as file:
            file.write(decrypted_data)
       
        return 0

class FileManage(Securing):

    def add_data(self):
        '''it will write essential data from user, its important for email procsessing'''

        receiver_mail = str(input('Please Enter Receiver Mail Address: '))
        sending_mail = str(input('Please Enter Sender Mail Address: '))
        sending_mail_password = str(input(f'Enter Password {sending_mail} : '))

        with open(fileName, 'w') as file:
             file.write(f'password: {sending_mail_password}\n')
             file.write(f'sender_mail: {sending_mail}\n')
             file.write(f'receiver_mail: {receiver_mail}\n')