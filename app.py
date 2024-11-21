from flask import Flask, jsonify, redirect, url_for, request

app = Flask(__name__)

def get_prompt_answer(query):
    import time
    import json
    from supabase import create_client
    from langchain_core.prompts import PromptTemplate
    from langchain_huggingface import HuggingFaceEndpoint
    import os
    
    supabase_creds = json.loads(open("keys/supabase_creds").read().strip())
    supabase_url = supabase_creds["url"]
    supabase_key = supabase_creds["key"]
    supabase = create_client(supabase_url, supabase_key)
    insert_response=supabase.table('query').insert([{"query": query}]).execute()
    time.sleep(1) #This is to allow trigger to do its work
    
    response = supabase.rpc("match_documents", {"query_text": query}).execute()
    context = ""
    for each_chunk in response.data:
        context += each_chunk["chunk"]
    
    # Setting the Hugging Face API Token and Supabase Credentials
    HUGGINGFACEHUB_API_TOKEN = open("keys/hf_token").read().strip()
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
    os.environ["HF_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

    # Initializing the Hugging Face Endpoint and Output Parser
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1"
    llm = HuggingFaceEndpoint(repo_id=repo_id,
                            max_length=128,
                            temperature=0.5,
                            token=HUGGINGFACEHUB_API_TOKEN)

    question = """Answer the question based only on following context:
    {context}
    Question: {query}"
    """


    prompt = PromptTemplate(
                        template=question, 
                        input_variables= ["context", "query"],
                        output_variables=["answer"]
                            )
    chain = prompt | llm
    result = chain.invoke({"context": context, "query": query})
    
    unique_urls = []
    for each_response in response.data:
        url = each_response["URL"]
        if url not in unique_urls:
            unique_urls.append(url)
    print(unique_urls)
    output = {
        "answer": result,
        "unique_urls": [{"URL": url} for url in unique_urls]
    }
    return output

@app.route('/')
def index():
    return redirect(url_for('get_answer'))

@app.route('/get_answer', methods=['GET'])
def get_answer():
    print("Get RAG answer")
    query = request.args.get('query')
    output=get_prompt_answer(query)
    return jsonify(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)