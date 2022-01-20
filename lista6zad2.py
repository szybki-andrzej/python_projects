import time

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2      
        
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)        
        
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
            
    def size(self):
        return self.currentSize
    
    def isEmpty(self):
        return self.currentSize == 0
    
    def __str__(self):
        txt = "{}".format(self.heapList[1:])
        return txt

    def binHeapSort(self,tab):
        start = time.time()
        self.buildHeap(tab)
        result=[]
        for n in range(0, self.size()):
            result.append(self.delMin())
        return result,time.time()

        

def main():
    bh = BinHeap()
    print(bh.binHeapSort([4,6,7,3,9,10,11,45,6664,642235,22345]))
    bt = BinHeap()
    print(bh.binHeapSort([3,5,4,666]))

if __name__=="__main__":
    main()





    
        




    
