#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints some basic
 *							info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}