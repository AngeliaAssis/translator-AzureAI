
import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
  response = requests.get(url)

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_style in soup(['script', 'style']):
      script_or_style.decompose
    text = soup.get_text(separator=' ')
    #limpar texto
    linhas = (line.strip() for line in text.splitlines())
    parts = (phrase.strip() for line in linhas for phrase in line.split(" "))
    clean_text = '\n'.join (part for part in parts if part)
    return clean_text
  else:
    print(f"Failed to fetch the URL. Status code: {response.status_code}")
    return None

  text = soup.get_text()
  return text


from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint="OPENAI_ENDPOINT",
    api_key="OPENAI_KEY",
    api_version="2024-02-15-preview",
    deployment_name="gpt-4o-mini",
    max_retries=0
)

def translate_article(text, lang):
  messages = [
      ("system", "Você atua como tradutor de textos"),
      ("user", f"Traduza o {text} para o idioma {lang} e responda em markdown")
  ]

  response = client.invoke(messages)
  print(response.content)
  return response.content


url = #(INSERIR URL)
text = extract_text_from_url(url)
article = translate_article(text, "português")

print(article)