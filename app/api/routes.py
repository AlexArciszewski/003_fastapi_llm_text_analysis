from fastapi import APIRouter
from app.schemas.text import TextRequest, TextResponse
from app.services.analysis import analyze_text


router: APIRouter = APIRouter()


@router.post("/analyze", response_model=TextResponse)
def analyze_endpoint(request: TextRequest) -> TextResponse:
    """
    Endpoint for the text analysis using LLM.

    Args:
        request (TextRequest): Request with text.

    Returns:
        TextResponse: Response - text outcome included
    """
    result: str = analyze_text(request.text)
    return TextResponse(result=result)
