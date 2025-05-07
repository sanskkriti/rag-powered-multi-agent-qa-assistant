class QAAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.log = []
    
    def process_query(self, query):
        self.log = []
        
        # Check for special commands
        if any(word in query.lower() for word in ['calculate', 'math', 'solve']):
            self.log.append("Routing to calculator")
            return self._calculator_tool(query)
        elif any(word in query.lower() for word in ['define', 'dictionary']):
            self.log.append("Routing to dictionary")
            return self._dictionary_tool(query)
        else:
            self.log.append("Routing to RAG pipeline")
            return self._rag_pipeline(query)
    
    def _calculator_tool(self, query):
        try:
            # Simple math evaluation (in production use a proper math parser)
            result = eval(query)  # WARNING: Only for demo - insecure in production
            return f"Calculation result: {result}", self.log
        except:
            return "Could not perform calculation", self.log
    
    def _dictionary_tool(self, query):
        # Mock dictionary - in production connect to an API
        return "Dictionary definitions would appear here", self.log
    
    def _rag_pipeline(self, query):
        context = self.retriever.retrieve(query)
        self.log.append(f"Retrieved {len(context)} context chunks")
        
        # Simplified generation - in production use proper LLM
        answer = f"Based on context: {context[0][:200]}..." if context else "No relevant context found"
        return answer, self.log
