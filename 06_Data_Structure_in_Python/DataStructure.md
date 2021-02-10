## Introduction
Every programming language provides salient features of data structures. A data structure is more precisely defined as a way of storing, organizing and retrieving data in a computer so that it can be used most efficiently to give optimal performance. There are several types of data structures which are designed and used for different kinds of applications.

An important sequential linear data structure, lists, which are ordered sequence of items. When we intend to refer to or access a specific value in the sequence/list, it is done using index value or subscript and is accessed from the 0th position till last_index - 1.

Python lists are dynamic in nature, i.e., they can grow/increase and shrink/decrease in size/ number of items as and when required. They are also heterogeneous, which means we can store elements of multiple datatypes in a single list. In this chapter, we shall further discuss two data structures-Stacks and Queues-and their implementation in Python using lists. 

## Stack
A Stack is a linear/sequence structure in which insertion and deletion can take place only at one end, i.e., Stack's top. Because of this, Stack is called LIFO (last in, first out) data structure. LIF0 means the element Stack: Last in, first out inserted last would be the first to be deleted. For example, a pile of books, a stack of coins, where you can remove only the top book or the coin placed at the top. 

The two Stack operations are performed through the "top"-elements are inserted as well as deleted from the top only. The Stack is a dynamic data structure as it grows (with an increase in the number of elements) or shrinks (with a decrease in the number of elements). A static data structure, on the other hand, is one that has a fixed size. Stacks are fundamentally important as they can be used to reverse the order of items o elements. The order of insertion is the reverse of the order of removal. Fig. 6.3 shows the Python data object Stack created in the original order and traversed/deleted in the reverse order.

The ist methods available in Python make it flexible and easy to implement Stack using lists.
In Python, when you declare/create a list, it creates an address in memory and can hold any
10er of heterogeneous elements. Thus, in order to create an empty Stack, we just need to
uSe inbuilt function 1ist() as per the syntax given below