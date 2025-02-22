# with open("output.txt","w")as file:
#      file.write("Hello,file\n")
# with open("output.txt","a")as file:
#       file.write("Hi siva\n")
# with open("output.txt","r")as file:
#      content=file.read()
#      print(content)
# with open("output.txt","r")as file:
#      for line in file:
#           print(line.strip())

File=open("output.txt","r")
print(File.read())
print(File.readline())
print(File.read(6))
File.close()
