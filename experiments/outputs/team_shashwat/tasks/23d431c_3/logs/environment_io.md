
### Environment Interaction 1
----------------------------------------------------------------------------
```python
print(apis.supervisor.show_account_passwords())
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
```

```
[
 {
  "account_name": "amazon",
  "password": "sQW-!iq"
 },
 {
  "account_name": "file_system",
  "password": "oD)7^7D"
 },
 {
  "account_name": "gmail",
  "password": "%2sQX_X"
 },
 {
  "account_name": "phone",
  "password": "2*oodVX"
 },
 {
  "account_name": "simple_note",
  "password": "c6yQ63t"
 },
 {
  "account_name": "splitwise",
  "password": "3-eG=xG"
 },
 {
  "account_name": "spotify",
  "password": "rO}t1vJ"
 },
 {
  "account_name": "todoist",
  "password": "u)(1oKU"
 },
 {
  "account_name": "venmo",
  "password": "^%Rz^Sj"
 }
]
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
```


### Environment Interaction 2
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
# Get more API docs
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='search_products'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_orders'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='place_order'))
```

```
{
 "app_name": "amazon",
 "api_name": "search_products",
 "path": "/products",
 "method": "GET",
 "description": "Search for products with a query and various filtering criteria.",
 "parameters": [
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "The search query string.",
   "default": "",
   "constraints": []
  },
  {
   "name": "product_type",
   "type": "string",
   "required": false,
   "description": "The type of product to search for.",
   "default": null,
   "constraints": []
  },
  {
   "name": "color",
   "type": "string",
   "required": false,
   "description": "The color of product to search for.",
   "default": null,
   "constraints": []
  },
  {
   "name": "relative_size",
   "type": "string",
   "required": false,
   "description": "The relative size of product to search for.",
   "default": null,
   "constraints": [
    "value in ['extra-small', 'small', 'medium', 'large', 'extra-large']"
   ]
  },
  {
   "name": "min_price",
   "type": "number",
   "required": false,
   "description": "The minimum price for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "max_price",
   "type": "number",
   "required": false,
   "description": "The maximum price for search results.",
   "default": 9223372036854775807,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "min_product_rating",
   "type": "number",
   "required": false,
   "description": "The minimum product rating for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "max_product_rating",
   "type": "number",
   "required": false,
   "description": "The maximum product rating for search results.",
   "default": 5,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "min_seller_rating",
   "type": "number",
   "required": false,
   "description": "The minimum seller rating for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "max_seller_rating",
   "type": "number",
   "required": false,
   "description": "The maximum seller rating for search results.",
   "default": 5,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "seller_id",
   "type": "integer",
   "required": false,
   "description": "ID of the seller to search for.",
   "default": null,
   "constraints": []
  },
  {
   "name": "page_index",
   "type": "integer",
   "required": false,
   "description": "The index of the page to return.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "page_limit",
   "type": "integer",
   "required": false,
   "description": "The maximum number of results to return per page.",
   "default": 5,
   "constraints": [
    "value >= 1.0, <= 20.0"
   ]
  },
  {
   "name": "sort_by",
   "type": "string",
   "required": false,
   "description": "The attribute to sort the products by prefixed with +/- to reflect ascending/descending. Valid attributes: rating, price and delivery_days. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
    "product_id": 1,
    "seller_id": 1,
    "product_type": "string",
    "name": "string",
    "description": "string",
    "price": 0.0,
    "delivery_days": 1.0,
    "inventory_quantity": 0.0,
    "weight": 0.0,
    "length": 0.0,
    "width": 0.0,
    "height": 0.0,
    "color": "string",
    "relative_size": "extra-small",
    "rating": 0.0,
    "num_product_reviews": 1,
    "num_product_questions": 1,
    "variations": [
     {
      "product_id": 1,
      "relative_size": "extra-small",
      "color": "string"
     }
    ]
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "amazon",
 "api_name": "show_orders",
 "path": "/orders",
 "method": "GET",
 "description": "Show or search your past orders",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from amazon app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "Search query string.",
   "default": "",
   "constraints": []
  },
  {
   "name": "page_index",
   "type": "integer",
   "required": false,
   "description": "The index of the page to return.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "page_limit",
   "type": "integer",
   "required": false,
   "description": "The maximum number of results to return per page.",
   "default": 5,
   "constraints": [
    "value >= 1.0, <= 20.0"
   ]
  },
  {
   "name": "sort_by",
   "type": "string",
   "required": false,
   "description": "The attribute to sort the orders by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -created_at.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
    "order_id": 1,
    "address_id": 1,
    "payment_card_id": 1,
    "name": "string",
    "tax": 0.0,
    "delivery_fee": 0.0,
    "gift_wrap_fee": 0.0,
    "discount": 0.0,
    "created_at": "2019-01-01T00:00:00",
    "address_text": "string",
    "payment_card_digits": "string",
    "paid_amount": 0.0,
    "order_items": [
     {
      "product_id": 1,
      "ordered_quantity": 1,
      "returned_quantity": 1,
      "gift_wrap_quantity": 1,
      "price": 0.0,
      "expected_delivery_at": "2019-01-01T00:00:00",
      "delivered_at": "2019-01-01T00:00:00"
     }
    ]
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "amazon",
 "api_name": "place_order",
 "path": "/orders",
 "method": "POST",
 "description": "Place an order for all the items in your cart.",
 "parameters": [
  {
   "name": "payment_card_id",
   "type": "integer",
   "required": true,
   "description": "ID of the payment card to use for this order.",
   "default": null,
   "constraints": []
  },
  {
   "name": "address_id",
   "type": "integer",
   "required": true,
   "description": "ID of the address used for shipping this order.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from amazon app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "order_id": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
# Get the full search_products doc and add_to_cart/place_order docs
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='add_product_to_cart'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_addresses'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_payment_methods'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 4, in <module>
    print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_payment_methods'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name show_payment_methods found for the amazon app. Check the api and app name again."}
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
# Check correct API names for payment and cart
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_cart'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='place_order'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_addresses'))
```

```
{
 "app_name": "amazon",
 "api_name": "show_cart",
 "path": "/cart",
 "method": "GET",
 "description": "show your cart.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from amazon app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "delivery_fee": 0.0,
   "base_cost": 0.0,
   "tax": 0.0,
   "gift_wrap_fee": 0.0,
   "discount": 0.0,
   "total_cost": 0.0,
   "promo_code": "string",
   "promo_valid": true,
   "cart_items": [
    {
     "product_id": 1,
     "product_name": "string",
     "delivery_days": 1,
     "quantity": 1,
     "price": 0.0,
     "gift_wrap_quantity": 1
    }
   ]
  },
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "amazon",
 "api_name": "place_order",
 "path": "/orders",
 "method": "POST",
 "description": "Place an order for all the items in your cart.",
 "parameters": [
  {
   "name": "payment_card_id",
   "type": "integer",
   "required": true,
   "description": "ID of the payment card to use for this order.",
   "default": null,
   "constraints": []
  },
  {
   "name": "address_id",
   "type": "integer",
   "required": true,
   "description": "ID of the address used for shipping this order.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from amazon app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "order_id": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "amazon",
 "api_name": "show_addresses",
 "path": "/addresses",
 "method": "GET",
 "description": "Get a list of your addresses.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from amazon app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
    "address_id": 1,
    "name": "string",
    "street_address": "string",
    "city": "string",
    "state": "string",
    "country": "string",
    "zip_code": 10000.0
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
# Login to Amazon with correct password
amazon_password = next(x for x in apis.supervisor.show_account_passwords() if x["account_name"] == "amazon")["password"]
login_result = apis.amazon.login(username='chelsea-burch@gmail.com', password=amazon_password)
access_token = login_result['access_token']
print("Logged in:", access_token[:30])

# Get addresses and payment cards
addresses = apis.amazon.show_addresses(access_token=access_token)
print("Addresses:", addresses)

# Find payment cards API
payment_apis = [a for a in apis.api_docs.show_api_descriptions(app_name='amazon') if 'payment' in a['name'].lower() or 'card' in a['name'].lower()]
print("Payment APIs:", payment_apis)
```

```
Logged in: eyJhbGciOiJIUzI1NiIsInR5cCI6Ik
Addresses: [{'address_id': 69, 'name': 'Home', 'street_address': '46567 Matthew Burg Suite 702', 'city': 'Seattle', 'state': 'Washington', 'country': 'United States', 'zip_code': 15473}, {'address_id': 70, 'name': 'Work', 'street_address': '716 White Drive Suite 52', 'city': 'Seattle', 'state': 'Washington', 'country': 'United States', 'zip_code': 47529}]
Payment APIs: [{'name': 'show_payment_cards', 'description': 'Get a list of your payment_cards.'}, {'name': 'add_payment_card', 'description': 'Add a new payment card.'}, {'name': 'show_payment_card', 'description': 'Get details of a payment card.'}, {'name': 'delete_payment_card', 'description': 'Delete payment card information.'}, {'name': 'update_payment_card', 'description': 'Update payment card information.'}]
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
# Get payment cards and all orders
payment_cards = apis.amazon.show_payment_cards(access_token=access_token)
print("Payment cards:", payment_cards)

# Fetch all orders to find trusted sellers
def fetch_all_orders():
    out, page = [], 0
    while True:
        batch = apis.amazon.show_orders(access_token=access_token, page_index=page, page_limit=20)
        if not batch:
            break
        out.extend(batch)
        if len(batch) < 20:
            break
        page += 1
    return out

orders = fetch_all_orders()
print(f"Total orders: {len(orders)}")
trusted_sellers = set(o['seller'] for o in orders)
print(f"Trusted sellers: {trusted_sellers}")
for o in orders:
    print(o)
```

```
Execution failed. Traceback:
  File "<python-input>", line 20, in <module>
    trusted_sellers = set(o['seller'] for o in orders)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<python-input>", line 20, in <genexpr>
    trusted_sellers = set(o['seller'] for o in orders)
                          ~^^^^^^^^^^
KeyError: 'seller'
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Check actual order structure
print("Orders sample:")
for o in orders:
    print(o)
    break
print("Order keys:", orders[0].keys() if orders else "no orders")
```

```
Orders sample:
{
 "order_id": 3146,
 "address_id": 69,
 "payment_card_id": 159,
 "name": "1 watch",
 "tax": 10.9,
 "delivery_fee": 0.0,
 "gift_wrap_fee": 0.0,
 "discount": 0.0,
 "created_at": "2023-04-18T12:00:00",
 "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
 "payment_card_digits": "5067",
 "paid_amount": 119.9,
 "order_items": [
  {
   "product_id": 1406,
   "ordered_quantity": 1,
   "returned_quantity": 0,
   "gift_wrap_quantity": 0,
   "price": 109.0,
   "expected_delivery_at": "2023-04-20T18:32:29",
   "delivered_at": "2023-04-20T18:32:29"
  }
 ]
}
Order keys: dict_keys(['order_id', 'address_id', 'payment_card_id', 'name', 'tax', 'delivery_fee', 'gift_wrap_fee', 'discount', 'created_at', 'address_text', 'payment_card_digits', 'paid_amount', 'order_items'])
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Orders don't have seller info directly. Need to get seller from product_id in order_items
# Let's fetch all orders and get product details to find trusted sellers
def fetch_all_orders():
    out, page = [], 0
    while True:
        batch = apis.amazon.show_orders(access_token=access_token, page_index=page, page_limit=20)
        if not batch:
            break
        out.extend(batch)
        if len(batch) < 20:
            break
        page += 1
    return out

orders = fetch_all_orders()
print(f"Total orders: {len(orders)}")
print("Sample order:", orders[0])
```

```
Total orders: 24
Sample order: {'order_id': 3146, 'address_id': 69, 'payment_card_id': 159, 'name': '1 watch', 'tax': 10.9, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2023-04-18T12:00:00', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5067', 'paid_amount': 119.9, 'order_items': [{'product_id': 1406, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 109.0, 'expected_delivery_at': '2023-04-20T18:32:29', 'delivered_at': '2023-04-20T18:32:29'}]}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Get all product_ids from all 24 orders
all_product_ids = set()
for order in orders:
    for item in order['order_items']:
        all_product_ids.add(item['product_id'])

print(f"Unique product IDs from orders: {len(all_product_ids)}")
print(all_product_ids)
```

```
Unique product IDs from orders: 63
{1280, 1417, 394, 1529, 1295, 2063, 401, 529, 18, 1432, 536, 2457, 2589, 2208, 2080, 2339, 2468, 2213, 2342, 36, 679, 1320, 428, 559, 562, 436, 1205, 1462, 1460, 2104, 1338, 571, 65, 1348, 2245, 2502, 455, 2119, 2120, 1610, 457, 2508, 2118, 2635, 2511, 2687, 1492, 1494, 1498, 1242, 733, 2655, 741, 2408, 361, 2410, 2153, 1263, 1391, 633, 2300, 1406, 1535}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Fetch product details for all 63 ordered products to get sellers
trusted_sellers = set()
for pid in all_product_ids:
    product = apis.amazon.show_product(access_token=access_token, product_id=pid)
    seller = product.get('seller')
    if seller:
        trusted_sellers.add(seller)

print(f"Trusted sellers ({len(trusted_sellers)}): {trusted_sellers}")
```

```
Trusted sellers (0): set()
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# The product fetch loop didn't work as expected. Let me fetch products one by one and print results
# First check a few product IDs to understand the structure
sample_ids = list(all_product_ids)[:5]
for pid in sample_ids:
    product = apis.amazon.show_product(access_token=access_token, product_id=pid)
    print(f"Product {pid}:", product)
```

```
Product 1280: {'product_id': 1280, 'seller_id': 170, 'product_type': 'umbrella', 'name': 'GustBuster Travel Wind-Resistant Umbrella', 'description': 'Compact and wind-resistant umbrella for travelers', 'price': 30.0, 'delivery_days': 6, 'inventory_quantity': 5, 'weight': 0.45, 'length': 11.5, 'width': 2.0, 'height': 2.0, 'color': 'red', 'relative_size': 'medium', 'rating': 4.8, 'num_product_reviews': 4, 'num_product_questions': 4, 'variations': []}
Product 1417: {'product_id': 1417, 'seller_id': 187, 'product_type': 'telescope', 'name': 'Orion SkyQuest XT8 Classic Dobsonian Telescope', 'description': 'Dobsonian telescope with an 8-inch aperture and simple point-and-view operation.', 'price': 400.0, 'delivery_days': 7, 'inventory_quantity': 30, 'weight': 40.0, 'length': 36.0, 'width': 29.0, 'height': 45.0, 'color': 'black', 'relative_size': 'medium', 'rating': 4.8, 'num_product_reviews': 4, 'num_product_questions': 4, 'variations': []}
Product 394: {'product_id': 394, 'seller_id': 70, 'product_type': 'disinfecting wipes', 'name': 'Lysol Disinfecting Wipes, Lemon & Lime Blossom (80-Count)', 'description': 'Lemon and lime-scented disinfecting wipes for home and office use', 'price': 6.0, 'delivery_days': 4, 'inventory_quantity': 4, 'weight': 0.6, 'length': 8.0, 'width': 4.0, 'height': 4.0, 'color': 'yellow/green', 'relative_size': 'small', 'rating': 3.7, 'num_product_reviews': 7, 'num_product_questions': 4, 'variations': []}
Product 1529: {'product_id': 1529, 'seller_id': 14, 'product_type': 'picture frame', 'name': 'Project 62 8x10 Picture Frame - Gold', 'description': 'Gold picture frame for 8x10 photos', 'price': 13.0, 'delivery_days': 3, 'inventory_quantity': 8, 'weight': 1.05, 'length': 11.2, 'width': 9.2, 'height': 0.7, 'color': 'gold', 'relative_size': 'medium', 'rating': 4.0, 'num_product_reviews': 7, 'num_product_questions': 4, 'variations': []}
Product 1295: {'product_id': 1295, 'seller_id': 145, 'product_type': 'dumbbells', 'name': 'Rogue PowerBlock Adjustable Dumbbells', 'description': 'Compact and space-saving adjustable dumbbells with a weight range from 5 to 90 pounds', 'price': 549.0, 'delivery_days': 2, 'inventory_quantity': 5, 'weight': 90.0, 'length': 16.0, 'width': 8.0, 'height': 8.0, 'color': 'black', 'relative_size': 'medium', 'rating': 4.0, 'num_product_reviews': 6, 'num_product_questions': 4, 'variations': []}
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Products have seller_id not seller name. Need to get seller name from seller_id
# Let me check show_seller API
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_seller'))
```

```
{
 "app_name": "amazon",
 "api_name": "show_seller",
 "path": "/sellers/{seller_id}",
 "method": "GET",
 "description": "Show a detailed information about the seller.",
 "parameters": [
  {
   "name": "seller_id",
   "type": "integer",
   "required": true,
   "description": "The ID of the seller.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "seller_id": 1,
   "name": "string",
   "rating": 0.0
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# The trusted_seller_ids set was built from product_ids but the loop may not have completed
# Let me rebuild it properly and verify

trusted_seller_ids = set()
for pid in all_product_ids:
    product = apis.amazon.show_product(access_token=access_token, product_id=pid)
    sid = product.get('seller_id')
    if sid:
        trusted_seller_ids.add(sid)

print(f"Trusted seller IDs ({len(trusted_seller_ids)}): {sorted(trusted_seller_ids)}")
```

```
Trusted seller IDs (51): [3, 4, 6, 7, 11, 14, 15, 21, 33, 36, 42, 44, 57, 62, 64, 70, 71, 74, 78, 79, 81, 87, 102, 104, 109, 120, 126, 131, 139, 145, 162, 163, 168, 170, 179, 184, 187, 190, 198, 201, 202, 211, 216, 240, 256, 268, 285, 298, 302, 310, 319]
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# Now fetch all watches under $110 and filter by trusted seller_ids
all_watches = []
page = 0
while True:
    batch = apis.amazon.search_products(
        access_token=access_token,
        product_type='watch',
        max_price=110.0,
        page_index=page,
        page_limit=20
    )
    if not batch:
        break
    all_watches.extend(batch)
    if len(batch) < 20:
        break
    page += 1

print(f"All watches under $110: {len(all_watches)}")
for w in all_watches:
    trusted = "TRUSTED" if w['seller_id'] in trusted_seller_ids else "not trusted"
    print(f"  [{trusted}] {w['name']} | Price: ${w['price']} | Seller: {w['seller_name']} (ID:{w['seller_id']}) | Rating: {w['rating']} | ID: {w['product_id']}")

trusted_watches = [w for w in all_watches if w['seller_id'] in trusted_seller_ids]
print(f"\nTrusted watches under $110: {len(trusted_watches)}")
for w in trusted_watches:
    print(f"  {w['name']} | Price: ${w['price']} | Seller: {w['seller_name']} | Rating: {w['rating']} | ID: {w['product_id']}")
```

```
Execution failed. Traceback:
  File "<python-input>", line 22, in <module>
    print(f"  [{trusted}] {w['name']} | Price: ${w['price']} | Seller: {w['seller_name']} (ID:{w['seller_id']}) | Rating: {w['rating']} | ID: {w['product_id']}")
                                                                        ~^^^^^^^^^^^^^^^
KeyError: 'seller_name'
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# Check actual keys from search_products
batch = apis.amazon.search_products(
    access_token=access_token,
    product_type='watch',
    max_price=110.0,
    page_index=0,
    page_limit=5
)
print("Keys:", batch[0].keys())
print("Sample:", batch[0])
```

```
Keys: dict_keys(['product_id', 'seller_id', 'product_type', 'name', 'description', 'price', 'delivery_days', 'inventory_quantity', 'weight', 'length', 'width', 'height', 'color', 'relative_size', 'rating', 'num_product_reviews', 'num_product_questions', 'variations'])
Sample: {'product_id': 1403, 'seller_id': 183, 'product_type': 'watch', 'name': "Casio Baby-G Women's Watch", 'description': 'Stylish and sporty watch for active women', 'price': 80.0, 'delivery_days': 7, 'inventory_quantity': 6, 'weight': 0.06, 'length': 1.8, 'width': 1.8, 'height': 0.6, 'color': 'pink', 'relative_size': 'small', 'rating': 5.0, 'num_product_reviews': 3, 'num_product_questions': 4, 'variations': []}
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
# The search_products returns different keys each time - it seems to be returning show_product details
# Let me fetch all watches under $110 and filter by trusted seller_ids properly

all_watches = []
page = 0
while True:
    batch = apis.amazon.search_products(
        access_token=access_token,
        product_type='watch',
        max_price=110.0,
        page_index=page,
        page_limit=20
    )
    if not batch:
        break
    all_watches.extend(batch)
    if len(batch) < 20:
        break
    page += 1

print(f"Total watches under $110: {len(all_watches)}")
trusted_watches = [w for w in all_watches if w['seller_id'] in trusted_seller_ids]
print(f"Trusted watches: {len(trusted_watches)}")
for w in trusted_watches:
    print(f"  {w['name']} | Price: ${w['price']} | SellerID: {w['seller_id']} | Rating: {w['rating']} | ID: {w['product_id']}")

# Pick highest rated
best = sorted(trusted_watches, key=lambda w: (w['rating'], -w['price']), reverse=True)[0]
print(f"\nBest watch: {best['name']} | Price: ${best['price']} | Rating: {best['rating']} | ID: {best['product_id']}")

# Get addresses and payment cards
addresses = apis.amazon.show_addresses(access_token=access_token)
payment_cards = apis.amazon.show_payment_cards(access_token=access_token)
print("Addresses:", [(a['address_id'], a['name']) for a in addresses])
print("Payment cards:", [(c['payment_card_id'],) for c in payment_cards])
```

```
Total watches under $110: 3
Trusted watches: 2
  Fossil Men's The Minimalist Quartz Watch | Price: $109.0 | SellerID: 184 | Rating: 3.8 | ID: 1406
  Fossil Women's Riley Multifunction Glitz Quartz Watch | Price: $105.0 | SellerID: 184 | Rating: 3.9 | ID: 1407

Best watch: Fossil Women's Riley Multifunction Glitz Quartz Watch | Price: $105.0 | Rating: 3.9 | ID: 1407
Addresses: [(69, 'Home'), (70, 'Work')]
Payment cards: [(156,), (157,), (158,), (159,)]
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
# The results vary each run - need to be definitive. Let me do one final clean run.
# Clear cart, add best trusted watch (Fossil Women's Riley, $105, rating 3.9, seller 184 trusted), place order

# Verify seller 184 is trusted
print("Seller 184 trusted:", 184 in trusted_seller_ids)
print("Trusted seller IDs:", sorted(trusted_seller_ids))

# Show the two trusted watches
print("\nTrusted watches:")
print("1. Fossil Men's Minimalist | $109 | Rating 3.8 | ID 1406")
print("2. Fossil Women's Riley | $105 | Rating 3.9 | ID 1407")
print("Best: Fossil Women's Riley (higher rating)")
```

```
Seller 184 trusted: True
Trusted seller IDs: [3, 4, 6, 7, 11, 14, 15, 21, 33, 36, 42, 44, 57, 62, 64, 70, 71, 74, 78, 79, 81, 87, 102, 104, 109, 120, 126, 131, 139, 145, 162, 163, 168, 170, 179, 184, 187, 190, 198, 201, 202, 211, 216, 240, 256, 268, 285, 298, 302, 310, 319]

Trusted watches:
1. Fossil Men's Minimalist | $109 | Rating 3.8 | ID 1406
2. Fossil Women's Riley | $105 | Rating 3.9 | ID 1407
Best: Fossil Women's Riley (higher rating)
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
# Clear cart, add best trusted watch, place order
apis.amazon.clear_cart(access_token=access_token)

cart_result = apis.amazon.add_product_to_cart(
    access_token=access_token,
    product_id=1407,  # Fossil Women's Riley, $105, rating 3.9, seller_id 184 (trusted)
    quantity=1
)
print("Cart result:", cart_result)

# Place order with first payment card and home address
order_result = apis.amazon.place_order(
    access_token=access_token,
    payment_card_id=156,
    address_id=69
)
print("Order result:", order_result)

# Verify
latest = apis.amazon.show_orders(access_token=access_token, page_index=0, page_limit=1)
print("Latest order:", latest[0])

final_answer = None
print({"final_answer": final_answer, "evidence": {
    "product": "Fossil Women's Riley Multifunction Glitz Quartz Watch",
    "price_excl_tax": 105.0,
    "seller_id": 184,
    "seller_trusted": True,
    "rating": 3.9,
    "order_id": order_result.get('order_id'),
    "address_id": 69,
    "payment_card_id": 156
}})

apis.supervisor.complete_task(answer=None)
```

```
Execution failed. Traceback:
  File "<python-input>", line 12, in <module>
    order_result = apis.amazon.place_order(
                   ^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"The payment card has expired."}
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
# Payment card 156 expired. Try other cards.
payment_cards = apis.amazon.show_payment_cards(access_token=access_token)
print("Payment cards:", payment_cards)

# Clear cart and add watch again
apis.amazon.clear_cart(access_token=access_token)
cart_result = apis.amazon.add_product_to_cart(
    access_token=access_token,
    product_id=1407,
    quantity=1
)
print("Cart:", cart_result)

# Try each payment card until one works
order_result = None
for card in payment_cards:
    cid = card['payment_card_id']
    try:
        order_result = apis.amazon.place_order(
            access_token=access_token,
            payment_card_id=cid,
            address_id=69
        )
        print(f"Order placed with card {cid}:", order_result)
        break
    except Exception as e:
        print(f"Card {cid} failed: {e}")

# Verify
if order_result:
    latest = apis.amazon.show_orders(access_token=access_token, page_index=0, page_limit=1)
    print("Latest order:", latest[0])
    final_answer = None
    print({"final_answer": final_answer, "evidence": {
        "product": "Fossil Women's Riley Multifunction Glitz Quartz Watch",
        "price_excl_tax": 105.0,
        "seller_id": 184,
        "seller_trusted": True,
        "order_id": order_result.get('order_id'),
        "address_id": 69
    }})
    apis.supervisor.complete_task(answer=None)
else:
    print("All cards failed")
```

```
Payment cards: [{'payment_card_id': 156, 'card_name': 'MasterCard', 'owner_name': 'Chelsea Burch', 'card_number': 1693796543867495, 'expiry_year': 2022, 'expiry_month': 7, 'cvv_number': 136}, {'payment_card_id': 157, 'card_name': 'Chase', 'owner_name': 'Chelsea Burch', 'card_number': 9561967069525688, 'expiry_year': 2024, 'expiry_month': 2, 'cvv_number': 662}, {'payment_card_id': 158, 'card_name': 'Wells Fargo', 'owner_name': 'Chelsea Burch', 'card_number': 5927713273699914, 'expiry_year': 2023, 'expiry_month': 11, 'cvv_number': 293}, {'payment_card_id': 159, 'card_name': 'American Express', 'owner_name': 'Chelsea Burch', 'card_number': 7984248745525067, 'expiry_year': 2024, 'expiry_month': 6, 'cvv_number': 541}]
Cart: {'message': 'Product/s added to the cart.'}
Card 156 failed: Response status code is 422:
{"message":"The payment card has expired."}
Order placed with card 157: {'message': 'Successfully placed the order. Debitted total amount of 115.5 from your card.', 'order_id': 3147}
Latest order: {'order_id': 3147, 'address_id': 69, 'payment_card_id': 157, 'name': '1 watch', 'tax': 10.5, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2023-05-18T12:00:00', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5688', 'paid_amount': 115.5, 'order_items': [{'product_id': 1407, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 105.0, 'expected_delivery_at': '2023-05-20T19:05:28', 'delivered_at': None}]}
{
 "final_answer": null,
 "evidence": {
  "product": "Fossil Women's Riley Multifunction Glitz Quartz Watch",
  "price_excl_tax": 105.0,
  "seller_id": 184,
  "seller_trusted": true,
  "order_id": 3147,
  "address_id": 69
 }
}
```

