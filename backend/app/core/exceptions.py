from fastapi import HTTPException


class AppException(HTTPException):
    def __init__(self, status_code: int, error: str, code: str):
        super().__init__(status_code=status_code, detail=error)
        self.code = code

class NotFoundException(AppException):
    def __init__(self, entity: str):
        super().__init__(
            status_code=404,
            error=f"{entity} not found",
            code="NOT_FOUND"
        )

class BadRequestException(AppException):
    def __init__(self, message: str):
        super().__init__(
            status_code=400,
            error=message,
            code="BAD_REQUEST"
        )