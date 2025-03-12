from fastapi import FastAPI, Header, Request, Response
from fastapi.exceptions import HTTPException
from openai.types.chat import ChatCompletion
from typing_extensions import Annotated

from patchwork.common.client.llm.aio import AioLlmClient
from patchwork.common.client.llm.anthropic import AnthropicLlmClient
from patchwork.common.client.llm.google_ import GoogleLlmClient
from patchwork.common.client.llm.openai_ import OpenAiLlmClient

app = FastAPI()


@app.post("/v1/chat/completions")
async def handle_openai(
    authorization: Annotated[str, Header()],
    request: Request,
    response: Response,
) -> ChatCompletion:
    _, _, api_key = authorization.partition("Bearer ")
    body = await request.json()

    openai_client = OpenAiLlmClient(api_key=api_key)
    google_client = GoogleLlmClient(api_key=api_key)
    anthropic_client = AnthropicLlmClient(api_key=api_key)
    aio_client = AioLlmClient(openai_client, google_client, anthropic_client)
    try:
        return aio_client.chat_completion(**body)
    except Exception as e:
        status_code = getattr(e, "status_code", 500)
        body = getattr(e, "body", {"error_message": str(e)})
        raise HTTPException(status_code=status_code, detail=body)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
