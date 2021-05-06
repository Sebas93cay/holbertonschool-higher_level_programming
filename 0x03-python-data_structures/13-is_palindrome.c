#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * listint_len - Returns the lenght of listint_t
 * @head: pointer of first node of listint_t list
 * Return:  Returns the lenght of listint_t
 */
int listint_len(listint_t *head)
{
	int len = 0;

	while (head != NULL)
	{
		head = head->next;
		len++;
	}
	return (len);
}



/**
 * is_palindrome - compare if a listint_t is palindrome
 * @head: list
 * Return: 1 if list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int *nums = NULL, *revnums = NULL;
	listint_t *tmp_node = NULL;
	int equal = 1, len = 0, i = 0;

	len = listint_len(*head);

	if (len == 0)
		return (1);

	nums = malloc(sizeof(int) * len);
	if (nums == NULL)
		return (0);
	revnums = malloc(sizeof(int) * len);
	if (revnums == NULL)
	{
		free(nums);
		return (0);
	}

	tmp_node = *head;
	while (tmp_node != NULL)
	{
		nums[i] = tmp_node->n;
		i++;
		tmp_node = tmp_node->next;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (nums[i] != nums[len - 1 - i])
		{
			equal = 0;
			break;
		}
	}
	free(nums);
	return (equal);
}
