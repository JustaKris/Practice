from provided_classes import SinglyLinkedListNode, SinglyLinkedList

# Complete the mergeLists function below.


def mergeLists(head1, head2):
    # Create a dummy node as the head of the merged list
    dummy = SinglyLinkedListNode(0)
    current = dummy

    # Iterate through both lists
    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # Add remaining nodes if any
    if head1:
        current.next = head1
    else:
        current.next = head2

    return dummy.next


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        while llist3:
            print(llist3.data, end=' ')
            llist3 = llist3.next

"""Sample Input 1
1
3
1
2
3
2
3
4
"""

"""Sample input 2
1
3
4
5
6
3
1
2
10
"""
