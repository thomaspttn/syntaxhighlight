import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

def extract_and_highlight(text):
    doc = nlp(text)
    highlighted_text = ""
    
    for token in doc:
        if token.dep_ == "nsubj" or token.dep_ in ["dobj", "pobj"]:
            highlighted_text += f'<strong>{token.text}</strong> '
        else:
            highlighted_text += token.text + " "
    
    return highlighted_text.strip()

def generate_html(original_text, highlighted_text):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="static/styles.css">
        <title>Text Visualization</title>
        <style>
            .container {{
                display: flex;
                justify-content: space-between;
                padding: 20px;
            }}
            .box {{
                width: 45%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f9f9f9;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="box">
                <h3>Original Text</h3>
                <p>{original_text}</p>
            </div>
            <div class="box">
                <h3>Highlighted Text</h3>
                <p>{highlighted_text}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

# Input text
text = """
It's what you have always wanted to accomplish. Everyone, when they are young, knows what their Personal Legend is. At that point in their lives, everything is clear and everything is possible. They are not afraid to dream, and to yearn for everything they would like to see happen to them in their lives. But, as time passes, a mysterious force begins to convince them that it will be impossible for them to realize their Personal Legend.

It's what you have always wanted to accomplish. Everyone, when they are young, knows what their Personal Legend is. At that point in their lives, everything is clear and everything is possible. They are not afraid to dream, and to yearn for everything they would like to see happen to them in their lives. But, as time passes, a mysterious force begins to convince them that it will be impossible for them to realize their Personal Legend.

It's what you have always wanted to accomplish. Everyone, when they are young, knows what their Personal Legend is. At that point in their lives, everything is clear and everything is possible. They are not afraid to dream, and to yearn for everything they would like to see happen to them in their lives. But, as time passes, a mysterious force begins to convince them that it will be impossible for them to realize their Personal Legend.
"""

# Extract and highlight subjects and objects
highlighted_text = extract_and_highlight(text)

# Generate HTML
html_output = generate_html(text, highlighted_text)

# Save to an HTML file
with open("text_visualization.html", "w") as file:
    file.write(html_output)

print("HTML file generated successfully.")

