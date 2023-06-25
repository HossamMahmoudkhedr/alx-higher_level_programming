#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if the singly linked list is palindrome
 *
 * @head: a pointer to the first node in the linked list
 * Return: 1 if it is palindrome, or 0 otherwise
 */

int is_palindrome(listint_t **head)
{
    listint_t *temp, *first;
    int *numbers = malloc(2 * sizeof(int));
    int length = 0;
    int i = 0;
    int l = 0;
    int result = 1;
    temp = *head;

    if (temp == NULL)
    {
        return (1);
    }

    while (temp != NULL)
    {
        length++;
        temp = temp->next;
    }
    numbers = realloc(numbers, length * sizeof(int));

    temp = *head;
    while (temp != NULL)
    {
        numbers[i] = temp->n;
        i++;
        temp = temp->next;
    }
    
    i = i - 1;
    while (i != (length / 2))
    {
        if (numbers[i] != numbers[l])
        {
            result = 0;
            break;
        }
        i--;
        l++;
    }
    return (result);
}
