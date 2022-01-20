class BinHeap:
    def __init__(self,n):
        self.heapList = [0]
        self.currentSize = 0
        self.maxSize = n
        
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2      
        
    def insert(self,k):
        if self.size()>=self.maxSize:
            if self.heapList[0]>k:
                nothing
            else:
                self.heapList.append(k)
                self.currentSize = self.currentSize + 1
                self.percUp(self.currentSize)
                self.delMin()
                self.percUp(self.currentSize)
        else:
            self.heapList.append(k)
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)

        if self.currentSize > self.maxSize:
            self.delMin()
        
    def findMin(self):
        return self.heapList[1]

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1    
            
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
        while self.currentSize > self.maxSize:
            self.delMin()
        
            
    def size(self):
        return self.currentSize
    
    def isEmpty(self):
        return self.currentSize == 0
    
    def __str__(self):
        txt = "{}".format(self.heapList[1:])
        return txt

    

def main():
    bh = BinHeap(5)
    bh.buildHeap([30,5,2,8,45,56])
    print(bh)
    bt = BinHeap(3)
    bt.buildHeap([4,3,5,8,9,99])
    print(bt)
    bt.insert(100)
    print(bt)
    

if __name__=="__main__":
    main()
