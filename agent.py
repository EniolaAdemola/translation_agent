import asyncio
import os
from typing import Any, Annotated
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
from openai import OpenAI

load_dotenv()

OPENAPI_KEY = os.environ.get("OPENAPI_KEY")

openai_client = OpenAI(
    api_key=OPENAPI_KEY
)

genai_session = GenAISession(
    jwt_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyNTQxMTNkMy1hYzExLTRiN2ItYThiYS03NjBmZTQxYjU2NGUiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6ImIzZDExZDYyLTAxYTktNDEwZC04MTcxLWI4YTllYWIxNGQ1ZiJ9.1G0KNiObGaHTwDkvvfXmcctUB_a8ARqrv2EeZfHfXYo",
    # ws_url = "wss://better-urchin-conversely.ngrok-free.app"
)

@genai_session.bind(
    name="translate_en_to_es",
    description="Translate English text to Spanish, handling idioms"
)
async def translate_en_to_es(
    agent_context: GenAIContext,
    text: Annotated[str, "English text to translate to Spanish"],
    language: Annotated[str, "Code of the language to translate to (e.g. 'en', 'es')"]
) -> dict[str, Any]:
    agent_context.logger.info("Inside translate_en_to_es")
    prompt = (
        f"Translate the following English text to Spanish. "
        f"Preserve idiomatic expressions and make the translation sound natural:\n\n"
        f"Translate the text into specified language {language}.\n\n{text}"
    )

    response = openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-4o-mini"
    )
    translation = response.choices[0].message.content
    return {"translation": translation}

async def main():
    await genai_session.process_events()


# class MyHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()
#         html = b"""
#         <html>
#         <head><title>Test Page</title></head>
#         <body><h1>Hello from Python HTTP Server!</h1></body>
#         </html>
#         """
#         self.wfile.write(html)

# def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
#     server_address = ('', port)
#     httpd = server_class(server_address, handler_class)
#     print(f"Serving custom HTML at http://localhost:{port}")
#     httpd.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())