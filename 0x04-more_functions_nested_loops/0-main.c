#include <stdio.h>
#include <ctype.h>
#include "main.h"
/**
 * main - checks and print 1 or 0 if the character is an uppercase
 *
 * Return: Always 0.
 */
int main(void)
{
	char c;

	c = 'A';
	printf("%c: %d\n", c, _isupper(c));
	c = 'a';
	printf("%c: %d\n", c, _isupper(c));
	return (0);
}
