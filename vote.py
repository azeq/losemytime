# coding: utf-8

# the file is orgarnized like this:
# 33DRfddf3,34,56
# id of the video, number of people who get bored, number of people who enjoyed the video

comma = ","

def insertNewElement(entry):
    print entry
    with open('chance.csv', 'r') as fR:
        l = list(fR)
        fR.close()
        i = 0
        hasBeenInserted = False
        for line in l:
            lineArray = line.split(comma)
            currentId = lineArray[0]
            nBored = int(lineArray[1])
            nEnjoyed = int(lineArray[2])
            if entry[0] <= currentId and not hasBeenInserted: # the last position
                # insert element
                if entry[0] == currentId:
                    if entry[1] == 'True':
                        nBored += 1
                    else:
                        nEnjoyed += 1
                    l.pop(i)
                    print "inserting new element in the middle..."
                    l.insert(i, currentId + comma + str(nBored) + comma + str(nEnjoyed) + '\n')
                else:
                    a = entry[1] == 'True'
                    nBored = "1" if a else "0"
                    nEnjoyed = "0" if a else "1"
                    print "inserting new element at the end..."
                    l.insert(i, entry[0] + comma + nBored + comma + nEnjoyed + '\n')
                hasBeenInserted = True
            i += 1
    print l

    with open('chance.csv', 'w') as fW:
        print "writing... "
        print entry
        fW.write(''.join(l))
        fW.close()

# for test purpose, when this file is executed
if __name__=='__main__':
    #new entry for test
    entryNewAtEnd = ["m",True] #id, bored = true, false = enjoyed
    entryAlreadyExists = ["i",True]
    entryIsFirst = ["a", False]

    insertNewElement(entryNewAtEnd)
    insertNewElement(entryAlreadyExists)
    insertNewElement(entryIsFirst)
    #p = input("New entry: ( letter, true/false):") # ex: 'a',False
    #insertNewElement(p)
