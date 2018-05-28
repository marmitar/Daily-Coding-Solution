#include <stdlib.h>
#include <stdbool.h>

#define SIZE 10

typedef struct _trie {
    struct _trie **next;
    bool *pos_end, *neg_end;
} *Trie;

Trie new_trie(void) {
    Trie new = calloc(1, sizeof(struct _trie));
    new->next = calloc(SIZE, sizeof(Trie));
    new->pos_end = calloc(SIZE, sizeof(bool));
    new->neg_end = calloc(SIZE, sizeof(bool));
    return new;
}

void destroy_trie(Trie trie) {
    if (trie == NULL) {
        return;
    }

    for (size_t i = 0; i < SIZE; i++) {
        destroy_trie(trie->next[i]);
    }

    free(trie->next);
    free(trie->pos_end);
    free(trie->neg_end);
    free(trie);
}

void insert_value(Trie trie, int value) {
    int pos = value % 10;
    int rem = value / 10;

    if (rem != 0) {
        if (trie->next[pos] == NULL) {
            trie->next[pos] = new_trie();
        }

        insert_value(trie->next[pos], rem);

    } else {
        if (pos >= 0) {
            trie->pos_end[pos] = true;
        } else {
            trie->neg_end[pos] = true;
        }
    }
}

bool has_value(Trie trie, int value) {
    int pos = value % 10;
    int rem = value / 10;

    if (rem != 0) {
        if (trie->next[pos] == NULL) {
            return false;
        }

        return has_value(trie->next[pos], rem);

    } else {
        if (pos >= 0) {
            return trie->pos_end[pos];
        } else {
            return trie->neg_end[pos];
        }
    }
}

bool can_sum(int *numbers, size_t size, int k) {
    Trie exists = new_trie();

    for (size_t i = 0; i < size; i++) {
        if (has_value(exists, k - numbers[i])) {
            destroy_trie(exists);
            return true;
        } else {
            insert_value(exists, numbers[i]);
        }
    }

    destroy_trie(exists);
    return false;
}

int main(int argc, char const *argv[]) {
    int array[4] = {10, 15, 3, 6};

    return can_sum(array, 4, 17);
}
