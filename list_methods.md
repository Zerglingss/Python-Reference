## Adding elements


**.append***(x)*
Append value x as the last element.

**.insert***(i, x)*
Append value x at index i. If i is negative, the value will be inserted at index `len(e) - abs(i)`.

**.extend(iterable)***(i, items)*
Append given iterable after the last element.


## Removing elements


**.remove***(x)
Delete the first element from a list with index x. A *ValueError* exception will be raised if no element matches x.

**.pop***(), (n)*
Delete and *return* the element at index i in a list and, if i is not given the last index element will be removed. An *IndexError* exception will be raised if the index is out of the bounds.

**.clear***()*
Delete *all* elements and leave the variable in scope for use. len(e) will be 0 after the operation.


## Finding values


**.index***(x), (x, start, [end]) -> index*
Finds and *returns* the lowest index of an element matching x. A *ValueError* exception will be raised if no element matches x.

If a *start* value is given, limit the search for an element to a given range of indexes.  The *returned* result will be relational to the beginning index, *not* the given start index.

**.count***(x) -> int*
Searches for all elements matching value x and *returns* the result as an int. If no such values are found the *return* value will be 0.


## Modification


**.sort()***(), (key=, reverse=)*
Sorts all elements in place, uses the *sorted()* routine.

*key* is a function that will be performed for all elements of the sort. If *reverse* is given as True elements will be sorted in reverse order.

**.reverse***()*
Reverse all elements in place, uses the *reversed()* routine.


## Creation


**.copy()**
*Returns* a *shallow* copy of the list. The copy will be a *new* list, but  collections contained within the lists will remain as the original elements.
