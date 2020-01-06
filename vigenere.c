#include <stdio.h>
#include <string.h>
#include <ctype.h>

int shift(char c);
int main(int argc, const char *argv[])
{

    if (argc == 2)
    {

        int n = strlen(argv[1]);
        for (int i = 0; i < n; i++)
        {
            if (!isalpha(argv[1][i]))
            {
                printf("Usage: ./viginere keyword \n");
                return 1;
            }
        }
        const char c[256];
        printf("Ciphertext:");
        scanf("%[^\n]s", c);

        int e = strlen(c);
        int j = 0;
        int i = 0;
        printf("ciphertext: ");

        for (i = 0; i < e; i++)
        {
            if (isupper(c[i]))
            {
                int l = shift(argv[1][j % n]) + c[i];
                j++;
                if (l > 90)
                {
                    l = l - 90 + 64;
                    printf("%c", l);
                }
                else
                {
                    printf("%c", l);
                }
            }
            else if (islower(c[i]))
            {
                int l = shift(argv[1][j % n]) + c[i];
                j++;
                if (l > 122)
                {
                    l = l - 122 + 96;
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
    }
    else
    {
        printf("Usage: ./vigenere key \n");
        return 1;
    }
}

int shift(char c)
{
    int key = c;
    if (islower(c))
    {
        key = (c - 97) % 26;
    }
    else if (isupper(c))
    {
        key = (c - 65) % 26;
    }
    return key;
}
