"""
Configure addresss.

Contains available address info.
"""

RESOURCES = {
    "attachments": {
        "address": "attachments",
        "verbs": ["GET", "POST", "DELETE"]
    },
    "contacts": {
        "address": "contacts",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["customer", "first_name", "last_name"]
    },
    "customers": {
        "address": "customers",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["company_name"]
    },
    "defects": {
        "address": "defects",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["item"]
    },
    "features": {
        "address": "features",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["item"]
    },
    "tasks": {
        "address": "tasks",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["item"]
    },
    "incidents": {
        "address": "incidents",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["item"]
    },
    "emails": {
        "address": "email",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["subject", "body", "to", "from", "email_type", "item"]
    },
    "fields": {
        "address": "fields",
        "verbs": ["GET"],
        "required": []
    },
    "fields/custom": {
        "address": "fields/custom",
        "verbs": ["GET"],
        "required": []
    },
    "item_relations": {
        "address": "item_relations",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["relation_type", "parent_item", "child_item"]
    },
    "me": {
        "address": "me",
        "verbs": ["GET"],
        "required": []
    },
    "picklists": {
        "address": "picklists",
        "verbs": ["GET", "POST", "DELETE"],
        "required": []
    },
    "projects": {
        "address": "projects",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["name"]
    },
    "releases": {
        "address": "releases",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["name", "release_type"]
    },
    "security_roles": {
        "address": "security_roles",
        "verbs": ["GET"]
    },
    "settings": {
        "address": "settings",
        "verbs": ["GET"],
        "required": []
    },
    "users": {
        "address": "users",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["first_name", "last_name", "security_roles"]
    },
    "work_logs": {
        "address": "work_logs",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["user", "work_done", "item", "date_time"]
    },
    "workflow_steps": {
        "address": "workflow_steps",
        "verbs": ["GET"],
        "required": []
    },
    "workflows": {
        "address": "workflows",
        "verbs": ["GET"],
        "required": []
    },
}
