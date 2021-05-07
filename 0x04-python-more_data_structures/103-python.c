#include <Python.h>
#include <stdio.h>
void print_python_list(PyObject *p)
{
    printf("puntero p = %p\n", (void *)p);
}

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    int bytes_count = 0, i = 0;

    printf("[.] bytes object info\n");
    bytes_count = (int)(bytes)->ob_base.ob_size;
    printf("size: %d\n", bytes_count);
    printf("trying string: %s\n", bytes->ob_sval);
    printf("first %d bytes:", (bytes_count + 1 < 10) ? bytes_count + 1 : 10);
    for (i = 0; i < bytes_count + 1 && i < 10; i++)
    {
        printf(" %02x", (char)(bytes->ob_sval)[i]);
    }
    printf("\n");
}