#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
void print_int_array(int *A, int length);

typedef struct Heap {
  int *nodes;
  int size;
  int capacity;
} Heap;

// one-base
int heap_parent(int i) { return (i - 1) / 2; }
int heap_left(int i) { return 2 * i + 1; }
int heap_right(int i) { return 2 * i + 2; }

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

void max_heapify(Heap *A, int i) {
  int l = heap_left(i);
  int r = heap_right(i);
  int largest = i;
  int size = A->size - 1;
  if (l <= size && A->nodes[l] > A->nodes[largest]) {
    largest = l;
  }

  if (r <= size && A->nodes[r] > A->nodes[largest]) {
    largest = r;
  }

  if (largest != i) {
    swap(A->nodes + i, A->nodes + largest);
    max_heapify(A, largest);
  }
}

Heap *build_max_heap(int *A, int n) {
  Heap *heap = malloc(sizeof *heap);
  heap->size = n;
  heap->nodes = A;
  for (int i = n / 2 - 1; i >= 0; i--) {
    max_heapify(heap, i);
  }
  return heap;
}

void print_int_array(int *A, int length) {
  for (int i = 0; i < length; i++) {
    printf("%d\t", A[i]);
  }
  printf("\n");
}

int heap_increase_key(Heap *A, int i, int key) {
  if (key < A->nodes[i]) {
    return 1;
  }
  A->nodes[i] = key;
  while (i > 1 && A->nodes[heap_parent(i)] < A->nodes[i]) {
    swap(A->nodes + i, A->nodes + heap_parent(i));
    i = heap_parent(i);
  }
  return 0;
}

int heap_extract_max(Heap *A) {
  if (A->size < 1) {
    return 1;
  }
  int max = A->nodes[1];
  A->nodes[1] = A->nodes[A->size];
  A->size -= 1;
  max_heapify(A, 1);
  return max;
}

int max_heap_insert(Heap *A, int key) {
  A->size += 1;
  A->nodes[A->size] = key - 1;
  heap_increase_key(A, A->size, key);
  return 0;
}

int main() {
  int A[10] = {4, 1, 3, 2, 16, 9, 10, 14, 8, 7};
  Heap *heap = build_max_heap(A, 10);
  print_int_array(A, 10);
  for (int i = 0; i < 10; i++) {

    int max = heap_extract_max(heap);
    max_heap_insert(heap, max);
  }
  print_int_array(A, 10);
  free(heap);
  return 0;
}
