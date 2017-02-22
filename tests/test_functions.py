from unittest import TestCase
from matrices.functions import create_vertex
from matrices.matrix import Matrix

class VertexTests(TestCase):

    def test_can_create_vertex(self):
        vertex = create_vertex(1, 4, 5, 6)
        self.assertIsInstance(vertex, Matrix)
        self.assertEqual(vertex, Matrix([1], [4], [5], [6]))
