file_counts={"jpg":10, "txt":7, "csv":10, "py":11}

for extension in file_counts:
    print(extension)
    
    
for extension in file_counts:
    print("{} --> {}".format(extension, file_counts[extension]))
    

for key, value in file_counts.items():
    print("There are {} file in .{} format.".format(value,key))
    
print(file_counts.keys())

print(file_counts.values())

for key in file_counts.keys():
    print(key)
    
for value in file_counts.values():
    print(value)
    
    