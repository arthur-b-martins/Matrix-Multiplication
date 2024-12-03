# Matrix Multiplication

This program multiplies two matrices of any size,  
as long as they are compatible for multiplication.

This was the first program I created after learning  
the basics of programming logic in Python.  

The idea came to me while struggling with my Linear Algebra  
class in college. I found it challenging to verify whether my  
matrix multiplication operations were correct, so I created  
this program to help me. I can confidently say it was truly useful.

The websites I found at the time required inputting a matrix  
element by element, adjusting the mouse cursor for each next input,  
and so on.  

My program, however, allows you to input an entire row of the  
matrix at once, separating the elements with spaces, and pressing  
Enter to input the next row.

---

## A Quick Recap of Matrix Multiplication

Matrix multiplication is only possible if the **number of columns** in the first matrix  
is equal to the **number of rows** in the second matrix. In other words:

**Example of a valid multiplication:**
_Matrix A_ (a × b) × _Matrix B_ (b × c)

**Example of an invalid multiplication:**
_Matrix A_ (a × b) × _Matrix B_ (c × d)
(where c ≠ b)

The resulting matrix will have the **number of rows of the first matrix**  
and the **number of columns of the second matrix**. For example:

_Matrix A_ (a × b) × _Matrix B_ (b × c) = _Matrix_ C (a × c)

Each element of the resulting matrix is the **dot product** of the respective row  
from the first matrix and the respective column from the second matrix.
