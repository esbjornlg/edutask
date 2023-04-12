import pytest
import pytest_cov
import unittest.mock as mock
from src.controllers.usercontroller import UserController, DAO

# @pytext.fixture
# def sut

@pytest.fixture
def sut():
    mocked_dao = mock.MagicMock()
    mocked_dao.dao.find.return_value=[{'name':"Esbjörn",'email':"user@example.com"},
                                      {'name':"James",'email':"user@example.com"},
                                      {'name':"Bullen",'email':"bullen@example.com"},
                                      ]
    sut = UserController(mocked_dao)
    return sut
    
@pytest.mark.unit
@pytest.mark.parametrize("email, expected", [("user@example.com", "Esbjörn"),("bullen@example.com", "Bullen")])
def test_get_user_by_email_single_user(sut,email, expected):
    validation_result = sut.get_user_by_email(email)
    assert validation_result['name'] == expected
    