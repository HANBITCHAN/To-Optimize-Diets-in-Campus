#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define HEAP_SIZE 64
#define MAX_STRUCT_MEMBERS 16

typedef enum {
    CHAR, SHORT, LONG, FLOAT
} Type;

typedef union {
    char c;
    short s;
    long l;
    float f;
} Variable;

typedef struct {
    Variable variables[MAX_STRUCT_MEMBERS];
    Type types[MAX_STRUCT_MEMBERS];
    size_t memberCount;
} Struct;

typedef union {
    char c;
    short s;
    long l;
    float f;
    Struct strct;
} Data;

typedef struct {
    Data data;
    Type type;
    size_t size;
} HeapData;

HeapData heap[HEAP_SIZE];
size_t heap_size = 0;

void dump_mem(const void *mem, size_t len) {
    const char *buffer = mem;
    size_t i;
    for (i=0; i<len; i++) {
        if (i>0 && i%16 == 0) {
            printf("\n");
        }
        printf("%02x ", buffer[i] & 0xff);
    }
    puts("");
}

size_t sizeOfType(Type type) {
    switch (type) {
        case CHAR: return sizeof(char);
        case SHORT: return sizeof(short);
        case LONG: return sizeof(long);
        case FLOAT: return sizeof(float);
        default: return 0;
    }
}

bool allocate(Data data, Type type, size_t size) {
    if (heap_size + size > HEAP_SIZE) {
        printf("There is not enough memory for the data, you can only use %lu byte(s)\n", HEAP_SIZE - heap_size);
        return false;
    }

    heap[heap_size].data = data;
    heap[heap_size].type = type;
    heap[heap_size].size = size;
    heap_size += size;
    return true;
}

void deallocate(size_t index) {
    if (index >= heap_size) {
        return;
    }

    memmove(&heap[index], &heap[index + 1], (heap_size - index - 1) * sizeof(HeapData));
    heap_size--;
}

int main() {
    while (1) {
        char command[16];
        printf("Enter command: ");
        scanf("%s", command);

        if (strcmp(command, "allocate") == 0) {
            char type[16];
            printf("Enter data type: ");
            scanf("%s", type);

            Data data;
            Type dataType;
            size_t size;
            if (strcmp(type, "char") == 0) {
                printf("Enter char: ");
                scanf(" %c", &data.c);
                dataType = CHAR;
                size = sizeof(char);
            } else if (strcmp(type, "short") == 0) {
                printf("Enter short: ");
                scanf("%hd", &data.s);
                dataType = SHORT;
                size = sizeof(short);
            } else if (strcmp(type, "long") == 0) {
                printf("Enter long: ");
                scanf("%ld",
                &data.l);
                dataType = LONG;
                size = sizeof(long);
            } else if (strcmp(type, "float") == 0) {
                printf("Enter float: ");
                scanf("%f", &data.f);
                dataType = FLOAT;
                size = sizeof(float);
            } else if (strcmp(type, "struct") == 0) {
                printf("Enter struct member count: ");
                scanf("%lu", &data.strct.memberCount);
                if (data.strct.memberCount > MAX_STRUCT_MEMBERS) {
                    printf("Too many struct members\n");
                    continue;
                }
                size = 0;
                for (size_t i = 0; i < data.strct.memberCount; i++) {
                    printf("Enter type and value for member %lu: ", i + 1);
                    char memberType[16];
                    scanf("%s", memberType);
                    if (strcmp(memberType, "char") == 0) {
                        scanf(" %c", &data.strct.variables[i].c);
                        data.strct.types[i] = CHAR;
                        size += sizeof(char);
                    } else if (strcmp(memberType, "short") == 0) {
                        scanf("%hd", &data.strct.variables[i].s);
                        data.strct.types[i] = SHORT;
                        size += sizeof(short);
                    } else if (strcmp(memberType, "long") == 0) {
                        scanf("%ld", &data.strct.variables[i].l);
                        data.strct.types[i] = LONG;
                        size += sizeof(long);
                    } else if (strcmp(memberType, "float") == 0) {
                        scanf("%f", &data.strct.variables[i].f);
                        data.strct.types[i] = FLOAT;
                        size += sizeof(float);
                    } else {
                        printf("Invalid member type\n");
                        break;
                    }
                }
                dataType = -1; // Special type for struct
            } else {
                printf("Invalid data type\n");
                continue;
            }

            if (allocate(data, dataType, size)) {
                printf("Successfully allocated\n");
            } else {
                printf("Allocation failed\n");
            }
        } else if (strcmp(command, "deallocate") == 0) {
            size_t index;
            printf("Enter index: ");
            scanf("%lu", &index);
            deallocate(index);
            printf("Successfully deallocated\n");
        } else if (strcmp(command, "dump") == 0) {
            dump_mem(heap, heap_size);
        } else {
            printf("Invalid command\n");
        }
    }

    return 0;
}
