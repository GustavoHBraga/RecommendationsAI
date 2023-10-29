import sys 
sys.path.append(r'.\config')
from OpenAIConfig import OpenAI

import FileManipulation
import json

def analyze_profiles(file_profiles_purchased):
    openai = OpenAI(file_system_assistent=r'.\IA_Assintent\system-assitent-identify-profile.txt')
    profiles = FileManipulation.load_data(file_profiles_purchased)
    return json.loads(openai.create_message(profiles))

def analyze_recommendations_by_profile(profile, file_products):

    products = FileManipulation.load_data(file_products)
    prompt_system = FileManipulation.load_data(r'.\IA_Assintent\system-assitent-recommendations.txt')
    prompt_system_format = prompt_system.format(perfil=profile,lista_de_produtos=products)
    openai = OpenAI(prompt_system=prompt_system_format)
    return openai.create_message_only_system()

def analyze_to_email(customername, recommendation):
    prompt_system = FileManipulation.load_data(r'.\IA_Assintent\system-assintent-create-email-by-profile.txt')
    prompt_system_format = prompt_system.format(customername=customername,recomendacoes=recommendation)
    openai = OpenAI(prompt_system=prompt_system_format)
    return openai.create_message_only_system()
