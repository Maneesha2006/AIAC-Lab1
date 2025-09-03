import pytest
from task_4 import ShoppingCart

def test_remove_existing_item(capsys):
    cart = ShoppingCart()
    cart.add_item("Apple", 1.0)
    cart.remove_item("Apple")
    assert "Apple" not in cart.items

def test_remove_nonexistent_item(capsys):
    cart = ShoppingCart()
    cart.add_item("Banana", 0.5)
    cart.remove_item("Orange")
    captured = capsys.readouterr()
    assert "Item 'Orange' not found in cart." in captured.out

def test_remove_item_from_empty_cart(capsys):
    cart = ShoppingCart()
    cart.remove_item("Milk")
    captured = capsys.readouterr()
    assert "Item 'Milk' not found in cart." in captured.out     