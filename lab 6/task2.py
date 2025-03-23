import os
def check_access(path):

    try:
       
        if os.path.exists(path): 
            print("The path exists.")
        else:
            print("The path does not exist.")
        
       
        if os.access(path, os.R_OK): 
            print("The path is readable.")
        else:
            print("The path is not readable.")
        
    
        if os.access(path, os.W_OK):
            print("The path is writable.")
        else:
            print("The path is not writable.")
        
        # Check executability
        if os.access(path, os.X_OK): #Проверка права на выполнение
            print("The path is executable.")
        else:
            print("The path is not executable.")
    
    except Exception as e:
        print("An error occurred: ", str(e))

check_access("extra_file")