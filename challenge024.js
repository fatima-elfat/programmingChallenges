/*
Remove Kth-Node from Linked List

Prompt
Using the Node and LinkedList classes that you created
in the previous question, add methods to it so that,
when given an kth-integer, you can delete that kth
 node from the linked list
*/

class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
    }
    set next(linked) {
        this.next = linked;
    }
}

class LinkedList {
    constructor() {
      this.head = null;
    }

    getFirst() {
        return this.head;
    }

    getLast() {
        let last = this.head;
        if(last) {
            while(last.next) {
                last = last.next;
            }
        }
        return last;
    }

    insertFirst(data) {
        if(this.head) {
            this.next = this.head;
            this.head = new Node(data);
            this.head.next = this.next;
        }
        else {
            this.head = new Node(data);
        }
    }

    insertLast(data) {
        let last = this.getLast();
        if(last) {
            this.next = new Node(data);
        }
        else {
            this.head = new Node(data);
        }
    }

    reverseList(head) {
        let temp01 = head;
        let temp02 = null;
        while(current) {
            temp01 = head.next;
            head.next = temp02;
            temp02 = head;
            head = temp01;
        }
        head = temp02;
        return head;
    }

    removeKth(k) {
        let temp01 = this.head;
        if(this.head) {
            if(n == 0) {
                this.head = temp01;
                temp01 = null;
            }
            else {
                while(n && temp01) {
                    if(temp01 && temp01.next) {
                        temp01 = temp01.next;
                        n--;
                    }
                }
            }
            temp01.next = temp01.next.next;
        }
    }
}
