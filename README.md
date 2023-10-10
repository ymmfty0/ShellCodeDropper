During my malware development course, I wrote ShellCodeDropper for training purposes.

*Compiler: Microsoft (R) C/C++ version 19.37.32822 for x64*

*Windows Version:*

*Edition	Windows 11 Pro
Version	22H2
OS build	22621.1702
Experience	Windows Feature Experience Pack 1000.22641.1000.0*

*Python version: Python 3.11.6*

It uses:

- Storiing payload in .data secrtion
- Encryption payload:
    - XOR
    - AES
- Function Call Obfuscation
- Injection to Remote Process
- Hiding console with FreeConsole();

Build in windows with Visual Studio code in Developer command prompt:

```cpp
pip install pycryptodomex
python crypt.py .\demon.bin
.\compile.bat
```