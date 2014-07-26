"""
Configure Endpoints.

Contains available endpoint info.
"""

RESOURCES = {
    "attachments": {
        "endpoint": "attachments",
        "verbs": ["GET", "POST", "DELETE"]
    },
    "contacts": {
        "endpoint": "contacts",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["customer", "first_name", "last_name"]
    },
    "customers": {
        "endpoint": "customers",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["company_name"]
    },
    "defects": {
        "endpoint": "defects",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["item"]
    },
    "features": {
        "endpoint": "features",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["item"]
    },
    "tasks": {
        "endpoint": "tasks",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["item"]
    },
    "incidents": {
        "endpoint": "incidents",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["item"]
    },
    "emails": {
        "endpoint": "email",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["subject", "body", "to", "from", "email_type", "item"]
    },
    "fields": {
        "endpoint": "fields",
        "verbs": ["GET"],
        "required": []
    },
    "itme_relations": {
        "endpoint": "item_relations",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["relation_type", "parent_item", "child_item"]
    },
    "me": {
        "endpoint": "me",
        "verbs": ["GET"],
        "required": []
    },
    "picklists": {
        "endpoint": "picklists",
        "verbs": ["GET", "POST", "DELETE"],
        "required": []
    },
    "projects": {
        "endpoint": "projects",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["name"]
    },
    "releases": {
        "endpoint": "releases",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["name", "release_type"]
    },
    "security_roles": {
        "endpoint": "security_roles",
        "verbs": ["GET"]
    },
    "settings": {
        "endpoint": "settings",
        "verbs": ["GET"],
        "required": []
    },
    "users": {
        "endpoint": "users",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["first_name", "last_name", "security_roles"]
    },
    "work_logs": {
        "endpoint": "work_logs",
        "verbs": ["GET", "POST", "DELETE"],
        "required": ["user", "work_done", "item", "date_time"]
    },
    "workflow_steps": {
        "endpoint": "workflow_steps",
        "verbs": ["GET"],
        "required": []
    },
    "workflows": {
        "endpoint": "workflows",
        "verbs": ["GET"],
        "required": []
    },
}
