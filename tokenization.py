import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

print("Vocab Size:", encoder.n_vocab) # 200,019 (200K)

text = "The dog chased the cat"
tokens = encoder.encode(text)
print("Tokens:", tokens) # [976, 6446, 135896, 290, 9059]

myTokens = [976, 6446, 135896, 290, 9059]
decoded = encoder.decode(myTokens);
print("Decoded:", decoded) # The dog chased the cat
