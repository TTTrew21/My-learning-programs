import google.generativeai as genai # import the google-generativeai first.

genai.configure(api_key="AIzaSyCxOTESj9xjpmEWgkBJCVnk-Uz2POf3tFE")

model = genai.GenerativeModel('models/gemini-2.0-flash')

questions = [
    "Explain Artificial Intelligence in a sentence.",
    "What's the capital city of Taiwan?",
]

output_file = "output.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for i, prompt in enumerate(questions):
        try:
            response = model.generate_content(prompt) # generate content of the prompt
            answer = response.text.strip()

            print(f"[Prompt {i+1}] {prompt}")
            print(f"Response:\n{answer}")
            print("-" * 50)

            # Write responses into the file
            f.write(f"Prompt {i+1}: {prompt}\n")
            f.write(f"Response:\n{answer}\n")
            f.write("-" * 50 + "\n")

        except Exception as e:
            print(e)