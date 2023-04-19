import pytest
import pytest_cov
from src.util.dao import DAO

@pytest.fixture()
def dao():
    collection_name = "task"
    dao = DAO(collection_name)
    return dao

@pytest.mark.integration
@pytest.mark.parametrize("data", [("hej")])
def test_create_valid(dao, data):
    validation_result = dao.create(data)
    assert validation_result is not None

# @pytest.mark.unit
# @pytest.mark.parametrize("email", [("bullen@example.com"), ("user@example.com")])
# def test_get_user_by_email_Valid_User(sut, email):
#     validation_result = sut.get_user_by_email(email)
#     assert validation_result is not None

# @pytest.mark.unit
# @pytest.mark.parametrize("email, expected_exception", [("invalid_email", ValueError)])
# def test_get_user_by_email_ValueError_invalid_email(sut, email, expected_exception):
#     with pytest.raises(expected_exception):
#         sut.get_user_by_email(email)

