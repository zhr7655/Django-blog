#include<stdio.h>
#include<stdlib.h>

typedef struct {
    int* data;
    int size;
    int capacity;
}DynamicArr;

DynamicArr* init_arr(int init_capacity) {
    DynamicArr* arr = malloc(sizeof(DynamicArr));
    arr->data = malloc(sizeof(int) * init_capacity);
    arr->capacity = init_capacity;
    arr->size = 0;
    return arr;
}

void resize(DynamicArr* arr, int new_capacity) {
    int* new_data = malloc(sizeof(int) * new_capacity);
    for (int i = 0; i < arr->size; i++) {
        new_data[i] = arr->data[i];
    }
    free(arr->data);
    arr->data = new_data;
    arr->capacity = new_capacity;
}

void append(DynamicArr* arr, int value) {
    if (arr->size >= arr->capacity) {
        resize(arr, arr->capacity * 2);
    }
    arr->data[arr->size] = value;
    arr->size++;
}

int get(DynamicArr* arr, int index) {
    return arr->data[index];
}

void show_capacity(DynamicArr* arr) {
    printf("%d\n", arr->capacity);
}

int main() {
    DynamicArr* arr = init_arr(2);
    append(arr, 124);
    append(arr, 3);
    show_capacity(arr);
    append(arr, 5);
    show_capacity(arr);
    printf("%d\n",get(arr, 2));
    return 0;
}
