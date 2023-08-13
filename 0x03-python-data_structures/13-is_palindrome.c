#include "lists.h"
/**
 * linked_len - Calculates the length of a linked list.
 * @head: A double pointer to the head of the linked list.
 * Return: The length of the linked list.
 */
int linked_len(listint_t **head)
{
	listint_t *l;
	int length = 0;

	l = *head;
	while (l != NULL)
	{
		length++;
		l = l->next;
	}
	return (length);
}
/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: A double pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int len = linked_len(head) - 1, i = 0;
	listint_t *current = *head;
	listint_t *temp = *head;
	int half_len = len / 2;

	while (len > half_len)
	{
		i = len;
		temp = *head;
		while (i)
		{
			temp = temp->next;
			i--;
		}
		if (temp->n != current->n)
			return (0);
		current = current->next;
		len--;
	}
	return (1);
}
