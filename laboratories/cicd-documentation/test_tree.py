import unittest
from tree import Tree
from node import Node

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        """Inițializăm un arbore pentru a fi folosit în teste."""
        self.tree = Tree()
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(8)
        self.tree.add(1)
        self.tree.add(4)

    def test_find_existing_node(self):
        """Verifică dacă _find returnează nodul corect pentru o valoare existentă."""
        # Căutăm valoarea 4 pornind de la rădăcină
        result = self.tree._find(4, self.tree.root)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Node)
        self.assertEqual(result.data, 4)

    def test_find_non_existing_node(self):
        """Verifică dacă _find returnează None pentru o valoare inexistentă."""
        result = self.tree._find(10, self.tree.root)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
