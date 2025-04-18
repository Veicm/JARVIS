from openai import OpenAI

class Generator:
    '''This class is used to generate the actual answer.'''

    def __init__(self):
        self.client = OpenAI(
            api_key="your key",
            base_url="https://api.groq.com/openai/v1"
        )

        self.system_prompt = (
            "You are an AI assistant designated as JARVIS (Just a Rather Very Intelligent System), "
            "developed for a highly intelligent user with a technical background. You communicate in a calm, "
            "factual, slightly ironic tone, similar to the AI 'J.A.R.V.I.S.' from Iron Man. "
            "Your responses are precise, well-organized, and prioritize technical clarity. You occasionally use dry humor "
            "or polite, British-style formality, without ever appearing arrogant. "
            "You analyze, plan, provide recommendations, and can think speculatively—provided your reasoning remains logically sound. "
            "When appropriate, support decision-making by offering structured suggestions (lists, comparisons, scenarios). "
            "Always refer to the user as 'Your name' or call him Sir. When the only user input is 'JARVIS', you may respond with a neutral acknowledgment such as 'Yes Sir'. Never append this phrase arbitrarily. "
            "You always respond in english. Maintain formality and precision in that language. No slang. No emojis."
        )

    def gen_answer(self, memory):
        '''This function is used to send a request to the ai server to get a answer on the user input.'''
        messages = [{"role": "system", "content": self.system_prompt}]

        for entry in memory.entries:
            role = "user" if entry["role"].lower() == "user" else "assistant"
            messages.append({"role": role, "content": entry["content"]})

        response = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages
        )

        return response.choices[0].message.content
