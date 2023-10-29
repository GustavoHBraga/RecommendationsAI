import sys
import os
sys.path.append(r'./data')
sys.path.append(r'./utils')
sys.path.append(r'./config')

from EmailConfig import send_email
import AnalysisAI as AI

import multiprocessing
import dotenv

dotenv.load_dotenv(dotenv_path=r".\.env")

def analyze_and_send_email(customer):
    
    # ENV 
    EMAIL_TO =  os.getenv("STMP_EMAIL_TO")

    customeraname = customer['name']
    profile = customer['profile']
    email = EMAIL_TO
    
    print(f'Analyzing profile {customeraname}...')
    products_file = r'.\data\lista-de-produtos.txt'

    print(f'Analyzing recommendations to {customeraname}...')
    recommendations = AI.analyze_recommendations_by_profile(profile, products_file)

    print(f'Create message to {customeraname}...')
    message_to_email = AI.analyze_to_email(customeraname, recommendations)

    send_email(email, subject=f"Recommendations for {customeraname} by best friend IA ", body=message_to_email)
    print("*"*15)

if __name__ == '__main__':
    
    file_profiles_purchased = r'.\data\lista_de_compras_100_clientes.csv'
    profiles = AI.analyze_profiles(file_profiles_purchased)
    
    # Crie uma pool de processos
    pool = multiprocessing.Pool(processes=10)

    # Mapeie a função analyze_and_send_email para cada cliente na lista
    pool.map(analyze_and_send_email, profiles['customers'])

    # Feche a pool de processos
    pool.close()
    pool.join()