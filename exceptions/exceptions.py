import os


class UnsupportedFileTypeError(Exception):
    """An exception for when a specified file type is not supported by the system."""

    def __init__(self, file_path: str) -> None:
        _, filetype = os.path.splitext(file_path)
        error_msg = f"File type '{filetype}' not supported."
        super().__init__(error_msg)


class NoSupportedFileTypeFoundError(Exception):
    """An exception for when a specified file type could not be found by the system in the directory `dir`."""

    def __init__(self, file: str) -> None:
        super().__init__(f"'{file}' is not a supported filetype")
