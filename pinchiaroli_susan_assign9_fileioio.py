"""
file_io_nested.py
Write data from a set of nested lists to a file,
then read it back in.

By: Susan Pinchiaroli
Date: 28 Nov 2018
"""

data = []#empty list
# This is our data
data.append(['Susan','Davis',23,7])#append data
data.append(['Harold','Humperdink',76,9])
data.append(['Lysistrata','Jones',40,12])
data.append(['Stan','Laurel',60])
data.append(['Rose','Harris',56,9,'Ambassador'])

# filename is a string
fname = "people.txt"#create file name
ffirstobj=open(fname,'w')#open file name to write, so that once we complete the file it will be rewritten each time we code
ffirstobj.write('')#write nothing
ffirstobj.close()3close file
# open file for actual writing
fobj = open(fname, "w")
line_text=''
# write the data file
# iterate through the list of people
for i in range(len(data)):
    line = ""
    # iterate through each datum for the person
    for j in range(len(data[i])):
        # convert this datum to a string and append it to our line
        # NOTE: change this so it doesn't add ',' if this is last datum
        if j==(len(data[i])-1):#this separates so we know when to add comma and when not to
            line += str(data[i][j])
        else:
            line += str(data[i][j]) + ","
    
    # NOTE: now, write this line to the data file
    line_text += line +'\n'#write linebreak after each line
fobj.write(line_text)#write line_text into code
    

# Don't forget to close the file!
fobj.close()

print("Done writing the file.")


# Now, read the data back

# Open the file for reading
fobj = open("people.txt","r")

# read the whole file into a string
raw_dat = fobj.read()
print("Read:",raw_dat)

# break the string into a list of lines
data_list = raw_dat.split("\n")

# NOW: process your list of lines, so that you can put the
# data back into a new list of lists, called data2
# this should have the exact same format as your original data structure
data2 = []

# process data here

print("Final data list:")
print(data2)
