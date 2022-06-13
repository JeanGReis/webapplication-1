# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request, redirect
from uuid import uuid4
import csv

app = Flask(__name__)

prisioneiros = [
    {'id': 1, 'nome': 'Túlio', 'crime': 'Assasinato de duas jovens', 'tempo': '10 anos'},
    {'id': 2, 'nome': 'Roberto', 'crime': 'Furto de carro', 'tempo': '4 anos'},
    {'id': 3, 'nome': 'Ibere', 'crime': 'Amar demais', 'tempo': 'Prisão perpétua'},
]

@app.route('/')
def index():
    with open('Prisioneiros.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out,['id','nome','crime','tempo'])
        escritor.writeheader()
        escritor.writerows(prisioneiros)
    with open('Prisioneiros.csv','rt') as file_out:
        leitor = csv.DictReader(file_out)
    return render_template('index.html', prisioneiros=prisioneiros)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome'] 
    crime = request.form['crime']      
    tempo = request.form['tempo']
    prisioneiros.append({"id": uuid4(), "nome": nome, "crime": crime, "tempo": tempo})
    return render_template('index.html', prisioneiros=prisioneiros)

@app.route('/delete/<id>')
def delete(id):
    for prisioneiro in prisioneiros:
        if ( id == str(prisioneiro['id'])):
            i = prisioneiros.index(prisioneiro)
            del prisioneiros[i]
            return redirect('/')

@app.route('/edit/<id>')
def edit(id):
    for prisioneiro in prisioneiros:
        if id == str(prisioneiro['id']):
            return render_template('update.html',prisioneiro = prisioneiro)

@app.route('/edit/prisioneiro/<id>', methods=['POST'])
def salvar_edicao(id):
    for prisioneiro in prisioneiros:
        if (id == str(prisioneiro['id'])):
            i = prisioneiros.index(prisioneiro)
            id_modificado = prisioneiro['id']
    upNome = request.form['nome']
    upCrime = request.form['crime']
    upTempo = request.form['tempo']
    prisioneiros[i] = {'id':id_modificado,'nome':upNome,'crime':upCrime,'tempo':upTempo}
    return redirect('/')

app.run(debug=True)

