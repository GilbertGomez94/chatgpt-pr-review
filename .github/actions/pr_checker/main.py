import openai
import os
import sys 


openai.api_key = os.getenv('OPENAI_KEY')


def main():
    prompt = os.environ.get("INPUT_PROMPT")
    changes = " ".join(prompt)
    changes = changes.replace('"', '')
    question = f"""
             Imaginando que eres un revisor de pull request, podrías decir explicitamente  que cambios se están realizando dentro de un repositorio de git:
             {changes}
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
    sys.exit(0)


if __name__ == '__main__':
    main()