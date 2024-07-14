from flask import Flask, request, jsonify
from models import Project, Chapter

app = Flask(__name__)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    # ... Manipulação de solicitações para projetos ...

@app.route('/projects/<project_id>', methods=['GET', 'PUT', 'DELETE'])
def project(project_id):
    # ... Manipulação de solicitações para um projeto específico ...

@app.route('/projects/<project_id>/chapters', methods=['GET', 'POST'])
def chapters(project_id):
    # ... Manipulação de solicitações para capítulos de um projeto ...

if __name__ == "__main__":
    app.run(debug=True)
  
