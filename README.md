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
Change the tokens based on the combination of each word which forms a sentence.
    - He broke the glass
    - He broke the news
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
(Neural Network)
    - Transforms each node to improve or modify its features.
    - Applies some learned weights for refinement.
    - Matrix multiplication, and more Mathmatics

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
- Linear Probability Distribution - probability score for each next token (word)
- Softmax picks the most appropriate probability
    - The more softmax the more creativity, low accuracy
    - The less softmax the more accuracy, low creativity
    (Temperature setting in ChatGPT / Google Gemini)









