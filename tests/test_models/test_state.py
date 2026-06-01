#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateInstantiation(unittest.TestCase):
    """Tests for State instantiation."""

    def test_is_basemodel_subclass(self):
        """Test that State is a subclass of BaseModel."""
        obj = State()
        self.assertIsInstance(obj, BaseModel)

    def test_name_class_attr(self):
        """Test that name is a class attribute and empty string."""
        self.assertEqual(State.name, "")

    def test_name_is_string(self):
        """Test that name attribute type is str."""
        self.assertIsInstance(State.name, str)

    def test_str_representation(self):
        """Test that str representation contains State."""
        obj = State()
        self.assertIn("State", str(obj))

    def test_to_dict_class_is_state(self):
        """Test that to_dict has __class__ equal to State."""
        obj = State()
        self.assertEqual(obj.to_dict()["__class__"], "State")

    def test_kwargs_instantiation(self):
        """Test instantiation from dictionary."""
        obj = State()
        obj_dict = obj.to_dict()
        new_obj = State(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)


if __name__ == "__main__":
    unittest.main()
