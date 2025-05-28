from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome to My Flask Website!</h1>
        <p>This is the home page. Deployed using Docker and ECS.</p>
        <a href="/about">Go to About Page</a>
    '''

@app.route('/about')
def about():
    return '''
        <h1>About This Project</h1>
        <p>This is a demo website created using Flask, Docker, and deployed to AWS ECS.</p>
        <a href="/">Back to Home</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
