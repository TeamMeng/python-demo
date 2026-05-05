from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:latest")

result = llm.invoke("你好")
print(result.content)
