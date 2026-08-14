import AskGemini


def generate_receipe(ingredients, cuisine, diet):

    prompt = f"""
    Generate one food receipe using ingrediant provided : {",".join(ingredients)}
    Cusine: {cuisine}
    Diet: {diet}
"""
    print("Prompt:", prompt)

    responseText = AskGemini.ask_gemini(prompt)

    print("Final Response: ",responseText)


recipe = generate_receipe(
    ["Eggs", "onion", "capsicum", "salt", "Beans"], "Mexican", "Any"
)
