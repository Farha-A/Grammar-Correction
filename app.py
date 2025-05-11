import torch
from flask import Flask, jsonify, request
from transformers import BartForConditionalGeneration, BartTokenizer

app = Flask(__name__)
tokenizer = BartTokenizer.from_pretrained("fine_tuned_bart")
model = BartForConditionalGeneration.from_pretrained("fine_tuned_bart")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


@app.route("/")
def home() -> str:
    """Return a simple greeting for the root endpoint.

    Returns:
        str: Smiley face string.
    """
    return ":D"


@app.route("/predict", methods=["POST"])
def predict() -> dict:
    """Correct grammar in input text using a fine-tuned BART model.

    Expects a JSON payload with a 'text' field. Returns corrected text.

    Returns:
        dict: JSON response with corrected text.
    """
    data = request.get_json()
    input_text = data.get("text", "")
    
    input_text = "fix grammar: " + input_text
    inputs = tokenizer([input_text], return_tensors="pt", padding=True).to(device)
    
    with torch.no_grad():
        output_ids = model.generate(
            **inputs, max_length=128, num_beams=4, early_stopping=True
        )
    
    corrected = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return jsonify({"corrected": corrected})


if __name__ == "__main__":
    app.run(debug=True)