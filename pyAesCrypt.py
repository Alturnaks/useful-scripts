import pyAesCrypt

password = input('Введите пароль для файла')
pyAesCrypt.encryptFile('data.text', 'data.txt.aes', password)