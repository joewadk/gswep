string1="cata"
string2="cathartic"


#initial approach: 2 pointers

#base case where prefix string (string 1) is empty
#edge case where string 1 is longer than string 2
#another case, where string1==string 2
#because it is case insensitive, we will have to apply the lower function
#stopping condition is that if prefix pointer reaches the end, we've exhausted our prefix string and is confirmed prefix

def isPrefix(string1, string2):
    i=0 
    if string1=='':
        return True

    if len(string1)>len(string2):
        return False

    if string1== string2:
        return True



    while string1[i]!=string1[::-1][0]:
        if(string1[i]!=string2[i]):         #at any point where there is a disjoint, return false immediately
            return False
        i+=1 #increment if the prefix pointer and string pointer holds
    return True #<--- potential error here
print(isPrefix(string1,string2))
#first submission returned true as expected for cat and cathartic
#second submission for cata and cathartic was not correct. 