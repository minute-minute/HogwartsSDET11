import os
import pytest
import shutil


def div(a, b):
    return a/b


def teardown_module(module):
    '''generate allure report'''
    print('tear down generate report...')

    if os.path.exists('unit/allure_results'):
        shutil.rmtree('unit/allure_results')

    if os.path.exists('unit/junit.xml'):
        os.remove('unit/junit.xml')

    if os.system('pytest --junitxml=unit/junit.xml --alluredir=unit/allure_results  unit/') == 0:
        # os.system('allure serve unit/allure_results/')
        os.system('allure generate unit/allure_results/ -o unit/allure_html')


class TestDiv:

    @pytest.mark.p0
    @pytest.mark.parametrize('a, b, expected', [
        (2, 1, 2),
        (1, 2, 0.5),
        (3, 9, 0.334),
        (-1, -2, 0.5),
        (2147483647, 2, 1073741823.5),
        (-2147483648, -2, 1073741824.0),
    ])
    def test_type_int(self, a, b, expected):
        '''
        test Integer division
        '''
        assert div(a, b) == expected

    @pytest.mark.p0    
    @pytest.mark.parametrize('a, b, expected', [
        (1.5, 1, 1.5),
        (2, 0.5, 4),
        (2.25, 0.5, 4.5),
        (2, -0.5, -4),
        (1.7976931348623157e+308, 2, 8.988465674311579e+307),
        (2.2250738585072014e-308, -1, -2.2250738585072014e-308),
    ])
    def test_type_float(self, a, b, expected):
        '''
        test division value has float
        '''
        assert div(a, b) == expected

    @pytest.mark.p1    
    @pytest.mark.parametrize('a, b', [
        ('2', 1),
        ('a', 5),
        (2, (1,)),
        ([2], 5),
        (5, {'a': 1}),
        (5, None),
        (False, 5),
        (2, True),
    ])
    def test_type_error(self, a, b):
        '''
        test division value has type not digital
        '''
        with pytest.raises(TypeError):
            div(a, b)

    @pytest.mark.p1    
    @pytest.mark.parametrize('a, b', [
        (2, 0)
    ])
    def test_dividend_zero(self, a, b):
        '''
        test divisor of 0
        '''
        with pytest.raises(ZeroDivisionError):
            div(a, b)

    @pytest.mark.p2    
    @pytest.mark.parametrize('a, b', [
        (2, 2147483648),
        (-2147483649, -2),
        (2, 1.7976931348623157e+307),
        (-2, 2.2250738585072014e-309),
    ])
    def test_over_digital_length(self, a, b):
        '''
        test int and float over max/min length
        '''
        assert div(a, b) is None
