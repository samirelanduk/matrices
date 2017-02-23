from unittest import TestCase
import matrices

class MatrixImportTests(TestCase):

    def test_matrix_imported(self):
        from matrices.matrix import Matrix
        self.assertIs(Matrix, matrices.Matrix)



class FunctionImportTests(TestCase):

    def test_vertex_imported(self):
        from matrices.functions import create_vertex
        self.assertIs(create_vertex, matrices.create_vertex)
