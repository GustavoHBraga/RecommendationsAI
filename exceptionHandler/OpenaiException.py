import openai.error as oai_err
import time

def handle_openai_exceptions(e):
    if isinstance(e, oai_err.APIError):
        print("Erro na API OpenAI (APIError):", e)
        print("Causa: Problema do nosso lado.")
        print("Solução: Tente novamente após uma breve espera e entre em contato conosco se o problema persistir.")
        time.sleep(0.35)

    elif isinstance(e, oai_err.Timeout):
        print("Erro na API OpenAI (Timeout):", e)
        print("Causa: Solicitação expirou.")
        print("Solução: Tente novamente após uma breve espera e entre em contato conosco se o problema persistir.")
        time.sleep(0.35)

    elif isinstance(e, oai_err.RateLimitError):
        print("Erro na API OpenAI (RateLimitError):", e)
        print("Causa: Você atingiu seu limite de requisições atribuído.")
        print("Solução: Reduza a frequência das suas requisições. Leia mais no nosso guia de limites de requisições.")

    elif isinstance(e, oai_err.APIConnectionError):
        print("Erro na API OpenAI (APIConnectionError):", e)
        print("Causa: Problema ao conectar aos nossos serviços.")
        print("Solução: Verifique suas configurações de rede, configuração de proxy, certificados SSL ou regras de firewall.")

    elif isinstance(e, oai_err.InvalidRequestError):
        print("Erro na API OpenAI (InvalidRequestError):", e)
        print("Causa: Sua requisição estava malformada ou faltando alguns parâmetros obrigatórios, como um token ou uma entrada.")
        print("Solução: A mensagem de erro deve indicar o erro específico cometido. Verifique a documentação para o método específico da API que você está chamando e certifique-se de estar enviando parâmetros válidos e completos. Você também pode precisar verificar a codificação, formato ou tamanho dos dados da sua requisição.")

    elif isinstance(e, oai_err.AuthenticationError):
        print("Erro na API OpenAI (AuthenticationError):", e)
        print("Causa: Sua chave de API ou token era inválido, expirado ou revogado.")
        print("Solução: Verifique sua chave de API ou token e certifique-se de que ela esteja correta e ativa. Você pode precisar gerar uma nova no painel da sua conta.")

    elif isinstance(e, oai_err.ServiceUnavailableError):
        print("Erro na API OpenAI (ServiceUnavailableError):", e)
        print("Causa: Problema em nossos servidores.")
        print("Solução: Tente novamente após uma breve espera e entre em contato conosco se o problema persistir. Verifique a página de status.")
        time.sleep(0.35)

    else:
        print(f"Erro desconhecido: {e}")