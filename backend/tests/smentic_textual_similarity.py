from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
model.to("cuda")

# our question
sentences_input = [
    "hi",
    "How the weather today?",
    "Do you know some knowledge from medicine",
]

# the output of model
sentences_output = [
    "Hello, I'm here to help you with your question.",
    "The weather today is generally warm and sunny, with a few exceptions.",
    "Yes, I do have knowledge from medicine.",
]

# Compute embeddings for both lists
embeddings1 = model.encode(sentences_input)
embeddings2 = model.encode(sentences_output)

# Compute cosine similarities
similarities = model.similarity(embeddings1, embeddings2)

# Output the pairs with their score
# 
# hi
#  - Hello, I'm here to help you with your question.: 0.3369
#  - The weather today is generally warm and sunny, with a few exceptions.: 0.0816
#  - Yes, I do have knowledge from medicine.: 0.0607
# How the weather today?
#  - Hello, I'm here to help you with your question.: 0.1738
#  - The weather today is generally warm and sunny, with a few exceptions.: 0.6880
#  - Yes, I do have knowledge from medicine.: 0.0026
# Do you know some knowledge from medicine
#  - Hello, I'm here to help you with your question.: 0.1628
#  - The weather today is generally warm and sunny, with a few exceptions.: 0.0615
#  - Yes, I do have knowledge from medicine.: 0.8638



for idx_i, sentence1 in enumerate(sentences_input):
    print(sentence1)
    for idx_j, sentence2 in enumerate(sentences_output):
        print(f" - {sentence2: <30}: {similarities[idx_i][idx_j]:.4f}")