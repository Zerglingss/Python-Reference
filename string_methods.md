# Built-in Functions

**print(), input(), ord(), chr(), ascii(), repr()**


## Character Properties


**.isdigit***()*
Return True if all characters in the string are *digits.*

**.isalpha***()*
Return True if all characters in the string are *alphabetic.*

**.isalnum***()*
Return True if all characters in the string are *alphanumeric.*

**.isspace***()*
Return True if all characters in the string are *whitespace.*

**.isupper***()*
Return True if all cased characters are *uppercase.*

**.islower***()*
Return True if all cased characters are *lowercase.*

**.istitle***()*
Return True if all words are *titlecased.* Titlecase words are words where the first and only the first alphabetic character that appears is uppercase.


## Substring Matching


**.find***(substring), (substring, start, [end])*
*Return* the *lowest* index of substring or -1 if no substring found.

**.rfind***(substring), (substring, start, [end])*
*Return* the *highest* index of substring or -1 if no substring found.

**.index***(substring), (substring, start, [end])*
*Return* the *lowest* index of substring or raises *ValueError* if substring is not found.

**.rindex***(substring), (substring, start, [end])*
*Return* the *highest* index of substring or raises *ValueError* if substring is not found.

**.count***(substring), (substring, start, [end])*
*Return* the number of non-overlapping occurrences of substring

**.startswith***(prefix), (prefix, start, [end])*
Return True if the string begins with prefix.

**.endswith***(suffix), (suffix, start, [end])*
Return True if the string ends with suffix.


# Splitting and Joining


**.join***(iterable)*
Join all elements in iterable seperated by the string and *return* the result.

**.split***(sep=None, maxsplit=-1)*
Split the string into a list of substrings, using sep as the delimiter. If sep is None, split on whitespace.

**.rsplit***(sep=None, maxsplit=-1)*
Split the string *from the right* into a list of substrings.

**.splitlines***(keepends=False)*
Split the string into a list of lines, optionally keeping line-endings.

**.partition***(sep)*
Split the string into a tuple (prefix, sep, suffix) where sep is the first occurrence of the delimiter.

**.rpartition***(sep)*
Split the string *from the right* into a tuple (prefix, sep, suffix) where sep is the first occurrence of the delimiter.


## Replacement and Removal


**.replace***(existingSeq, newSeq), (existingSeq, newSeq, count)*
*Return* a copy of the string with *all* or up to *count* occurrences of substring replaced by newstring.

**.strip***(), (chars)*
Return a copy of a string with *all whitespace characters* removed or return a copy of a string with all characters in *chars* removed.

**.lstrip***(), (chars)*
Return a copy of the string with all leading characters removed or return a copy of a string with all characters in *chars* removed.

**.rstrip***(), (chars)*
Return a copy of the string with all trailing characters removed or return a copy of a string with all characters in *chars* removed.

**.expandtabs***(), (n)*
Replace tab '\t' characters with one or *n* spaces

**.removeprefix***(prefix), (prefix, start, [end])*

**.removesuffix***(suffix), (suffix, start, [end])*


# Alignment and Padding


**.center***(width), (width, fillchar)*
*Return* the string centered in a field of size width padded with ' ' or *fillchar.*

**.ljust***(width), (width, fillchar)*
*Return* the string left-justified in a field of size width.

**.rjust***(width), (width, fillchar)*
*Return* the string right-justified in a field of size width 

**.zfill***(width)*
Pad the string with zeros on the left to make it a minimum width.


## Case Conversion


**.lower***()*
Return a copy of the string with all characters converted to lowercase.

**.upper***()*
Return a copy of the string with all characters converted to uppercase.

**.capitalize***()*
Return a copy of the string with the first character capitalized and the rest lowercased.

**.title***()*
Return a copy of the string with the first letter of each word capitalized.

**.swapcase***()*
Return a copy of the string with uppercase characters converted to lowercase and vice versa.

**.casefold***()*
Return a case-insensitive version of the string, suitable for caseless comparisons.


# Formating


**.format***(`*args, **kwargs`)*
Return a formatted string using placeholders in the string.

**.format_map***(mapping)*
Return a formatted string using a mapping (e.g., a dictionary) for placeholders.

**.translate***(table)*
Return a copy of the string with characters mapped through the table (usually created with str.maketrans()).

**.maketrans***(x, y=None, z=None)*
Create a translation table for use with .translate().


# Encoding and Decoding

**.encode***(encoding='utf-8', errors='strict')*
Return a bytes object encoded using the specified encoding.

**.decode***(encoding='utf-8', errors='strict')*
Decode a bytes object into a string using the specified encoding.
Miscellaneous