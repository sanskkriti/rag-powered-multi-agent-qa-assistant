class QAAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.log = []

        # Simple mock dictionary
        self.dictionary = {
            "computer vision": "Computer vision is a field of AI that enables machines to interpret visual data.",
            "nlp": "NLP refers to techniques enabling computers to process human language.",
            "machine learning": "ML is the science of enabling systems to learn from data.",
            "rag": "RAG (Retrieval-Augmented Generation) combines document retrieval with LLM generation."
        }

    def process_query(self, query):
        self.log = []

        query_lower = query.lower()

        if any(word in query_lower for word in ['calculate', 'math', 'solve']):
            self.log.append("Routing to calculator")
            return self._calculator_tool(query)

        elif any(word in query_lower for word in ['define', 'dictionary']):
            self.log.append("Routing to dictionary")
            answer = self._dictionary_tool(query_lower)
            if "No definition" in answer:
                self.log.append("No dictionary result — routing to RAG pipeline")
                return self._rag_pipeline(query)
            return answer, self.log

        else:
            self.log.append("Routing to RAG pipeline")
            return self._rag_pipeline(query)

    def _calculator_tool(self, query):
        try:
            result = eval(query)  # ⚠️ Insecure — use only for demo!
            return f"Calculation result: {result}", self.log
        except:
            return "Could not perform calculation", self.log

    def _dictionary_tool(self, query):
        for keyword in self.dictionary:
            if keyword in query:
                return self.dictionary[keyword], self.log
        return "No definition found in dictionary.", self.log

    def _rag_pipeline(self, query):
        context = self.retriever.retrieve(query)
        self.log.append(f"Retrieved {len(context)} context chunks")

        if context:
            snippet = context[0].strip().replace('\n', ' ').replace('\r', ' ')
            short_answer = f"Here’s what I found based on the documents:\n\n{snippet}"
            return short_answer, self.log
        else:
            return "No relevant context found.", self.log
