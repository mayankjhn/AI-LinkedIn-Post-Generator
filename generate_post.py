import openai

openai.api_key = my api

def generate_linkedin_post(topic):
    prompt = f"Create an engaging LinkedIn post about {topic}. Make it professional yet engaging."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert content writer for LinkedIn."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"].strip()
