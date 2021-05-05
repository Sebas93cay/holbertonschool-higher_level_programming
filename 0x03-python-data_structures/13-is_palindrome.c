#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *add_node(listint_t **head, const int n)
{
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * list_compare - compare if two linked list listint_t are equal
 * @a: first list
 * @b: second list
 * Return: 1 if list is a palindrome, 0 otherwise
 */
int list_compare(listint_t *a, listint_t *b)
{
	if (a == NULL && b == NULL)
		return (1);
	if (a == NULL || b == NULL)
		return (0);
	if (a->n != b->n)
		return (0);
	else
		return (list_compare(a->next, b->next));
}

/**
 * is_palindrome - compare if a listint_t is palindrome
 * @head: list
 * Return: 1 if list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *reverted = NULL;
	listint_t *tmp_node = NULL;
	int equal = 0;

	tmp_node = *head;
	while (tmp_node != NULL)
	{
		add_node(&reverted, tmp_node->n);
		tmp_node = tmp_node->next;
	}
	equal = list_compare(*head, reverted);
	free_listint(reverted);
	return (equal);


}
