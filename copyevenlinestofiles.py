#7(d) WAP to read a file and Copy even lines of the file* **to a file named ‘File1’ and odd lines* 
 #*to another file named ‘File2* ’.* 


file = open("input.txt", "r")
lines = file.readlines()
file1 = open("File1.txt", "w")
file2 = open("File2.txt", "w")
for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        file1.write(lines[i])
    else:
        file2.write(lines[i])
file.close()
file1.close()
file2.close()