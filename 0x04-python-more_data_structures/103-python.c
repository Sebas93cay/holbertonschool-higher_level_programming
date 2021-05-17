#include <Python.h>
#include <stdio.h>


void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = NULL;
	int bytes_count = 0, i = 0;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	bytes_count = (int)(bytes)->ob_base.ob_size;
	printf("  size: %d\n", bytes_count);
	printf("  trying string: %s\n", bytes->ob_sval);
	printf("  first %d bytes:", (bytes_count + 1 < 10) ? bytes_count + 1 : 10);
	for (i = 0; i < bytes_count + 1 && i < 10; i++)
	{
		printf(" %02x", (char)((bytes->ob_sval)[i]) & 0xFF);
	}
	printf("\n");
}


void print_python_list(PyObject *p)
{
	PyListObject *l = (PyListObject *)p;
	int i = 0, items = 0;
	const char *tipo = NULL;
	PyObject *item = NULL;

	items = (int)(((PyVarObject *)p)->ob_size);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", items);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	for (i = 0; i < items; i++)
	{
		printf("Element %d: ", i);
		item = (*(l->ob_item + i));
		tipo = item->ob_type->tp_name;
		printf("%s\n", tipo);
		if (strcmp(tipo, "bytes") == 0)
			print_python_bytes(item);
	}

}
