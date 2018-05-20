#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

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
  if (data == NULL) {
    return NULL;
  }
  Heap *heap = malloc(sizeof *heap);
  if (heap == NULL) {
    free(data);
    return NULL;
  }
  heap->data = data;
  heap->length = 0;
  heap->capacity = capacity;
  return heap;
}

void free_heap(Heap *heap) {
  free(heap->data);
  free(heap);
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

int pop(Heap *heap, int *item) {
  if (heap->length == 0) {
    return 1;
  }

  *item = heap->data[heap->length - 1];
  heap->length -= 1;
  if (heap->length != 0) {
    swap(item, heap->data);
    sift_down_bottom(heap, 0);
  }

  return 0;
}

int push(Heap *heap, int item) {
  int old_len = heap->length;
  if (old_len == heap->capacity) {
    return -1;
  }

  heap->data[old_len] = item;
  sift_up(heap, 0, old_len);
  old_len += 1;
  heap->length = old_len;
  return old_len;
}

int main() {
  Heap *heap = new_heap(5);
  push(heap, 3);
  push(heap, 1);
  assert(heap->length == 2);
  assert(heap->data[0] == 3);

  int item = 0;
  int error = pop(heap, &item);
  assert(item == 3);
  assert(error == 0);
  error = pop(heap, &item);
  assert(item == 1);
  assert(error == 0);
  error = pop(heap, &item);
  assert(item == 1);
  assert(error == 1);
  free_heap(heap);
  return 0;
}
