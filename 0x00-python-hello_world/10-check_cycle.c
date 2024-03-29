#include "lists.h"

/**
 * check_cycle - Function that checks if a linked list contains a cycle
 * @list: A linked list to check
 * Return: 0 if it doesnt have a cycle, 1 if it has a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
