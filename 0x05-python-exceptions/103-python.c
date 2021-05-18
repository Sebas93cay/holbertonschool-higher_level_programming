#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = NULL;
	int bytes_count = 0, i = 0;

	fflush(stdout);
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


void print_python_float(PyObject *p)
{
	PyFloatObject *flo = NULL;
	char *number_str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	flo = (PyFloatObject *)p;


	number_str = PyOS_double_to_string(flo->ob_fval, 'r',
					   0, Py_DTSF_ADD_DOT_0,
					   Py_DTST_FINITE);
	printf("  value: %s\n", number_str);
	PyMem_Free(number_str);
}



void print_python_list(PyObject *p)
{
	PyListObject *l = (PyListObject *)p;
	int i = 0, items = 0;
	const char *tipo = NULL;
	PyObject *item = NULL;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	items = (int)(((PyVarObject *)p)->ob_size);

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
		if (strcmp(tipo, "float") == 0)
			print_python_float(item);
	}

}

