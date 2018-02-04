class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
    def insert(self,head,data):
        #Complete this methode
        if head==None:
            head=Node(data)
            return head
        else:
            tempNode=Node(data)
            current=head
            while current.next!=None:
                current=current.next
            current.next=Node(data)
            return head
    def sortedInsert(self,head, data):
        if head==None:
            head=Node(data)
            return head
        else:
            tempNode=Node(data)
            if tempNode.data<=head.data:
                tempNode.next=head
                head=tempNode
                return head
            else:
                current=head
                p=current
                q=p.next
                while current!=None:
                    if p.data>=tempNode.data and q.data<tempNode.data:
                        p.next = tempNode
                        tempNode.next=q
                        return head
                    p=p.next
                    q=p.next
                    current=current.next
                current.next=tempNode
                return head
    def sortedInsert1(self,head, data):
        tempNode = Node(data)
        if head==None:
            head = tempNode
            return head
        if data<head.data:
            tempNode.next=head
            head=tempNode
            return head
        else:
            current=head
            while current.next != None:
                next = current.next
                if data>=current.data and data<next.data:
                    current.next=tempNode
                    tempNode.next=next
                    return head
                current = current.next
                next=current.next
            current.next=tempNode
            return head

if __name__=="__main__":
    mylist = Solution()
    T = int(input())
    head = None
    print "Running"
    for i in range(T):
        data = int(input())
        head = mylist.sortedInsert1(head, data)
        mylist.display(head)
   # mylist.display(head);