#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: head of listint_t
 * @n: int to add in listint_t list
 * Return: address of the new element, or NULL if it failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;
    return (new);
}

/**
 * is_palindrome - identify if a single linked list is palindrome
 * @head: head of listint_t
 * Return: 1 if it is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
    listint_t *aux = NULL, *aux2 = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (*head != NULL)
    {
        add_nodeint(&aux, (*head)->n);
        *head = (*head)->next;
    }

    aux2 = aux;
    *head = aux;

    while (*head != NULL)
    {
        if ((*head)->n != aux2->n)
        {
            free_listint(aux);
            return (0);
        }
        *head = (*head)->next;
        aux2 = aux2->next;
    }

    free_listint(aux);
    return (1);
}
