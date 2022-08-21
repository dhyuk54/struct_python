class SingleNode(object):
    """单链表的结点"""

    def __init__(self, item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self.__head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item, end=' ')
            cur = cur.next
        print()

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将__head指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = SingleNode(item)
            node.next = pre.next
            pre.next = node

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.element == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == '__main__':
    li = SingleLinkList()
    print(li.is_empty())
    print(li.length())
    li.append(1)
    print(li.is_empty())
    print(li.length())
    li.add(8)
    li.append(2)
    li.append(3)
    li.append(4)
    li.append(5)
    li.append(6)
    # 812345
    li.insert(-1, 9)
    li.insert(2, 100)  # 811002345
    li.insert(11, 200)  #
    li.travel()
    li.remove(100)
    li.travel()
    li.remove(200)
    li.travel()
