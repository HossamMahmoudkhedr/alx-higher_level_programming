#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newNode, *temp, *prev;

    newNode = malloc(sizeof(listint_t));
    if (newNode == NULL)
    {
        return (NULL);
    }
    newNode->n = number;
    temp = *head;
    if (temp == NULL)
    {
        *head = newNode;
        newNode->next = NULL;
    }
    else
    {
        while (temp->n < number)
            {
                prev = temp;
                temp = temp->next;
            }
        prev->next = newNode;
        newNode->next = temp;
    }

    return (newNode);
}
