#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Heap {
  int *data;
  int length;
  int capacity;
} Heap;

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

Heap *new_heap(int capacity) {
  if (capacity <= 0) {
    return NULL;
  }
  int *data = malloc(sizeof(int) * capacity);
  Heap *heap = malloc(sizeof *heap);
  if (data == NULL || heap == NULL) {
    free(data);
    free(heap);
    return NULL;
  }
  heap->data = data;
  heap->length = 0;
  heap->capacity = capacity;
  return heap;
}

void free_heap(Heap *heap) {
  if (heap != NULL) {
    free(heap->data);
    free(heap);
  }
}

int sift_up(Heap *heap, int start, int pos) {
  assert(pos >= start);
  int elm = heap->data[pos];
  while (pos > start) {
    int parent = (pos - 1) / 2;
    if (elm <= heap->data[parent]) {
      break;
    }
    heap->data[pos] = heap->data[parent];
    pos = parent;
  }
  heap->data[pos] = elm;
  return pos;
}

int sift_down_range(Heap *heap, int pos, int end) {
  assert(pos >= 0 && pos < end);
  int elem = heap->data[pos];
  int child = 2 * pos + 1;
  while (child < end) {
    int right = child + 1;
    if (right < end && (heap->data[child] < heap->data[right])) {
      child = right;
    }
    if (elem >= heap->data[child]) {
      break;
    }
    heap->data[pos] = heap->data[child];
    pos = child;
    child = 2 * pos + 1;
  }
  heap->data[pos] = elem;
  return pos;
}

void sift_down(Heap *heap, int pos) {
  int len = heap->length;
  sift_down_range(heap, pos, len);
}

void sift_down_bottom(Heap *heap, int pos) {
  int end = heap->length;
  assert(pos >= 0 && pos < end);
  int start = pos;
  int elem = heap->data[pos];
  int child = 2 * pos + 1;
  while (child < end) {
    int right = child + 1;
    if (right < end && (heap->data[child] < heap->data[right])) {
      child = right;
    }
    heap->data[pos] = heap->data[child];
    pos = child;
    child = 2 * pos + 1;
  }
  heap->data[pos] = elem;
  sift_up(heap, start, pos);
}

bool pop(Heap *heap, int *key) {
  if (heap->length == 0) {
    return false;
  }

  heap->length -= 1;
  *key = heap->data[heap->length];
  if (heap->length != 0) {
    swap(key, heap->data);
    sift_down_bottom(heap, 0);
  }

  return true;
}

bool push(Heap *heap, int key) {
  int old_len = heap->length;
  if (old_len == heap->capacity) {
    return false;
  }

  heap->data[old_len] = key;
  sift_up(heap, 0, old_len);
  heap->length = old_len + 1;
  return true;
}

void test_push() {
  Heap *heap = new_heap(5);
  push(heap, 3);
  push(heap, 1);
  push(heap, 5);
  assert(heap->length == 3);
  assert(heap->capacity == 5);
  int key = 0;
  assert(pop(heap, &key));
  assert(key == 5);
  free_heap(heap);
}
void test_pop() {
  Heap *heap = new_heap(5);
  push(heap, 3);
  push(heap, 1);
  push(heap, 5);
  int key = 0;

  assert(pop(heap, &key));
  assert(heap->length == 2);
  assert(key == 5);

  assert(pop(heap, &key));
  assert(heap->length == 1);
  assert(key == 3);

  assert(pop(heap, &key));
  assert(heap->length == 0);
  assert(key == 1);

  assert(!pop(heap, &key));
  free_heap(heap);
}

int main() {
  test_push();
  test_pop();
  return 0;
}
