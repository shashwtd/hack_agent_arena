
### Environment Interaction 1
----------------------------------------------------------------------------
```python
# First, let's discover the Amazon app APIs
print(apis.api_docs.show_app_descriptions())
```

```
[
 {
  "name": "api_docs",
  "description": "An app to search and explore API documentation."
 },
 {
  "name": "supervisor",
  "description": "An app to access supervisor's personal information, account credentials, addresses, payment cards, and manage the assigned task."
 },
 {
  "name": "amazon",
  "description": "An online shopping app to buy products and manage orders, returns, etc."
 },
 {
  "name": "phone",
  "description": "An app to find and manage contact information for friends, family members, etc., send and receive messages, and manage alarms."
 },
 {
  "name": "file_system",
  "description": "A file system app to create and manage files and folders."
 },
 {
  "name": "spotify",
  "description": "A music streaming app to stream songs and manage song, album and playlist libraries."
 },
 {
  "name": "venmo",
  "description": "A social payment app to send, receive and request money to and from others."
 },
 {
  "name": "gmail",
  "description": "An email app to draft, send, receive, and manage emails."
 },
 {
  "name": "splitwise",
  "description": "A bill splitting app to track and split expenses with people."
 },
 {
  "name": "simple_note",
  "description": "A note-taking app to create and manage notes"
 },
 {
  "name": "todoist",
  "description": "A task management app to manage todo lists and collaborate on them with others."
 }
]
```


### Environment Interaction 2
----------------------------------------------------------------------------
```python
# Get Amazon API descriptions and credentials
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
print(apis.supervisor.show_account_passwords())
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
[
 {
  "account_name": "amazon",
  "password": "@#@wvsw"
 },
 {
  "account_name": "file_system",
  "password": "]NVpauc"
 },
 {
  "account_name": "gmail",
  "password": "W%wsM+p"
 },
 {
  "account_name": "phone",
  "password": "vK6UAEL"
 },
 {
  "account_name": "simple_note",
  "password": "85${X=c"
 },
 {
  "account_name": "splitwise",
  "password": ")^_ixpD"
 },
 {
  "account_name": "spotify",
  "password": "@BfHM4T"
 },
 {
  "account_name": "todoist",
  "password": "eRlD2Ci"
 },
 {
  "account_name": "venmo",
  "password": "+){p}(9"
 }
]
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
# Get Amazon API docs for prime subscription and login
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='login'))
```

```
{
 "app_name": "amazon",
 "api_name": "login",
 "path": "/auth/token",
 "method": "POST",
 "description": "Login to your account.",
 "parameters": [
  {
   "name": "username",
   "type": "string",
   "required": true,
   "description": "Your account email.",
   "default": null,
   "constraints": []
  },
  {
   "name": "password",
   "type": "string",
   "required": true,
   "description": "Your account password.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "access_token": "string",
   "token_type": "string"
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
# Get credentials and login to Amazon, then check prime subscription
accounts = apis.supervisor.show_account_passwords()
amazon_pw = next(x["password"] for x in accounts if x["account_name"] == "amazon")
print(f"Amazon password found: {amazon_pw[:3]}...")

# Login
login_resp = apis.amazon.login(username="kevin.blac@gmail.com", password=amazon_pw)
print(login_resp)
```

```
Amazon password found: @#@...
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24ra2V2aW4uYmxhY0BnbWFpbC5jb20iLCJleHAiOjE2ODQ0NTUzMDh9.1P89yNjCShVO9e8-OFf8aHoZzg3QXi39tTmEfCB4Cac",
 "token_type": "Bearer"
}
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24ra2V2aW4uYmxhY0BnbWFpbC5jb20iLCJleHAiOjE2ODQ0NTUzMDh9.1P89yNjCShVO9e8-OFf8aHoZzg3QXi39tTmEfCB4Cac"

# Check prime subscription API
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_prime_subscription'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 4, in <module>
    print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_prime_subscription'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name show_prime_subscription found for the amazon app. Check the api and app name again."}
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
# Let's see all Amazon APIs to find the right one for prime subscription
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


### Environment Interaction 7
----------------------------------------------------------------------------
```python
# Get the full list - let me search for prime-related APIs
all_apis = apis.api_docs.show_api_descriptions(app_name='amazon')
for api in all_apis:
    print(api['name'], '-', api['description'])
```

```
show_account - Show your account information. Unlike show_profile, this includes private information.
signup - Sign up to create account.
delete_account - Delete your account.
update_account_name - Update your first or last name in the account profile.
login - Login to your account.
logout - Logout from your account.
send_verification_code - Send account verification code to your email address.
verify_account - Verify your account using the verification code sent to your email address.
send_password_reset_code - Send password reset code to your email address.
reset_password - Reset your password using the password reset code sent to your email address.
show_profile - Show public profile information of a user.
show_product - Show product information based on its ID.
search_sellers - Search for sellers with a query.
show_seller - Show a detailed information about the seller.
search_product_types - Search product types present in the database.
show_product_feature_choices - Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database.
search_products - Search for products with a query and various filtering criteria.
show_cart - show your cart.
clear_cart - Clear your cart.
add_product_to_cart - Add product by id and quantities to your cart.
delete_product_from_cart - Remove a product from your cart.
update_product_quantity_in_cart - Update product quantity in the user cart.
apply_promo_code_to_cart - Apply a promo code to your cart.
remove_promo_code_from_cart - Remove a promo code from your cart.
show_wish_list - Get list of products in your wishlist.
clear_wish_list - Clear wish list.
add_product_to_wish_list - Add product by id and quantities to your wish list.
delete_product_from_wish_list - Remove product from the user wish list.
update_product_quantity_in_wish_list - Update product quantity in the user wish_list.
move_product_from_cart_to_wish_list - Move product from the cart to the wish list.
move_product_from_wish_list_to_cart - Move product from the wish list to the cart.
add_gift_wrapping_to_product - Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated.
remove_gift_wrapping_from_product - Remove gift wrapping from a product in your cart.
show_orders - Show or search your past orders
place_order - Place an order for all the items in your cart.
show_order - Get details of a past order.
download_order_receipt - Download the receipt of a past order.
show_payment_cards - Get a list of your payment_cards.
add_payment_card - Add a new payment card.
show_payment_card - Get details of a payment card.
delete_payment_card - Delete payment card information.
update_payment_card - Update payment card information.
show_addresses - Get a list of your addresses.
add_address - Add a new address.
delete_address - Delete address information.
update_address - Update address information.
show_product_reviews - Get a list of product reviews.
write_product_review - Write a product review.
delete_product_review - Delete a product review.
update_product_review - Update a product review.
show_product_questions - Get a list of product questions.
write_product_question - Post a question about a product.
show_product_question_answers - Get a list of answers to a product question.
write_product_question_answer - Write a answer to a product question.
delete_product_question - Delete a product question.
update_product_question - Update a product question.
delete_product_question_answer - Delete a answer to a product question.
update_product_question_answer - Update answer to a product question.
show_returns - Get a list of your product returns.
initiate_return - Initiate a product return.
show_return - Show product return status.
show_return_deliverers - Get a list of product return deliverers.
show_prime_plans - Show information about prime plans available. Delivery fee is waived for prime members.
show_prime_subscriptions - Show your prime subscription history.
subscribe_prime - Subscribe to prime membership.
download_prime_subscription_receipt - Download the receipt for a prime subscription.
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Get the full list
all_apis = apis.api_docs.show_api_descriptions(app_name='amazon')
prime_apis = [api for api in all_apis if 'prime' in api['name'].lower() or 'prime' in api['description'].lower() or 'subscription' in api['name'].lower() or 'subscription' in api['description'].lower()]
print(prime_apis)
print("\nAll API names:")
for api in all_apis:
    print(api['name'])
```

```
[
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

All API names:
show_account
signup
delete_account
update_account_name
login
logout
send_verification_code
verify_account
send_password_reset_code
reset_password
show_profile
show_product
search_sellers
show_seller
search_product_types
show_product_feature_choices
search_products
show_cart
clear_cart
add_product_to_cart
delete_product_from_cart
update_product_quantity_in_cart
apply_promo_code_to_cart
remove_promo_code_from_cart
show_wish_list
clear_wish_list
add_product_to_wish_list
delete_product_from_wish_list
update_product_quantity_in_wish_list
move_product_from_cart_to_wish_list
move_product_from_wish_list_to_cart
add_gift_wrapping_to_product
remove_gift_wrapping_from_product
show_orders
place_order
show_order
download_order_receipt
show_payment_cards
add_payment_card
show_payment_card
delete_payment_card
update_payment_card
show_addresses
add_address
delete_address
update_address
show_product_reviews
write_product_review
delete_product_review
update_product_review
show_product_questions
write_product_question
show_product_question_answers
write_product_question_answer
delete_product_question
update_product_question
delete_product_question_answer
update_product_question_answer
show_returns
initiate_return
show_return
show_return_deliverers
show_prime_plans
show_prime_subscriptions
subscribe_prime
download_prime_subscription_receipt
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Get the prime subscriptions
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_prime_subscriptions'))
```

```
{
 "app_name": "amazon",
 "api_name": "show_prime_subscriptions",
 "path": "/prime/subscriptions",
 "method": "GET",
 "description": "Show your prime subscription history.",
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
  }
 ],
 "response_schemas": {
  "success": [
   {
    "prime_subscription_id": 1,
    "start_date": "2019-01-01T00:00:00",
    "end_date": "2019-01-01T00:00:00",
    "payment_card_digits": "string",
    "paid_amount": 0.0
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24ra2V2aW4uYmxhY0BnbWFpbC5jb20iLCJleHAiOjE2ODQ0NTUzMDh9.1P89yNjCShVO9e8-OFf8aHoZzg3QXi39tTmEfCB4Cac"

# Fetch all prime subscriptions
def fetch_all_subscriptions(token):
    out, page = [], 0
    while True:
        batch = apis.amazon.show_prime_subscriptions(access_token=token, page_index=page, page_limit=20)
        if not batch:
            break
        out.extend(batch)
        if len(batch) < 20:
            break
        page += 1
    return out

subs = fetch_all_subscriptions(access_token)
print(f"Total subscriptions: {len(subs)}")
for s in subs:
    print(s)
```

```
Total subscriptions: 2
{
 "prime_subscription_id": 122,
 "start_date": "2023-03-19T16:27:43",
 "end_date": "2024-03-18T23:59:59",
 "payment_card_digits": "4582",
 "paid_amount": 140.0
}
{
 "prime_subscription_id": 121,
 "start_date": "2023-02-16T16:27:43",
 "end_date": "2023-03-18T23:59:59",
 "payment_card_digits": "4582",
 "paid_amount": 15.0
}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
from datetime import datetime

# Current date from task context
now = datetime(2023, 5, 19, 0, 0, 10)

# The active subscription (most recent with end_date in the future)
active_sub = None
for s in subs:
    end_date = datetime.fromisoformat(s['end_date'])
    if end_date > now:
        active_sub = s
        break

print(f"Active subscription: {active_sub}")
end_date = datetime.fromisoformat(active_sub['end_date'])
print(f"End date: {end_date}")
print(f"Now: {now}")

# Calculate months remaining
diff = end_date - now
days_remaining = diff.days
print(f"Days remaining: {days_remaining}")

# Convert to months (approximately 30.44 days per month)
months_remaining = days_remaining / 30.44
print(f"Months remaining (raw): {months_remaining}")
months_rounded = round(months_remaining)
print(f"Months remaining (rounded): {months_rounded}")

final_answer = str(months_rounded)
print({"final_answer": final_answer, "evidence": f"End date: {end_date}, Now: {now}, Days remaining: {days_remaining}, Months: {months_remaining}"})
```

```
Active subscription: {'prime_subscription_id': 122, 'start_date': '2023-03-19T16:27:43', 'end_date': '2024-03-18T23:59:59', 'payment_card_digits': '4582', 'paid_amount': 140.0}
End date: 2024-03-18 23:59:59
Now: 2023-05-19 00:00:10
Days remaining: 304
Months remaining (raw): 9.986859395532194
Months remaining (rounded): 10
{
 "final_answer": "10",
 "evidence": "End date: 2024-03-18 23:59:59, Now: 2023-05-19 00:00:10, Days remaining: 304, Months: 9.986859395532194"
}
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
apis.supervisor.complete_task(answer="10")
```

```
Execution successful.
```

