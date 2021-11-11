#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int data;
    Node *prev;
    Node *next;
};
Node *head;
Node *getNewNode(int data)
{
    Node *newNode = new Node();
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}
void printListWithAddresses()
{
    Node *temp = head;
    while (temp)
    {
        if (temp == head)
        {
            cout << "[Head " << temp->prev << "|" << temp << "|" << temp->data << "|" << temp->next << "]";
        }
        else if (temp->next == NULL)
        {
            cout << "-> [Tail: " << temp->prev << "|" << temp << "|" << temp->data << "|" << temp->next << "]";
        }
        else
        {
            cout << "-> [" << temp->prev << "|" << temp << "|" << temp->data << "|" << temp->next << "]";
        }
        temp = temp->next;
    }
    cout << endl;
}
void printListWithoutAddresses()
{
    Node *temp = head;
    while (temp)
    {
        if (temp == head)
        {
            cout << "[Head: " << temp->data << "]";
        }
        else if (temp->next == NULL)
        {
            cout << "-> [Tail: " << temp->data << "]";
        }
        else
        {
            cout << "-> [" << temp->data << "]";
        }
        temp = temp->next;
    }
    cout << endl;
}
void insertAt1(int data)
{
    Node *newNode = getNewNode(data);
    if (head == NULL)
    {
        head = newNode;
        printListWithoutAddresses();
        return;
    }
    Node *newNode1 = head;
    newNode1->prev = newNode;
    newNode->next = head;
    head = newNode;
    printListWithoutAddresses();
}
void insertAtLast(int data)
{
    Node *newNode2 = getNewNode(data);
    Node *newNode = head;
    while (newNode->next)
    {
        newNode = newNode->next;
    }
    newNode2->prev = newNode;
    newNode->next = newNode2;
    newNode2->next = NULL;
    printListWithoutAddresses();
}
void insertAtN(int data, int position)
{
    Node *newNode2 = getNewNode(data);
    Node *newNode = head;
    for (int i = 0; i < position - 2; i++)
    {
        newNode = newNode->next;
    }
    newNode2->next = newNode->next;
    newNode2->prev = newNode;
    newNode->next->prev = newNode2;
    newNode->next = newNode2;
    printListWithoutAddresses();
}
void print_reverse_list()
{
    Node *newNode = head;
    while (newNode->next)
    {
        newNode = newNode->next;
    }
    while (newNode)
    {
        cout << newNode->data << " ";
        newNode = newNode->prev;
    }
}

int main()
{
    head = NULL;
    insertAt1(20);    // 20
    insertAtLast(30); // 20 30
    insertAt1(40);    // 40 20 30
    insertAtLast(50); // 40 20 30 50
    insertAtLast(60); // 40 20 30 50 60
    insertAtN(70, 3); // 40 20 70 30 50 60
    insertAtN(80, 5); // 40 20 70 30 80 50 60
    print_reverse_list();
}