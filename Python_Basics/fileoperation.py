my_file = open('fruits.txt')
content = my_file.read()
my_file.close()
print(content)

with open('fruits.txt') as my_file1:
    content_1 = my_file1.read()

print(content_1)

with open('files/vegetables.txt','w') as my_file:
    my_file.write('Tomoto\n')
    my_file.write('Perper\n')

with open('files/vegetables.txt','a') as myFile:
    myFile.write('Onion\nCucumber')

# read & write
with open('files/vegetables.txt', 'a+') as myFile:
    myFile.write('\nEnd')
    myFile.seek(0)
    content2=myFile.read()

print(content2)      