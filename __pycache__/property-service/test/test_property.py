from property import get_property

def test_get_property_has_elements():
    propertys = get_property()
    assert len(propertys)>0

