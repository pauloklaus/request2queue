class RequiredFieldException(Exception):
    def __init__(self, field, *args):
        super().__init__(args)
        self.field = field

    def __str__(self):
        return f"missing required field: {self.field}"
