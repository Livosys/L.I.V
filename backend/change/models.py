class ChangeRequest:
    def __init__(
        self,
        id,
        title,
        description=None,
        category=None,
        service=None,
        window_start=None,
        window_end=None,
        change_type=None,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.service = service
        self.window_start = window_start
        self.window_end = window_end
        self.change_type = change_type
