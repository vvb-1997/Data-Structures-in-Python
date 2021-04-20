class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        
    def __iter__(self):
        node = self.head
        
        while node is not None:
            yield node
            node = node.next
            
    def add_first(self,node):
        node.next = self.head
        self.head = node
    
    def add_last(self,node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
    
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
    
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
            
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                new_node.next = node
                prev_node.next = new_node
                return
            prev_node = node
    
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
            
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
    
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def no_of_nodes(self):
        n=0
        node = self.head
        
        while node is not None:
            n+=1
            node = node.next
        
        return n
        
    def get(self,index):
        if self.head is None:
            raise Exception("List is empty")
        
        if(self.no_of_nodes()-1<index):
            raise Exception("No of Nodes not higher than {}".format(str(index)))
        
        node = self.head
        for _ in range(index):
            node = node.next
        
        return node.data
    
    def reverse(self):
        if self.head is None:
            raise Exception("List is empty")
        
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data

llist = LinkedList()
first_ele = Node('a')
llist.head = first_ele

second_ele = Node('b')
third_ele = Node('c')

first_ele.next = second_ele
second_ele.next = third_ele

for node in llist:
    print(node)

llist.add_first(Node('head'))
llist.add_after('c',Node('y'))
llist.add_before('c',Node('x'))
llist.remove_node('c')
llist.add_last(Node('tail'))

print(llist.no_of_nodes())
print(llist.get(5))
print(llist)

llist.reverse()
print(llist)
