#include <stdio.h>

int main() {
    FILE *fp1 = fopen("sedscore.csv", "r");
    FILE *fp2 = fopen("outputscore  .txt", "w");
    for (int i = 0; i < 10; i++)
        while (getc(fp1) != ',');
    while (1) {
        char character = getc(fp1);
        fprintf(fp2, "%c", character);
        if (getc(fp1) == EOF)
            break;
        for (int i = 0; i < 5; i++)
            while (getc(fp1) != ',');
    }
}