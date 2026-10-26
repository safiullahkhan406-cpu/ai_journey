import os
from flask import Flask, request, jsonify, render_template, session
from groq import Groq

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY")

if not app.secret_key:
    raise RuntimeError("FLASK_SECRET_KEY environment variable set karein.")

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

MAX_HISTORY = 20


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    if not client:
        return jsonify({
            "answer": "GROQ_API_KEY environment variable set nahi hai."
        }), 503

    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"answer": "Please apna sawal likhein."}), 400

    if len(message) > 4000:
        return jsonify({
            "answer": "Message 4000 characters se chhota rakhein."
        }), 400

    history = session.get("history", [])

    history = [
        item for item in history
        if isinstance(item, dict)
        and item.get("role") in ("user", "assistant")
        and isinstance(item.get("content"), str)
    ][-MAX_HISTORY:]

    history.append({
        "role": "user",
        "content": message
    })

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Safiullah AI Assistant. "
                        "Be helpful, respectful, and clear. "
                        "Answer in the same language and script as the user. "
                        "Use Roman Urdu when the user writes Roman Urdu. "
                        "Use English when the user writes English. "
                        "Do not invent personal facts."
                    )
                },
                *history
            ]
        )

        answer = response.choices[0].message.content

        history.append({
            "role": "assistant",
            "content": answer
        })

        session["history"] = history[-MAX_HISTORY:]

        return jsonify({"answer": answer})

    except Exception as error:
        print("CHAT ERROR:", repr(error))

        return jsonify({
            "answer": "Maazrat, jawab nahi mil saka. Dobara koshish karein."
        }), 500


@app.route("/new-chat", methods=["POST"])
def new_chat():
    session.pop("history", None)
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=False)
    