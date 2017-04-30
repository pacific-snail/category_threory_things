import unittest

# 1.Implement, as best as you can, the identity function in your favorite language (or the second favorite, if your favorite language happens to be Haskell).
class Function(object):
    def __init__(self, do = lambda x: x):
        self.do = do
    # 2. Implement the composition function in your favorite language. It takes two functions as arguments and returns a function that is their composition.
    def __mul__(self, other):
        # compose self(other):
        return Function(lambda y: self.do(other.do(y)))
    def __call__(self, value):
        return self.do(value)


class Test(unittest.TestCase):
    # 3. Write a program that tries to test that your composition function respects identity.
    def test_identity_composition(self):
        id_ = Function()
        f = Function(lambda x: x**2+5)
        self.assertEqual((id_*f)(6),
                         (f*id_)(6))
    def test_identity(self):
        id_ = Function()
        self.assertEqual(id_(5), 5)
    def test_square(self):
        square = Function(lambda x: x**2)
        self.assertEqual(25, square(5))
    def test_add(self):
        plus_two = Function(lambda x: x+2)
        plus_three = Function(lambda x: x+3)

        self.assertEqual(7, plus_two(5))
        self.assertEqual(8, plus_three(5))
    def test_composition(self):
        square = Function(lambda x: x**2)
        plus_two = Function(lambda x: x+2)
        plus_three = Function(lambda x: x+3)
        
        self.assertEqual(49, (square*plus_two)(5))
        self.assertEqual(27, (plus_two*square)(5))
        self.assertEqual(28, (plus_three*square)(5))
    def test_associativity(self):
        square = Function(lambda x: x**2)
        plus_two = Function(lambda x: x+2)
        plus_three = Function(lambda x: x+3)
                
        self.assertEqual(((plus_two*square)*plus_three)(5),
                         ((plus_two*(square*plus_three))(5)))
        

# tests:
if __name__ ==  "__main__":
    unittest.main()
    

'''
Other, more abstract questions:
4. Is the world-wide web a category in any sense? Are links morphisms?
the subset of web such that each link is in 1-to-1 correspondence with 
its content is a category:
- has an identity function
- linking is associative

(erroneous pages are excluded, as well as stateful links which 
act 'non-deterministically' from a state-agnostic perspective 
and refer to different content; there might be other edge cases, but
the pre-condition of 1-to-1 mapping should be sufficient)

5. Is Facebook a category, with people as objects and friendships as morphisms?
No, friendship is not an associative relationship
thus cannot compose a morphism
(as well as there is no identity function since a person cannot 
be friends with themselves)


6. When is a directed graph a category?
- nodes are objects
- arrows are morphism 

- identity function exists (node to itself)
- following the arrow to obtain next node is associative
'''

