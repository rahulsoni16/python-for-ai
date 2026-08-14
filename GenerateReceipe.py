import AskGemini


def generate_receipe(ingredients, cuisine, diet):
    """Generate a recipe using the provided ingredients, cuisine and diet.

    Returns the generated recipe text.
    """
    prompt = (
        f"Generate one food recipe using the ingredients provided: {', '.join(ingredients)}\n"
        f"Cuisine: {cuisine}\n"
        f"Diet: {diet}"
    )

    # forward prompt to AskGemini and return the text response
    response_text = AskGemini.ask_gemini(prompt)
    return response_text


if __name__ == "__main__":
    recipe = generate_receipe(
        [
            "Eggs",
            "onion",
            "capsicum",
            "salt",
            "Beans",
        ],
        "Mexican",
        "Any",
    )
    print("Final Response:", recipe)
