import cohere

co = cohere.ClientV2(api_key="bb018Cx8YGIuL2NBrRyauXTlgJqlRZf87tsCGWfc")

def generate_response(prompt):
    response = co.generate(
        model='command-light-nightly',  # You can also try 'command-light', 'command-nightly', etc.
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        stop_sequences=["--"]
    )
    return response.generations[0].text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Enter a prompt (or 'quit' to exit): ").strip()
        if not user_input:
            print("Please enter something!")
            continue
        if user_input.lower() == 'quit':
            break
        output = generate_response(user_input)
        print("\nResponse:\n", output)