def buildseq(az, ao, function, n):
    az = az +0.0
    ao=ao+0.0
    output=[az,ao]
    for i in range(n):
        add = function(ao)/az
        output.append(add)
        az=ao
        ao=add
    return output
        
def periodic(inputlist):
    a = inputlist[0]
    b = inputlist[1]
    l = len(inputlist)
    i=2
    while i<l-2:
        if inputlist[i]==a and inputlist[i+1]==b:
            return i
        else:
            i = i+1
    return False 
        
        

def plusone(x):
    return x+1
def squared(x):
    return x*x
def plustwo(x):
    return x+2
def minusone(x):
    return x-1
def plusz(x):
    return x+.5
def line(x):
    return 3*x+1
b= buildseq(1,1,plustwo,400)
#print b
print periodic(b)
