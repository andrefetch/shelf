from datetime import datetime
import uuid

'''
Note dataclass, handles title, body, and tags.

Generates:
id, and created_at time stamp.
'''

class Note:

    def __init__(self, title: str, body: str, tags: list[str], id: int, created_at: str):

        self.title = title
        self.body = body
        self.tags = tags if tags is not None else []
        self.id = id if id is not None else str(uuid.uuid4())[:8]
        self.created_at = created_at if created_at is not None else datetime.now().isoformat()

