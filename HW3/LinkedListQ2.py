

class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def reverse(self):
        prev = None
        current = self.__head
        while(current is not None):
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        self.__head = prev
    
    def findNode(self,data):
        current_node = self.__head
        while(current_node is not None):
            if(current_node.get_data()==data):
                #print(current_node.get_data())
                return(current_node)
            current_node = current_node.get_next()
        
            

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

def count_nodes(biscuit_list):
    count=0
    # Write your logic here

    return count


a = [35, 1, 89, 47, 9, 100, 5]

linkedList = LinkedList()
for i in a:
    linkedList.add(i)
linkedList.reverse()
linkedList.display()