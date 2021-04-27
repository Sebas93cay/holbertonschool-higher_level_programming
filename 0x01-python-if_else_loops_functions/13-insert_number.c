#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp_head;

	if (head == NULL)
		return (NULL);

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (*head == NULL)
	{
		*head = node;
		(*head)->next = NULL;
		return (*head);
	}

	tmp_head = *head;
	if (number < tmp_head->n)
	{
		*head = node;
		node->next = tmp_head;
		return (node);
	}

	while (tmp_head->next != NULL)
	{
		if (number < tmp_head->next->n)
		{
			node->next = tmp_head->next;
			tmp_head->next = node;
			return (node);
		}
		else
			tmp_head = tmp_head->next;
	}

	tmp_head->next = node;
	node->next = NULL;
	return (node);
}
