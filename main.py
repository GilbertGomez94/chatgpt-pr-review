import openai
import os
import sys 


openai.api_key = os.getenv('OPENAI_KEY')


def main():
    prompt = os.environ.get("INPUT_PROMPT")
    print("received impunt ", prompt)
    # changes = " ".join(prompt)
    changes = prompt.replace('"', '')
    question = f"""
             Ejecute un git diff y lo siguiente fue el output que me dio:
             {changes}
             Imaginando que eres un revisor de pull request, podrías explicar qué cambios se están realizando?
             """
    response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=(question),
                max_tokens=2048,
                n =1,
                stop=None,
                temperature=0.5
            )
    out = response["choices"][0]["text"]
    print(f"::set-output name=prompt_output::{out}")
    


if __name__ == '__main__':
    main()
