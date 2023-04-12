import pytest
import pytest_cov
import unittest.mock as mock
from src.controllers.usercontroller import UserController, DAO
@pytest.fixture
def sut():
    mocked_dao = mock.MagicMock()
    def find_side_effect(object):
        users = []
        for user in [{'name': "Esbjörn",'email': "user@example.com"},
                     {'name': "James",'email': "user@example.com"},
                     {'name': "Bullen",'email': "bullen@example.com"}
                    ]:
            if user['email'] == object['email']:
                users.append(user)
        if (len(users) == 0):
            return [None]
        return users;
    mocked_dao.find.side_effect = find_side_effect
    sut = UserController(mocked_dao)
    return sut

@pytest.mark.unit
@pytest.mark.parametrize("email", [("blablabla@example.com")])
def test_get_user_by_email_None(sut, email):
    validation_result = sut.get_user_by_email(email)
    assert validation_result is None

@pytest.mark.unit
@pytest.mark.parametrize("email", [("bullen@example.com"), ("user@example.com")])
def test_get_user_by_email_Valid_User(sut, email):
    validation_result = sut.get_user_by_email(email)
    assert validation_result is not None

@pytest.mark.unit
@pytest.mark.parametrize("email, expected_exception", [("invalid_email", ValueError)])
def test_get_user_by_email_single_user(sut, email, expected_exception):
    with pytest.raises(expected_exception):
        sut.get_user_by_email(email)