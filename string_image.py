#!/usr/bin/env python3
"""
 Author: Sboniso Gordon Mzizi
"""

def cone (number):
    width = number
    h = ""
    for i in range(width):
        h = 'H'*(i+1) + "H"*i
        h = h.rjust(width+i,' ') 
        print (h)
    space = ((1 +(2*(number-1))) - number)/2
    return(space)

def alpha_H(number,space):
    for i in range(number+1):
        h = 'H'*number
        line = h.rjust(len(h)+space," ") + h.rjust(len(h) *4," ")
        print(line)
    for i in range((number+1) //2):
        line = (h*5).rjust(len(h)*5 +space, " ")
        print (line)
    for i in range(number+1):
        h = 'H'*number
        line = h.rjust(len(h)+space," ") + h.rjust(len(h) *4," ")    
        print(line)
        
def r_cone (number,space):
    width = (number * 5)
    h = "" 
    for i in range(number,-1,-1):
        h = 'H'*(i-1) + "H"*i
        h = h.rjust(width +i -1 ,' ')
        print (h)
 

if __name__=="__main__":
    number = int(input())      
    space = int(cone(number)) 
    alpha_H(number,space)
    r_cone(number,space)