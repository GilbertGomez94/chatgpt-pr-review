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
             Como un revisor experto de pull request, podrías dar un resumen de 1 línea sobre los cambios entre una rama y otra:
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
    print(f"prompt_output={out}")
    sys.exit(0)


if __name__ == '__main__':
    main()
