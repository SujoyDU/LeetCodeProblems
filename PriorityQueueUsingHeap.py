#Implement Heap.
#Methods to impelement:
    # 1.buildHeap(list)
    # 2.findMax()
    # 3.Delete()
    # 4. Insert(k)
    # 5. isEmpty()
    # 6.size()


class Node:
    def __init__(self,val,priority):
        self.val = val
        self.priority = priority


class BinaryHeap:
    def __init__(self):
        self.items=[0]

    def __len__(self):
        return len(self.items)-1

    def insert(self,k):
        self.items.append(k)
        self.heapifyUp()

    def heapifyUp(self):
        i = len(self)
        while i //2 > 0:
            if self.items[i] > self.items[i // 2]:
                self.items[i],self.items[i // 2] = self.items[i //2], self.items[i]
            i = i // 2


    def heapifyDown(self,i):
        while ( i * 2) <= len(self):
            mc = self.maxChild(i)
            if self.items[i] < self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def maxChild(self,i):
        if i*2 + 1 > len(self):
            return i*2
        return i * 2 if self.items[i *2] > self.items[i * 2 +1] else i * 2 +1


    def delMax(self):
        max_val = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.heapifyDown(1)
        return max_val


    def buildHeap(self,numList):
        i = len(numList) // 2
        self.items = [0] + numList
        while(i > 0):
            self.heapifyDown(i)
            i = i -1


    def printHeap(self):
        if(len(self)>0):
            for i in range(1,len(self)//2+1):
                lc = "None"
                rc = "None"
                if 2*i <= len(self) :
                    lc = self.items[2*i]
                if 2*i + 1 <= len(self):
                    rc = self.items[2*i +1]
                print("Parent: {p} Left Child: {lch} Right Child {rch}".\
                      format(p=self.items[i],lch=lc, rch= rc))



x = BinaryHeap()
x.buildHeap([4,5,6,3])
x.insert(10)
x.insert(5)
x.insert(1)
x.printHeap()