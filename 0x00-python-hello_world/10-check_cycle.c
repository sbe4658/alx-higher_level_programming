#include "lists.h"
/**
 * check_cycle - checks whether a list contains a cycle.
 * @list: the head node of the list.
 *
 * Return: 0 if no cycle was found, if not 1.
*/
int check_cycle(listint_t *list)
{
	listint_t *ahead = list, *last;

	last = ahead;
	while (ahead && ahead->next)
	{
		last = last->next;
		if (!last)
			break;
		ahead = ahead->next->next;
		if (last == ahead)
			return (1);
	}
	return (0);
}
