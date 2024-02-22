def maxSeq(a):
    short = a[0]
    for i in range(len(a)):
        if(len(a[i])<len(short)):
            short = a[i]
    index = 0
    s = ""
    for i in range(len(short)):
        if(helper(a,i,short[i])):
            s += short[i]
    return(s)

def helper(a,pos,letter):
    for j in range(len(a)):
        if(a[j][pos]!=letter):
            return(False)
    return(True)  

a = ["flower","flow","flown"]
print(maxSeq(a))


