import logging
from flask import Flask, request, jsonify, render_template
from groq import Groq

# ---------------- Flask App ----------------
app = Flask(__name__)

# ---------------- Logging Setup ----------------
logging.basicConfig(
    filename="llama_chat1.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ---------------- Initialize Groq Client ----------------
client = Groq(api_key="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")

logging.info("=== Flask Chat API started ===")

# ---------------- LLM Models ----------------
MODELS = {
    "model_1": "llama-3.1-8b-instant",
    "model_2": "llama-3.1-8b-instant",
    "model_3": "llama-3.3-70b-versatile",
}

AGGREGATOR_MODEL = "llama-3.3-70b-versatile"


# ---------------- Home Page ----------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------- Chat Endpoint ----------------
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        logging.info(f"User: {prompt}")

        responses = {}

        # ---------- Call 3 LLMs ----------
        for name, model in MODELS.items():
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            reply = completion.choices[0].message.content.strip()
            responses[name] = reply

        # ---------- Aggregator ----------
        aggregator_prompt = f"""
You are an Aggregator AI.

Combine the following answers into one high-quality response.

User Question:
{prompt}

Model 1:
{responses['model_1']}

Model 2:
{responses['model_2']}

Model 3:
{responses['model_3']}
"""

        final_completion = client.chat.completions.create(
            model=AGGREGATOR_MODEL,
            messages=[
                {"role": "system", "content": "You are an expert AI aggregator."},
                {"role": "user", "content": aggregator_prompt}
            ]
        )

        final_answer = final_completion.choices[0].message.content.strip()

        logging.info(f"FINAL RESPONSE: {final_answer}")

        return jsonify({
            "answer": final_answer
        })

    except Exception as e:
        logging.error(str(e))
        return jsonify({"error": str(e)}), 500


# ---------------- Run Flask Server ----------------
if __name__ == "__main__":
    app.run(debug=True)
