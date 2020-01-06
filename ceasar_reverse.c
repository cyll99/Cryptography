#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

void min(int a);
int main(int argc, char *argv[])
{

    if (argc == 2)
    {
        int k = atoi(argv[1]);
        signed char c[265];
        int *text = NULL;
        printf("Plaintext:");
        scanf("%[^\n]s", c);

        int e = strlen(c);
        text = malloc(sizeof(int) * e);
        if (text == NULL)
            exit(1);

        printf("ciphertext: ");
        for (int i = 0; i < e; i++)
        {
            int l = c[i] - k;
            if (c[i] > 64 && c[i] < 91)
            {

                if (l < 64)
                {
                    while (l < 64)
                    {
                        l = l + 90 - 64;
                    }

                    printf("%c", l);
                }
                else
                {
                    printf("%c", l);
                }
            }
            else if (c[i] > 96 && c[i] < 123)
            {
                if (l < 97)
                {
                    while (l < 97)
                    {
                        l = l + 122 - 96;
                    }

                    printf("%c", l);
                }
                else
                {
                    printf("%c", l);
                }
            }
            else
            {
                printf("%c", c[i]);
            }
        }
        printf("\n");
        return 0;
        free(text);
    }

    else
    {
        printf("Usage: ./caesar key \n");
        return 1;
    }
}
