from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="qwen2.5:7b")

messages = [
    SystemMessage(content="请帮我进行翻译，由英文翻译成中文！"),
    HumanMessage(content="My name is xiaoming"),
]

# result = model.invoke(messages)
# print(result)
#
parser = StrOutputParser()
# print(parser.invoke(result))

# 执行链
# chain = model | parser
# chain = RunnableSequence(first=model, last=parser)
chain = model.pipe(parser)
print(chain.invoke(messages))
