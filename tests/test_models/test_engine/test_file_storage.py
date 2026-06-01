#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestFileStorageInstantiation(unittest.TestCase):
    """Tests for FileStorage instantiation."""

    def test_no_args(self):
        """Test that FileStorage can be instantiated without args."""
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_storage_is_filestorage(self):
        """Test that the storage variable is a FileStorage instance."""
        self.assertIsInstance(storage, FileStorage)

    def test_file_path_is_private(self):
        """Test that __file_path is a private class attribute."""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_private(self):
        """Test that __objects is a private class attribute."""
        self.assertFalse(hasattr(FileStorage(), "__objects"))


class TestFileStorageAll(unittest.TestCase):
    """Tests for FileStorage all method."""

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_all_returns_same_dict(self):
        """Test that all() returns the same dict object consistently."""
        self.assertIs(storage.all(), storage.all())


class TestFileStorageNew(unittest.TestCase):
    """Tests for FileStorage new method."""

    def test_new_adds_object(self):
        """Test that new() adds an object to __objects."""
        obj = BaseModel()
        storage.new(obj)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def test_new_adds_user(self):
        """Test that new() adds a User object."""
        obj = User()
        storage.new(obj)
        key = "User.{}".format(obj.id)
        self.assertIn(key, storage.all())


class TestFileStorageSave(unittest.TestCase):
    """Tests for FileStorage save method."""

    def test_save_creates_file(self):
        """Test that save() creates file.json."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_file_is_valid_json(self):
        """Test that the saved file contains valid JSON."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIsInstance(data, dict)

    def test_save_includes_basemodel(self):
        """Test that saved file includes BaseModel object."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, data)


class TestFileStorageReload(unittest.TestCase):
    """Tests for FileStorage reload method."""

    def test_reload_does_not_raise_if_no_file(self):
        """Test that reload does not raise if file.json doesn't exist."""
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json.bak")
        try:
            storage.reload()
        except Exception as e:
            self.fail("reload raised an exception: {}".format(e))
        finally:
            if os.path.exists("file.json.bak"):
                os.rename("file.json.bak", "file.json")

    def test_reload_restores_objects(self):
        """Test that reload restores previously saved objects."""
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        old_id = obj.id
        storage.reload()
        key = "BaseModel.{}".format(old_id)
        self.assertIn(key, storage.all())

    def test_reload_restores_user(self):
        """Test that reload restores User objects."""
        obj = User()
        obj.email = "test@test.com"
        storage.new(obj)
        storage.save()
        old_id = obj.id
        storage.reload()
        key = "User.{}".format(old_id)
        self.assertIn(key, storage.all())

    def test_reload_all_classes(self):
        """Test that reload handles all supported classes."""
        classes = [State, City, Amenity, Place, Review]
        ids = []
        for cls in classes:
            obj = cls()
            storage.new(obj)
            ids.append((cls.__name__, obj.id))
        storage.save()
        storage.reload()
        for class_name, obj_id in ids:
            key = "{}.{}".format(class_name, obj_id)
            self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
