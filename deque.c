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
void free_heap(Deque *d);
int len(Deque *d);
int cap(Deque *d);
bool is_empty(Deque *d);
bool is_full(Deque *d);
bool front(Deque *d, int *key);
bool back(Deque *d, int *key);
bool push_back(Deque *d, int key);
bool pop_front(Deque *d, int *key);
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
  free_heap(d);
}

void test_pop_front() {
  int capacity = 7;
  Deque *d = new (capacity);

  push_back(d, 1);
  push_back(d, 3);
  push_back(d, 5);

  int key = 0;

  assert(pop_front(d, &key));
  assert(len(d) == 2);
  assert(key == 1);

  assert(pop_front(d, &key));
  assert(len(d) == 1);
  assert(key == 3);

  assert(pop_front(d, &key));
  assert(len(d) == 0);
  assert(key == 5);

  assert(!pop_front(d, &key));
  free_heap(d);
}
int main() {
  test_push_back();
  test_pop_front();
  return 0;
}

Deque *new (int capacity) {
  if (capacity <= 0) {
    return NULL;
  }
  capacity += 1;
  // TODO make sure capacity is power of 2
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

void free_heap(Deque *d) {
  if (d != NULL) {
    free(d->data);
    free(d);
  }
};
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

bool pop_front(Deque *d, int *key) {
  if (is_empty(d)) {
    return false;
  }
  *key = d->data[d->tail];
  d->tail = (d->tail + 1) & (d->capacity - 1);
  return true;
}
