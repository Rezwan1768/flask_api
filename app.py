from flask import Flask, request, jsonify

app = Flask(__name__)

movies = [
    {
        'id': 1,
        'director': 'Christopher Nolan',
        'language': 'English',
        'title': 'Inception'
    },
    {
        'id': 2,
        'director': 'Quentin Tarantino',
        'language': 'English',
        'title': 'Pulp Fiction'
    },
    {
        'id': 3,
        'director': 'Steven Spielberg',
        'language': 'English',
        'title': 'Jurassic Park'
    },
    {
        'id': 4,
        'director': 'Hayao Miyazaki',
        'language': 'Japanese',
        'title': 'Spirited Away'
    },
    {
        'id': 5,
        'director': 'Martin Scorsese',
        'language': 'English',
        'title': 'The Wolf of Wall Street'
    },
    {
        'id': 6,
        'director': 'Francis Ford Coppola',
        'language': 'English',
        'title': 'The Godfather'
    }
]

@app.route('/movies', methods=['GET', 'POST'])
def movie_list():
    if request.method == 'GET':
        if len(movies) > 0:
            return jsonify(movies)
        else:
            return 'No Movies Found', 404  # Added 'return'

    if request.method == 'POST':
        m_id = movies[-1]['id'] + 1
        m_author = request.form['author']
        m_lang = request.form['language']
        m_title = request.form['title']

        new_movie = {
            'id': m_id,
            'author': m_author,
            'language': m_lang,
            'title': m_title,
        }

        movies.append(new_movie)
        return jsonify(movies), 201
    
if __name__ == "__main__":
    app.run()