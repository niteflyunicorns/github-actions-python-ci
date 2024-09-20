import unittest

from src.calculator import add, subtract, divide

class TestCalculator( unittest.TestCase ):
    def test_add( self ):
        self.assertEqual( add( 2, 3 ), 5 )
        self.assertEqual( add( -1, 1 ), 0 )
        self.assertEqual( add( -1, -1 ), -2 )

    def test_subtract( self ):
        self.assertEqual( subtract( 4, 3 ), 1 )
        self.assertEqual( subtract( 3, 4 ), -1 )
        self.assertEqual( subtract( -1, -1 ), 0 )

    def test_divide( self ):
        self.assertMultiLineEqual( divide( 2, 0 ), "Error: divide by zero" )
        self.assertEqual( divide( -1, 2 ), -0.5 )
        self.assertEqual( divide( -10, -2 ), 5 )


if __name__ == '__main__':
    unittest.main()
