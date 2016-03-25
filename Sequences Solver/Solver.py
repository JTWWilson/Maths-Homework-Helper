##Sequence Solver
##
##-OUTPUT- Nth term
##       - Next 3 terms
##       - 100th term
import misc
import math

def checkType(seq):
    """
    Identify the type of sequence given
    :argument seq: The sequence that is used
    :returns type: Either returns 'linear' or 'quadratic' depending on what type of equation it is
    """
    if type(findDif(seq)) is int:
        return 'linear'
    else:
        return 'quadratic'

def findDif(seq):
    """
    Finds the difference between each number in the sequence provided,
    if the difference between each of them is the same, it must be linear, if not; quadratic
    :argument seq: The sequence that is tested by the function
    :returns nextLayer[0]: If it is linear it returns the number that it goes up in
    :returns nextLayer: If it is quadratic then it returns all of the differences between the terms
    """
    nextLayer=[]
    i=0
    while i<(len(seq)-1):
        nextLayer.append(seq[i+1]-seq[i])
        i+=1
    if misc.all_same(nextLayer)==True:
        return nextLayer[0]
    else:
        return nextLayer

def nthTerm(seq): ##outputs the nthTerm rule
    """
    Outputs the nth term rule written as n=n^a
    """
    if checkType(seq)=='linear': ##if it's a linear sequence then the nth term
        coefficient=findDif(seq) ##must be the difference between the numbers
        constant=seq[0]-coefficient ##plus or minus a constant
        if constant==0:
            constant=''
        elif constant>0:
            constant='+'+str(constant)
        return 'n=%sn%s' %(str(coefficient),str(constant))
    if checkType(seq)=='quadratic': ##if it's a quadratic sequence
        layer=seq
        index=0
        while type(layer) is not int:
            layer=findDif(layer)
            index+=1
            if index>20:
                return 'error'
        coefficient=seq
        for i in range(0,index,1):
            coefficient=findDif(coefficient)
        print(layer)
        coefficient=coefficient/2/index
        print(coefficient)

        constant=seq[0]-coefficient*pow(1,index) ##useless "*(1^index)" just there for sensibility
        if constant==0:
            constant=''
        elif constant>0:
            constant='+'+str(constant)
        if coefficient==1:
            coefficient=''
        return 'n=%sn^%s%s' %(str(coefficient),str(index),str(constant))

def findTerm(seq,Pos): ##predicts a number in a given seq
    if checkType(seq)=='linear':
        coefficient=findDif(seq)

        constant=seq[0]-coefficient
        return (coefficient*Pos)+constant
    if checkType(seq)=='quadratic':
        layer=seq
        index=0
        while type(layer) is not int:
            layer=findDif(layer)
            index+=1
            if index>20:
                return 'error'
        coefficient=seq
        for i in range(0,index,1):
            coefficient=findDif(coefficient)
        coefficient=coefficient/index/2
        constant=seq[0]-coefficient*pow(1,index)
        return (coefficient*pow(Pos,index)+constant)

def main():
    Input=input('What is the sequence? ')
    Sequence=Input.split()
    Seq=[]
    for item in Sequence:
        Seq.append(int(item))
    #Seq=[int(a) for a in Seq]
    print('The Nth Term is... '+nthTerm(Seq))
    print('The next three terms are... '+str(findTerm(Seq,len(Seq)+1))+','+str(findTerm(Seq,len(Seq)+2))+','+str(findTerm(Seq,len(Seq)+3)))
    print('The 100th term is... '+str(findTerm(Seq,100)))
    main()

main()
