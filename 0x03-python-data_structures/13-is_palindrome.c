#include "lists.h"
/**
 * is_palindrome - checks if a list is palindrome.
 * @head: the head node.
 *
 * Return: 1 if palindrome, otherwise 0.
*/
int is_palindrome(listint_t **head)
{
	listint_t *tail, *h;
	int i = 0, len = 0, half_len = 0;

	h = *head;
	len = listlen(h);
	half_len = (len % 2 ? (len / 2) + 1 : len / 2);
	while (i < half_len)
	{
		tail = node_at(*head, len - i - 1);
		if (tail->n != h->n)
			return (0);
		h = h->next;
		i++;
	}
	return (1);
}
/**
 * listlen - returns the number of nodes.
 * @head: the head node.
 *
 * Return: the number of nodes.
*/
int listlen(listint_t *head)
{
	int len = 0;

	while (head)
	{
		head = head->next;
		len++;
	}
	return (len);
}
/**
 * node_at - gets the node at specific index.
 * @head: the head node.
 * @idx: the index of the node.
 *
 * Return: The node at the specific index.
*/
listint_t *node_at(listint_t *head, int idx)
{
	while (idx > 0)
	{
		if (head)
			head = head->next;
		idx--;
	}
	return (head);
}
