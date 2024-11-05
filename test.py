from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="fang")
response = llm.invoke("The meaning of life is")
print(response)
