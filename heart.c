#include <math.h>
#include <stdio.h>

int main()
{
	int array[100];
	for (int i = 0; i < 100; i++)
	{
		array[i] = 0;
	}

	int index = 1;
	for (double y = 1.5; y >= -1.5; y -= 0.05, index++)
	{
		printf("\n");
		for (double x = -1.0; x <= 1.0; x += 0.016, array[index]++)
		{
			/* 笛卡尔心形线公式 */
			double f = x * x + pow(y - pow(x * x, 1.0 / 3), 2) - 1;

			/* 画心形线 - 实心 */
			if (array[index] + 10 != index * 3 || x >= 0)
			{
				printf("\033[1;30;91m"); //颜色控制
				putchar(f <= 1E-5 ? '*' : ' '); //误差控制
			}

			/* 画弓箭 - 无箭头 */
			if (array[index] + 10 == index * 3 && (x < 0 || f > 1E-5))
			{
				printf("\033[1;30;93m"); //颜色控制
				printf("\b\b\baaa"); //字符控制
			}
		}
	}
	
	return 0;
}
