import datetime #for getting the universal type that can be formatted to any timezone
print datetime.datetime.utcnow()

class Node:
    def __init__(self, dataval=None):
        self.timestamp=timestamp
        self.nodeNumber=nodeNumber
        self.referenceNodeId = referenceNodeId
        seld.nodeId=nodeId
        self.childReferenceNodeId=childReferenceNode
        self.genesisReferenceNode= genesisReferenceNode
        self.HashValue = HashValue
        self.data = data
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata):   
        NewNode = Node(newdata)

        
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode



class Encryption:
    def encrypt(self.data,s):
    result = ""
 
    
    for i in range(len(self.data)):
        char = text[i]
 
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
