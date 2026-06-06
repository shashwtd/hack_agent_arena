
### Environment Interaction 1
----------------------------------------------------------------------------
```python
# First, get supervisor credentials and explore relevant apps
print(apis.supervisor.show_account_passwords())
print(apis.api_docs.show_app_descriptions())
```

```
[
 {
  "account_name": "amazon",
  "password": "oIhoOb9"
 },
 {
  "account_name": "file_system",
  "password": "4k9jcny"
 },
 {
  "account_name": "gmail",
  "password": "#x}}5n5"
 },
 {
  "account_name": "phone",
  "password": "X53y6aW"
 },
 {
  "account_name": "simple_note",
  "password": "eizVxAh"
 },
 {
  "account_name": "splitwise",
  "password": "F{Q8_pw"
 },
 {
  "account_name": "spotify",
  "password": "3a-m^o6"
 },
 {
  "account_name": "todoist",
  "password": "+&R$o4K"
 },
 {
  "account_name": "venmo",
  "password": "rl2A-Xl"
 }
]
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
print(apis.api_docs.show_api_descriptions(app_name='gmail'))
print(apis.api_docs.show_api_descriptions(app_name='splitwise'))
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
  "name": "search_users",
  "description": "Search Gmail users by name or email address."
 },
 {
  "name": "show_inbox_threads",
  "description": "Show or search email threads you have received. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_outbox_threads",
  "description": "Show or search email threads you have sent. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_archived_threads",
  "description": "Show or search email threads you have archived. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_spam_threads",
  "description": "Show or search email threads that have been marked as spam. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_category_sizes",
  "description": "Show the number of email threads in each category of inbox, outbox, archived, spam, and the number of unscheduled and scheduled email drafts."
 },
 {
  "name": "show_thread",
  "description": "Show detailed information about a given email thread, including emails and drafts within it."
 },
 {
  "name": "delete_thread",
  "description": "Delete an email thread."
 },
 {
  "name": "show_email",
  "description": "Show detailed information about a given email."
 },
 {
  "name": "label_thread",
  "description": "Label an email thread."
 },
 {
  "name": "unlabel_thread",
  "description": "Remove label from an email thread."
 },
 {
  "name": "mark_thread_read",
  "description": "Mark an email thread as read."
 },
 {
  "name": "mark_thread_unread",
  "description": "Mark an email thread as unread."
 },
 {
  "name": "mark_thread_archived",
  "description": "Mark an email thread as archived."
 },
 {
  "name": "mark_thread_unarchived",
  "description": "Mark an email thread as unarchived."
 },
 {
  "name": "mark_thread_spam",
  "description": "Mark an email thread as spam."
 },
 {
  "name": "mark_thread_not_spam",
  "description": "Mark an email thread as not spam."
 },
 {
  "name": "mark_thread_starred",
  "description": "Mark an email thread as starred."
 },
 {
  "name": "mark_thread_unstarred",
  "description": "Mark an email thread as unstarred."
 },
 {
  "name": "delete_email_in_thread",
  "description": "Delete an email in a thread."
 },
 {
  "name": "send_email",
  "description": "Send a new email to one or more recipients."
 },
 {
  "name": "reply_to_email",
  "description": "Reply to an existing email in a thread."
 },
 {
  "name": "forward_email_from_thread",
  "description": "Forward an email from an email thread to one or more recipients."
 },
 {
  "name": "forward_email_thread",
  "description": "Forward entire email thread to one or more recipients."
 },
 {
  "name": "show_drafts",
  "description": "Show a list of user drafts."
 },
 {
  "name": "create_draft",
  "description": "Create a new draft."
 },
 {
  "name": "show_draft",
  "description": "Show detailed draft information."
 },
 {
  "name": "delete_draft",
  "description": "Delete draft information."
 },
 {
  "name": "update_draft",
  "description": "Update draft information."
 },
 {
  "name": "send_email_from_draft",
  "description": "Send a new email from a draft right away."
 },
 {
  "name": "download_attachment",
  "description": "Download a file attachment."
 },
 {
  "name": "upload_attachments_to_draft",
  "description": "Upload attachments to a draft."
 },
 {
  "name": "remove_attachment_from_draft",
  "description": "Delete an attachment from a draft."
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
  "name": "search_users",
  "description": "Search Splitwise users by name or email address."
 },
 {
  "name": "show_activity",
  "description": "Show a history of your expenses and payments combined."
 },
 {
  "name": "show_groups",
  "description": "Get a list of groups you are a member of."
 },
 {
  "name": "create_group",
  "description": "Create a new group of friends or family to share expenses with."
 },
 {
  "name": "show_group",
  "description": "Show group details based on its ID."
 },
 {
  "name": "delete_group",
  "description": "Delete a group you are a member of. Any member can undelete it later."
 },
 {
  "name": "update_group",
  "description": "Update group information."
 },
 {
  "name": "undelete_group",
  "description": "Undelete a group you are a member of."
 },
 {
  "name": "add_member_to_group",
  "description": "Add a member to a group."
 },
 {
  "name": "remove_member_from_group",
  "description": "Remove a member from a group."
 },
 {
  "name": "exit_group",
  "description": "Exit from a group you are a part of."
 },
 {
  "name": "regenerate_invitation_code",
  "description": "Regenerate the invitation code for a group. Anyone with this code can join the group. The old code will be invalidated."
 },
 {
  "name": "accept_group_invitation",
  "description": "Accept a group invitation shared with you by one of its members."
 },
 {
  "name": "record_expense",
  "description": "Record a new expense to share with others."
 },
 {
  "name": "download_expense_receipt_file",
  "description": "Download a receipt file attachment for an expense."
 },
 {
  "name": "attach_expense_receipt_file",
  "description": "Attach a receipt file to an expense."
 },
 {
  "name": "delete_expense_receipt_file",
  "description": "Delete the receipt file from an expense."
 },
 {
  "name": "show_expense",
  "description": "Show detailed expense information based on its ID."
 },
 {
  "name": "delete_expense",
  "description": "Mark the expense you are involved in as deleted. Anyone involved in the expense or a member of its group can undelete it later."
 },
 {
  "name": "update_expense",
  "description": "Update expense information."
 },
 {
  "name": "show_group_expenses",
  "description": "Show or search your expenses from a given group based on various criteria."
 },
 {
  "name": "show_no_group_expenses",
  "description": "Show or search your expenses that are not part of any group based on various criteria."
 },
 {
  "name": "undelete_expense",
  "description": "Restore a previously deleted expense you are involved in."
 },
 {
  "name": "show_expense_comments",
  "description": "Get a list of expense comments."
 },
 {
  "name": "post_expense_comment",
  "description": "Post a a comment on an expense."
 },
 {
  "name": "show_expense_comment",
  "description": "Get information about a comment posted on an expense."
 },
 {
  "name": "delete_expense_comment",
  "description": "Delete a comment you posted on an expense."
 },
 {
  "name": "update_expense_comment",
  "description": "Update a comment you posted on an expense."
 },
 {
  "name": "record_payment",
  "description": "Record a new payment for an expense. This only records payment on splitwise and does not move real money."
 },
 {
  "name": "download_payment_receipt_file",
  "description": "Download receipt file attachment for a payment."
 },
 {
  "name": "attach_payment_receipt_file",
  "description": "Attach a receipt file to a payment."
 },
 {
  "name": "delete_payment_receipt_file",
  "description": "Delete the receipt file from a payment."
 },
 {
  "name": "show_payment",
  "description": "Show payment details based on its ID."
 },
 {
  "name": "delete_payment",
  "description": "Mark the payment you are involved in as deleted. Anyone involved in the payment or a member of its group can undelete it later."
 },
 {
  "name": "update_payment",
  "description": "Update payment information."
 },
 {
  "name": "show_group_payments",
  "description": "Show all the payments that are part of the given group."
 },
 {
  "name": "show_no_group_payments",
  "description": "Show payments you are involved in that are not part of any group."
 },
 {
  "name": "undelete_payment",
  "description": "Restore a previously deleted payment you are involved in."
 },
 {
  "name": "show_person_balance",
  "description": "Show the amounts you and a given person owe to each other, broken down by group. The non-grouped expenses/payments will be shown as a group with ID None."
 },
 {
  "name": "show_people_balance",
  "description": "Show the aggregate amounts you owe to each person and they owe to you."
 },
 {
  "name": "show_group_balance",
  "description": "For the given group, show the detailed breakdown of amounts different members owe to each other. If group_id is not passed, show the amounts you owe to others and vice-versa for non-grouped expenses/payments."
 },
 {
  "name": "show_groups_balance",
  "description": "Show the aggregate amounts you owe to others or others owe you for each group you are member of. The non-grouped expenses/payments will be shown as a group with group_id of None."
 },
 {
  "name": "settle_up",
  "description": "Settle up outstanding balance with a user in a group. This only records payment on splitwise and does not move real money."
 },
 {
  "name": "show_payment_comments",
  "description": "Get a list of payment comments."
 },
 {
  "name": "post_payment_comment",
  "description": "Create a new payment comment."
 },
 {
  "name": "show_payment_comment",
  "description": "Get information about a comment posted on a payment."
 },
 {
  "name": "delete_payment_comment",
  "description": "Delete a comment you posted on a payment."
 },
 {
  "name": "update_payment_comment",
  "description": "Update a payment comment."
 },
 {
  "name": "show_notifications",
  "description": "Get a list of your notifications."
 },
 {
  "name": "delete_notifications",
  "description": "Delete all of your notifications."
 },
 {
  "name": "mark_notifications",
  "description": "Mark all notifications as read or unread."
 },
 {
  "name": "show_notifications_count",
  "description": "Get the count of your notifications."
 },
 {
  "name": "delete_notification",
  "description": "Delete a notification."
 },
 {
  "name": "mark_notification",
  "description": "Mark a notification as read or unread."
 }
]
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='show_inbox_threads'))
```

```
{
 "app_name": "gmail",
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
{
 "app_name": "gmail",
 "api_name": "show_inbox_threads",
 "path": "/email_threads/category/inbox",
 "method": "GET",
 "description": "Show or search email threads you have received. This will not show detailed information about emails within the thread.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from gmail app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "The search query string.",
   "default": "",
   "constraints": []
  },
  {
   "name": "label",
   "type": "string",
   "required": false,
   "description": "The label to filter the emails by.",
   "default": null,
   "constraints": []
  },
  {
   "name": "starred",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by starred status.",
   "default": null,
   "constraints": []
  },
  {
   "name": "archived",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by archived status.",
   "default": false,
   "constraints": []
  },
  {
   "name": "spam",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by spam status.",
   "default": false,
   "constraints": []
  },
  {
   "name": "read",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by read status.",
   "default": null,
   "constraints": []
  },
  {
   "name": "attachment",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by whether they have an attachment or not.",
   "default": null,
   "constraints": []
  },
  {
   "name": "from_email",
   "type": "string",
   "required": false,
   "description": "Filter emails by sender email address.",
   "default": null,
   "constraints": [
    "value is email address"
   ]
  },
  {
   "name": "to_email",
   "type": "string",
   "required": false,
   "description": "Filter emails by recipient email address.",
   "default": null,
   "constraints": [
    "value is email address"
   ]
  },
  {
   "name": "min_created_at",
   "type": "string",
   "required": false,
   "description": "Filter emails by minimum created_at date in YYYY-MM-DD format.",
   "default": "1500-01-01",
   "constraints": []
  },
  {
   "name": "max_created_at",
   "type": "string",
   "required": false,
   "description": "Filter emails by maximum created_at date in YYYY-MM-DD format.",
   "default": "3000-01-01",
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
   "description": "The attribute to sort the email threads by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at and updated_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -updated_at.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
    "email_thread_id": 1,
    "email_ids": [
     1
    ],
    "draft_ids": [
     1
    ],
    "incoming": true,
    "outgoing": true,
    "read": true,
    "label": "string",
    "starred": true,
    "archived": true,
    "spam": true,
    "created_at": "2019-01-01T00:00:00",
    "updated_at": "2019-01-01T00:00:00",
    "subject": "string",
    "participants": [
     {
      "name": "string",
      "email": "user@example.com"
     }
    ]
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='show_thread'))
print(apis.api_docs.show_api_doc(app_name='splitwise', api_name='login'))
```

```
{
 "app_name": "gmail",
 "api_name": "show_thread",
 "path": "/email_threads/{email_thread_id}",
 "method": "GET",
 "description": "Show detailed information about a given email thread, including emails and drafts within it.",
 "parameters": [
  {
   "name": "email_thread_id",
   "type": "integer",
   "required": true,
   "description": "The ID of the email thread to show.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from gmail app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "email_thread_id": 1,
   "incoming": true,
   "outgoing": true,
   "read": true,
   "label": "string",
   "starred": true,
   "archived": true,
   "spam": true,
   "created_at": "2019-01-01T00:00:00",
   "updated_at": "2019-01-01T00:00:00",
   "emails": [
    {
     "email_id": 1,
     "subject": "string",
     "sender": {
      "name": "string",
      "email": "user@example.com"
     },
     "recipients": [
      {
       "name": "string",
       "email": "user@example.com"
      }
     ],
     "body": "string",
     "attachments": [
      {
       "id": 1,
       "file_name": "string"
      }
     ],
     "created_at": "2019-01-01T00:00:00"
    }
   ],
   "drafts": [
    {
     "draft_id": 1,
     "response_to_email_id": 1,
     "subject": "string",
     "recipients": [
      {
       "name": "string",
       "email": "user@example.com"
      }
     ],
     "body": "string",
     "attachments": [
      {
       "id": 1,
       "file_name": "string"
      }
     ],
     "scheduled_send_at": "2019-01-01T00:00:00",
     "created_at": "2019-01-01T00:00:00",
     "updated_at": "2019-01-01T00:00:00"
    }
   ]
  },
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "splitwise",
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


### Environment Interaction 5
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='splitwise'))
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
  "name": "search_users",
  "description": "Search Splitwise users by name or email address."
 },
 {
  "name": "show_activity",
  "description": "Show a history of your expenses and payments combined."
 },
 {
  "name": "show_groups",
  "description": "Get a list of groups you are a member of."
 },
 {
  "name": "create_group",
  "description": "Create a new group of friends or family to share expenses with."
 },
 {
  "name": "show_group",
  "description": "Show group details based on its ID."
 },
 {
  "name": "delete_group",
  "description": "Delete a group you are a member of. Any member can undelete it later."
 },
 {
  "name": "update_group",
  "description": "Update group information."
 },
 {
  "name": "undelete_group",
  "description": "Undelete a group you are a member of."
 },
 {
  "name": "add_member_to_group",
  "description": "Add a member to a group."
 },
 {
  "name": "remove_member_from_group",
  "description": "Remove a member from a group."
 },
 {
  "name": "exit_group",
  "description": "Exit from a group you are a part of."
 },
 {
  "name": "regenerate_invitation_code",
  "description": "Regenerate the invitation code for a group. Anyone with this code can join the group. The old code will be invalidated."
 },
 {
  "name": "accept_group_invitation",
  "description": "Accept a group invitation shared with you by one of its members."
 },
 {
  "name": "record_expense",
  "description": "Record a new expense to share with others."
 },
 {
  "name": "download_expense_receipt_file",
  "description": "Download a receipt file attachment for an expense."
 },
 {
  "name": "attach_expense_receipt_file",
  "description": "Attach a receipt file to an expense."
 },
 {
  "name": "delete_expense_receipt_file",
  "description": "Delete the receipt file from an expense."
 },
 {
  "name": "show_expense",
  "description": "Show detailed expense information based on its ID."
 },
 {
  "name": "delete_expense",
  "description": "Mark the expense you are involved in as deleted. Anyone involved in the expense or a member of its group can undelete it later."
 },
 {
  "name": "update_expense",
  "description": "Update expense information."
 },
 {
  "name": "show_group_expenses",
  "description": "Show or search your expenses from a given group based on various criteria."
 },
 {
  "name": "show_no_group_expenses",
  "description": "Show or search your expenses that are not part of any group based on various criteria."
 },
 {
  "name": "undelete_expense",
  "description": "Restore a previously deleted expense you are involved in."
 },
 {
  "name": "show_expense_comments",
  "description": "Get a list of expense comments."
 },
 {
  "name": "post_expense_comment",
  "description": "Post a a comment on an expense."
 },
 {
  "name": "show_expense_comment",
  "description": "Get information about a comment posted on an expense."
 },
 {
  "name": "delete_expense_comment",
  "description": "Delete a comment you posted on an expense."
 },
 {
  "name": "update_expense_comment",
  "description": "Update a comment you posted on an expense."
 },
 {
  "name": "record_payment",
  "description": "Record a new payment for an expense. This only records payment on splitwise and does not move real money."
 },
 {
  "name": "download_payment_receipt_file",
  "description": "Download receipt file attachment for a payment."
 },
 {
  "name": "attach_payment_receipt_file",
  "description": "Attach a receipt file to a payment."
 },
 {
  "name": "delete_payment_receipt_file",
  "description": "Delete the receipt file from a payment."
 },
 {
  "name": "show_payment",
  "description": "Show payment details based on its ID."
 },
 {
  "name": "delete_payment",
  "description": "Mark the payment you are involved in as deleted. Anyone involved in the payment or a member of its group can undelete it later."
 },
 {
  "name": "update_payment",
  "description": "Update payment information."
 },
 {
  "name": "show_group_payments",
  "description": "Show all the payments that are part of the given group."
 },
 {
  "name": "show_no_group_payments",
  "description": "Show payments you are involved in that are not part of any group."
 },
 {
  "name": "undelete_payment",
  "description": "Restore a previously deleted payment you are involved in."
 },
 {
  "name": "show_person_balance",
  "description": "Show the amounts you and a given person owe to each other, broken down by group. The non-grouped expenses/payments will be shown as a group with ID None."
 },
 {
  "name": "show_people_balance",
  "description": "Show the aggregate amounts you owe to each person and they owe to you."
 },
 {
  "name": "show_group_balance",
  "description": "For the given group, show the detailed breakdown of amounts different members owe to each other. If group_id is not passed, show the amounts you owe to others and vice-versa for non-grouped expenses/payments."
 },
 {
  "name": "show_groups_balance",
  "description": "Show the aggregate amounts you owe to others or others owe you for each group you are member of. The non-grouped expenses/payments will be shown as a group with group_id of None."
 },
 {
  "name": "settle_up",
  "description": "Settle up outstanding balance with a user in a group. This only records payment on splitwise and does not move real money."
 },
 {
  "name": "show_payment_comments",
  "description": "Get a list of payment comments."
 },
 {
  "name": "post_payment_comment",
  "description": "Create a new payment comment."
 },
 {
  "name": "show_payment_comment",
  "description": "Get information about a comment posted on a payment."
 },
 {
  "name": "delete_payment_comment",
  "description": "Delete a comment you posted on a payment."
 },
 {
  "name": "update_payment_comment",
  "description": "Update a payment comment."
 },
 {
  "name": "show_notifications",
  "description": "Get a list of your notifications."
 },
 {
  "name": "delete_notifications",
  "description": "Delete all of your notifications."
 },
 {
  "name": "mark_notifications",
  "description": "Mark all notifications as read or unread."
 },
 {
  "name": "show_notifications_count",
  "description": "Get the count of your notifications."
 },
 {
  "name": "delete_notification",
  "description": "Delete a notification."
 },
 {
  "name": "mark_notification",
  "description": "Mark a notification as read or unread."
 }
]
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='splitwise', api_name='show_groups'))
print(apis.api_docs.show_api_doc(app_name='splitwise', api_name='create_expense'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.api_docs.show_api_doc(app_name='splitwise', api_name='create_expense'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name create_expense found for the splitwise app. Check the api and app name again."}
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='splitwise', api_name='show_groups'))
# Find the correct expense creation API name
print(apis.api_docs.show_api_descriptions(app_name='splitwise'))
```

```
{
 "app_name": "splitwise",
 "api_name": "show_groups",
 "path": "/groups",
 "method": "GET",
 "description": "Get a list of groups you are a member of.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from splitwise app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "delete",
   "type": "boolean",
   "required": false,
   "description": "Filter groups by whether they are deleted or not.",
   "default": false,
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
    "value >= 1.0, <= 9.223372036854776e+18"
   ]
  }
 ],
 "response_schemas": {
  "success": [
   {
    "group_id": 1,
    "name": "string",
    "description": "string",
    "created_at": "2019-01-01T00:00:00",
    "deleted": true,
    "creator": {
     "name": "string",
     "email": "user@example.com"
    },
    "members": [
     {
      "name": "string",
      "email": "user@example.com"
     }
    ],
    "invitation_code": "string"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
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
  "name": "search_users",
  "description": "Search Splitwise users by name or email address."
 },
 {
  "name": "show_activity",
  "description": "Show a history of your expenses and payments combined."
 },
 {
  "name": "show_groups",
  "description": "Get a list of groups you are a member of."
 },
 {
  "name": "create_group",
  "description": "Create a new group of friends or family to share expenses with."
 },
 {
  "name": "show_group",
  "description": "Show group details based on its ID."
 },
 {
  "name": "delete_group",
  "description": "Delete a group you are a member of. Any member can undelete it later."
 },
 {
  "name": "update_group",
  "description": "Update group information."
 },
 {
  "name": "undelete_group",
  "description": "Undelete a group you are a member of."
 },
 {
  "name": "add_member_to_group",
  "description": "Add a member to a group."
 },
 {
  "name": "remove_member_from_group",
  "description": "Remove a member from a group."
 },
 {
  "name": "exit_group",
  "description": "Exit from a group you are a part of."
 },
 {
  "name": "regenerate_invitation_code",
  "description": "Regenerate the invitation code for a group. Anyone with this code can join the group. The old code will be invalidated."
 },
 {
  "name": "accept_group_invitation",
  "description": "Accept a group invitation shared with you by one of its members."
 },
 {
  "name": "record_expense",
  "description": "Record a new expense to share with others."
 },
 {
  "name": "download_expense_receipt_file",
  "description": "Download a receipt file attachment for an expense."
 },
 {
  "name": "attach_expense_receipt_file",
  "description": "Attach a receipt file to an expense."
 },
 {
  "name": "delete_expense_receipt_file",
  "description": "Delete the receipt file from an expense."
 },
 {
  "name": "show_expense",
  "description": "Show detailed expense information based on its ID."
 },
 {
  "name": "delete_expense",
  "description": "Mark the expense you are involved in as deleted. Anyone involved in the expense or a member of its group can undelete it later."
 },
 {
  "name": "update_expense",
  "description": "Update expense information."
 },
 {
  "name": "show_group_expenses",
  "description": "Show or search your expenses from a given group based on various criteria."
 },
 {
  "name": "show_no_group_expenses",
  "description": "Show or search your expenses that are not part of any group based on various criteria."
 },
 {
  "name": "undelete_expense",
  "description": "Restore a previously deleted expense you are involved in."
 },
 {
  "name": "show_expense_comments",
  "description": "Get a list of expense comments."
 },
 {
  "name": "post_expense_comment",
  "description": "Post a a comment on an expense."
 },
 {
  "name": "show_expense_comment",
  "description": "Get information about a comment posted on an expense."
 },
 {
  "name": "delete_expense_comment",
  "description": "Delete a comment you posted on an expense."
 },
 {
  "name": "update_expense_comment",
  "description": "Update a comment you posted on an expense."
 },
 {
  "name": "record_payment",
  "description": "Record a new payment for an expense. This only records payment on splitwise and does not move real money."
 },
 {
  "name": "download_payment_receipt_file",
  "description": "Download receipt file attachment for a payment."
 },
 {
  "name": "attach_payment_receipt_file",
  "description": "Attach a receipt file to a payment."
 },
 {
  "name": "delete_payment_receipt_file",
  "description": "Delete the receipt file from a payment."
 },
 {
  "name": "show_payment",
  "description": "Show payment details based on its ID."
 },
 {
  "name": "delete_payment",
  "description": "Mark the payment you are involved in as deleted. Anyone involved in the payment or a member of its group can undelete it later."
 },
 {
  "name": "update_payment",
  "description": "Update payment information."
 },
 {
  "name": "show_group_payments",
  "description": "Show all the payments that are part of the given group."
 },
 {
  "name": "show_no_group_payments",
  "description": "Show payments you are involved in that are not part of any group."
 },
 {
  "name": "undelete_payment",
  "description": "Restore a previously deleted payment you are involved in."
 },
 {
  "name": "show_person_balance",
  "description": "Show the amounts you and a given person owe to each other, broken down by group. The non-grouped expenses/payments will be shown as a group with ID None."
 },
 {
  "name": "show_people_balance",
  "description": "Show the aggregate amounts you owe to each person and they owe to you."
 },
 {
  "name": "show_group_balance",
  "description": "For the given group, show the detailed breakdown of amounts different members owe to each other. If group_id is not passed, show the amounts you owe to others and vice-versa for non-grouped expenses/payments."
 },
 {
  "name": "show_groups_balance",
  "description": "Show the aggregate amounts you owe to others or others owe you for each group you are member of. The non-grouped expenses/payments will be shown as a group with group_id of None."
 },
 {
  "name": "settle_up",
  "description": "Settle up outstanding balance with a user in a group. This only records payment on splitwise and does not move real money."
 },
 {
  "name": "show_payment_comments",
  "description": "Get a list of payment comments."
 },
 {
  "name": "post_payment_comment",
  "description": "Create a new payment comment."
 },
 {
  "name": "show_payment_comment",
  "description": "Get information about a comment posted on a payment."
 },
 {
  "name": "delete_payment_comment",
  "description": "Delete a comment you posted on a payment."
 },
 {
  "name": "update_payment_comment",
  "description": "Update a payment comment."
 },
 {
  "name": "show_notifications",
  "description": "Get a list of your notifications."
 },
 {
  "name": "delete_notifications",
  "description": "Delete all of your notifications."
 },
 {
  "name": "mark_notifications",
  "description": "Mark all notifications as read or unread."
 },
 {
  "name": "show_notifications_count",
  "description": "Get the count of your notifications."
 },
 {
  "name": "delete_notification",
  "description": "Delete a notification."
 },
 {
  "name": "mark_notification",
  "description": "Mark a notification as read or unread."
 }
]
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Get full list of splitwise API names
apis_list = apis.api_docs.show_api_descriptions(app_name='splitwise')
for a in apis_list:
    print(a['name'])
```

```
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
search_users
show_activity
show_groups
create_group
show_group
delete_group
update_group
undelete_group
add_member_to_group
remove_member_from_group
exit_group
regenerate_invitation_code
accept_group_invitation
record_expense
download_expense_receipt_file
attach_expense_receipt_file
delete_expense_receipt_file
show_expense
delete_expense
update_expense
show_group_expenses
show_no_group_expenses
undelete_expense
show_expense_comments
post_expense_comment
show_expense_comment
delete_expense_comment
update_expense_comment
record_payment
download_payment_receipt_file
attach_payment_receipt_file
delete_payment_receipt_file
show_payment
delete_payment
update_payment
show_group_payments
show_no_group_payments
undelete_payment
show_person_balance
show_people_balance
show_group_balance
show_groups_balance
settle_up
show_payment_comments
post_payment_comment
show_payment_comment
delete_payment_comment
update_payment_comment
show_notifications
delete_notifications
mark_notifications
show_notifications_count
delete_notification
mark_notification
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='splitwise', api_name='record_expense'))
```

```
{
 "app_name": "splitwise",
 "api_name": "record_expense",
 "path": "/expenses",
 "method": "POST",
 "description": "Record a new expense to share with others.",
 "parameters": [
  {
   "name": "description",
   "type": "string",
   "required": true,
   "description": "A short note or description of the expense.",
   "default": null,
   "constraints": []
  },
  {
   "name": "paid_amount",
   "type": "number",
   "required": true,
   "description": "The total amount of the expense paid.",
   "default": null,
   "constraints": []
  },
  {
   "name": "payer_email",
   "type": "string",
   "required": true,
   "description": "Email of the user who paid for the expense.",
   "default": null,
   "constraints": [
    "value is email address"
   ]
  },
  {
   "name": "debtor_emails",
   "type": "list[string]",
   "required": true,
   "description": "Emails of the users who owe a share of the expense.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from splitwise app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "debt_amounts",
   "type": "list[number]",
   "required": false,
   "description": "The amounts owed by each debtor. If not passed, it is assumed that each debtor owes an equal share. If passed, the list must be of the same length as debtor_ids.",
   "default": null,
   "constraints": []
  },
  {
   "name": "group_id",
   "type": "integer",
   "required": false,
   "description": "The ID of the group this expense should belong to. Keep it none if it should not belong to any group.",
   "default": null,
   "constraints": []
  },
  {
   "name": "receipt_file_path",
   "type": "string",
   "required": false,
   "description": "Absolute file path (starting with /) from the file_system app to attach as a receipt for this expense.",
   "default": null,
   "constraints": []
  },
  {
   "name": "file_system_access_token",
   "type": "string",
   "required": false,
   "description": "Access token obtained from file_system app login. Only needed for attaching receipt file.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "expense_id": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Login to gmail and splitwise
gmail_token = apis.gmail.login(username='carbrown@gmail.com', password='#x}}5n5')['access_token']
splitwise_token = apis.splitwise.login(username='carbrown@gmail.com', password='F{Q8_pw')['access_token']
print("Gmail token:", gmail_token)
print("Splitwise token:", splitwise_token)

# Search for cable bill emails in inbox
cable_threads = apis.gmail.show_inbox_threads(access_token=gmail_token, query='cable bill', page_limit=20)
print("Cable threads:", cable_threads)
```

```
Gmail token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtjYXJicm93bkBnbWFpbC5jb20iLCJleHAiOjE2ODk2ODI0OTh9.Z3ojsBN5_Q4H4baXgCxEaj6vNNHfr5_M_MlgdH1Saz8
Splitwise token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcGxpdHdpc2UrY2FyYnJvd25AZ21haWwuY29tIiwiZXhwIjoxNjg5NjgzMTQxfQ.Ib0wLXFlylF_BLMmYbPevxWzVwd-sZTqxgAI3eufnqU
Cable threads: [{'email_thread_id': 47825, 'email_ids': [20869], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-07-01T10:49:29', 'updated_at': '2023-07-01T10:49:29', 'subject': 'Cable Bill for June 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47831, 'email_ids': [20872], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-06-01T14:42:52', 'updated_at': '2023-06-01T14:42:52', 'subject': 'Cable Bill for May 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47837, 'email_ids': [20875], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-05-01T17:11:09', 'updated_at': '2023-05-01T17:11:09', 'subject': 'Cable Bill for April 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47843, 'email_ids': [20878], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-04-01T11:54:59', 'updated_at': '2023-04-01T11:54:59', 'subject': 'Cable Bill for March 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47849, 'email_ids': [20881], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-03-01T15:53:45', 'updated_at': '2023-03-01T15:53:45', 'subject': 'Cable Bill for February 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47855, 'email_ids': [20884], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-02-01T12:12:54', 'updated_at': '2023-02-01T12:12:54', 'subject': 'Cable Bill for January 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47861, 'email_ids': [20887], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-01-01T13:11:43', 'updated_at': '2023-01-01T13:11:43', 'subject': 'Cable Bill for December 2022', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47867, 'email_ids': [20890], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2022-12-01T15:16:52', 'updated_at': '2022-12-01T15:16:52', 'subject': 'Cable Bill for November 2022', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47873, 'email_ids': [20893], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2022-11-01T11:49:33', 'updated_at': '2022-11-01T11:49:33', 'subject': 'Cable Bill for October 2022', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47879, 'email_ids': [20896], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2022-10-01T10:00:24', 'updated_at': '2022-10-01T10:00:24', 'subject': 'Cable Bill for September 2022', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47885, 'email_ids': [20899], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2022-09-01T10:54:54', 'updated_at': '2022-09-01T10:54:54', 'subject': 'Cable Bill for August 2022', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47891, 'email_ids': [20902], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2022-08-01T10:19:23', 'updated_at': '2022-08-01T10:19:23', 'subject': 'Cable Bill for July 2022', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Thundercable Notifications', 'email': 'notifications@thundercable.com'}]}, {'email_thread_id': 47823, 'email_ids': [20868], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-07-01T10:49:29', 'updated_at': '2023-07-01T10:49:29', 'subject': 'Internet Bill for June 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Netboost Notifications', 'email': 'notifications@netboost.com'}]}, {'email_thread_id': 47829, 'email_ids': [20871], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-06-01T14:42:52', 'updated_at': '2023-06-01T14:42:52', 'subject': 'Internet Bill for May 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Netboost Notifications', 'email': 'notifications@netboost.com'}]}, {'email_thread_id': 47835, 'email_ids': [20874], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-05-01T17:11:09', 'updated_at': '2023-05-01T17:11:09', 'subject': 'Internet Bill for April 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Netboost Notifications', 'email': 'notifications@netboost.com'}]}, {'email_thread_id': 47841, 'email_ids': [20877], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-04-01T11:54:59', 'updated_at': '2023-04-01T11:54:59', 'subject': 'Internet Bill for March 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Netboost Notifications', 'email': 'notifications@netboost.com'}]}, {'email_thread_id': 47847, 'email_ids': [20880], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-03-01T15:53:45', 'updated_at': '2023-03-01T15:53:45', 'subject': 'Internet Bill for February 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Netboost Notifications', 'email': 'notifications@netboost.com'}]}, {'email_thread_id': 47853, 'email_ids': [20883], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-02-01T12:12:54', 'updated_at': '2023-02-01T12:12:54', 'subject': 'Internet Bill for January 2023', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Netboost Notifications', 'email': 'notifications@netboost.com'}]}, {'email_thread_id': 47859, 'email_ids': [20886], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2023-01-01T13:11:43', 'updated_at': '2023-01-01T13:11:43', 'subject': 'Internet Bill for December 2022', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Netboost Notifications', 'email': 'notifications@netboost.com'}]}, {'email_thread_id': 47865, 'email_ids': [20889], 'draft_ids': [], 'incoming': True, 'outgoing': False, 'read': False, 'label': None, 'starred': False, 'archived': False, 'spam': False, 'created_at': '2022-12-01T15:16:52', 'updated_at': '2022-12-01T15:16:52', 'subject': 'Internet Bill for November 2022', 'participants': [{'name': 'Carl Brown', 'email': 'carbrown@gmail.com'}, {'name': 'Netboost Notifications', 'email': 'notifications@netboost.com'}]}]
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Get all cable bill threads with pagination
def fetch_all_threads(query):
    out, page = [], 0
    while True:
        batch = apis.gmail.show_inbox_threads(access_token=gmail_token, query=query, page_limit=20, page_index=page)
        if not batch:
            break
        out.extend(batch)
        if len(batch) < 20:
            break
        page += 1
    return out

cable_threads = fetch_all_threads('cable bill')
print(f"Total cable threads: {len(cable_threads)}")
for t in cable_threads:
    print(t['created_at'], t['subject'], t['email_thread_id'])
```

```
Total cable threads: 383
2023-07-01T10:49:29 Cable Bill for June 2023 47825
2023-06-01T14:42:52 Cable Bill for May 2023 47831
2023-05-01T17:11:09 Cable Bill for April 2023 47837
2023-04-01T11:54:59 Cable Bill for March 2023 47843
2023-03-01T15:53:45 Cable Bill for February 2023 47849
2023-02-01T12:12:54 Cable Bill for January 2023 47855
2023-01-01T13:11:43 Cable Bill for December 2022 47861
2022-12-01T15:16:52 Cable Bill for November 2022 47867
2022-11-01T11:49:33 Cable Bill for October 2022 47873
2022-10-01T10:00:24 Cable Bill for September 2022 47879
2022-09-01T10:54:54 Cable Bill for August 2022 47885
2022-08-01T10:19:23 Cable Bill for July 2022 47891
2023-07-01T10:49:29 Internet Bill for June 2023 47823
2023-06-01T14:42:52 Internet Bill for May 2023 47829
2023-05-01T17:11:09 Internet Bill for April 2023 47835
2023-04-01T11:54:59 Internet Bill for March 2023 47841
2023-03-01T15:53:45 Internet Bill for February 2023 47847
2023-02-01T12:12:54 Internet Bill for January 2023 47853
2023-01-01T13:11:43 Internet Bill for December 2022 47859
2022-12-01T15:16:52 Internet Bill for November 2022 47865
2022-11-01T11:49:33 Internet Bill for October 2022 47871
2022-10-01T10:00:24 Internet Bill for September 2022 47877
2022-09-01T10:54:54 Internet Bill for August 2022 47883
2022-08-01T10:19:23 Internet Bill for July 2022 47889
2023-07-01T10:49:29 Electricity Bill for 2023-06-01 - 2023-06-30 47821
2023-06-01T14:42:52 Electricity Bill for 2023-05-01 - 2023-05-31 47827
2023-05-01T17:11:09 Electricity Bill for 2023-04-01 - 2023-04-30 47833
2023-04-01T11:54:59 Electricity Bill for 2023-03-01 - 2023-03-31 47839
2023-03-01T15:53:45 Electricity Bill for 2023-02-01 - 2023-02-28 47845
2023-02-01T12:12:54 Electricity Bill for 2023-01-01 - 2023-01-31 47851
2023-01-01T13:11:43 Electricity Bill for 2022-12-01 - 2022-12-31 47857
2022-12-01T15:16:52 Electricity Bill for 2022-11-01 - 2022-11-30 47863
2022-11-01T11:49:33 Electricity Bill for 2022-10-01 - 2022-10-31 47869
2022-10-01T10:00:24 Electricity Bill for 2022-09-01 - 2022-09-30 47875
2022-09-01T10:54:54 Electricity Bill for 2022-08-01 - 2022-08-31 47881
2022-08-01T10:19:23 Electricity Bill for 2022-07-01 - 2022-07-31 47887
2023-03-23T19:35:23 Amazon Delivery Update for Order #2675 42747
2023-03-18T17:31:36 Amazon Order Confirmation 42745
2023-03-21T01:54:10 Amazon Return Confirmation and Label 42755
2023-05-15T15:01:38 Book Club Reminder 10245
2023-04-30T11:17:53 Need Help with Cleaning Schedule 13319
2023-04-26T17:37:44 Sharing Childhood Memories 13322
2023-05-17T12:11:41 Creating a Chores Roster 13329
2022-11-25T12:08:13 Planning a Movie Marathon 13332
2023-04-26T17:13:34 Remote Work Policy Refinement 13336
2023-01-12T17:20:34 Community Event: Potluck Dinner 6170
2023-04-23T12:59:24 Thank You for Your Thoughtful Gift 13344
2022-09-04T14:42:09 Sharing Family Recipes 13346
2023-04-20T10:55:24 Weekly Team Meeting Agenda 13350
2023-05-16T18:24:47 Office Maintenance Notice 13359
2023-05-15T09:27:21 Performance Review Schedules 13368
2022-09-09T15:08:00 Childhood Photos 13369
2022-12-08T13:19:17 Updated Company Policies 13373
2023-01-11T13:03:06 Creating a Chores Roster 6208
2022-10-30T18:43:32 Reminder: Expense Report Submission 13384
2023-04-21T11:24:06 Employee Training Session 2121
2023-04-27T12:10:20 New Software Training 13393
2023-05-03T09:41:58 Internship Program Applications Open 2130
2022-07-21T13:41:51 Year-End Party Planning Committee 10328
2023-02-14T13:35:45 Community Event: Potluck Dinner 13401
2023-05-05T17:14:47 New HR Policies 13405
2023-05-01T18:10:41 Invitation: Diversity and Inclusion Workshop 10337
2023-04-23T12:05:37 Office Space Renovation Updates 2148
2022-07-05T08:43:43 Remote Work Policy Refinement 10346
2023-04-29T18:23:30 Monthly Sales Update 10357
2023-03-05T08:39:01 Office Maintenance Notice 2170
2023-05-14T08:39:01 Feedback Request: Team Building Event 10366
2023-05-15T13:53:45 New Software Training 10382
2023-03-09T12:21:10 Invitation: Diversity and Inclusion Workshop 2192
2023-05-11T14:23:37 Travel Memories 13458
2022-08-01T18:56:21 Checking In On You 5271
2022-06-23T17:06:51 Year-End Party Planning Committee 2201
2023-04-17T15:53:58 Upcoming Public Holiday Notice 10395
2023-05-05T15:24:54 Monthly Sales Update 2210
2023-04-14T17:28:51 Dinner Party RSVP 5282
2022-09-02T08:03:41 Client Visit Next Week 10406
2022-11-02T12:19:09 Sibling Virtual Game Night 13483
2022-12-13T09:51:07 Feedback Request: Team Building Event 2221
2023-05-17T16:18:37 New Employee Onboarding 10415
2023-05-15T11:40:49 Updated Office Protocols 2230
2022-07-22T10:52:21 Upcoming Project Deadlines 10424
2022-09-02T17:26:15 Client Feedback on Recent Presentation 2246
2023-04-14T14:06:25 Photos from Our Last Adventure 5319
2022-10-18T09:32:44 Movie Night 13511
2023-01-26T17:10:12 Project Update: Milestone Achieved 2258
2022-11-14T12:51:45 Photos from Our Last Adventure 3284
2023-04-26T18:21:54 Updated Office Security Protocols 2268
2022-09-13T11:44:31 Thank You for Your Thoughtful Gift 1295
2023-04-30T09:30:28 New Software Training Session 8482
2023-04-21T12:58:45 Recipe Exchange! 3368
2022-07-11T16:05:13 Dinner Party RSVP 3371
2023-04-18T11:29:50 Year-End Party Planning Committee 8497
2022-09-27T14:09:42 Dinner Party RSVP 1332
2023-05-06T16:41:22 Recipe Exchange 13620
2022-11-17T13:44:50 New HR Policies 8510
2023-03-28T17:09:14 Spotify Premium Subscription Confirmation 47423
2023-02-27T17:13:39 Upcoming Project Deadlines 6464
2023-05-13T15:38:02 Book Club 13635
2023-04-18T16:53:39 Reminder: Team Lunch Tomorrow 8525
2023-04-26T10:58:48 New Employee Onboarding 8534
2022-12-16T16:52:16 Invitation: Diversity and Inclusion Workshop 6491
2023-04-20T18:49:56 Corporate Social Responsibility Initiative 6517
2022-05-25T09:12:43 Sibling Virtual Game Night 13694
2023-04-19T01:52:18 Todoist Project Invitation 47487
2023-01-27T22:19:13 Amazon Order Confirmation 42381
2023-01-28T17:27:12 Amazon Delivery Update for Order #2640 42383
2023-02-03T18:47:59 Amazon Delivery Update for Order #2640 42385
2023-02-02T19:07:46 Amazon Delivery Update for Order #2640 42387
2022-09-23T11:15:18 Upcoming Team Meeting 6549
2023-01-28T08:17:52 Amazon Return Confirmation and Label 42389
2023-01-29T04:06:30 Amazon Return Confirmation and Label 42391
2023-05-02T10:28:59 Amazon Order Confirmation 42393
2023-05-04T19:49:56 Amazon Delivery Update for Order #2641 42395
2023-05-03T19:45:02 Amazon Delivery Update for Order #2641 42397
2023-05-05T18:47:49 Amazon Delivery Update for Order #2641 42399
2023-05-07T17:43:01 Amazon Delivery Update for Order #2641 42401
2023-05-02T22:29:38 Amazon Return Confirmation and Label 42403
2023-03-10T05:59:50 Amazon Order Confirmation 42405
2023-03-16T19:16:58 Amazon Delivery Update for Order #2642 42407
2023-03-10T07:06:13 Amazon Return Confirmation and Label 42409
2022-09-23T17:51:25 Amazon Order Confirmation 42411
2022-09-24T19:47:47 Amazon Delivery Update for Order #2643 42413
2022-09-24T17:16:07 Amazon Delivery Update for Order #2643 42415
2022-09-25T17:17:01 Amazon Delivery Update for Order #2643 42417
2022-09-27T18:39:31 Amazon Delivery Update for Order #2643 42419
2022-09-24T12:32:22 Amazon Return Confirmation and Label 42421
2022-09-24T04:28:55 Amazon Return Confirmation and Label 42423
2023-05-13T10:30:47 Monthly Sales Update 11705
2022-09-26T11:50:54 Amazon Return Confirmation and Label 42425
2022-09-26T08:42:43 Amazon Return Confirmation and Label 42427
2022-08-27T07:29:41 Amazon Order Confirmation 42429
2022-08-28T19:48:39 Amazon Delivery Update for Order #2644 42431
2022-09-03T19:37:03 Amazon Delivery Update for Order #2644 42433
2022-09-02T18:33:38 Amazon Delivery Update for Order #2644 42435
2022-09-01T17:51:38 Amazon Delivery Update for Order #2644 42437
2022-08-29T08:16:41 Amazon Return Confirmation and Label 42439
2023-05-16T17:28:21 Year-End Party Planning Committee 11720
2023-03-29T09:32:25 Amazon Order Confirmation 42441
2023-04-01T18:57:17 Amazon Delivery Update for Order #2645 42443
2023-04-03T18:44:05 Amazon Delivery Update for Order #2645 42445
2023-04-05T18:23:34 Amazon Delivery Update for Order #2645 42447
2022-12-06T14:42:21 Office Maintenance Notice 11729
2023-04-01T17:15:16 Amazon Delivery Update for Order #2645 42449
2023-03-31T13:50:37 Amazon Return Confirmation and Label 42451
2023-04-16T19:26:29 Amazon Order Confirmation 42453
2023-04-23T18:40:17 Amazon Delivery Update for Order #2646 42455
2023-04-17T17:41:51 Amazon Delivery Update for Order #2646 42457
2022-11-06T10:09:27 Office Space Renovation Updates 11738
2023-04-17T11:55:44 Amazon Return Confirmation and Label 42459
2023-04-18T08:02:10 Amazon Return Confirmation and Label 42461
2022-07-15T19:12:17 Amazon Order Confirmation 42463
2022-07-19T17:00:49 Amazon Delivery Update for Order #2647 42465
2023-05-16T17:03:20 IT Helpdesk Satisfaction Survey 11747
2022-07-22T18:13:04 Amazon Delivery Update for Order #2647 42467
2022-07-22T18:02:36 Amazon Delivery Update for Order #2647 42469
2022-07-16T00:32:45 Amazon Return Confirmation and Label 42471
2022-11-14T14:40:05 Amazon Order Confirmation 42473
2022-11-16T19:09:52 Amazon Delivery Update for Order #2648 42475
2023-05-17T11:31:17 Updated Office Protocols 11756
2022-11-17T08:43:20 Amazon Return Confirmation and Label 42477
2022-08-11T23:09:46 Amazon Order Confirmation 42479
2022-08-17T18:36:52 Amazon Delivery Update for Order #2649 42481
2022-08-13T19:30:40 Amazon Delivery Update for Order #2649 42483
2023-05-05T14:15:45 Corporate Social Responsibility Initiative 11765
2022-08-12T07:26:39 Amazon Return Confirmation and Label 42485
2022-07-18T10:30:47 Amazon Order Confirmation 42487
2022-07-21T17:04:18 Amazon Delivery Update for Order #2650 42489
2022-07-22T19:31:38 Amazon Delivery Update for Order #2650 42491
2022-07-20T14:21:53 Game Night Next Saturday 6652
2022-07-25T18:27:18 Amazon Delivery Update for Order #2650 42493
2022-07-19T05:52:57 Amazon Return Confirmation and Label 42495
2022-07-18T12:36:38 Amazon Return Confirmation and Label 42497
2022-07-19T00:45:44 Amazon Return Confirmation and Label 42499
2022-10-21T08:38:17 Employee Training Session 11780
2022-08-21T19:34:11 Amazon Order Confirmation 42501
2022-08-24T17:21:55 Amazon Delivery Update for Order #2651 42503
2022-08-26T19:08:35 Amazon Delivery Update for Order #2651 42505
2022-08-25T17:48:10 Amazon Delivery Update for Order #2651 42507
2023-05-05T16:46:32 Office Space Available for Use 11788
2022-08-28T18:17:52 Amazon Delivery Update for Order #2651 42509
2022-08-22T14:30:16 Amazon Return Confirmation and Label 42511
2022-08-23T08:29:56 Amazon Return Confirmation and Label 42513
2022-08-22T11:46:57 Amazon Return Confirmation and Label 42515
2023-04-28T11:41:21 Updated Company Policies 11797
2022-08-22T12:33:47 Amazon Return Confirmation and Label 42517
2023-03-29T00:06:09 Amazon Order Confirmation 42519
2023-04-05T19:15:52 Amazon Delivery Update for Order #2652 42521
2023-04-02T19:40:21 Amazon Delivery Update for Order #2652 42523
2023-03-30T17:54:33 Amazon Return Confirmation and Label 42525
2022-12-15T08:36:56 Amazon Order Confirmation 42527
2022-12-01T14:14:17 Upcoming Webinar: Digital Marketing Trends 11808
2022-12-21T19:23:37 Amazon Delivery Update for Order #2653 42529
2022-12-20T17:56:39 Amazon Delivery Update for Order #2653 42531
2022-12-16T19:33:51 Amazon Return Confirmation and Label 42533
2022-12-16T17:18:30 Amazon Return Confirmation and Label 42535
2023-01-16T09:18:41 Amazon Order Confirmation 42537
2023-01-17T19:54:58 Amazon Delivery Update for Order #2654 42539
2023-01-22T17:42:55 Amazon Delivery Update for Order #2654 42541
2023-01-16T23:42:12 Amazon Return Confirmation and Label 42543
2023-02-05T01:33:59 Amazon Order Confirmation 42545
2023-02-10T19:20:33 Amazon Delivery Update for Order #2655 42547
2023-02-12T19:09:19 Amazon Delivery Update for Order #2655 42549
2023-02-12T18:16:40 Amazon Delivery Update for Order #2655 42551
2023-02-07T02:50:09 Amazon Return Confirmation and Label 42553
2023-02-05T11:58:53 Amazon Return Confirmation and Label 42555
2023-03-03T02:49:15 Amazon Order Confirmation 42557
2023-03-09T17:59:14 Amazon Delivery Update for Order #2656 42559
2023-03-04T17:29:11 Amazon Delivery Update for Order #2656 42561
2023-03-09T17:32:28 Amazon Delivery Update for Order #2656 42563
2023-03-03T11:08:56 Amazon Return Confirmation and Label 42565
2022-10-25T01:15:16 Amazon Order Confirmation 42567
2022-10-29T18:03:19 Amazon Delivery Update for Order #2657 42569
2022-11-01T17:55:01 Amazon Delivery Update for Order #2657 42571
2022-10-29T18:06:46 Amazon Delivery Update for Order #2657 42573
2022-10-27T10:04:10 Amazon Return Confirmation and Label 42575
2022-12-14T23:00:58 Amazon Order Confirmation 42577
2023-02-08T11:34:23 Todoist Project Invitation 47699
2022-12-16T17:36:18 Amazon Delivery Update for Order #2658 42579
2023-03-13T20:23:18 Amazon Order Confirmation 42581
2023-03-17T17:47:37 Amazon Delivery Update for Order #2659 42583
2023-05-09T14:33:02 Book Club Reminder 15960
2023-03-15T19:29:28 Amazon Delivery Update for Order #2659 42585
2023-03-20T18:21:48 Amazon Delivery Update for Order #2659 42587
2023-01-05T18:25:51 Team Building Retreat 7772
2023-03-15T18:42:27 Amazon Delivery Update for Order #2659 42589
2023-03-16T00:18:11 Amazon Return Confirmation and Label 42591
2023-03-14T06:09:37 Amazon Return Confirmation and Label 42593
2023-03-16T05:59:51 Amazon Return Confirmation and Label 42595
2023-05-03T13:58:10 Invitation: Diversity and Inclusion Workshop 7781
2023-04-09T03:09:28 Amazon Order Confirmation 42597
2023-04-13T19:08:05 Amazon Delivery Update for Order #2660 42599
2023-04-16T19:21:58 Amazon Delivery Update for Order #2660 42601
2023-04-11T02:24:30 Amazon Return Confirmation and Label 42603
2022-12-21T11:01:20 Amazon Order Confirmation 42605
2022-12-28T19:54:57 Amazon Delivery Update for Order #2661 42607
2022-12-23T17:39:29 Amazon Return Confirmation and Label 42609
2022-10-08T14:09:57 New Employee Onboarding 7794
2022-12-26T03:28:04 Amazon Order Confirmation 42611
2022-12-29T19:05:34 Amazon Delivery Update for Order #2662 42613
2023-01-01T19:45:26 Amazon Delivery Update for Order #2662 42615
2022-12-31T19:32:41 Amazon Delivery Update for Order #2662 42617
2023-04-20T10:52:16 Client Feedback on Recent Presentation 7803
2022-12-31T18:11:23 Amazon Delivery Update for Order #2662 42619
2022-12-27T23:33:28 Amazon Return Confirmation and Label 42621
2022-12-28T09:10:03 Amazon Return Confirmation and Label 42623
2022-12-28T21:28:55 Amazon Return Confirmation and Label 42625
2022-12-26T08:43:15 Amazon Return Confirmation and Label 42627
2023-04-28T02:56:12 Amazon Order Confirmation 42629
2023-05-03T18:15:17 Amazon Delivery Update for Order #2663 42631
2022-09-06T17:15:53 Amazon Order Confirmation 42633
2022-09-09T17:02:08 Amazon Delivery Update for Order #2664 42635
2022-09-10T18:15:52 Amazon Delivery Update for Order #2664 42637
2022-09-12T19:26:35 Amazon Delivery Update for Order #2664 42639
2022-09-10T18:41:43 Amazon Delivery Update for Order #2664 42641
2022-09-07T00:41:57 Amazon Return Confirmation and Label 42643
2022-09-08T06:37:44 Amazon Return Confirmation and Label 42645
2022-09-09T03:56:45 Amazon Return Confirmation and Label 42647
2022-10-17T22:06:14 Amazon Order Confirmation 42649
2022-10-18T19:23:58 Amazon Delivery Update for Order #2665 42651
2023-05-06T11:21:41 Project Update: Milestone Achieved 7836
2022-10-21T19:10:18 Amazon Delivery Update for Order #2665 42653
2022-10-22T19:05:39 Amazon Delivery Update for Order #2665 42655
2022-10-20T21:46:46 Amazon Return Confirmation and Label 42657
2022-10-18T00:34:09 Amazon Return Confirmation and Label 42659
2022-10-19T19:23:13 Amazon Return Confirmation and Label 42661
2022-10-30T08:39:23 Amazon Order Confirmation 42663
2022-11-01T17:28:19 Amazon Delivery Update for Order #2666 42665
2022-07-18T14:03:09 Amazon Order Confirmation 42667
2022-07-19T17:28:33 Amazon Delivery Update for Order #2667 42669
2022-12-02T16:59:39 Weekly Team Meeting Agenda 7854
2022-07-25T18:45:01 Amazon Delivery Update for Order #2667 42671
2022-07-19T18:51:42 Amazon Delivery Update for Order #2667 42673
2022-07-23T18:13:46 Amazon Delivery Update for Order #2667 42675
2022-07-18T21:52:01 Amazon Return Confirmation and Label 42677
2022-07-18T21:36:31 Amazon Return Confirmation and Label 42679
2022-07-20T10:24:48 Amazon Return Confirmation and Label 42681
2022-09-18T19:51:38 Amazon Order Confirmation 42683
2022-09-25T19:39:54 Amazon Delivery Update for Order #2668 42685
2022-09-21T17:09:09 Amazon Delivery Update for Order #2668 42687
2022-09-11T14:09:36 Updated Company Policies 7872
2022-09-21T03:35:37 Amazon Return Confirmation and Label 42689
2022-10-14T01:09:46 Amazon Order Confirmation 42691
2022-10-17T19:10:43 Amazon Delivery Update for Order #2669 42693
2023-03-22T21:42:37 Amazon Order Confirmation 42695
2023-03-29T17:11:56 Amazon Delivery Update for Order #2670 42697
2023-04-08T10:42:26 Upcoming Public Holiday Notice 7883
2023-03-29T17:12:02 Amazon Delivery Update for Order #2670 42699
2023-03-24T04:54:01 Amazon Return Confirmation and Label 42701
2023-03-23T14:37:49 Amazon Return Confirmation and Label 42703
2023-01-06T17:33:07 Amazon Order Confirmation 42705
2023-01-08T19:43:04 Amazon Delivery Update for Order #2671 42707
2023-01-10T17:07:51 Amazon Delivery Update for Order #2671 42709
2023-01-08T18:28:46 Amazon Delivery Update for Order #2671 42711
2023-01-08T06:00:23 Amazon Return Confirmation and Label 42713
2023-01-08T11:38:48 Amazon Return Confirmation and Label 42715
2023-01-09T02:49:42 Amazon Return Confirmation and Label 42717
2023-04-26T14:59:36 Amazon Order Confirmation 42719
2023-04-28T19:56:02 Amazon Delivery Update for Order #2672 42721
2023-04-30T17:40:43 Amazon Delivery Update for Order #2672 42723
2022-08-29T11:06:23 New HR Policies 7908
2023-04-27T19:07:26 Amazon Return Confirmation and Label 42725
2022-10-07T22:17:27 Amazon Order Confirmation 42727
2022-10-10T19:08:31 Amazon Delivery Update for Order #2673 42729
2022-10-10T19:04:27 Amazon Delivery Update for Order #2673 42731
2022-10-12T18:03:20 Amazon Delivery Update for Order #2673 42733
2022-10-10T19:14:58 Amazon Return Confirmation and Label 42735
2022-10-08T07:08:01 Amazon Return Confirmation and Label 42737
2023-05-10T23:18:40 Amazon Order Confirmation 42739
2023-05-17T18:09:33 Amazon Delivery Update for Order #2674 42741
2023-05-13T10:22:49 Amazon Return Confirmation and Label 42743
2023-03-23T19:45:46 Amazon Delivery Update for Order #2675 42749
2023-03-21T18:19:03 Amazon Delivery Update for Order #2675 42751
2023-03-20T11:40:07 Amazon Return Confirmation and Label 42753
2023-02-18T10:59:01 Amazon Order Confirmation 42757
2023-02-20T18:39:48 Amazon Delivery Update for Order #2676 42759
2023-02-23T19:06:48 Amazon Delivery Update for Order #2676 42761
2023-02-24T18:45:27 Amazon Delivery Update for Order #2676 42763
2023-02-20T13:54:12 Amazon Return Confirmation and Label 42765
2023-02-18T15:49:13 Amazon Return Confirmation and Label 42767
2022-11-19T00:25:17 Amazon Order Confirmation 42769
2023-04-12T17:43:02 Updated Office Protocols 14099
2022-11-23T19:45:06 Amazon Delivery Update for Order #2677 42771
2022-11-23T17:08:56 Amazon Delivery Update for Order #2677 42773
2022-11-26T19:47:41 Amazon Delivery Update for Order #2677 42775
2022-11-26T19:42:16 Amazon Delivery Update for Order #2677 42777
2022-11-20T16:20:50 Amazon Return Confirmation and Label 42779
2022-11-19T06:35:19 Amazon Return Confirmation and Label 42781
2022-10-17T22:52:32 Amazon Order Confirmation 42783
2022-10-28T17:33:11 Remote Work Policy Refinement 14112
2022-10-21T19:38:52 Amazon Delivery Update for Order #2678 42785
2022-10-18T19:02:18 Amazon Delivery Update for Order #2678 42787
2022-10-24T18:47:24 Amazon Delivery Update for Order #2678 42789
2022-10-24T18:53:14 Amazon Delivery Update for Order #2678 42791
2022-07-21T13:28:02 Dinner Party RSVP 2856
2022-10-18T10:02:36 Amazon Return Confirmation and Label 42793
2022-10-19T11:08:56 Amazon Return Confirmation and Label 42795
2022-10-19T11:39:14 Amazon Return Confirmation and Label 42797
2023-04-21T15:48:04 Office Space Available for Use 14126
2023-05-01T08:38:29 Amazon Order Confirmation 42799
2023-05-02T17:43:23 Amazon Delivery Update for Order #2679 42801
2023-05-03T03:45:29 Amazon Return Confirmation and Label 42803
2022-12-12T13:13:56 Amazon Order Confirmation 42805
2022-12-18T17:12:12 Amazon Delivery Update for Order #2680 42807
2022-12-18T18:24:30 Amazon Delivery Update for Order #2680 42809
2023-03-30T14:43:24 Amazon Prime Subscription Confirmation 16187
2022-12-13T17:22:42 Amazon Delivery Update for Order #2680 42811
2023-04-30T14:43:24 Amazon Prime Subscription Confirmation 16189
2022-12-14T13:09:01 Amazon Return Confirmation and Label 42813
2022-07-31T00:43:23 Amazon Order Confirmation 42815
2022-08-06T18:21:44 Amazon Delivery Update for Order #2681 42817
2022-08-07T18:46:37 Amazon Delivery Update for Order #2681 42819
2023-05-15T12:39:42 Quarterly Team Goals 14149
2022-08-07T17:18:03 Amazon Delivery Update for Order #2681 42821
2022-07-31T02:19:49 Amazon Return Confirmation and Label 42823
2023-02-26T02:02:29 Amazon Order Confirmation 42825
2023-03-03T18:10:33 Amazon Delivery Update for Order #2682 42827
2023-03-03T18:44:48 Amazon Delivery Update for Order #2682 42829
2023-02-28T19:19:27 Amazon Delivery Update for Order #2682 42831
2023-02-26T04:51:30 Amazon Return Confirmation and Label 42833
2023-03-29T23:53:53 Amazon Order Confirmation 42835
2023-04-03T18:15:35 Amazon Delivery Update for Order #2683 42837
2023-04-03T19:27:01 Amazon Delivery Update for Order #2683 42839
2023-04-01T19:28:13 Amazon Delivery Update for Order #2683 42841
2022-09-29T16:51:03 Team Building Retreat 14170
2023-03-31T12:01:10 Amazon Return Confirmation and Label 42843
2023-04-22T14:21:59 Reminder: Team Lunch Tomorrow 14196
2022-10-15T15:06:28 Movie Night This Friday? 7030
2023-05-15T12:18:32 Creating a Chores Roster 7033
2023-04-13T13:17:35 Updated Company Policies 14205
2022-06-15T12:58:22 Cooking Dinner Together? 7085
2022-09-27T15:58:13 Need Help with Cleaning Schedule 7091
2022-11-22T08:47:03 Grocery Shopping List 7120
2022-12-25T14:48:46 Emergency Contact Information 13266
2022-07-05T18:28:40 Team Building Retreat 13270
2023-02-19T15:51:51 Cleaning Supplies Inventory 7134
2022-09-21T18:40:54 Updated Office Security Protocols 13279
2023-02-08T12:47:09 Game Night Next Saturday 10206
2022-09-25T08:33:38 Year-End Party Planning Committee 13290
2022-08-17T08:11:01 Dinner Party RSVP 10222
2023-04-19T08:50:43 Feedback Request: Team Building Event 13299
2022-11-22T16:57:01 Planning a Movie Marathon 6138
2022-07-29T11:57:44 Sharing Exciting News 13307
2023-05-11T08:33:46 Client Visit Next Week 13311
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# Filter only "Cable Bill for" threads from 2023 (this year's usage)
# Bills received on 1st of month, for previous month's usage
# "this year's cable usage" = usage months in 2023 = Jan 2023 through Jun 2023 (bills received Feb 2023 through Jul 2023)
# Current date is 2023-07-18, so bills received in 2023 for 2023 usage:
# - Received 2023-02-01 -> Jan 2023 usage
# - Received 2023-03-01 -> Feb 2023 usage
# - Received 2023-04-01 -> Mar 2023 usage
# - Received 2023-05-01 -> Apr 2023 usage
# - Received 2023-06-01 -> May 2023 usage
# - Received 2023-07-01 -> Jun 2023 usage

cable_only = [t for t in cable_threads if t['subject'].startswith('Cable Bill for')]
print(f"Cable Bill threads: {len(cable_only)}")
for t in cable_only:
    print(t['created_at'], t['subject'], t['email_thread_id'])
```

```
Cable Bill threads: 12
2023-07-01T10:49:29 Cable Bill for June 2023 47825
2023-06-01T14:42:52 Cable Bill for May 2023 47831
2023-05-01T17:11:09 Cable Bill for April 2023 47837
2023-04-01T11:54:59 Cable Bill for March 2023 47843
2023-03-01T15:53:45 Cable Bill for February 2023 47849
2023-02-01T12:12:54 Cable Bill for January 2023 47855
2023-01-01T13:11:43 Cable Bill for December 2022 47861
2022-12-01T15:16:52 Cable Bill for November 2022 47867
2022-11-01T11:49:33 Cable Bill for October 2022 47873
2022-10-01T10:00:24 Cable Bill for September 2022 47879
2022-09-01T10:54:54 Cable Bill for August 2022 47885
2022-08-01T10:19:23 Cable Bill for July 2022 47891
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Filter only bills for 2023 usage (subject contains "2023")
cable_2023 = [t for t in cable_only if '2023' in t['subject']]
print(f"Cable bills for 2023 usage: {len(cable_2023)}")
for t in cable_2023:
    print(t['created_at'], t['subject'], t['email_thread_id'])
```

```
Cable bills for 2023 usage: 6
2023-07-01T10:49:29 Cable Bill for June 2023 47825
2023-06-01T14:42:52 Cable Bill for May 2023 47831
2023-05-01T17:11:09 Cable Bill for April 2023 47837
2023-04-01T11:54:59 Cable Bill for March 2023 47843
2023-03-01T15:53:45 Cable Bill for February 2023 47849
2023-02-01T12:12:54 Cable Bill for January 2023 47855
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# Fetch each email thread to get the total cost
for t in cable_2023:
    thread = apis.gmail.show_thread(email_thread_id=t['email_thread_id'], access_token=gmail_token)
    email = thread['emails'][0]
    print(f"Subject: {email['subject']}")
    print(f"Body: {email['body']}")
    print("---")
```

```
Subject: Cable Bill for June 2023
Body: Please find attached the cable bill for June 2023.
---
Subject: Cable Bill for May 2023
Body: Please find attached the cable bill for May 2023.
---
Subject: Cable Bill for April 2023
Body: Please find attached the cable bill for April 2023.
---
Subject: Cable Bill for March 2023
Body: Please find attached the cable bill for March 2023.
---
Subject: Cable Bill for February 2023
Body: Please find attached the cable bill for February 2023.
---
Subject: Cable Bill for January 2023
Body: Please find attached the cable bill for January 2023.
---
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# Check attachments in each email
for t in cable_2023:
    thread = apis.gmail.show_thread(email_thread_id=t['email_thread_id'], access_token=gmail_token)
    email = thread['emails'][0]
    print(f"Subject: {email['subject']}, Attachments: {email['attachments']}")
```

```
Subject: Cable Bill for June 2023, Attachments: [{'id': 8485, 'file_name': '2023-06.txt'}]
Subject: Cable Bill for May 2023, Attachments: [{'id': 8488, 'file_name': '2023-05.txt'}]
Subject: Cable Bill for April 2023, Attachments: [{'id': 8491, 'file_name': '2023-04.txt'}]
Subject: Cable Bill for March 2023, Attachments: [{'id': 8494, 'file_name': '2023-03.txt'}]
Subject: Cable Bill for February 2023, Attachments: [{'id': 8497, 'file_name': '2023-02.txt'}]
Subject: Cable Bill for January 2023, Attachments: [{'id': 8500, 'file_name': '2023-01.txt'}]
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# Download each attachment to get the total cost
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='show_email_attachment'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.api_docs.show_api_doc(app_name='gmail', api_name='show_email_attachment'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name show_email_attachment found for the gmail app. Check the api and app name again."}
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
# Find the correct attachment API
gmail_apis = apis.api_docs.show_api_descriptions(app_name='gmail')
for a in gmail_apis:
    if 'attach' in a['name'].lower() or 'download' in a['name'].lower() or 'file' in a['name'].lower():
        print(a)
```

```
{"name": "show_profile", "description": "Show public profile information of a user."}
{"name": "download_attachment", "description": "Download a file attachment."}
{"name": "upload_attachments_to_draft", "description": "Upload attachments to a draft."}
{"name": "remove_attachment_from_draft", "description": "Delete an attachment from a draft."}
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
# Download attachments and get costs, then create splitwise expenses
# First get attachment content
attachment_data = {}
for t in cable_2023:
    thread = apis.gmail.show_thread(email_thread_id=t['email_thread_id'], access_token=gmail_token)
    email = thread['emails'][0]
    att_id = email['attachments'][0]['id']
    content = apis.gmail.download_attachment(attachment_id=att_id, access_token=gmail_token)
    print(f"{email['subject']}: {content}")
    attachment_data[email['subject']] = content
```

```
Execution failed. Traceback:
  File "<python-input>", line 8, in <module>
    content = apis.gmail.download_attachment(attachment_id=att_id, access_token=gmail_token)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"Validation error. Reason: \nfile_system_access_token: field required"}
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
import re

# Login to file_system and download attachments, then create splitwise expenses
fs_token = apis.file_system.login(username='carbrown@gmail.com', password='4k9jcny')['access_token']

# Get splitwise group info
groups = apis.splitwise.show_groups(access_token=splitwise_token, page_limit=20)
print("Groups:", [(g['group_id'], g['name'], [m['email'] for m in g['members']]) for g in groups])

# Download each attachment
bills = []
for t in cable_2023:
    thread = apis.gmail.show_thread(email_thread_id=t['email_thread_id'], access_token=gmail_token)
    email = thread['emails'][0]
    att_id = email['attachments'][0]['id']
    content = apis.gmail.download_attachment(attachment_id=att_id, access_token=gmail_token, file_system_access_token=fs_token)
    print(f"{email['subject']}: {content}")
    bills.append({'subject': email['subject'], 'content': content})
```

```
Groups: [(236, 'Climbers', ['gl.moore@gmail.com', 'carbrown@gmail.com', 'andrew_brow@gmail.com']), (181, 'Gardening Club', ['mar_blac@gmail.com', 'joseph.webe@gmail.com', 'ma_smith@gmail.com', 'cod.smith@gmail.com', 'carbrown@gmail.com']), (71, 'NanoFlex Systems', ['an-harrison@gmail.com', 'mar_blac@gmail.com', 'joseph.webe@gmail.com', 'hun.weaver@gmail.com', 'ma_smith@gmail.com', 'diwils@gmail.com', 'william_mart@gmail.com', 'carbrown@gmail.com', 'nan_ritt@gmail.com']), (235, 'Snow Adventurers', ['gl.moore@gmail.com', 'william_mart@gmail.com', 'carbrown@gmail.com']), (217, 'Literary Club', ['ja-solomon@gmail.com', 'clmiller@gmail.com', 'kevin.blac@gmail.com', 'carbrown@gmail.com']), (5, 'Roommates', ['ad.blackburn@gmail.com', 'jer.calhoun@gmail.com', 'carbrown@gmail.com']), (167, 'Holiday Group', ['carbrown@gmail.com', 'connorbrow@gmail.com', 'alexwhite@gmail.com']), (102, 'Board Game Nights', ['clmiller@gmail.com', 'chelsea-burch@gmail.com', 'carbrown@gmail.com', 'andrew_brow@gmail.com', 'nan_ritt@gmail.com']), (25, 'Siblings', ['carbrown@gmail.com', 'connorbrow@gmail.com', 'andrew_brow@gmail.com']), (142, 'House Party', ['deniseburch@gmail.com', 'carbrown@gmail.com', 'connorbrow@gmail.com']), (238, 'Creative Group', ['mir-powe@gmail.com', 'jer.calhoun@gmail.com', 'carbrown@gmail.com'])]
Cable Bill for June 2023: {'message': 'Attachment downloaded in file_system app.', 'file_path': '/home/carl/downloads/2023-06.txt'}
Cable Bill for May 2023: {'message': 'Attachment downloaded in file_system app.', 'file_path': '/home/carl/downloads/2023-05.txt'}
Cable Bill for April 2023: {'message': 'Attachment downloaded in file_system app.', 'file_path': '/home/carl/downloads/2023-04.txt'}
Cable Bill for March 2023: {'message': 'Attachment downloaded in file_system app.', 'file_path': '/home/carl/downloads/2023-03.txt'}
Cable Bill for February 2023: {'message': 'Attachment downloaded in file_system app.', 'file_path': '/home/carl/downloads/2023-02.txt'}
Cable Bill for January 2023: {'message': 'Attachment downloaded in file_system app.', 'file_path': '/home/carl/downloads/2023-01.txt'}
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
import re

# Read each file to get total cost
file_paths = {
    'June 2023': '/home/carl/downloads/2023-06.txt',
    'May 2023': '/home/carl/downloads/2023-05.txt',
    'April 2023': '/home/carl/downloads/2023-04.txt',
    'March 2023': '/home/carl/downloads/2023-03.txt',
    'February 2023': '/home/carl/downloads/2023-02.txt',
    'January 2023': '/home/carl/downloads/2023-01.txt',
}

# MM-YY mapping
mm_yy_map = {
    'June 2023': '06-23',
    'May 2023': '05-23',
    'April 2023': '04-23',
    'March 2023': '03-23',
    'February 2023': '02-23',
    'January 2023': '01-23',
}

# Roommates group
roommates_group_id = 5
roommates_members = ['ad.blackburn@gmail.com', 'jer.calhoun@gmail.com', 'carbrown@gmail.com']
# Carl is payer, debtors are the other members
debtor_emails = ['ad.blackburn@gmail.com', 'jer.calhoun@gmail.com']

bills_info = []
for month, path in file_paths.items():
    content = apis.file_system.show_file(file_path=path, access_token=fs_token)
    text = content if isinstance(content, str) else str(content)
    # Find total amount
    match = re.search(r'[Tt]otal[^\d]*\$?([\d,]+\.?\d*)', text)
    if not match:
        match = re.search(r'\$\s*([\d,]+\.?\d*)', text)
    amount = float(match.group(1).replace(',', '')) if match else None
    bills_info.append({'month': month, 'mm_yy': mm_yy_map[month], 'amount': amount, 'text': text[:300]})
    print(f"{month}: amount={amount}, text={text[:200]}")

# Create splitwise expenses for each bill
for bill in bills_info:
    desc = f"cable bill [{bill['mm_yy']}]"
    result = apis.splitwise.record_expense(
        description=desc,
        paid_amount=bill['amount'],
        payer_email='carbrown@gmail.com',
        debtor_emails=debtor_emails,
        access_token=splitwise_token,
        group_id=roommates_group_id
    )
    print(f"Created expense: {desc}, amount={bill['amount']}, result={result}")

final_answer = None
print({"final_answer": final_answer, "evidence": "Created 6 cable bill expenses in Roommates group"})
apis.supervisor.complete_task(answer=None)
```

```
June 2023: amount=186.0, text={'file_id': 25887, 'path': '/home/carl/downloads/2023-06.txt', 'content': '\nCable Bill from ThunderCable for duration => 2023-06-01 - 2023-06-30\n\nCarl Brown\n478 Daniel Bridge Suite 056\nSeattle\nW
May 2023: amount=117.0, text={'file_id': 25888, 'path': '/home/carl/downloads/2023-05.txt', 'content': '\nCable Bill from ThunderCable for duration => 2023-05-01 - 2023-05-31\n\nCarl Brown\n478 Daniel Bridge Suite 056\nSeattle\nW
April 2023: amount=153.0, text={'file_id': 25889, 'path': '/home/carl/downloads/2023-04.txt', 'content': '\nCable Bill from ThunderCable for duration => 2023-04-01 - 2023-04-30\n\nCarl Brown\n478 Daniel Bridge Suite 056\nSeattle\nW
March 2023: amount=146.0, text={'file_id': 25890, 'path': '/home/carl/downloads/2023-03.txt', 'content': '\nCable Bill from ThunderCable for duration => 2023-03-01 - 2023-03-31\n\nCarl Brown\n478 Daniel Bridge Suite 056\nSeattle\nW
February 2023: amount=200.0, text={'file_id': 25891, 'path': '/home/carl/downloads/2023-02.txt', 'content': '\nCable Bill from ThunderCable for duration => 2023-02-01 - 2023-02-28\n\nCarl Brown\n478 Daniel Bridge Suite 056\nSeattle\nW
January 2023: amount=164.0, text={'file_id': 25892, 'path': '/home/carl/downloads/2023-01.txt', 'content': '\nCable Bill from ThunderCable for duration => 2023-01-01 - 2023-01-31\n\nCarl Brown\n478 Daniel Bridge Suite 056\nSeattle\nW
Created expense: cable bill [06-23], amount=186.0, result={'message': 'Expense recorded.', 'expense_id': 5040}
Created expense: cable bill [05-23], amount=117.0, result={'message': 'Expense recorded.', 'expense_id': 5041}
Created expense: cable bill [04-23], amount=153.0, result={'message': 'Expense recorded.', 'expense_id': 5042}
Created expense: cable bill [03-23], amount=146.0, result={'message': 'Expense recorded.', 'expense_id': 5043}
Created expense: cable bill [02-23], amount=200.0, result={'message': 'Expense recorded.', 'expense_id': 5044}
Created expense: cable bill [01-23], amount=164.0, result={'message': 'Expense recorded.', 'expense_id': 5045}
{"final_answer": null, "evidence": "Created 6 cable bill expenses in Roommates group"}
```

