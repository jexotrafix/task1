import unittest 
from model.instr import Save, Eval, apply


class TestApply(unittest.TestCase):
    def test_apply_corectness(self):
        # тестируем правильность работы функции
        self.assertEqual(apply((Save(10), Save(15), Eval('Mult'), Save(10), Eval('Plus')), []), [160])

    # тестируем то, что программа выбрасывает правильный exception при некорректной передаче данных
    def test_apply_throws_right_exception(self):    
        with self.assertRaises(AssertionError):
            apply([Eval("Mult")], [])
  
    # тестировать работу на пустых stack или program - нету смысла ведь это ничего не меняет

if __name__ == '__main__':
    unittest.main()