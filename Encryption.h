#include <string>
#include <Windows.h>
#pragma comment (lib, "crypt32.lib")
#pragma comment (lib, "advapi32")
#include <psapi.h>
#include <vector>

void XOR(std::string& data, const std::string& key);
int AESDecrypt(std::vector<BYTE>& payload, char* key, size_t keylen);