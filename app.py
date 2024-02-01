from flask import Flask, request, jsonify

app = Flask(__name__)

movie_list = [
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
def movies():
    if request.method == 'GET':
        if len(movie_list) > 0:
            return jsonify(movie_list)
        else:
            return 'No Movies Found', 404  
        
    if request.method == 'POST':
        m_id = movie_list[-1]['id'] + 1
        m_director = request.form['director']  
        m_lang = request.form['language']
        m_title = request.form['title']

        new_movie = {
            'id': m_id,
            'director': m_director,
            'language': m_lang,
            'title': m_title,
        }

        movie_list.append(new_movie)
        return jsonify(movie_list), 201
    
@app.route('/movies/<int:id>', methods=['GET', 'PUT', 'DELETE'])  
def single_movie(id):
    if request.method == 'GET':
        for movie in movie_list:
            if movie['id'] == id:
                return jsonify(movie)

    if request.method == "PUT":
        for movie in movie_list:
            if movie['id'] == id:
                movie['director'] = request.form['director']
                movie['language'] = request.form['language']
                movie['title'] = request.form['title']  
                
                updated_movie = {
                    'id': id,
                    'director': movie['director'],
                    'language': movie['language'],
                    'title': movie['title'],
                }
                return jsonify(updated_movie)
            
    if request.method == "DELETE":
        for index, movie in enumerate(movie_list):
            if movie['id'] == id:
                movie_list.pop(index)
                return jsonify(movie_list)
            

if __name__ == "__main__":
    app.run()
