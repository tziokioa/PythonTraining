import pickle
import sys

log_file = open("log.txt","a")
sys.stdout = log_file

try:
    myfile=open("dataDump.txt","rb")
    janis = pickle.load(myfile)
    alex = pickle.load(myfile)
    myfile.close()
    print(janis)
    print(alex)
    log_file.close()
except Exception as ex:
    print(str(ex))
    exit(1)
