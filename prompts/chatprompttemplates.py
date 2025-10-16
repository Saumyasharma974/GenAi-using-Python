from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate({
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Tell me about {topic}.')
})

prompt=chat_template.invoke({'domain': 'AI', 'topic': 'Langchain'})
print(prompt)