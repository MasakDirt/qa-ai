from openai import AsyncOpenAI

from src.configs.external.openai import OpenAIConfig
from src.models.openai import OpenAIEmbeddingModel


class OpenAIClient:
    def __init__(self):
        self._config = OpenAIConfig()
        self._client = AsyncOpenAI(api_key=self._config.OPENAI_API_KEY)

    async def get_embedding(self, text: str, model: str | None = None) -> list[float]:
        model = model if model is not None else self._config.OPENAI_API_EMBEDDED_MODEL
        text = text.strip().replace("\n", " ")

        openai_response = await self._client.embeddings.create(input=[text], model=model)
        embedding_model = OpenAIEmbeddingModel.model_validate(openai_response)

        return embedding_model.data[0].embedding

    async def get_response(self, users_question: str, answers: list[str]) -> str:
        input_prompt = (
            f"You're an assistant answering user questions.\n"
            f"Question: {users_question}\n"
            f"Retrieved answer's from the knowledge base: {answers}\n\n"
            f"Based on the above, write a final answer to the user."
        )

        response = await self._client.responses.create(
            model=self._config.OPENAI_API_MODEL,
            input=input_prompt
        )

        return response.output_text.strip()

