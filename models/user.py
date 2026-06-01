#!/usr/bin/python3
"""This module defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User with public class attributes."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
