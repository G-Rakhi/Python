class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def createLL(self,n):
        i=0
        while  i<n:
            val=int(input("Enter data:"))
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next!=None:
                    t=t.next
                t.next=new_node
            i+=1
    def show(self, head):
        t = head
        s=0
        print("\nList of Nodes:")
        while t:
            print(t.val,end=" ")
            s=s+t.val
            t=t.next
        print("\nTotal;",s)
    def split(self):
        slow,fast=self.head,self.head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        second=slow
        prev.next=None
        self.show(self.head)
        self.show(second)
obj=LinkedList()
n=int(input("enter n:"))
obj.createLL(n)
obj.show(obj.head)
obj.split()