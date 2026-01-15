class ChangeRequest:
    def __init__(
        self,
        id,
        title,
        description,
        category,
        service,
        window_start,
        window_end,
        requester,
        change_type
    ):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.service = service
        self.window_start = window_start
        self.window_end = window_end
        self.requester = requester
        self.change_type = change_type  # standard / normal / emergency
