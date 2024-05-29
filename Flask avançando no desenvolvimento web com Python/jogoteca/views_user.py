from jogoteca import app,db
from flask import render_template, request, redirect,session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario, FormularioNovoUsuario
from flask_bcrypt import check_password_hash, generate_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario()
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

@app.route('/cadastro')
def cadastro():
    form = FormularioNovoUsuario()
    return render_template('cadastro.html', form=form)

@app.route('/novousuario', methods=['POST',])
def cadastrar():
    form = FormularioNovoUsuario()
    if not form.validate_on_submit():
        return redirect(url_for('cadastro'))
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    if usuario:
        flash('Nickname indisponível!')
        return redirect(url_for('cadastro'))
    elif form.senha.data != form.repetir_senha.data:
        flash('As senhas devem ser iguais!')
        return redirect(url_for('cadastro'))
    else:
        nome = form.nome.data
        nickname = form.nickname.data
        senha = generate_password_hash(form.senha.data).decode('utf-8')

        novo_usuario = Usuarios(nome=nome, nickname=nickname, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Novo usuário cadastrado com sucesso!')
        return redirect(url_for('index'))

