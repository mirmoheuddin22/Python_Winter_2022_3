import string #String module, which is containing a set of constants.
myfile = open('file.txt','r') #Default value and reading the file.
d = dict() #Creating an empty dictionary.
for line in myfile: #Looping through each line of the file.
    line = line.lower().strip() #Avoiding case mismatch (lowercase) and removing the leading spaces and newline character.
    line = line.translate(line.maketrans("", "", string.punctuation)) #Deleting the punctuation marks from the line.
    words = line.split(" ") #Splitting the line into words.
    for i in words: #Iterating over each word in line
        if i in d:  #Checking if the word is already in dictionary.
            d[i] += 1   #Increment the word by 1.
        else:
            d[i] = 1  #Adding the word to dictionary with count 1.
for k in d.keys(): #d.keys():Returning a list of all keys in d.
    print('Counting words:') #Showing the comment.
    print(f'{k}: {d[k]}') #Printing the contents of dictionary.
myfile.close() #Closing files.

