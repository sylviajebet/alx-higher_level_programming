#include "lists.h"
/**
  * check_cycle - Function to check if linked list
  * contains a cycle
  *
  * @list: Linked list to check
  * Return: 1 if there is a cycle, otherwise 0
  */
int check_cycle(listint_t *list)
{
	listint_t *this_node = list, *next_node = list;

	if (list == NULL)
		return (0);

	while (this_node && next_node && next_node->next)
	{
		this_node = this_node->next;
		next_node = next_node->next->next;
		if (this_node == next_node)
			return (1);
	}
	if (this_node != next_node)
		return (0);
	return (1);
}
