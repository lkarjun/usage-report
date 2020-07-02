from cryptography.fernet import Fernet
from typing import Union
import yaml

fileName = 'credential\cred.yaml'
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
        names = ['receiverMail', 'sendingMail', 'sendingMailPassword']
        values = [receiver_mail, sending_mail, sending_mail_password]

        with open(fileName, 'w') as file:
            ziped_file = dict(zip(names, values))
            yaml.safe_dump(ziped_file, file)
        
    def sendReceiverEmail(self) -> str:
        '''
        decrypt the data and send the data then encrypt
        '''
        self.decrypt_data()
        openData = open(fileName)
        loadData = yaml.load(openData, Loader=yaml.FullLoader)
        copyFile = loadData.copy()
        openData.close()
        self.encrypt_data()
        return copyFile["receiverMail"]

    def sendSenderEmail(self) -> str:
        '''
        decrypt the data and send the sendSenderEmail data then encrypt
        '''
        self.decrypt_data()
        openData = open(fileName)
        loadData = yaml.load(openData, Loader=yaml.FullLoader)
        copyFile = loadData.copy()
        self.encrypt_data()
        return copyFile['sendingMail']
    
    def sendSenderPassword(self) -> str:
        '''
        decrypt the data and send the senderEmail password data then encrypt
        '''
        self.decrypt_data()
        openData = open(fileName)
        loadData = yaml.load(openData, Loader=yaml.FullLoader)
        copyFile = loadData.copy()
        self.encrypt_data()
        return copyFile['sendingMailPassword']