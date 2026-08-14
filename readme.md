Recipe Generator Streamlit App
=============================

Setup
-----

1. Create a `.env` file in the project root and set your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Run
----

Start the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Usage
-----
Enter ingredients as comma-separated text, choose a cuisine and diet, then click "Generate recipe".

Notes
-----
- The app forwards prompts to the Gemini client via `AskGemini.py`.
- If you prefer a different LLM client, update `AskGemini.py` accordingly.
#python-for-ai


# YT: https://www.youtube.com/watch?v=ygXn5nV5qFc&list=PL-Y17yukoyy0SupAJSPQYg_Lvre9Kt9EG
# Course: https://python.datalumina.com/basics
# Resources: https://gumroad.com/d/223256056a3586a79a4ea820d9053d1f

