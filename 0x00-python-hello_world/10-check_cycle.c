#include "lists.h"

int check_cycle(listint_t *list)
{
	int checked_nodes = 0, i = 0;
	listint_t *node, *node_checked;

	if (list == NULL)
		return (0);

	node = list;
	while (node != NULL)
	{
		node_checked = list;
		for (i = 0; i < checked_nodes; i++)
		{
			if (node == node_checked)
				return (1);
			node_checked = node_checked->next;
		}
		checked_nodes++;
		node = node->next;
	}
	return (0);
}
