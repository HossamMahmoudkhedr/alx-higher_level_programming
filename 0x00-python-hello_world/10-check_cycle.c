#include "lists.h"
int check_cycle(listint_t *list)
{
    if (list->next != NULL)
    {
        return (1);
    }

    return (0);
}
