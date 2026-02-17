import sys
sys.path.append('../ex03')

from financial import parse_finance, get_html

import pytest
from unittest.mock import patch, Mock


def test_success_connection():
    txt = get_html('MSFT')
    assert isinstance(txt, str)

def test_right_search():
    txt = get_html('MSFT')
    assert 'MSFT' in txt

def test_exception():
    with pytest.raises(Exception) as exc_info:
        get_html('UFO')
        assert "not found" in str(exc_info.value)

def test_parsing():
    txt = get_html('MSFT')
    result = parse_finance(txt, 'Total Revenue')
    assert isinstance(result, tuple)
    assert 'Total Revenue' in result

def test_parsing_error():
    txt = get_html('MSFO')
    with pytest.raises(Exception) as exc_info:
        parse_finance(txt, 'Total Revenue')
        assert 'URL does not exist' in str(exc_info.value)


def test_main_incorrect_args():

    test_args = ["financial.py", "only_one_arg"]
    
    with patch.object(sys, 'argv', test_args), \
        patch('builtins.print') as mock_print:
        
        from financial import main
        main()
        
        mock_print.assert_called_with("incorrect input")