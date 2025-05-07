from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os
import numpy as np

class DocumentRetriever:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Use a pretrained model for embedding
        self.documents = []
        self.embeddings = []

    def ingest_documents(self, folder_path):
        """Load and embed documents from the folder."""
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        self.documents = [open(os.path.join(folder_path, f), 'r').read() for f in files]
        self.embeddings = self.model.encode(self.documents)  # Get embeddings for the documents

    def retrieve(self, query):
        """Retrieve the most relevant document using cosine similarity."""
        query_embedding = self.model.encode([query])  # Get the embedding for the query
        similarities = cosine_similarity(query_embedding, self.embeddings)  # Compute cosine similarities
        best_match_index = np.argmax(similarities)  # Get the index of the most similar document
        return self.documents[best_match_index]
