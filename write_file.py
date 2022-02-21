infile = open("pelican.txt","w")
infile.write("A wonderful bird is the pelican," "\n")
infile.write("His bill holds more than his belican," "\n")
lines = "He can take in his beak," "\n" "Enough food for a week," "\n" "But I'm damned if i see how the helican." "\n"
infile.write(lines)

#the \n indicates a new line
#be careful where you put the commas as it could read it as a list and not a string

infile = open("pelican.txt","r")
content = infile.read()
print(content)