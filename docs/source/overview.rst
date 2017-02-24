Overview
--------

Creating a matrix
~~~~~~~~~~~~~~~~~

The :py:class:`.Matrix` class is used to represent matrices. Just pass them
rows as arguments:

  >>> import matrices
  >>> matrix = matrices.Matrix([1, 2], [3, 4], [5, 6])
  >>> matrix
  <Matrix (3×2)>

The rows can be either lists or tuples.

Matrix properties
#################

All matrices have rows and columns. They can also report their dimensions.

  >>> matrix.rows()
  ((1, 2), (3, 4), (5, 6))
  >>> matrix.columns()
  ((1, 3, 5), (2, 4, 6))
  >>> matrix.size()
  (3, 2)

The rows and columns are returned as tuples regardless of how they were
supplied.

Matrix operations
#################

If two matrices are the same size, they can be added:

  >>> matrix2 = matrices.Matrix([7, 8], [9, 10], [11, 12])
  >>> matrix3 = matrix + matrix2
  >>> matrix3.rows()
  ((8, 10), (12, 14), (16, 18))

They can also be subtracted.

You can get the dot product of two matrices, as long as the number of columns in
the first matrix equals the number of rows in the second one:

  >>> matrix4 = matrices.Matrix([10, 20], [30, 40])
  >>> matrix5 = matrix * matrix4
  >>> matrix5.rows()
  ((70, 100), (150, 220), (230, 340))

Creating vertices
~~~~~~~~~~~~~~~~~

A vertex is just a matrix with one column/dimension. They are created with
:py:func:`.create_vertex`, like so:

  >>> vertex = matrices.create_vertex(1, 2, 3)
  >>> vertex
  <Matrix (3×1)>
