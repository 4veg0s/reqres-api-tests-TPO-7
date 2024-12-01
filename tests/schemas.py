get_users = {
    "page": "integer",
    "per_page": "integer",
    "total": "integer",
    "total_pages": "integer",
    "data": [
        {
            "id": "integer",
            "email": "string",
            "first_name": "string",
            "last_name": "string",
            "avatar": "string"
        }
    ]
}

get_user = {
    "data": {
        "id": "integer",
        "email": "string",
        "first_name": "string",
        "last_name": "string",
        "avatar": "string"
    }
}

put_user = {
    "updatedAt": "string"
}

post_login_success = {
    "token": "string"
}

post_login_failure = {
    "error": "string"
}

post_register_success = {
    "id": "string",
    "token": "string"
}

post_register_failure = {
    "error": "string"
}
