# Gen AI Learn Playground

## Setup Code

### Create a Python environment

- Windows

```
python -m venv venv
```

- Mac

```
python3 -m venv venv
```

### Activate the Environment

- Windows

```
.\venv\Scripts\activate
```

- Mac

```
source venv/bin/activate
```

### Freeze Requirements

```
pip freeze > requirements.txt
```

### Install Dependencies (Requirements)

```
pip install -r requirements.txt
```

## Transformer Architecture

![image](https://github.com/user-attachments/assets/16b217d4-0236-47ad-90bd-eb78b20d8932)

### Input, Encoding and Embeddings

- Tokenization Process
  Example: Split into different words. And covert that into numbers.
  `tokenization.py`
- Vector Embeddings
  Semantic Meaning
  `embeddings.py`

### Positional Encoding

- The position of tokens is important.
  Example: "The dog chased the cat" carries a different meaning than "The cat chased the dog"

### Attention

#### Self Attention

(Always has one HEAD)
Change the tokens based on the combination of each word which forms a sentence. - He broke the glass - He broke the news
Contextual understanding. Tokens talk to each other to adjust its embeddings.

#### Multi-Head Attention

(Has more than one HEAD)

Example: Watching a cricket match. (CSK vs RCB)

- Dhoni is the captain
- Who is the current bowler
- Who is the current batter
- What will be the score
  Focusing on different aspects / different perspectives

Advantage: More context aware.

### Feed Forward

(Neural Network) - Transforms each node to improve or modify its features. - Applies some learned weights for refinement. - Matrix multiplication, and more Mathmatics

### Input and Output

#### Training Phase

    - Give input: "This animal is a "
    (The expected next word is "dog")
    - AI generates the output based on given input.
    - Next word can be some random word. (Say "banana")
    - Calculate the loss between expected output and actual output.
    - Do back-propagation and repeat the steps until your loss is zero.

    Example:
    - <start> of training
    - I ask you 2+2
    (Expected output is 4)
    - You say 100
    - Loss is 100-4 = 96
    - Repeat the process (Back propagation)
    - You say 50
    - Loss is 50-4=46 (loss has reduced from previous iteration, but its still very high)
    - Repeat the process (Back propagation)
    - You say 5
    - Loss is 5-4=1 (better but its still not 0)
    - Repeat the process (Back propagation)
    - You say 4
    - Loss is 4-4=0 (Boom, that's the correct output)
    - <end> of training

#### Inferencing Phase

- Linear Probability Distribution - probability score for each next token (word).
- Softmax picks the most appropriate probability from the probability distribution.
  - The more softmax the more creativity, low accuracy.
  - The less softmax the more accuracy, low creativity.
    (Temperature setting in ChatGPT / Google Gemini)

## Prompt Engineering (Prompt Styles)

### Alpaca Prompt
Reference: [Standford Alpaca Prompt Style](https://github.com/tatsu-lab/stanford_alpaca)

    Instructions:
    For the given number by user, perform
    Input: what is 2+2
    Response:


### INST Format (llama-2)
Reference: [INST Prompt Style by LLAMA](https://www.llama.com/docs/model-cards-and-prompt-formats/meta-llama-2/)

    -- User Prompt
    [INST][/INST]
    -- System Prompt
    <<SYS>><</SYS>>
    ---------------------------------------
    <s>[INST] <<SYS>>
    {{ system_prompt }}
    <</SYS>>

    {{ user_message_1 }} [/INST] {{ model_answer_1 }} </s>
    <s>[INST] {{ user_message_2 }} [/INST]

### ChatML (OpenAI)

    {role: "system", "content": "You are an assistant"},
    {role: "user", "content": "usermessage"}

## Prompt Engineering (Prompt Techniques)

### Zero Shot Prompting
Task without examples for the model to handle.

### Few Shot Prompting
Task with a few examples to guide the model.

### Chain Of Thought
Step-by-step reasoning to solve a problem.

### Self-Consistency Prompting
Using multiple answers to find the most consistent one.

### Persona-based Prompting
Guiding the model to respond with a specific personality or role.

### Roleplaying Prompting
Asking the model to act as a specific character or persona.

## Running a Model in Local Machine
Refer https://ollama.com/search 
 - `docker-compose.yml` -> `docker compose up`: A docker container on which ollama is running. 
 - `ollama_api.py`
  - A FastAPI app that hosts the Chat endpoint which connects to ollama.
  - The ollama client will pull `gemma3:1b` model into the docker which is lightweight.
  - Briging up FastAPI app: `uvicorn ollama_api:app --port 8000`.
 - Sending a POST to http://127.0.0.1:8000/docs#/default/chat_chat_post with a message say "How are you" to chat with local model.

    > - **Uvicorn** is an **ASGI server** (Asynchronous Server Gateway Interface), and it is commonly used to run **FastAPI** apps, though it can also be used with other ASGI-based web frameworks.
    > - **FastAPI** is a Python web framework, and **Uvicorn** serves as the server that runs the FastAPI app. So, Uvicorn is indeed a server runtime for FastAPI, as it handles the HTTP requests and interacts with the FastAPI application.

 

    



