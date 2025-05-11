# Grammar-Correction
Using BART to fix grammar mistakes.

### How to use
1. Download finetuned model from here: https://drive.google.com/file/d/1DXpzA7ENa2gwMzlCCuux1gei0nWij_My/view?usp=sharing
2. Unzip folder and add it to the same directory as "app.py"
3. Run app.py
4. Access via curl commands
   * Sample command: curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"text\": \"She have water.\"}"
   * Swap [She have water.] with your input sentence
