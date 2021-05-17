#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *l = (PyListObject *)p;
	int i = 0, items = 0;

	items = (int)Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", items);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	for (i = 0; i < items; i++)
	{
		printf("Element %d: ", i);
		printf("%s\n", Py_TYPE(*(l->ob_item + i))->tp_name);
	}
}
