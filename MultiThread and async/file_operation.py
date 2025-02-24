import os
import threading
import time


def download_files(source,destin,file_name):
    with open("C:/Users/karthikeyan.muniraj/Documents/file_d1.txt",'r') as src:
        content=src.read()

    name=os.path.join("C:/Users/karthikeyan.muniraj/Documents/downloaded_file",file_name)

    with open(name,'w') as destin_file:
        destin_file.write(content)

    print(f"download successful - {file_name}")

# download_files("C:/Users/karthikeyan.muniraj/Documents/file_d1.txt","C:/Users/karthikeyan.muniraj/Documents/downloaded_file","make")
thread1= threading.Thread(target=download_files, args=("C:/Users/karthikeyan.muniraj/Documents/file_d1.txt","C:/Users/karthikeyan.muniraj/Documents/downloaded_file","make"))
thread2= threading.Thread(target=download_files, args=("C:/Users/karthikeyan.muniraj/Documents/file_d2.txt","C:/Users/karthikeyan.muniraj/Documents/downloaded_file","make2"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

