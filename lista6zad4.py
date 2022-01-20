
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):#zmieniłem działanie funkcji względem tej z wykładu
        """Function that replace root of self with itself and make itself the leftChild for the previous root
             or is new leftChild if there is not rightChild of the root"""
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            t.rightChild = self.rightChild
            self.rightChild = None
            self.leftChild = t
            
    def insertRight(self,newNode):#tutaj również jak wyżej
        """Function that replace root of self with itself and make itself the rightChild for the previous root
            or is new rightChild if there is not rightChild of the root"""

        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            t.leftChild = self.leftChild
            self.rightChild = t
            self.leftChild  = None

    def setLeft(self,other):
        """Function that makes leftChild the root of new Binary Tree which's the same as given one"""
        self.leftChild = BinaryTree(other.key)
        if other.leftChild!=None:
            self.leftChild.setLeft(other.leftChild)
        if other.rightChild!=None:
            self.leftChild.setRight(other.rightChild)
        

    def setRight(self,other):
        """Function that makes rightChild the root of new Binary Tree which's the same as given one"""

        self.rightChild = BinaryTree(other.key)
        if other.leftChild!=None:
            self.rightChild.setLeft(other.leftChild)
        if other.rightChild!= None:
            self.rightChild.setRight(other.rightChild)

    def __add__(self,n = str):
        return self.key.__add__(n)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key 

    def deriv(self):
        """Function that return derivated BinaryTree based on given one."""
        if self.key == "+" or self.key == "-":
            self.leftChild.deriv()
            self.rightChild.deriv()

        elif self.key == "*":
            self.key = "+"
            self.insertLeft("*")
            self.insertRight("*")
            self.rightChild.setLeft(self.leftChild.leftChild)
            self.rightChild.setRight(self.leftChild.rightChild)
            self.leftChild.leftChild.deriv()
            self.rightChild.rightChild.deriv()

        elif self.key == "/":
            self.insertLeft("-")
            self.insertRight("*")
            self.leftChild.insertLeft("*")
            self.leftChild.insertRight("*")
            self.leftChild.rightChild.setLeft(self.leftChild.leftChild.leftChild)
            self.leftChild.rightChild.setRight(self.leftChild.leftChild.rightChild)
            self.rightChild.setLeft(self.leftChild.leftChild.rightChild)
            self.rightChild.setRight(self.leftChild.leftChild.rightChild)
            self.leftChild.leftChild.leftChild.deriv()
            self.leftChild.rightChild.rightChild.deriv()

        elif self.key == "exp":
            self.key = "*"
            self.insertRight("exp")
            self.rightChild.setLeft(self.leftChild)
            self.leftChild.deriv()

        elif self.key == "log":
            self.key = "/"
            self.setRight(self.leftChild)
            self.leftChild.deriv()

        elif self.key == "sin":
            self.key = "*"
            self.insertRight("cos")
            self.rightChild.setLeft(self.leftChild)
            self.leftChild.deriv()

        elif self.key == "cos":
            self.key = "*"
            self.insertRight("*")
            self.rightChild.setLeft(self.leftChild)
            self.rightChild.insertLeft("sin")
            self.rightChild.insertRight("-1")
            self.leftChild.deriv()

        elif self.key == "**":
            self.key = "*"
            self.insertLeft(self.leftChild)
            self.leftChild.key="**"
            self.rightChild = BinaryTree(self.leftChild.rightChild.key)
            self.leftChild.rightChild.key = self.leftChild.rightChild.key +"-1"

        elif self.key == "x":
            self.key = "1"

        else:
            self.key = "0"

        return self

    def finalEquation(self):
        """Function returns string representation of BinaryTree."""
            
        if self.key == "+" or self.key == "-" or self.key == "*" or self.key == "/" or self.key == "**":
            return self.leftChild.finalEquation()+self.key+self.rightChild.finalEquation()
        elif self.key == "sin" or self.key == "cos" or self.key == "exp" or self.key == "log":
            return self.key + self.leftChild.finalEquation()
        else:
            return self.key

def main():
    bt1 = BinaryTree("*")
    bt1.leftChild = BinaryTree("x")
    bt1.rightChild = BinaryTree("**")
    bt1.rightChild.leftChild = BinaryTree("x")
    bt1.rightChild.rightChild = BinaryTree("5")

    bt2 = BinaryTree("-")
    bt2.leftChild = BinaryTree("exp")
    bt2.leftChild.leftChild = BinaryTree("+")
    bt2.leftChild.leftChild.leftChild = BinaryTree("x")
    bt2.leftChild.leftChild.rightChild = BinaryTree("1")
    bt2.rightChild = BinaryTree("x")

    bt3 = BinaryTree("/")
    bt3.leftChild = BinaryTree("sin")
    bt3.leftChild.leftChild = BinaryTree("x")
    bt3.rightChild = BinaryTree("cos")
    bt3.rightChild.leftChild = BinaryTree("x")


    bt4 = BinaryTree("log")
    bt4.leftChild = BinaryTree("*")
    bt4.leftChild.leftChild = BinaryTree("2")
    bt4.leftChild.rightChild = BinaryTree("x")

    print(bt1.finalEquation())
    print(bt1.deriv().finalEquation())
    print(bt2.finalEquation())
    print(bt2.deriv().finalEquation())
    print(bt3.finalEquation())
    print(bt3.deriv().finalEquation())
    print(bt4.finalEquation())
    print(bt4.deriv().finalEquation())

if __name__=="__main__":
    main()