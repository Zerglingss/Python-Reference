# Set a breakpoint

```python
import custom_pdb
from custom_pdb import MyPdb
```

```python
import pdb; pdb.set_trace()

breakpoint()

# If using a custom pdb
MyPdb().set_trace()
```


# Essential Commands (Hotkeys)

l (list): Displays a few lines of code around the current execution point.
n (next): Executes the next line of code, stepping over function calls.
s (step): Steps into a function call.
c (continue): Resumes execution until the next breakpoint or program end.
b (breakpoint): Sets a breakpoint at a specific line or function (e.g., b 10, b my_function).
cl (clear): Clears all breakpoints or a specific one (e.g., cl 1 to clear breakpoint 1).
q (quit): Exits the debugger.

# Inspecting Variables

p (print): Prints the value of a variable (e.g., p my_var).
pp (pretty-print): Pretty-prints complex objects (e.g., pp my_var).
whos: Lists all local variables (this is not native to pdb but you can define it in your script).

# Additional Commands

args: Shows arguments passed to the current function.
where (or w): Displays the current stack trace.
up / down: Moves up or down the call stack.
retval: Displays the return value of the last executed function.
! (execute): Executes Python expressions in the current context (e.g., !my_var.append(10)).