4 GB Patch
----------

Current Version: 1.0.0.1 	

I originally wrote this tool for a friend of mine who needed it. This very little tool patches x86 executables in order to let them have 4GB (instead of only 2) of virtual memory on x64 platforms. This tool comes very handy for applications which need a great amount of virtual memory like games, 3D renderization, multimedia etc. To gain these 2GB, you just have to use this tool to patch the executable (*.exe file) of the software you want to have these additional GBs of virtual memory. It can be used by clicking on it and choosing the file or through command line (e.g.: "4gb_patch file.exe"). It automatically creates a backup copy of the original executable.

Why things are this way on x64 is easy to explain. On x86 applications have 2GB of virtual memory out of 4GB (the other 2GB are reserved for the system). On x64 these two other GB can now be accessed by 32bit applications. In order to achieve this, a flag has to be set in the file's internal format. This is, of course, very easy for insiders who do it every day with the CFF Explorer. This tool was written because not everybody is an insider, and most probably a lot of people don't even know that this can be achieved. Even I wouldn't have written this tool if someone didn't explicitly ask me to.

Daniel Pistelli 2007

http://www.ntcore.com/4gb_patch.php