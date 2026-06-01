#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUserInstantiation(unittest.TestCase):
    """Tests for User instantiation."""

    def test_is_basemodel_subclass(self):
        """Test that User is a subclass of BaseModel."""
        obj = User()
        self.assertIsInstance(obj, BaseModel)

    def test_email_class_attr(self):
        """Test that email is a class attribute and empty string."""
        self.assertEqual(User.email, "")

    def test_password_class_attr(self):
        """Test that password is a class attribute and empty string."""
        self.assertEqual(User.password, "")

    def test_first_name_class_attr(self):
        """Test that first_name is a class attribute and empty string."""
        self.assertEqual(User.first_name, "")

    def test_last_name_class_attr(self):
        """Test that last_name is a class attribute and empty string."""
        self.assertEqual(User.last_name, "")

    def test_email_is_string(self):
        """Test that email attribute type is str."""
        self.assertIsInstance(User.email, str)

    def test_password_is_string(self):
        """Test that password attribute type is str."""
        self.assertIsInstance(User.password, str)

    def test_first_name_is_string(self):
        """Test that first_name attribute type is str."""
        self.assertIsInstance(User.first_name, str)

    def test_last_name_is_string(self):
        """Test that last_name attribute type is str."""
        self.assertIsInstance(User.last_name, str)

    def test_str_representation(self):
        """Test that str representation contains User."""
        obj = User()
        self.assertIn("User", str(obj))

    def test_to_dict_class_is_user(self):
        """Test that to_dict has __class__ equal to User."""
        obj = User()
        self.assertEqual(obj.to_dict()["__class__"], "User")

    def test_kwargs_instantiation(self):
        """Test instantiation with keyword arguments."""
        obj = User()
        obj.email = "test@test.com"
        obj_dict = obj.to_dict()
        new_obj = User(**obj_dict)
        self.assertEqual(new_obj.email, "test@test.com")


class TestUserSave(unittest.TestCase):
    """Tests for User save method."""

    def test_save_updates_updated_at(self):
        """Test that save updates updated_at."""
        import time
        obj = User()
        old = obj.updated_at
        time.sleep(0.01)
        obj.save()
        self.assertGreater(obj.updated_at, old)


if __name__ == "__main__":
    unittest.main()
