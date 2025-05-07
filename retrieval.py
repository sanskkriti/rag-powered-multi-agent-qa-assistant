from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

class DocumentRetriever:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.documents = []
        
    def ingest_documents(self, folder_path):
        """Process text files from folder"""
        self.documents = []
        embeddings = []
        
        if not os.path.exists(folder_path):
            return
            
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                with open(os.path.join(folder_path, filename)) as f:
                    chunks = self._chunk_text(f.read())
                    self.documents.extend(chunks)
                    embeddings.extend(self.model.encode(chunks))
        
        if embeddings:
            embeddings = np.array(embeddings).astype('float32')
            self.index = faiss.IndexFlatL2(embeddings.shape[1])
            self.index.add(embeddings)
    
    def _chunk_text(self, text, chunk_size=300):
        """Split text into fixed-size chunks"""
        words = text.split()
        return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    
    def retrieve(self, query, k=3):
        """Retrieve top k relevant chunks"""
        if not self.index:
            return ["No documents were found in the 'documents' folder. Please add some .txt files and restart the app."]
            
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k)
        return [self.documents[i] for i in indices[0]]
