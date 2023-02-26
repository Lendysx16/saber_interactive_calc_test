class ParenthesisError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ParenthesisError, {0} '.format(self.message)
        else:
            return 'Problem with parenthesis in input expression'


class InputExpressionError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'InputExpressionError, {0} '.format(self.message)
        else:
            return 'Check your input expression'
