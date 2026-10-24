from cryptography.fernet import Fernet
import os

#1. Carregar a chave de descriptografia
def load_key():
    return open("chave.key", "rb").read()

#2. Descriptografar
def decrypt_file(files, key):
    f = Fernet(key)
    with open(files, "rb") as file:
        data = file.read()
        decrypted_data = f.decrypt(data)
    with open(files, "wb") as file:
        file.write(decrypted_data)

#3. Encontrar os arquivos
def find_file(direct):
    list = [] 
    for raiz, _, files in os.walk(direct):
            for name in files:
                path = os.path.join(raiz, name)
                if name != "ransoware.py" and not name.endswith(".key"):
                    list.append(path)
    return list

#4. Função principal
def main():
    key = load_key()
    files = find_file("test_files")
    for file in files:
        decrypt_file(file, key)
    print("Arquivo descriptografado") 
     
if __name__ == "__main__":
    main()