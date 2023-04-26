import pytest
import pytest_cov
from unittest.mock import patch
from src.util.dao import DAO
import unittest.mock as mock
import pymongo
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

@pytest.mark.integration
@pytest.mark.parametrize("data", [{"name": "Bullen", "age": 30}, {"name": "Bullen", "age": 30}])
def test_create_not_unique_WriteError(dao, data):
    validation_result = False
    try:
        dao.create(data)
    except pymongo.errors.WriteError:
        validation_result = True
    assert validation_result == True
    dao.drop()

@pytest.mark.integration
@pytest.mark.parametrize("data", [{"name": "Bullen", "age": "Age"}])
def test_create_wrong_Bson_WriteError(dao, data):
    validation_result = False
    try:
        dao.create(data)
    except pymongo.errors.WriteError:
        validation_result = True
    assert validation_result == True
    dao.drop()

@pytest.mark.integration
@pytest.mark.parametrize("data", [{"name": "Bullen", "city": 30}])
def test_create_wrong_properties_WriteError(dao, data):
    validation_result = False
    try:
        dao.create(data)
    except pymongo.errors.WriteError:
        validation_result = True
    assert validation_result == True
    dao.drop()