#!/usr/bin/python3
"""
Defines the State class, a subclass of BaseModel.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    Represents a state, inheriting from the BaseModel class.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
    """The name of the state."""
