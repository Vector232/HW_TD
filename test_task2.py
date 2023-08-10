from task2 import *
import pytest
import os
from dotenv import load_dotenv


load_dotenv()

class TestTask2:
    token = os.getenv('token')
    name = 'test'

    def test_create_folder(self):
        assert create_folder(self.token, self.name).status_code == 201

    def test_existence_folder(self):
        assert get_info(self.token, self.name).status_code == 200
        
    def test_delete_folder(self):
        assert delete_folder(self.token, self.name).status_code == 204



if __name__ == '__main__':
    pytest.main(["-vv"])
