import pytest
import pytest_cov
from unittest.mock import patch
from src.util.dao import DAO
import unittest.mock as mock

collection_name = "mockedcollection"
validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "age"],
        "properties": {
            "name": {
                "bsonType": "string",
                "uniqueItems": True
            },
            "age": {
                "bsonType": "int"
            }
        }
    }
}
@pytest.fixture()
@patch("src.util.dao.getValidator")
def dao(mockedValidator):
    mockedValidator.return_value = validator
    print(mockedValidator)
    dao = DAO(collection_name)
    return dao

@pytest.mark.integration
@pytest.mark.parametrize("data", [{"name": "Bullen", "age": 30}])
def test_create_valid(dao, data):
    validation_result = dao.create(data)
    assert validation_result is not None
    dao.drop()

# @pytest.mark.unit
# @pytest.mark.parametrize("email, expected_exception", [("invalid_email", ValueError)])
# def test_get_user_by_email_ValueError_invalid_email(sut, email, expected_exception):
#     with pytest.raises(expected_exception):
#         sut.get_user_by_email(email)

