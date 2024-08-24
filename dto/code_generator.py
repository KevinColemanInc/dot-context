from octoai.client import OctoAI
from octoai.text_gen import ChatMessage


class CodeGenerator:
    def __init__(self, messages: list[ChatMessage]) -> None:
        self.messages = messages
        self.client = OctoAI(
            api_key="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNkMjMzOTQ5In0.eyJzdWIiOiI2MTczMTEzNi01NzdiLTQ4ODEtYmYyNi0xNTEzYTYyZTBlNzUiLCJ0eXBlIjoidXNlckFjY2Vzc1Rva2VuIiwidGVuYW50SWQiOiI0ZjY5Y2ZmNS1jMmQ1LTQ3MjMtOGEyYy03YTNlN2Q5Yjg4MTIiLCJ1c2VySWQiOiJhMDVjNWE0Yy04ZTg0LTQ3ODEtOWFjYS1jYTk3MDEzYjliMzEiLCJhcHBsaWNhdGlvbklkIjoiYTkyNmZlYmQtMjFlYS00ODdiLTg1ZjUtMzQ5NDA5N2VjODMzIiwicm9sZXMiOlsiRkVUQ0gtUk9MRVMtQlktQVBJIl0sInBlcm1pc3Npb25zIjpbIkZFVENILVBFUk1JU1NJT05TLUJZLUFQSSJdLCJhdWQiOiIzZDIzMzk0OS1hMmZiLTRhYjAtYjdlYy00NmY2MjU1YzUxMGUiLCJpc3MiOiJodHRwczovL2lkZW50aXR5Lm9jdG8uYWkiLCJpYXQiOjE3MjQ1Mjc3MzB9.Iol_DlMKz5-ncjOO5kAHXIiUf7f12MrANnGfOH5uHnly8J8nQUlJuGpKj8ex4p6dncgyGC3he3-m-PY5E3krk6FKrxrhqoa9t2RP-Io9prRf05jR8Mia9CWK4X2ZPYyd1nWRn_vLuOSZtGTHKmWHh2pO5PbzK0DaHhuZXC4hoSyQbE8E1jqGpZfA4MQCxfZZsTyOYrxHNG_hAqklTiYHFKCj2SeD474YqtZgqifT1QdvAze-0iQib8j7z40zDz9z7uzYbmHg5bez9cePxyNnR65u73AeCO5Jmv2pdG4MATrgnD4tHtKuK7ZrYL-uPIQOHQyzcGBO6C1xkPbTiqphtQ"
        )

    def generate_code(self):
        self.client.text_gen.create_chat_completion_stream(
            max_tokens=65536,
            messages=self.messages,
            model="meta-llama-3.1-405b-instruct",
            presence_penalty=0,
            temperature=0,
            top_p=1,
        )
