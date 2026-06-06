──────────────────────────────── Overall Stats ─────────────────────────────────
Num Passed Tests : 8
Num Failed Tests : 1
Num Total  Tests : 9
──────────────────────────────────── Passes ────────────────────────────────────
>> Passed Requirement
assert answers match.
>> Passed Requirement
assert model changes match
amazon.Product, amazon.Order, amazon.OrderItem,
gmail.UserEmailThread, gmail.GlobalEmailThread, gmail.Email,
gmail.Attachment, file_system.Directory, file_system.File,
ignoring amazon.CartEntry, amazon.Address.
>> Passed Requirement
assert there is >= 1 added record in amazon.Order.
>> Passed Requirement
assert added orders have private_data.num_relatives quantity of products
collectively.
>> Passed Requirement
assert all the ordered products have type data.public.product_type.
>> Passed Requirement
assert ordered products are in price range .
>> Passed Requirement
assert all the orders are to be delivered at main_user.home_address.text
(normalize_text=True)
>> Passed Requirement
assert 0 records have been updated or deleted from amazon.Address using
models.changed_records.
──────────────────────────────────── Fails ─────────────────────────────────────
>> Failed Requirement
assert the ordered products have rating equal to private_data.max_rating
```python
with test(
    """
    assert the ordered products have rating equal to private_data.max_rating
    """
):
    ordered_product_ratings = set_of(ordered_items, "product.rating")
    test.case(ordered_product_ratings, "all ==", private_data.max_rating)
```
----------
AssertionError:  3.8 == 3.9