import openai

openai.api_key = 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

def generate_linkedin_post(topic):
    prompt = f"Create an engaging LinkedIn post about {topic}. Make it professional yet engaging."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert content writer for LinkedIn."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"].strip()
