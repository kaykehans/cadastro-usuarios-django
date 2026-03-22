from .models import Usuario
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

#==========================
# View Para Cadastrar Usuario
#==========================

def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(senha) < 6:
            messages.error(request, 'A senha deve conter Pelo Menos 6 Caracteres')
            return redirect('cadastro')
        #Verifica se email ja existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este Email ja esta cadastrado')
            return redirect('cadastro')
        # Salvar no banco
        Usuario.objects.create(
            nome=nome,
            email=email,
            senha=make_password(senha)
            )
        

        if not nome or not email or not senha:
            messages.error(request, 'Preencha Todos Os Campos')
            return redirect('cadastro')
        
        
        messages.success(request, 'Usuario Cadastrado Com Sucesso')
        return redirect('cadastro')                #Continua na Pagina de Cadastro
    
    return render(request, 'usuarios/cadastro.html')

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios':usuarios})

def deletar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    messages.success(request, 'Usuario Deletado com Sucesso')
    return redirect('listar_usuarios')
  

