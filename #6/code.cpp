#include <iostream>
#include <cstdint>

#define XOR(p1, p2) \
    (decltype(p1))((uintptr_t)p1^(uintptr_t)p2)

class Node {
        Node *both;

    public:
        void *data;
        Node(void *element) {
            data = element;
            both = nullptr;
        }
        Node(void) {
            data = nullptr;
            both = nullptr;
        }

        void add(void *element) {
            Node *new_node = new Node(element);

            Node *prev = nullptr;
            Node *curr = this;
            Node *next = XOR(prev, curr->both);

            while (next != nullptr) {
                prev = curr;
                curr = next;
                next = XOR(curr->both, prev);
            }

            curr->both = XOR(new_node, curr->both);
            new_node->both = curr;
        }

        Node get(int index) {
            Node *curr = this;
            Node *next = both;

            for (int i = 0; i < index && next != nullptr; i++) {
                Node *prev = curr;
                curr = next;
                next = XOR(curr->both, prev);
            }

            return next;
        }
};

int main(void) {
    Node raiz = Node();

    for (int i = 0; i < 10; i++) {
        raiz.add(&i);
    }

    std::cout << *((int *)raiz.get(6).data) << std::endl;

    return EXIT_SUCCESS;
}