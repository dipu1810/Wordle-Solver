from flask import Flask, render_template, request, jsonify
from solver import isValid, generateGuesses

# -----------------------
# Load wordlist
# -----------------------
with open("valid-wordle-words.txt", "r") as f:
    WORDLIST = [line.strip() for line in f.readlines()]

app = Flask(__name__)

# Keep track of current state
current_wordlist = WORDLIST.copy()
curr_guess = "tares"


@app.route("/")
def index():
    return render_template("index.html", guess=curr_guess)


@app.route("/next", methods=["POST"])
def next_guess():
    global current_wordlist, curr_guess

    data = request.get_json()
    feedback = data.get("feedback")

    # filter wordlist based on feedback
    current_wordlist = [
        w for w in current_wordlist if isValid(curr_guess, feedback, w)
    ]

    if len(current_wordlist) == 1:
        return jsonify({
            "message": f"The word is {current_wordlist[0]}",
            "done": True
        })

    # pick next guess
    curr_guess = generateGuesses(current_wordlist)

    return jsonify({
        "next_guess": curr_guess,
        "possible_count": len(current_wordlist),
        "possible_words": current_wordlist[:20]  # just show first 20
    })


if __name__ == "__main__":
    app.run(debug=True)
