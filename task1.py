import copy

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data: int):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.get_last_node()
            last_node.next = new_node

    def insert_after(self, prev_node: Node, data: int):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def insert_before(self, next_node: Node, data: int):
        if next_node is None:
            print("Немає такого наступного вузла.")
            return
        
        if next_node == self.head:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        
        while current.next != next_node:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, node: Node):
        cur = self.head
        if cur and cur == node:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur != node:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def reverse_list(self):
        first_node = self.head
        
        while first_node.next:
            new_node = Node(first_node.next.data)
            self.insert_at_beginning(new_node.data)
            self.delete_node(first_node.next)
            
    def get_last_node(self):
        current = self.head
        while current.next:
            current = current.next
        return current
    
    def sort(self, reversed=False):
        
        # define the first node as an end of a sorted linked list
        end_of_sorted = self.head
        
        # do some sort stuff while there are nodes outside of a sorted part
        while end_of_sorted.next:
            
            # if next element is bigger than the end of sorted part, just add it to sorted part
            if end_of_sorted.next.data >= end_of_sorted.data:
                end_of_sorted = end_of_sorted.next
                continue
            
            # if not, compare an outside node with every in sorted part (current)
            current = self.head
            while current != end_of_sorted.next:
                if end_of_sorted.next.data <= current.data:
                    self.insert_before(current, end_of_sorted.next.data)
                    self.delete_node(end_of_sorted.next)
                    break
                current = current.next
            

def merge_and_sort_llists(sorted_llist1: LinkedList, sorted_llist2: LinkedList) -> LinkedList:
    # create new linked list equivalent to the first sorted linked list
    new_list = copy.deepcopy(sorted_llist1)
    
    # define its last node as the end of a sorted part
    end_of_sorted = new_list.get_last_node()
    
    # merge two lists
    end_of_sorted.next = sorted_llist2.head

    # do some sort stuff while there are nodes outside of a sorted part
    current = new_list.head
    
    while end_of_sorted.next:
            
            # if next element is bigger than the end of sorted part, just merge two parts
            if end_of_sorted.next.data >= end_of_sorted.data:
                end_of_sorted = end_of_sorted.next
                return new_list
            
            # if not, compare an outside node with every in sorted part (current)
            while current != end_of_sorted.next:
                if end_of_sorted.next.data <= current.data:
                    new_list.insert_before(current, end_of_sorted.next.data)
                    new_list.delete_node(end_of_sorted.next)
                    break
                current = current.next
    return new_list

if __name__ == "__main__":

    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(7)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)
    llist.insert_at_end(16)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()
    print()

    # # Пошук елемента у зв'язному списку
    # print("\nШукаємо елемент 15:")
    # element = llist.search_element(15)
    # if element:
    #     print(element.data)

    llist.reverse_list()

    print("Reversed linked list:")
    llist.print_list()
    print()
    
    llist.sort()

    print("Відсортований зв'язний список:")
    llist.print_list()
    print()
    print()

    print("Merge and sort two sorted linked lists:")
    print()
    
    llist1 = LinkedList()
    
    llist1.insert_at_end(2)
    llist1.insert_at_end(4)
    llist1.insert_at_end(6)
    llist1.insert_at_end(8)
    llist1.insert_at_end(10)
    
    print("sorted llist1: ", end='')
    llist1.print_list()
    print()
    
    llist2 = LinkedList()
    
    llist2.insert_at_end(3)
    llist2.insert_at_end(5)
    llist2.insert_at_end(7)
    llist2.insert_at_end(9)
    llist2.insert_at_end(11)
    llist2.insert_at_end(13)
    llist2.insert_at_end(15)
    llist2.insert_at_end(17)
    
    print("sorted llist2: ", end='')
    llist2.print_list()
    print()

    merge_and_sort_llists(llist1, llist2).print_list()
    print()