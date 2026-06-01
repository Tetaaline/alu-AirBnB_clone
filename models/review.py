#!/usr/bin/python3
"""This module defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review with public class attributes."""

    place_id = ""
    user_id = ""
    text = ""
