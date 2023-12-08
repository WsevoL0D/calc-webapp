from bs4 import BeautifulSoup
import pytest
import requests #NOTE: requst module must be installed previous to tests

def test_http_avail(endpoint):
  response = requests.get(endpoint)
  assert response.status_code == 200

calc_buttons = list(range(0,9))
@pytest.mark.parametrize("item",calc_buttons)
def test_http_content(endpoint,item):
  response = requests.get(endpoint)
  # print (str(item) in BeautifulSoup(response.text,"html.parser").find('table').text)
  # print ('@' in BeautifulSoup(response.text,"html.parser").find('table').text)
  assert str(item) in BeautifulSoup(response.text,"html.parser").find('table').text


# def test_http_file_avalability(endpoint, file_path):
#   response = requests.get(endpoint+f"/{file_path}")
#   assert response.status_code == 200