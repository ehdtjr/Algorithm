#include <stdio.h>
#include <string.h>
int main()
{
	char a[16];
	int sum = 0;
	int b;

	scanf("%s", &a);

	b = strlen(a);

	for (int i = 0; i < b; i++)
	{
		if (a[i] == 'A' || a[i] == 'B' || a[i] == 'C')
			sum += 3;
		if (a[i] == 'D' || a[i] == 'E' || a[i] == 'F')
			sum += 4;
		if (a[i] == 'G' || a[i] == 'H' || a[i] == 'I')
			sum += 5;
		if (a[i] == 'J' || a[i] == 'K' || a[i] == 'L')
			sum += 6;
		if (a[i] == 'M' || a[i] == 'N' || a[i] == 'O')
			sum += 7;
		if (a[i] == 'P' || a[i] == 'Q' || a[i] == 'R' || a[i] == 'S')
			sum += 8;
		if (a[i] == 'T' || a[i] == 'U' || a[i] == 'V')
			sum += 9;
		if (a[i] == 'W' || a[i] == 'X' || a[i] == 'Y' || a[i] == 'Z')
			sum += 10;
	}
	printf("%d", sum);
}