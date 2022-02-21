infile = open("pelican.txt","r")
content = infile.read()
print(content)
print(type(content))

print("----------------------------------")

#the data is printed as a string

#change to a list
infile = open("pelican.txt","r")
content_list = infile.readlines()
print(content_list)

#print the length
print(len(content_list))

print("-----------------------------------")

#create a loop to display the text

for line in open("pelican.txt"):
    print(line, end="")