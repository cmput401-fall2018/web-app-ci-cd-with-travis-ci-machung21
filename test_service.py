from unittest.mock import patch
from unittest import TestCase
from service import Service

class UnitTestService(TestCase):
    
    # returns a random number
    @patch('service.Service.bad_random')
    def test_bad_random(self, mock_bad_random):
        mock_bad_random.return_value = 10
        randNum = Service.bad_random()
        self.assertEqual(randNum, 10)

    @patch('service.Service.bad_random')
    def test_divide(self, mock_bad_random):
        mock_bad_random.return_value = 10
        import_serv = Service()
        divNum = import_serv.divide(5)
        self.assertEqual(divNum, 2)

    @patch('service.Service.bad_random')
    def test_abs_plus(self, x):
        import_serv = Service()
        absNum = import_serv.abs_plus(-4)
        self.assertEqual(absNum, 5)

    @patch('service.Service.bad_random')    
    def test_complicated_function(self, mock_bad_random):
        mock_bad_random.return_value = 10
        import_serv = Service()
        compNum = import_serv.complicated_function(5)
        self.assertEqual(compNum, (2.0, 0))