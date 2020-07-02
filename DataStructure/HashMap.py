class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class HashMap:

    def hash_func(self, key, table_len):
        return key % table_len

    def insert(self, hash_table, node, table_len):
        hash_key = self.hash_func(node.val, table_len)
        node.next = hash_table[hash_key]
        hash_table[hash_key] = node

    def search(self,hash_table, value, table_len):
        hash_key = self.hash_func(value, table_len)

        head = hash_table[hash_key]
        while head:
            if head.val == value:
                return True
            head = head.next

        return False


    def main(self):
        TABLE_LEN = 11
        hash_table = [0]*TABLE_LEN
        hash_node_vec = []
        test = [1,1,4,9,20,30,150,500]

        for i in range(8):
            hash_node_vec.append(ListNode(test[i]))

        for item in hash_node_vec:
            self.insert(hash_table, item, TABLE_LEN)

        print("Hash table:")
        for i in range(TABLE_LEN):
            print(f"[{i}]",)
            head = hash_table[i]
            while head:
                print(f"->{head.val}",)
                head = head.next


        print("Test Search:")

        for i in range(10):
            if self.search(hash_table, i, TABLE_LEN):
                print(f"{i} is in the table")
            else:
                print(f"{i} is not in the table")
        return


if __name__ == '__main__':
    hash = HashMap()
    hash.main()
