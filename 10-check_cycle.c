#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *current;

	current = list;
	while (current != NULL)
	{
		head = current->next;
		while (head != NULL)
		{
			if (head->n == current->n)
				return (1);
			head = head->next;
		}
		current = current->next;
	}
	return (0);
}
