class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            self.last = cur.next

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def reverse_list(self):
        count = 0
        current = self.head
        old_current = current
        while current:
            try:
                if current.next:
                    count += 1
                    future_prev = current.next
                    if current == self.head:
                        current.next = None
                        old_current = current
                        current = future_prev
                        continue
                    current.next = old_current
                    old_current = current
                    current = future_prev

                elif not current.next and count == 0:
                    current.next = None
                    break
                else:
                    current.next = old_current
                    self.head = current
                    break
            except:
                print("Something went wrong..")
                break

    def sort_list(self):
        current = self.head
        arr_rep = []
        while current:
            arr_rep.append(current)
            if not current.next:
                self.last = current
            current = current.next
        
        sorted_linked_list = LinkedList()
        
        n = len(arr_rep)
        gap = n // 2
        
        while gap > 0:
            for i in range(gap, n):
                temp = arr_rep[i].data
                j = i
                while j >= gap and arr_rep[j - gap].data > temp:
                    arr_rep[j].data = arr_rep[j - gap].data
                    j -= gap
                arr_rep[j].data = temp
            
            gap //= 2

        for i in arr_rep:
            sorted_linked_list.insert_at_end(i.data)
        return sorted_linked_list

    @staticmethod
    def merge_lists(list_1, list_2):
        list_1.last.next = list_2.head
        merged_list = list_1.sort_list()
        return merged_list

            
    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = " ")
            current = current.next


llist = LinkedList()
llist_2 = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

llist_2 = LinkedList()
llist_2.insert_at_beginning(23)
llist_2.insert_at_beginning(13)
llist_2.insert_at_beginning(3)

# Вставляємо вузли в кінець
llist_2.insert_at_end(7)
llist_2.insert_at_end(88)

# Друк зв'язного списку
print("Зв'язний список:", end = " ")
llist.print_list()
llist.reverse_list()
print("\n")

print("Зв'язний список (reversed):", end = " ")
llist.print_list()
print("\n")

print("Зв'язний список 1 (sorted):", end = " ")
sorted_llist_1 = llist.sort_list()
sorted_llist_1.print_list()
print("\n")

print("Зв'язний список 2 (sorted):", end = " ")
sorted_llist_2 = llist_2.sort_list()
sorted_llist_2.print_list()
print("\n")

print("Обʼєднані списки:", end = " ")
merged_list = LinkedList.merge_lists(sorted_llist_1, sorted_llist_2)
merged_list.print_list()