this is from a tutorial here: http://webcache.googleusercontent.com/search?q=cache:http://www.openrce.org/blog/view/1135/Basic_tutorial_about_how_to_dump_a_process_and_update_the_IAT_using_Immunity_Debug,_LordPE,_and_ImpRec this even couldn't be accessed on Internet
What you will need:
1) Immunity Debug:  http://debugger.immunityinc.com/register.html
2) PE Dumper:  http://www.woodmann.com/collaborative/tools/index.php/PE_Dumper
2) LordPE:  http://www.woodmann.com/collaborative/tools/index.php/LordPE
3) ImpRec:  http://www.woodmann.com/collaborative/tools/index.php/ImpREC
4) An account on Offensive Computing to get the sample:  http://offensivecomputing.net

Now first we need to unpack the binary.  The Evilcodecave's Blog was helpful here

many of links are out of date, here are some good one:
Immunity Debug: https://www.immunityinc.com/products/debugger/

Adobe PDF reader is lovely, but it comes with Mcfee security guard, making it arguly
and windows get out of control
I don't like software that open without permit

# following the basic-reverse-engineering-immunity-debugger-36982.pdf
using immunity debugger in windows7

follow code compiled with Microsoft Visual C++ 98
```cpp
	// test.cpp : Defines the entry point for the console application.
	//

	#include "stdafx.h"
	#include <stdio.h>
	#include <windows.h>

	int main(int argc, char* argv[])
	{
		printf("Hello World!\n");
		if(MoveFile("c:\\temp\\notepad.txt", "c:\\temp\\notepad.exe")){
			// ShellExecute(NULL, "open", "c:\\temp\\notepad.exe", "", NULL, SW_SHOW);
			printf("MoveFile success\n");
		}else{
			printf("Errato %d\n", GetLastError());
		}
		return 0;
	}
```

this is example2
```cpp
	#include<stdio.h>
	#include<windows.h>
	#include<strings.h>
	#include<stdbool.h>
	#include<aclapi.h>
	#include<winsock.h>
	#pragma comment(lib, "ws2_32.lib")

	int contrlla(const char*);
	void scrivifile(void);
	void scriviregistro(void);
	void connetti(void);

	int valore;
	HANDLE hFile;
	BOOL bRet = FALSE;
	char* bBuffer;
	DWORD butesadscrivere;
	DWORD dwWritten;

	int main(void){
		valore = controlla("C:\\WINDOWS\\system456");
		if(valore == 1){
			printf("valore trovato: %d\n", valore);
			exit(0);
		}
		if(valore == 0){
			scrivifile();
			scriviregistro();
			connetti();
			exit();
		}
		else
			exit(0);
	}

	int controlla(const char* percorso){
		DWORD var = GetFileAttributesA(percorso);
		if(var == INVALID_FILE_ATTRIBUTES)
			return false;
		if(var & FILE_ATTRIBUTE_DIRECTORY)
			return true;
		return false;
	}

	int scrivifile(void){
		hFile = CreateFile("C:\\txtdiprova.txt", GENERIC_WRITE, 0, NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL, NULL);
		bBuffer = "Scrivi qualcosa.";
		bytesdascrivere = (DWORD) strlen(bBuffer);
		bRet = WriteFile(hFile, bBuffer, butesdascrivere, &dwWritten, NULL);
	}

	void scriviregistro(void){
		PSECURITY_DESCRIPTOR secdesc = NULL;
		DWORD dwDisposition;
		SECURITY_ATTRIBUTES sa;
		LONG IRes;
		HKEY hkSub = NULL;

		sa.nLength = sizeof(SECURITY_ATTRIBUTES);
		sa.lpSecurityDescriptor = secdesc;
		sa.bInheritHandle = FALSE;

		char cName[] = "Provadiscrittura";
		HKEY hKey = HKEY_CURRENT_USER;
		IRes = RegCreateKeyEx(hKey, cName, 0, "", 0, KEY_ALL_ACCESS, &sa, $hkSbu, $dwDisposition);
	}

	void connetti(void){
		WSADATA wsa;
		SOCKET s;
		struct sockaddr_in server;
		SWAStartup(MAKEWORD(2,2), &wsa);
		s = socket(AF_INET, SOCK_STREAM, 0);

		server.sin_addr.s_addr = inet_addr("74.125.235.20");
		server.sin_family = AF_INET;
		server.sim_port = htons(80);
		connect(s, (struct sockaddr*)&server, sizeof(server));
		exit(0);
	}
```

I know I am entering a area I am not confortable with, maybe I need this experience
using MSVS, it really unconfortable with me, I like vim and shell set up

I need this experience so do it quickly

I think I stop here, in the middle of example 2

need more understanding of assembly code, I'm explore in dark

# following this tutorial
here: http://sector876.blogspot.com/2013/03/backdooring-pe-files-part-1.html
and need new tool: http://www.softpedia.com/get/Programming/File-Editors/XVI32.shtml

like, right now, I hate work without summary

here's links that I probably want to revisit
https://github.com/Microsoft/Detours/tree/master/samples/opengl
http://www.woodmann.com/collaborative/tools/index.php/LordPE
https://www.soldierx.com/tools/LordPE
https://www.google.com/search?rlz=1C1CHFX_enUS735US735&ei=rz4hW_GHCMLVzgKirr3ADg&q=lordpe+manual&oq=lordpe+manual&gs_l=psy-ab.3...435484493.435493205.0.435494028.16.16.0.0.0.0.108.1150.13j3.16.0....0...1c.1.64.psy-ab..0.13.892...0j0i22i30k1j0i67k1j0i30k1j0i22i10i30k1j33i160k1.0.v-H_LwCUGIs
http://sector876.blogspot.com/2013/03/backdooring-pe-files-part-1.html
http://sector876.blogspot.com/2013/03/backdooring-pe-files-part-2.html
http://webcache.googleusercontent.com/search?q=cache:http://www.openrce.org/blog/view/1135/Basic_tutorial_about_how_to_dump_a_process_and_update_the_IAT_using_Immunity_Debug,_LordPE,_and_ImpRecw
https://evilcodecave.wordpress.com/about/
https://forum.quequero.org/categories/reverse-engineering
http://www.antionline.com/showthread.php?269701-Offensive-Computing
