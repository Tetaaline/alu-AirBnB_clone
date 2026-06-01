#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCityInstantiation(unittest.TestCase):
    """Tests for City instantiation."""

    def test_is_basemodel_subclass(self):
        """Test that City is a subclass of BaseModel."""
        obj = City()
        self.assertIsInstance(obj, BaseModel)

    def test_state_id_class_attr(self):
        """Test that state_id is a class attribute and empty string."""
        self.assertEqual(City.state_id, "")

    def test_name_class_attr(self):
        """Test that name is a class attribute and empty string."""
        self.assertEqual(City.name, "")

    def test_state_id_is_string(self):
        """Test that state_id attribute type is str."""
        self.assertIsInstance(City.state_id, str)

    def test_name_is_string(self):
        """Test that name attribute type is str."""
        self.assertIsInstance(City.name, str)

    def test_str_representation(self):
        """Test that str representation contains City."""
        obj = City()
        self.assertIn("City", str(obj))

    def test_to_dict_class_is_city(self):
        """Test that to_dict has __class__ equal to City."""
        obj = City()
        self.assertEqual(obj.to_dict()["__class__"], "City")

    def test_kwargs_instantiation(self):
        """Test instantiation from dictionary."""
        obj = City()
        obj_dict = obj.to_dict()
        new_obj = City(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)


if __name__ == "__main__":
    unittest.main()
