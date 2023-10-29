import openai 
import tiktoken
import dotenv
import os
import sys

sys.path.append(r'./exceptionHandler')
from OpenaiException import handle_openai_exceptions

dotenv.load_dotenv(dotenv_path=r".\.env")

class OpenAI:

    def __init__(self, prompt_system=None, file_system_assistent=None):
        if not file_system_assistent is None:
            with open(file_system_assistent, 'r') as file:
                self.prompt_system = file.read()
        else:
            self.prompt_system = prompt_system

    def create_message_only_system(self):
        prompt_usuario=''
        total_values = self.calculate_tiktoken(prompt_usuario)
        model, max_token = self.change_types_by_token(total_values)
        
        openai.api_key = os.getenv("OPENAI_API_KEY")
        try:
            
            resposta = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": self.prompt_system
                    }
                ],
                temperature=1,
                max_tokens=max_token,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return resposta.choices[0].message.content
        
        except openai.error.OpenAIError as e:
            handle_openai_exceptions(e)

    def create_message(self, prompt_usuario):

        total_values = self.calculate_tiktoken(prompt_usuario)
        model, max_token = self.change_types_by_token(total_values)
        
        openai.api_key = os.getenv("OPENAI_API_KEY")
        try:
            
            resposta = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": self.prompt_system
                    },
                    {
                        "role": "user",
                        "content": prompt_usuario
                    }
                ],
                temperature=1,
                max_tokens=max_token,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return resposta.choices[0].message.content
        
        except openai.error.OpenAIError as e:
            handle_openai_exceptions(e)

    def calculate_tiktoken(self, message):
        encoding_type = tiktoken.encoding_for_model(os.getenv("OPENAI_DEFAULT_TYPE"))
        values = len(encoding_type.encode(self.prompt_system + message))
        return values

    def change_types_by_token(self,value):
        if value > 4096:
            return os.getenv("OPENAI_DEFAULT_TYPE") + '-16k', 3000
        return os.getenv("OPENAI_DEFAULT_TYPE"), 1000

if __name__ == '__main__':
    message = "Cliente1 - Bola de futebol, Roupa para casamento, Mochila"
    file_path = r'.\IA_Assintent\system-assitente-1.txt'
    openai_instance = OpenAI(file_path)
    print(openai_instance.create_message(message))