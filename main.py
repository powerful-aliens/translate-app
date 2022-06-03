from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)
LANGS = [['zh-cn', 'chinese (simplified)'],
	['es', 'spanish'],
	['en', 'english'],
	['hi', 'hindi'],
	['bn', 'bengali'],
	['pt', 'portuguese'],
	['ru', 'russian'],
	['ja', 'japanese'],
	['pa', 'punjabi'],
	['vi', 'vietnamese'],
	['mr', 'marathi'],
	['te', 'telugu'],
	['tr', 'turkish'],
	['ko', 'korean'],
	['fr', 'french'],
	['de', 'german'],
	['ta', 'tamil'],
	['ur', 'urdu'],
	['jw', 'javanese'],
	['it', 'italian']]
translator = Translator()


def gen_get_index_page():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Translate</title>
        </head>
        <body>
            <form action="" method="post">
                <p>
                    <label for="text">Text:</label>
                    <input type="text" name="text">
                </p>
                <p>
                    <input type="submit">
                </p>
            </form>
        </body>
        </html>
"""


def gen_post_index_page(mass):
    return render_template('index.html', languages_table=mass)


@app.route('/', methods=['post', 'get'])
def index():
    try:
        if request.method == 'POST':
            text = request.form.get('text')
            res = []
            for lang in LANGS:
                res.append([lang[1], translator.translate(text, dest=lang[0]).text])
            return gen_post_index_page(res)
        else:
            return gen_get_index_page()
    except:
        return "You are so smart that you caused a server error"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
