from dataclasses import dataclass

from fastapi import APIRouter
from langchain_ollama import OllamaLLM, ChatOllama

ai_router = APIRouter(prefix="/ai", tags=['AI'])

message = []

@dataclass
class AiMessageReq:
    message: str

@ai_router.post('/')
def send_message(request: AiMessageReq):
    model = 'deepseek-r1:8b'
    model = 'gemma:latest'
    llm = ChatOllama(model=model)

    message.append(('human', request.message))

    response = llm.invoke(message)
    content = response.content
    message.append(('ai', content))

    print(message)

    return {
        'message': content
    }
