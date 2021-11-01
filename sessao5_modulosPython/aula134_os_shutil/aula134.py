import os
import shutil

caminho_original = r'C:\Users\Filipe Henrique\Desktop\teste2'
caminho_novo = r'C:\Users\Filipe Henrique\Desktop\teste'
try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        # print(new_file_path)
        # if '.png' in file:
        #     shutil.copy(old_file_path, new_file_path)
        #     print(f'Arquivo {file} copiado com sucesso!')
        if '.png' in file:
            os.remove(new_file_path)
            print(f'Arquivo {file} excluido com sucesso!')
