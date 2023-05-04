from main import fibonacci, is_prime

def test_is_prime():
    assert is_prime(2) == {"is_prime": True}



#####
def test_fibonacci():
    assert fibonacci(-1) == {"fibonacci": 0}