#include "lists.h"
/**
 * insert_node - inserts a number into a sorted list.
 * @head: the head node if the list.
 * @number: the number to be inserted.
 *
 * Return: The address of the new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;
	int index = 0;

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!tmp)
		*head = new;
	else
	{
		index = locate_place(*head, number);
		if (index == 0)
		{
			new->next = tmp;
			*head = new;
		}
		else
		{
			for (; index - 1 > 0; index--)
				tmp = tmp->next;
			new->next = tmp->next;
			tmp->next = new;
		}
	}
	return (new);
}

/**
 * locate_place - locates where the node should be inserted.
 * @head: the head node of the list.
 * @number: number to be included.
 *
 * Return: The index where to insert the node, -1 if failed.
*/
int locate_place(listint_t *head, int number)
{
	int idx = 0;

	while (head)
	{
		if (number < head->n)
			return (idx);
		head = head->next;
		idx++;
	}
	return (idx);
}
