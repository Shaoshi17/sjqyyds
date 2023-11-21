#include <stdio.h>
#include <windows.h>
main()
{
	while (1)
	{
		system("taskkill /f /im studentmain.exe");
		Sleep(1500);

	}

}