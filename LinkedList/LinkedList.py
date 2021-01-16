from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def prepend(self, data=None):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find_key(self, key):
        current = self.head
        while current:
            if current.data == key:
                print("Found key: " + str(key))
                return current
            current = current.next

        print("Key not found: " + str(key))
        return current

    def insert_after(self, key, data):
        prev_node = self.find_key(key)
        if prev_node:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def delete_by_key(self, key):
        current = self.head
        prev_node = None

        while current:
            if current.data == key:
                if current is self.head:
                    self.head = self.head.next
                else:
                    prev_node.next = current.next
                current.next = None
                print("Deleted key: " + str(key))
                return
            prev_node = current
            current = current.next

        print('Key not found: ' + str(key))

    def delete_by_pos(self, position = None):
        current = self.head
        current_position = 0
        while current:
            if position == 0:
                self.head = self.head.next
                current.next = None
                print ('Deleted head: ' + current.data)
                return

            prev_node = current
            current = current.next
            current_position += 1

            if current_position == position:
                prev_node.next = current.next
                current.next = None
                print ('Delete at pos: {0}, key: {1}'.format(position, current.data))
                return

        print('Position {0} exceeded length {1}'.format(position, len(self)))

    def reverse(self):
        # HEAD -> A -> B -> C -> None
        #  prev  curr  next
        # HEAD -> C -> B -> A -> None
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def remove_duplicates(self):
        current = self.head
        duplicate_set = set()

        previous = None
        while current:
            if current.data in duplicate_set:
                previous.next = current.next
                current.next = None
            else:
                duplicate_set.add(current.data)
                previous = current
            current = previous.next

    def is_cycle(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                print('Found cycle at ' + slow_pointer.data)
                return True

        return False


    def swap(self, key1, key2):
        if key1 == key2:
            print("Same keys - no swap")
            return

        prev_node_1 = None
        current_node_1 = self.head

        prev_node_2 = None
        current_node_2 = self.head

        # move until you find key1
        while current_node_1 and current_node_1.data != key1:
            prev_node_1 = current_node_1
            current_node_1 = current_node_1.next

        # move until you find key2
        while current_node_2 and current_node_2.data != key2:
            prev_node_2 = current_node_2
            current_node_2 = current_node_2.next

        if not current_node_1 or not current_node_2:
            print("At least one of the key is missing")
            return

        # Case1: first node is head
        # Case2: first node is not head
        if not prev_node_1:
            self.head = current_node_2
        else:
            prev_node_1.next = current_node_2

        if not prev_node_2:
            self.head = current_node_1
        else:
            prev_node_2.next = current_node_1

        current_node_1.next, current_node_2.next = current_node_2.next, current_node_1.next

    def print_list(self):
        if self.head:
            current = self.head
            print('HEAD', end = '->')
            while current:
                print(current.data, end='->')
                current = current.next
        print('None')

    def move_tail_to_head(self):
        if self.head and self.head.next:
            current = self.head
            previous = None
            while current.next:
                previous = current
                current = current.next

            previous.next = current.next
            current.next = self.head
            self.head = current

if __name__ =="__main__":
    list = LinkedList()
    list.append('A')
    list.append('B')
    list.prepend('C')
    list.prepend('D')
    list.print_list()
    list.insert_after('Z', 'Z')
    list.insert_after('C', 'Z')
    list.print_list()
    list.delete_by_key('Z')
    list.print_list()
    list.delete_by_key('D')
    list.print_list()
    list.delete_by_key('X')
    list.print_list()
    list.delete_by_pos(0)
    list.print_list()
    list.delete_by_pos(1)
    list.print_list()
    list.append('B')
    list.append('C')
    list.delete_by_pos(100)
    list.append('D')
    list.append('E')
    print(len(list))
    list.print_list()
    list.swap('A', 'B')
    list.print_list()
    list.swap('A', 'D')
    list.print_list()
    list.swap('A', 'A')
    list.swap('A', 'Z')
    list.reverse()
    list.print_list()

    dups_list = LinkedList()
    dups_list.prepend(1)
    dups_list.prepend(2)
    dups_list.prepend(2)
    dups_list.prepend(3)
    dups_list.prepend(3)
    dups_list.prepend(3)
    dups_list.prepend(0)
    dups_list.print_list()
    dups_list.remove_duplicates()
    dups_list.print_list()
