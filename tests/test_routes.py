import pytest
from app import app
from app import default_route_text, mean_route_text

def test_default_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == default_route_text.encode('UTF-8')
    
def test_mean_route():
    response = app.test_client().get('/the_mean?the_list=1,2')
    assert response.status_code == 200
    
def test_the_mean_output():
    response = app.test_client().get('/the_mean?the_list=1,2,3')
    expected_result = mean_route_text.format(2.0)
    assert response.status_code == 200
    assert response.data == expected_result.encode('UTF-8')