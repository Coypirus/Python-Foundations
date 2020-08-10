f = open("MyData", 'r')

f1 = open("abc", 'w')

for data in f:
    f1.write(data)

#You need to access photos in binary format
photo = open("CloneCaptainRex.png", "rb") #rb means read binary.

photo1 = open("CopyofRex.png", "wb") #wb means write binary

for i in photo:
    photo1.write(i)