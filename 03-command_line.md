# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. mv = This command is used to move files or renames them.
2. cp = This command is used to copy files. This command not only allows one to copy files directly but also to a file in another directory.
3. touch = This command creates an empty file.
4. cd = This command is used to change directories.  Allows one to move up and down.
5. pwd = This command outputs the present directory.
6. ls = This command lists the contents of the directory.
7. man = This command is used to look up details on a specific command.
8. grep = This command allows one to search files containing specific words or phrases.
9. * = This command matches anything in a wildcard.
10. rm = This command removes a file.
11. rmdir = This command removes an (empty) directory.
12. mkdir = This command creates a directory.
13. cat = This command outputs a whole file to the screen without page separation.
14. less = This command displays the file one page at a time.  Use "q" to exit.
15. ls -lt | head = This command displays, in long format, 10 recently modified contents.

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls = This command lists the complete contents of a directory.

ls -a = This command lists content with names that begin with a dot.

ls -l = This command lists the contents in long format, and provides full detail on access, size and when it was last updated.

ls -lh = This command lists the contents in long format.  However, unit suffixes are used for size of the file/directory to reduce the number of digits displayed.

ls -lah = This command lists the contents in long format of files that begin with a dot.  Again, unit suffixes are used to condense the digit size.

ls -t = This command lists content names from most recently modified and then alphabetically.

ls -Glp = This command lists in long format with the directory names in color and followed by a forward slash (/).


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -r = This command lists the content in reverse order (in comparison to "ls").

ls -1 = This command lists the content one per line.

ls -g = This command lists the content in long format, but omits the owner name.

ls -m = This command lists the contents continuously and separated by a comma.

ls -u = This command lists the content by access time.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

The xargs command reads input from the standard input and executes the command.    The default command executed by xargs is echo.  Standard input is delimited, or separated, by a blank space.  Additionally, blank lines in standard input are ignored.  If no standard input is provided, issuing the xargs command will allow the user to enter data followed by Ctrl-d.  This will output the content entered.
For example:
$ xargs  (The xargs command is issued and prompts the user to enter data)
Hello!   (Text entered, standard input, enter Ctrl-d to exit)
Hello!   (Text outputed, or echo-ed, by issuing the xargs command)
Another example:
$ ls     (List all files in directory "testdir")
test1.txt    test2.txt      (Contents of testdir.)
$ find . -name "*.txt" | xargs rm -rf     (Find where I am now, all content with wildcard .txt in its name and use xargs command to remove those files)
$ ls     (List all files in testdir)
$        (All content with .txt in its name have been removied, testdir is now an empty directory)
The command xargs allowed two actions to be performed with one line of commands.  Files with ".txt" are the standard input and are piped into the xargs command which deletes these files.



 

