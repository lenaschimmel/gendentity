# The backend server file. This is the entrypoint into the backend.

import logging

from flask import Flask, request

from suggest_fixes import SuggestFixes

app = Flask("Farnsworth")

# Global vars.
# If true, return a string. If false, return a json. This flag is useful
# for debugging when the client is a browser.
ONLY_RETURN_STRING = True

@app.route("/giveSentenceSuggestions")
def main():
    sentence = request.args.get("sentence")

    if not isinstance(sentence, unicode):
        logging.error("Server did not receive unicode.")
        # TODO(joelshor): Return an error object.
        return "Server did not receive unicode."

    if ONLY_RETURN_STRING: return str(SuggestFixes(sentence))
    else: return flask.jsonify(suggestions=SuggestFixes(sentence))


if __name__ == "__main__":
    app.run()