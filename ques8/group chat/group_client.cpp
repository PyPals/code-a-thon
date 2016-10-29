// ...

/**
 *	TCP from client side
 *	socket() -> connect() -> read() -> write()
 */

#include "common.h"

void commit_suicide(string message) {
	perror(message);
	exit(7);
}

int main (int argc, char const * argv []) {
	
	sockaddr_in_t server_address;
	
	int sockfd, i;
	socklen_t slen = sizeof(server_address);
	
	char input[BUFLEN];
	char buffer[BUFLEN];
	char handle[30];
	int ch;

	printf("It's Ross' birthday everybody. Let's plan a good one.\n");
	printf("Enter your email address: ");
	scanf(" %s", handle);

	if (!strcmp(handle, "chandler@rossbirthday.com") || !strcmp(handle, "rachel@rossbirthday.com"))
	{
		// create a TCP server
		if ((sockfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0) {
			commit_suicide("socket()");
	}
	else
	{
		printf("Sorry! You don't have the correct credentials. Please contact Monica for the same.")
	}
	// zero out the structure
	memset((char *)&server_address, 0, slen);
	
	// set family and port
	server_address.sin_family = AF_INET;
	server_address.sin_port = htons(PORT);
	server_address.sin_addr.s_addr = inet_addr(SERVER);
	
	// get address
	if (connect(sockfd, (sockaddr_p_t)&server_address, slen) < 0) {
		commit_suicide("connect()");
	}

	int pid = fork();
	if (pid == 0) {

		while (YES) {
			fgets(input, BUFLEN, stdin);
			if (strlen(input) > 1) {
				memset(buffer, '\0', BUFLEN);
				sprintf(buffer, "[%s]: %s", handle, input);
				send(sockfd, buffer, BUFLEN, 0);
			}
		}

	} else {

		while (YES) {
			if (recv(sockfd, buffer, BUFLEN, 0) > 0) {
				if (strlen(buffer) > 0)
					printf(">> %s", buffer);
			}
		}

	}



	}	
	
	return 0;
}