# GeoAI Mentor 

O **GeoAI Mentor** é um assistente conversacional desenvolvido com **Python e LangChain** que orienta geocientistas interessados em migrar para a área de **Ciência de Dados**.
O projeto demonstra a criação de um agente de IA simples com **memória de conversa**, permitindo que o modelo responda levando em conta perguntas anteriores. Este é um projeto feito com base nas instruções do curso de Especialista em IA da Alura. 

---

# Tecnologias

* Python
* LangChain
* Groq API (LLM)
* dotenv

---

# Configuração do ambiente

1. Instale as dependências:

```bash
pip install langchain-groq python-dotenv
```

2. Crie um arquivo `.env` na raiz do projeto:

```
GROQ_API_KEY=sua_chave_aqui
```

A chave pode ser obtida em:
https://console.groq.com/keys

---

# Como executar

Execute o script:

```bash
python chatbot_mentor.py
```

O programa fará perguntas ao **GeoAI Mentor** e exibirá as respostas no terminal.

---

# Arquitetura

A aplicação foi construída usando o padrão de cadeia do **LangChain**:

```
Prompt Template → Modelo LLM → Output Parser
```

* **ChatPromptTemplate** define o comportamento do agente e estrutura as mensagens.
* **ChatGroq** conecta o sistema ao modelo LLM (`llama-3.1-8b-instant`).
* **StrOutputParser** converte a resposta do modelo em texto simples.

---

# Memória da Conversa

Para manter o contexto entre mensagens foi utilizado:

```
RunnableWithMessageHistory
```

Esse componente adiciona **memória ao agente**, utilizando `InMemoryChatMessageHistory` para armazenar o histórico de cada sessão (`session_id`).
Assim, o modelo consegue responder levando em conta perguntas feitas anteriormente.

---

# Estrutura

```
geoai-mentor
│
├── chatbot_mentor.py
├── .env
├── requirements.txt
└── README.md
```

---

Projeto desenvolvido para fins de estudo em **LLMs e aplicações com LangChain**.
