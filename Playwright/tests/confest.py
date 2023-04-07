import pytest
import requests
from config import *
@pytest.fixture 
def get_req():
    req = requests.get(url_get_list) 
    return req.status_code