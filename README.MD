# Fang - the python developer

Me having a play, and a simple AI prompt for python, (https://ollama.com/blog/how-to-prompt-code-llama)

- Install ollama for windows

pip install streamlit
pip install langchain_community
streamlit run main.py

## To create the AI model

Init only or reset

```console
ollama pull codellama
ollama rm fang
```

```console
ollama create fang -f Modelfile
```

## To run the model

```console
ollama run fang
```
