#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceInstantiation(unittest.TestCase):
    """Tests for Place instantiation."""

    def test_is_basemodel_subclass(self):
        """Test that Place is a subclass of BaseModel."""
        obj = Place()
        self.assertIsInstance(obj, BaseModel)

    def test_city_id_class_attr(self):
        """Test that city_id is a class attribute and empty string."""
        self.assertEqual(Place.city_id, "")

    def test_user_id_class_attr(self):
        """Test that user_id is a class attribute and empty string."""
        self.assertEqual(Place.user_id, "")

    def test_name_class_attr(self):
        """Test that name is a class attribute and empty string."""
        self.assertEqual(Place.name, "")

    def test_description_class_attr(self):
        """Test that description is a class attribute and empty string."""
        self.assertEqual(Place.description, "")

    def test_number_rooms_class_attr(self):
        """Test that number_rooms is a class attribute and 0."""
        self.assertEqual(Place.number_rooms, 0)

    def test_number_bathrooms_class_attr(self):
        """Test that number_bathrooms is a class attribute and 0."""
        self.assertEqual(Place.number_bathrooms, 0)

    def test_max_guest_class_attr(self):
        """Test that max_guest is a class attribute and 0."""
        self.assertEqual(Place.max_guest, 0)

    def test_price_by_night_class_attr(self):
        """Test that price_by_night is a class attribute and 0."""
        self.assertEqual(Place.price_by_night, 0)

    def test_latitude_class_attr(self):
        """Test that latitude is a class attribute and 0.0."""
        self.assertEqual(Place.latitude, 0.0)

    def test_longitude_class_attr(self):
        """Test that longitude is a class attribute and 0.0."""
        self.assertEqual(Place.longitude, 0.0)

    def test_amenity_ids_class_attr(self):
        """Test that amenity_ids is a class attribute and empty list."""
        self.assertEqual(Place.amenity_ids, [])

    def test_number_rooms_is_int(self):
        """Test that number_rooms is an int."""
        self.assertIsInstance(Place.number_rooms, int)

    def test_latitude_is_float(self):
        """Test that latitude is a float."""
        self.assertIsInstance(Place.latitude, float)

    def test_amenity_ids_is_list(self):
        """Test that amenity_ids is a list."""
        self.assertIsInstance(Place.amenity_ids, list)

    def test_str_representation(self):
        """Test that str representation contains Place."""
        obj = Place()
        self.assertIn("Place", str(obj))

    def test_to_dict_class_is_place(self):
        """Test that to_dict has __class__ equal to Place."""
        obj = Place()
        self.assertEqual(obj.to_dict()["__class__"], "Place")

    def test_kwargs_instantiation(self):
        """Test instantiation from dictionary."""
        obj = Place()
        obj_dict = obj.to_dict()
        new_obj = Place(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)


if __name__ == "__main__":
    unittest.main()
