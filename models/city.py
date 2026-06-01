#!/usr/bin/python3
"""This module defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City with public class attributes."""

    state_id = ""
    name = ""
