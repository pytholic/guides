This gist describes how to add Anaconda Prompt to the Windows right click context menu. This is because at some point, Anaconda no longer adds itself to the PATH after installation.

1. Run regedit.exe
2. Navigate to `HKEY_CLASSES_ROOT > Directory > Background > shell`
3. Add a key named `AnacondaPrompt` and set its value to "Anaconda Prompt Here" (or anything you'd like it to appear as in the right click context menu)
4. Add a key under this key, called `command`, and set its value to `cmd.exe /K C:\Anaconda3\Scripts\activate.bat` (may have to change the activate.bat file to whereever Anaconda is installed)
