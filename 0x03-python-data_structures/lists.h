#ifndef LISTS_H
#define LISTS_H

/* Headers */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct listint_s - singly linked list.
 * @n: integer.
 * @next: points to the next node
 *
 * Description: singly linked list node structure.
*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/* Functions*/
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
int listlen(listint_t *head);
listint_t *node_at(listint_t *h, int idx);

#endif
