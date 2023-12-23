#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - loop for infinity
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * infinite_while - loop for infinity
 * Return: 0 on success
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		pid_t child_pid = fork();
		if (child_pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", child_pid);
	}
	infinite_while();
	return (0);
}
