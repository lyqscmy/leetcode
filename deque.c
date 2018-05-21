#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Deque {
  int *data;
  int head;
  int tail;
  int capacity;
} Deque;

Deque *new (int capacity);
int len(Deque *d);
int cap(Deque *d);
bool is_empty(Deque *d);
bool is_full(Deque *d);
bool front(Deque *d, int *key);
bool back(Deque *d, int *key);
bool push_back(Deque *d, int key);
bool pop_front(Deque *d, int key);
/* int pop_back(Deque *d, int key); */
/* int push_front(Deque *d, int key); */
void print_dequeue(Deque *d) {
  printf("head=%d\ttail=%d\tcapacity=%d\n", d->head, d->tail, d->capacity);
}

void test_push_back() {
  int capacity = 7;
  Deque *d = new (capacity);
  assert(d != NULL);
  assert(cap(d) == 7);
  assert(len(d) == 0);
  push_back(d, 1);
  assert(len(d) == 1);
  push_back(d, 3);
  assert(len(d) == 2);
  int key = 0;
  assert(front(d, &key) == true);
  assert(key == 1);
  assert(back(d, &key) == true);
  assert(key == 3);
}

int main() {
  test_push_back();
  return 0;
}

Deque *new (int capacity) {
  capacity += 1;
  if (capacity % 2 != 0) {
    capacity += 1;
  }
  int *data = malloc(sizeof(int) * capacity);
  Deque *d = malloc(sizeof *d);
  if (data == NULL || d == NULL) {
    free(data);
    free(d);
    return NULL;
  }
  d->head = 0;
  d->tail = 0;
  d->capacity = capacity;
  d->data = data;
  return d;
}

int len(Deque *d) { return (d->head - d->tail) & (d->capacity - 1); }

int cap(Deque *d) { return d->capacity - 1; }

bool is_empty(Deque *d) { return d->head == d->tail; }

bool is_full(Deque *d) { return d->capacity - len(d) == 1; }

bool front(Deque *d, int *key) {
  if (is_empty(d)) {
    return false;
  }
  *key = d->data[d->tail];
  return true;
}

bool back(Deque *d, int *key) {
  if (is_empty(d)) {
    return false;
  }
  *key = d->data[(d->head - 1) & (d->capacity - 1)];
  return true;
}

bool push_back(Deque *d, int key) {
  if (is_full(d)) {
    return false;
  }
  d->data[d->head] = key;
  d->head = (d->head + 1) & (d->capacity - 1);
  return true;
}

bool pop_front(Deque *d, int key) {
  if (is_empty(d)) {
    return false;
  }
  key = d->data[d->tail];
  d->tail = (d->tail - 1) & (d->capacity - 1);
  return true;
}
