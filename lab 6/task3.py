#Этот код проверяет существование указанного пути и, если он существует, 
# выводит его директорию и имя файла
import os
def path_info(path):
    if os.path.exists(path):
        print("Path exists")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist")

path_info('pp2_labs/lab 1-2')  
