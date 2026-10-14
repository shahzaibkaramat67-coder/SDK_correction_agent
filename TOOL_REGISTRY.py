search_tool = {
    "type": "function",
    "function": {
        "name": "search",
        "description": """
Search the internet for factual, current, or external information.

Use this tool when:
- The answer requires web information.
- The user asks about a person, company, product, technology, event, place, or topic.
- The user asks for recent or up-to-date information.
- Sources are needed before deeper analysis.

Do NOT use for:
- Greetings
- Small talk
- Casual conversation
- Thank-you messages
- Questions answerable without external information.
""",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The search query."}
            },
            "required": ["query"],
        },
    },
}


research_tool = {
    "type": "function",
    "function": {
        "name": "research",
        "description": """
Perform deep research and analysis using sources.

Use this tool when:
- The user asks for detailed explanations.
- The user asks for comparisons.
- The user asks for research, investigation, reports, or analysis.
- Search results alone are insufficient.

Requirements:
- Search should normally be used first.
- Research requires sources from search().
- Use research after gathering relevant search results.
""",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "The research question."},
                "sources": {
                    "type": "array",
                    "description": "Sources obtained from search.",
                    "items": {"type": "object"},
                },
            },
            "required": ["query", "sources"],
        },
    },
}
