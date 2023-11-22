#!/usr/bin/python3
"""
Unittests for Console (command line)
"""
import unittest
import json
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """Class testing the console"""

    def setUp(self):
        """Sets Up"""
        self.hbnb_cmd = HBNBCommand()
        self.hbnb_cmd.stdout = StringIO()


    def tearDown(self):
        self.hbnb_cmd.stdout.close()

    def test_create_string_param(self):
        """tests the create command with a string"""
        with patch('builtins.input', side_effect=['create State\n', 'quit\n']):
            self.hbnb_cmd.cmdloop()
            output = self.hbnb_cmd.stdout.getvalue()
            self.assertIn("** class name missing **", output)

        # cmd.onecmd('create State name="California"')
        # self.assertIn()
