import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory 

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    raise ValueError("A chave da API não foi definida no .env")


#criando o agente de IA
modelo = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    api_key=api_key
)


perguntas = [
    "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?",
    "E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?"
]


#criando um prompt template para nosso modelo
modelo_prompt = ChatPromptTemplate.from_messages(
    [
        ('system', '"Você é o "GeoAI Mentor", um assistente especializado em ajudar geocientistas a migrar para a área de Ciência de Dados. Seja amigável e didático.'),
        ('placeholder', '{historico}'),
        ('human', '{query}')
    ]
)


#criando uma cadeia
cadeia = modelo_prompt | modelo | StrOutputParser()


#criando um armazenamento de memorias
memoria_sessoes = {}
session_id = "sessao_1"

def obter_historico_por_sessao(session_id : str):
    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()
    return memoria_sessoes[session_id]


#nova cadeia com memoria
cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=cadeia,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key='historico'
)


print("\n")
print("\n")
#mandando as perguntas para nosso agente responder
for pergunta in perguntas:
    resposta = cadeia_com_memoria.invoke({'query' : pergunta}, config={"configurable": {"session_id": session_id}})
    print("Usuario: ", pergunta)
    print("IA: ", resposta)
    print("\n")
    print("\n")