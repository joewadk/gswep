#2 string inputs
#string 2 will have to contain items from string 1
#case insensitive

#base case, if either string is empty return false
#assume that order does not matter in note and magazine
#trivial case where note greater in length than magazine

#o(m+n) solution
#one loop to iterate through string 2 and initiate the map
#separate loop to iterate through string 1, and decrement if the item's value in the map >0
#if it isnt in the map or our count reached 0, return false and break

#consideration: initiate map using note or magazine. initiate using note and checking magazine is need based. initiate using magazine and checking note is seeing what you have

string1='help'
string2='hello people'

def makeNote(string1,string2):
    if len(string1)>len(string2):
        return False
    if string2=='' or string1=='':
        return False
    map={}
    for i in range(0,len(string1)): #iterate through note
        if string1[i] not in map:
            map[string1[i]]=1
        else:
            map[string1[i]]+=1
    for i in range(0,len(string2)):
        if string2[i] not in map:
            return False            #if any value not in map, cant make a note.
        elif map[string2[i]]==0:
            return False        #we've exhausted this letter and cant make note
        else:
            map[string2[i]]-=1
    return True
