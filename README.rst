matrices
========

matrices is a pure-python matrix processing package with no C dependencies.

Example
-------

  >>> import matrices
  >>> matrix = matrices.Matrix([1, 2], [3, 4], [5, 6])
  >>> matrix
  <Matrix (3×2)>
  >>> matrix.size()
  (3, 2)



Installing
----------

pip
~~~

matrices can be installed using pip:

``$ pip install matrices``

matrices is written for Python 3. If the above installation fails, it may be
that your system uses ``pip`` for the Python 2 version - if so, try:

``$ pip3 install matrices``

Requirements
~~~~~~~~~~~~

matrices currently has no dependencies - compiled or otherwise.


Overview
--------

Creating a matrix
~~~~~~~~~~~~~~~~~

The ``Matrix`` class is used to represent matrices. Just pass them
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
``create_vertex``, like so:

  >>> vertex = matrices.create_vertex(1, 2, 3)
  >>> vertex
  <Matrix (3×1)>


Changelog
---------

Release 0.1.0
~~~~~~~~~~~~~

`24 February 2017`

* Added Matrix class,

  * Matrices can be added and multiplied,

  * They can also return their rows, columns and size.

* Added vertex function.
