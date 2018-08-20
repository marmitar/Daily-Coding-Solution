#include <iostream>
#include <random>
#include <vector>
using namespace std;

template <class T>
struct UnivalTest {
    bool unival;
    unsigned subs;
    T data;
};

template <class T>
struct Node {
    T value;
    Node *left;
    Node *right;

    Node(T val) :
    value(val), left(nullptr), right(nullptr) {}

    Node(T val, Node<T> &left, Node<T> &right) :
    value(val), left(&left), right(&right) {}

    UnivalTest<T> unival() {
        UnivalTest<T> l; // left
        if (left == nullptr) {
            l = {true, 0, value};
        } else {
            l = left->unival();
        }

        UnivalTest<T> r; // right
        if (right == nullptr) {
            r = {true, 0, value};
        } else {
            r = right->unival();
        }

        UnivalTest<T> t; // this
        t.data = value;
        t.subs = l.subs + r.subs;

        if (l.unival && r.unival && l.data == t.data && r.data == t.data) {
            t.unival = true;
            t.subs++;
        } else {
            t.unival = false;
        }

        return t;
    }
};

template <class T>
class Tree {
    private:
        Node<T> *root;
        unsigned depth;

        std::mt19937_64 rng;
        std::bernoulli_distribution dist;

        void insert_rec(Node<T> *root, T val) {
            if (choose()) {
                if (root->left == nullptr) {
                    root->left = new Node<T>(val);
                } else {
                    insert_rec(root->left, val);
                }
            } else {
                if (root->right == nullptr) {
                    root->right = new Node<T>(val);
                } else {
                    insert_rec(root->right, val);
                }
            }
        }

        vector<string> strs_rec(Node<T> *root) {
            if (root == nullptr) {
                return vector<string>();

            } else {
                vector<string> vl = strs_rec(root->left);
                vector<string> vr = strs_rec(root->right);

                auto lend = vl.end();
                auto rend = vr.end();
                auto s1 = vl.begin(), s2 = vr.begin();

                vector<string> v;

                string top = "";
                if (s1 != lend) {
                    top += string((*s1).length(), ' ');
                }
                top += to_string(root->value);
                if (s2 != rend) {
                    top += string((*s2).length(), ' ');
                }

                v.push_back(top);

                for (; s1 != lend && s2 != rend; s1++, s2++) {
                    v.push_back(*s1 + " " + *s2);
                }

                for (; s1 != lend; s1++) {
                    v.push_back(*s1 + " " + string((*s1).length(), ' '));
                }

                for (; s2 != rend; s2++) {
                    v.push_back(string((*s2).length(), ' ') + " " + *s2);
                }

                return v;
            }
        }

        int nodes_rec(Node<T> *root) {
            if (root == nullptr) {
                return 0;
            } else {
                return 1 + nodes_rec(root->left) + nodes_rec(root->right);
            }
        }

        int height_rec(Node<T> *root) {
            if (root == nullptr) {
                return 0;
            } else {
                return 1 + max(height_rec(root->left), height_rec(root->right));
            }
        }

    public:
        Tree() : root(nullptr), depth(0), dist() {
            rng.seed(std::random_device()());
        }

        void insert(T val) {
            if (root != nullptr) {
                insert_rec(root, val);
            } else {
                root = new Node<T>(val);
            }
        }

        unsigned unival() {
            if (root == nullptr) {
                return 0;
            }

            return root->unival().subs;
        }

        bool choose() {
            return dist(rng);
        }

        void print() {
            auto strs = strs_rec(root);

            for (auto s = strs.begin(); s != strs.end(); s++) {
                cout << *s << endl;
            }
        }
};

int main(int argc, char *argv[]) {
    Tree<int> tree;
    for (int i = 0; i < 10; i++) {
        tree.insert(tree.choose());
    }

    tree.print();

    cout << "Univals: " << tree.unival() << endl;

    return 0;
}