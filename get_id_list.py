import subprocess as sb
import os
count = 0
with open('id_list.txt', 'w') as f:
    for filename in os.listdir("data"):
        #I am on mac, this is an apple specific file generated by OSX
        #Yall wont need to worry about it, just ignore it
        if (filename != ".DS_Store"):
            f.write(filename)
            f.write('\n')
            count += 1
print ("Number of unique ID's is: " + str(count))  
