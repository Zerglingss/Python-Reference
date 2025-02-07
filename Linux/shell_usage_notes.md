# Linux Distros

## Debian
  - Stable, Older package versions

## Red Hat
  - Controlled Distribution
  - opensource
  - RPM Package manager

## Ubuntu
   - Popular
   - Developed by Canonical
   - uses core Debian Components

## Fedora
   - Backed by Red Hat
   - More user friendly than Red Hat

## Mint
  - Same package manager as Debian and Ubuntu
  - lightweight
  - Good UI

 ## Gentoo
   - Commercial
   - High flexibility
   - Portage package manager, modular and easy to maintain

## Arch
  - Rolling release model
  - lightweight
  - flexible
  - high learning curve
  - Uses pacman

## openSUSE
  - High focus on opensource community
  - RPM package manager

# Shell Navigation

## Clear Line
  - `[ctrl] + [home], [ctrl] + [k]`

## Move up and down by page
  - `[shift] + [pageUp]`, `[shift] + [pageDown]`

## "cut"
  - `[ctrl] + [u]`
  - does not seem to use the system clipboard

## "paste"
  - `[ctrl] + [y]`
  - paste back the content that was cut using ctrl+u

## "cut" to the clipboard
  - `[ctrl] + [y] | xclip -selection clipboard`
    - appends to clipboard? in some contexts??
  - or `echo [ctrl] + [y] | xclip -selection clipboard`
    - This method is generally more useful, as it sets the clipboard.

## saving arguments
  - `[alt]+[.]` can bring up a previous argument
  - type `var=[alt]+[.]` to store a prev arg in *var* for recalling later, such as a long directory name

# Shell command shortcuts

## Rerunning commands from history
  - `!!`
  - `!str` rerun the last command begining with *str* and include args
  - `!^` expands to the first argument of the most recent command of the same name
  - `!$` expands to the last argument of the most recent command of the same name
  - `[alt] + [.]` cycles through previous arguments

## Shell history
  - the shell history is kept in a file in your home directory
  - you can access it with the `history` command
  - use `!N` to run the -Nth command from history
  - a pipeline such as `history | grep alias` can be useful for recalling specific commands
  - use `[ctrl] + [r]` for a reverse search

## fc
  - use fc to edit and rerun commands


# Shell commands

## pwd
  - print working directory

## cd
   - move dir by relative or absolute path
   - `cd ~` home dir
   - `cd /` root dir
   - `cd -` previous dir

## ls
   - `ls -la` show attributes and hidden files

## touch
   - create a file or update last access time

## file
  - show a description of a file's context

## cat
  - list a file, or multiple files, output

## less
  - navigate through a file
  - `g` nav to start, `G` nav to end.
  - /search search a file
  - PageUp or `N`, PageDown or `n` navigate a file
  - `h` help
  - `q` quit

## history
  - Show previous commands

## clear
  - clear the terminal

## cp
  - copy a file or files
  - wildcard can copy multiple files to a dir
  - `cp -r` recursive file copy
  - `cp -i` can prevent an accidental overwrite

## mv
  - move a file to a new location, or rename it
  - `mv -i` can prevent accidental overwrite
  - `mv -b` if a file of the new name already exists, append a ~ to the existing file

## mkdir
  - create one or many directories
  - `mkdir -p` create multiple nested directories

## rm
  - delete a file
  - `rm -f` to delete write protected files
  - `rm -i` to prompt a prompt, for caution when deleting multiple files
  - `rm -r` delete a directory and all subdirectories and files

## find
  - `find <directory> -name <file_name>` search within a directory recursively
  - use the -type flag to return files of a specified type, `d` for directories

## help
  - information on bash builtins

## man
  - retrieve the manual page for the specified command

## info
  - may also has information on a given command

## whatis
  - returns a short description of a specified command

## alias
  - define a signature for a command and optionally it's arguments
  - `alias dir='ls -la'`
  - use `unalias <cmd>` to remove the alias

## exit & logout
  - end the session

# stdout & stdin

## redirection
  - use `>` to route a commands output to a file
  - ex. `echo hello world > file.txt`

## append to file
  - use `>>` to append output to an existing file

## stdin
  - use `<` to ... do something, i dunno the example is terrible
  - this is probably useful somewhere
  - `1>` refers to stdin, this breaks things, may be useful somewhere

## stderr
  - use `2>` to route any error messages to the specified location or file
  - use `&>` to route both stdout and stderr to a file
  - use `2> /dev/null` to throw away stderr output

## Pipeline
  - route the output of one command to the input of another
  - `ls -r / | less` to view your entire root directory with less

## tee
  - use `tee` to route the output of a command to both stdout and a location
  - ex. `ls -la | tee file.txt`

## env
  - list all environment variables
  - use $VAR_NAME to access a variable
  - use $PATH to see available programs

## cut
  - copies specified characters from a file
  - does not remove content from the file
  - use `-d` to select a delimiter

## paste
  - joins elements in a file with a delimiter, tab by default.

## head
  - `head -n 20 file.txt` outputs the first 20 lines from a file (default 10)

## tail
  - `tail -n 20 file.txt` outputs the last 20 lines from a file (default 10)
  - use `tail -f` to follow a file as it grows (for instance a log)

## expand and unexpand
  - convert spaces to tabs and vice-versa
  - use `unexpand -a` to convert each group of spaces

## join
  - zip two files

## split
  - seperate a file into multiple files, default split at each 1000 lines

## sort
  - sort lines within a file

## tr
  - translate a set of chars to another set, or remove a set of chars entirely

## uniq
  - remove duplicate adjacent lines from a file
  - can also combine the lines and add a counter of the number of occurances with the `-c` option
  - use `-u` to get unique values only, and `-d` to get dupliccates only
  - Combine sort and unique in a pipeline to delete all duplicates

## nl
  - output file with line numbers

## wc
  - word count
  - use `-l` to get the line count
  - use `-c` to get character count

## grep
  - search files and their contents
  - use `-i` for case-insensitive
  - very useful in a pipeline
  - grep accepts regular expressions
