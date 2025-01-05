# llama-consult
RAG with consulting use cases in mind, all running locally

## Setup
- Follow instructions here to install and use Ollama https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/
- Install dependencies from `requirements.txt`

## Usage
- Create a folder called `data` in the `code` directory with the data that you want the model to be aware of (e.g. slide decks)
- Run index-data.py to get the data into a format that the LLM can query
- Run query.py, which takes one command line argument that is the question for your data e.g. `python query.py "What work have we done previously on solar power?"`

## Contributing
This is an early stage project, please get in touch if you want to collaborate! You can email me on edfagedeveloper@gmail.com
