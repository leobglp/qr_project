from cryptography.fernet import Fernet

encKey = Fernet.generate_key()

def encryption_data(self):
    cipher_suite = Fernet(encKey)
    dado_bytes = self.encode('utf-8')
    dado_criptografado = cipher_suite.encrypt(dado_bytes)
    return dado_criptografado.decode('utf-8')

def decryption_data(dado_criptografado):
    cipher_suite = Fernet(encKey)
    dado_bytes = dado_criptografado.encode('utf-8')
    dado_descriptografado = cipher_suite.decrypt(dado_bytes)
    return dado_descriptografado.decode('utf-8')