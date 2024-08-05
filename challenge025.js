/*
Circular Linked List

Prompt
Given a linked list, return true if the list is circular, false if it is not.



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

    iscircular() {
        let res = false;
        let temp01 = this.head;
        let temp02 = this.head;
        if (this.head) {
            temp01 = temp01.next;
            temp02 = temp02.next.next;
            if(temp01 == temp02) {
                temp01 = temp02;
                while(temp01 != temp02) {
                    temp01 = temp01.next;
                    temp02 = temp02.next;
                }
                res = true;
            }
        }
        return res;
    }
}
