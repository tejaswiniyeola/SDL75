from time import gmtime, strftime
import time


localtime=time.asctime(time.localtime(time.time())) #to print the time in format manner
print("Local time is: ",localtime)


print(time.strftime("%D-%M-%Y"))

print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
