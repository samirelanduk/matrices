from .matrix import Matrix

def create_vertex(*values):
    return Matrix(*[(value,) for value in values])
