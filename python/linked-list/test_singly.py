
import pytest
from singly import List

@pytest.fixture
def sample_list():
    ll = List()
    for val in [1, 2, 3]:
        ll.insert(val)
    return ll

def list_to_array(ll):
    """Helper to convert linked list to Python list"""
    result = []
    current = ll.head
    while current:
        result.append(current.data)
        current = current.next
    return result

def test_insert_at_beginning(sample_list):
    sample_list.insert_head(0)
    assert list_to_array(sample_list) == [0, 1, 2, 3]

def test_insert_at_end(sample_list):
    sample_list.insert_tail(4)
    assert list_to_array(sample_list) == [1, 2, 3, 4]

def test_insert_at_position(sample_list):
    sample_list.insert_at(99, 1)
    assert list_to_array(sample_list) == [1, 99, 2, 3]

def test_delete_any_item(sample_list):
    sample_list.delete(2)
    assert list_to_array(sample_list) == [1, 3]
    sample_list.delete(1)
    assert list_to_array(sample_list) == [3]
    sample_list.delete(3)
    assert list_to_array(sample_list) == []

def test_search_found(sample_list):
    assert sample_list.search(2) == 2

def test_search_not_found(sample_list):
    assert sample_list.search(99) == None

def test_reverse_list(sample_list):
    sample_list.reverse()
    assert list_to_array(sample_list) == [3, 2, 1]
