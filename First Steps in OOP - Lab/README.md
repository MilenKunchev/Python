# Lab: First Steps in OOP

Problems for exercise and homework for the [Python OOP Course
\@SoftUni](https://softuni.bg/courses/python-oop).

Submit your solutions in the SoftUni judge system at
<https://judge.softuni.bg/Contests/1934>.

## Rhombus of Stars

> Create a program that reads a **positive** **integer N** as input and
> prints on the console a **rhombus** with size **n**:
>
> **Examples**

+--------------------+-------------------------------------------------+
| **Input**          | **Output**                                      |
+====================+=================================================+
| 1                  | \*                                              |
+--------------------+-------------------------------------------------+
| 2                  | \*                                              |
|                    |                                                 |
|                    | \* \*                                           |
|                    |                                                 |
|                    | \*                                              |
+--------------------+-------------------------------------------------+
| 3                  | \*                                              |
|                    |                                                 |
|                    | \* \*                                           |
|                    |                                                 |
|                    | \* \* \*                                        |
|                    |                                                 |
|                    | \* \*                                           |
|                    |                                                 |
|                    | \*                                              |
+--------------------+-------------------------------------------------+
| 4                  | \*                                              |
|                    |                                                 |
|                    | \* \*                                           |
|                    |                                                 |
|                    | \* \* \*                                        |
|                    |                                                 |
|                    | \* \* \* \*                                     |
|                    |                                                 |
|                    | \* \* \*                                        |
|                    |                                                 |
|                    | \* \*                                           |
|                    |                                                 |
|                    | \*                                              |
+--------------------+-------------------------------------------------+

## Scope Mess

Fix the code below, so it returns the expected output. Submit the fixed
code in the judge system.

### Examples

+-----------------------------------+----------------------------------+
| **Current Output**                | **Expected Output**              |
+===================================+==================================+
| global                            | global                           |
|                                   |                                  |
| outer: local                      | outer: local                     |
|                                   |                                  |
| inner: nonlocal                   | inner: nonlocal                  |
|                                   |                                  |
| outer: local                      | outer: nonlocal                  |
|                                   |                                  |
| global                            | global: changed!                 |
+-----------------------------------+----------------------------------+

## Class Book

Create a class called **Book**. It should have an **\_\_init\_\_()**
method that should receive:

-   **name: string**

-   **author: string**

-   **pages**: **int**

Submit only the class in the judge system.

### Examples

+------------------------------------------------------+---------------+
| **Test Code**                                        | **Output**    |
+======================================================+===============+
| book = Book(\"My Book\", \"Me\", 200)                | My Book       |
|                                                      |               |
| print(book.name)                                     | Me            |
|                                                      |               |
| print(book.author)                                   | 200           |
|                                                      |               |
| print(book.pages)                                    |               |
+------------------------------------------------------+---------------+

## Car

Create a class called **Car**. Upon initialization it should receive a
**name**, **model** and **engine** (all strings). Create a method called
**get_info()** which will return a string in the following format:\
**\"This is {name} {model} with engine {engine}\"**.

### Examples

+----------------------------------+-----------------------------------+
| **Test Code**                    | **Output**                        |
+==================================+===================================+
| car = Car(\"Kia\", \"Rio\",      | This is Kia Rio with engine 1.3L  |
| \"1.3L B3 I4\")                  | B3 I4                             |
|                                  |                                   |
| print(car.get_info())            |                                   |
+----------------------------------+-----------------------------------+

## Music

Create class named **Music** that receives **title (string)**,
**artist** **(string)** and **lyrics** **(string)** upon initialization.
The class should also have methods **print_info()** and **play()**:

-   The **print_info()** method should return the following: **\'This is
    \"{title}\" from \"{artist}\"\'**

-   The **play()** method should **return** the **lyrics**.

Submit **only the class** in the judge system. **Test your code** with
your own examples.

### Examples

+----------------------------------------+-----------------------------+
| **Test Code**                          | **Output**                  |
+========================================+=============================+
| song = Music(\"Title\", \"Artist\",    | This is \"Title\" from      |
| \"Lyrics\")                            | \"Artist\"                  |
|                                        |                             |
| print(song.print_info())               | Lyrics                      |
|                                        |                             |
| print(song.play())                     |                             |
+----------------------------------------+-----------------------------+
