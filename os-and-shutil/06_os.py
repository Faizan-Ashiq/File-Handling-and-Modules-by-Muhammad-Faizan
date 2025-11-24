import os 


a = os.listdir("dir")
print(a)
# print(os.get())
print(os.path.exists("faizan"))
os.remove("dir/samples.txt")
os.rmdir("dir")