from pydantic import BaseModel


class TextRequest(BaseModel):
    """Request model for text analysis"""
    text: str


class TextResponse(BaseModel):
    """Request model for text analysis"""
    result: str