import requests
from config import Config


class AIServiceError(Exception):
    pass


class AIService:
    def sistem_talimati(self):
        return Config.BUSINESS_CONTEXT

    def groq_istegi(self, messages):
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {Config.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.1-8b-instant",
            "messages": messages
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=data,
                timeout=30
            )

            response.raise_for_status()
            return response

        except requests.RequestException as hata:
            raise AIServiceError(
                f"Yapay zeka servisine baglanirken hata olustu: {hata}"
            ) from hata

    def yanit_uret(self, mesaj, gecmis):
        if not Config.GROQ_API_KEY:
            return "Demo modu: Yapay zeka servisi icin API anahtari tanimlanmamis."

        messages = [
            {
                "role": "system",
                "content": self.sistem_talimati()
            }
        ]

        if gecmis:
            messages.extend(gecmis)

        messages.append(
            {
                "role": "user",
                "content": mesaj
            }
        )

        response = self.groq_istegi(messages)

        try:
            data = response.json()
            return data["choices"][0]["message"]["content"]

        except (KeyError, IndexError, TypeError, ValueError) as hata:
            raise AIServiceError(
                f"Yapay zeka yaniti okunamadi: {hata}"
            ) from hata

ai_service = AIService()