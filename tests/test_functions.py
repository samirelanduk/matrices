from unittest import TestCase
from unittest.mock import Mock
from matrices.functions import create_vertex, can_add, can_multiply
from matrices.matrix import Matrix

class VertexTests(TestCase):

    def test_can_create_vertex(self):
        vertex = create_vertex(1, 4, 5, 6)
        self.assertIsInstance(vertex, Matrix)
        self.assertEqual(vertex, Matrix([1], [4], [5], [6]))



class MatrixOperandFunctionTests(TestCase):

    def test_can_add_function(self):
        matrix1 = Matrix((1, 2, 3), (4, 5, 6))
        matrix2 = Matrix((1, 2, 3), (4, 5, 6))
        self.assertTrue(can_add(matrix1, matrix2))
        matrix2 = Matrix((1, 2, 3, 3.5), (4, 5, 6, 6.5))
        self.assertFalse(can_add(matrix1, matrix2))


    def test_can_multiply_function(self):
        matrix1 = Mock(Matrix)
        matrix2 = Mock(Matrix)
        matrix1.size.return_value = (4, 3)
        matrix2.size.return_value = (3, 2)
        self.assertTrue(can_multiply(matrix1, matrix2))
        matrix1.size.return_value = (3, 4)
        matrix2.size.return_value = (2, 3)
        self.assertFalse(can_multiply(matrix1, matrix2))
