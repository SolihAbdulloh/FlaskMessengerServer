from flask import Flask
app = Flask('name')

@app.route('/')
def hello_world():
    return 'nima gap polvon oxshadimi keyin'

if __name__ == '__main__':
    app.run()
