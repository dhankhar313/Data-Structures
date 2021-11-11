#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int data;
    Node *next;
};
Node *getNewNode(int data)
{
    Node *newNode = new Node();
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
Node *head;
void printList()
{
    if (!head)
    {
        cout << "Head pointer is NULL" << endl;
        return;
    }
    Node *newNode = head;
    while (newNode)
    {
        cout << newNode->data << " ";
        newNode = newNode->next;
    }
    cout << endl;
}
void insertAt1(int data)
{
    Node *newNode = getNewNode(data);
    if (!head)
    {
        head = newNode;
        printList();
        return;
    }
    newNode->next = head;
    head = newNode;
    printList();
}
void insertAtLast(int data)
{
    Node *newNode = head;
    while (newNode->next)
    {
        newNode = newNode->next;
    }
    Node *newNode1 = getNewNode(data);
    newNode->next = newNode1;
    printList();
}
void insertAtN(int data, int position)
{
    if (position == 1)
    {
        insertAt1(data);
        return;
    }
    Node *newNode = head;
    for (int i = 0; i < position - 2; i++)
    {
        newNode = newNode->next;
    }
    Node *newNode1 = getNewNode(data);
    newNode1->next = newNode->next;
    newNode->next = newNode1;
    printList();
}
void deleteAt1()
{
    if (head)
    {
        Node *newNode = head;
        head = newNode->next;
        delete newNode;
        printList();
    }
}
void deleteAtLast()
{
    Node *newNode = head;
    while (newNode->next->next)
    {
        newNode = newNode->next;
    }
    Node *newNode1 = newNode->next;
    newNode->next = NULL;
    delete newNode1;
    printList();
}
void deleteAtN(int position)
{
    if (position == 1)
    {
        deleteAt1();
        return;
    }
    Node *newNode = head;
    for (int i = 0; i < position - 2; i++)
    {
        newNode = newNode->next;
    }
    Node *newNode1 = newNode->next;
    newNode->next = newNode1->next;
    delete newNode1;
    printList();
}
void recursive_reverse_print(Node *head_ref)
{
    if (!head_ref)
    {
        return;
    }
    recursive_reverse_print(head_ref->next);
    cout << head_ref->data << " ";
}
void reverse()
{
    Node *current = head;
    Node *prev = NULL;
    Node *tail;
    while (current)
    {
        tail = current->next;
        current->next = prev;
        prev = current;
        current = tail;
    }
    head = prev;
    printList();
}
int main()
{
    head = NULL;
    insertAt1(10);
    insertAtLast(20);
    insertAt1(30);
    insertAtN(40, 2);
    insertAtN(50, 3);
    insertAtN(60, 4);
    cout << "Reversed: ";
    recursive_reverse_print(head);
    cout << endl;
    reverse();
    deleteAt1();
    deleteAt1();
    deleteAtLast();
    deleteAtN(2);
    deleteAtN(1);
    deleteAt1();
}