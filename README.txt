Kane

Version: 2.1
__________________________________________________
WARNING
For users updating kane from before 2.0.9.7:

RENAME "users" FOLDER IN "usrs"
__________________________________________________

Setup:
    To correctly setup Kane on windows I suggest to place the MainKane folder directly in the C: directory. This makes all easier ;)
    You can then create a shortcut to the terminal in the startup folder
    C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    To get the full geek experience press fn+f11 to make the terminal window full screen
    On linux, I suggest to place MainKane in /home folder. 

CHANGELOG:
   # Version 2.1
    @ added desktop enviroment!
    @ fixed a bunch of bugs
   # Version 2.0.9.8
    @ added playground (pg), manual soon
    @ fixed a bunch of bugs
    @ added rename command
   # Version 2.0.9.8
    @ Improved terminal interface
    	- added colored text
    @ pkg fixed (use man pkg to get further information)
    @ added rm command to delete files and folder
   # Version 2.0.9.7.8
    @ Fixed issues:
    	- Password now encripted. (Encription module made from scratch, compiled for security reasons)
	- InputLog now saves input on newline.
   # Version 2.0.9.7.7
    @ moddellized stout&stderr for every command, now the pull function will return an object like this
    	output.|stdout
	       |stderr
    @ now kane is a python function: kanescript coming soon
   # Version 2.0.9.7.7-
    @ added sysconfig options to tweak around yor kane.
     (when updating, if you want to keep thoose tweaks don't overwrite it ;] )
    @ Improced syshost command management, now I have more control over stderr and stdout of your main os' commands
   # Version 2.0.9.7.3 -> 6
    @ *fixed syshost commands
    @ Finally, cd will check if the directory exists
    @ Added shortcuts
   # Version 2.0.9.7.2 - networking -
    @ Added stream services: use and host simple servers
   # Version 2.0.9.6.1  - internal security -
    @ Added protection to user's home folder. Only that user can access it
    @ Added user verification: you were able to switch user without verification with py user='TargetUserName',
      now Kane will check for discrepancies in usernames
    @ Improved 'lemme see' command: now it gives you a list of active variables in the program
      With 'lemme see all' it will also show functions(with memory adress) and modules
	

Sintax:
    Kane terminal supports either his own commands either your os ones.
    To get a list of useful commands type help.

What's Kane?
    Kane is a subOS. A subOS is an Operating Sistem that lives on another.

    Why having a subOS?
	since kane has just a terminal with no graphics, you might miss (is it possible?) the window based stuff.

Open Source Notes:
    This is a full open source. This means than you have free access to the project and its source code.
    If you paid for this pretend a refund!

If you're doing any treasure hunt, the password will always be: cheese
