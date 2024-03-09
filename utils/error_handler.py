import sys
from database.messages import ClientText


class ErrorHandler:
    def __init__(self):
        pass

    @staticmethod
    def default_exit(message: str) -> None:
        print(message)
        sys.exit()

    @staticmethod
    def empty_string(value: str) -> None:
        if value == "":
            print(ClientText.ERROR["empty_string"])
            sys.exit()

        return

    @staticmethod
    def false_return(value: bool) -> None:
        if not value:
            print(ClientText.ERROR["force_close"])
            sys.exit()

        return
