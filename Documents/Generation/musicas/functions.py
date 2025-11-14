import csv 

file_path = "musicas/assets/musicas.csv"


def read_file():
    print('------------Lista de Musicas-----------------')
    try:
        #caminho do arquivo, operação, no exemplo read, e o tipo de encoding
        #arquivo_musica é um alias para essa instrução
        with open(file_path, "r", encoding="utf-8") as arquivo_musica:
            leitor = csv.reader(arquivo_musica)
            next(leitor) # para pular a primeira linha do arquivo
            for musica in leitor:
                if musica:
                    titulo,artista,ano,genero,duracao_segundos = musica
                    #Precisa incluir todos os cabeçalhos do arquivo
                print(f"Titulo {titulo} | Artista {artista} | Genero {genero} | Duração {duracao_segundos}" )
    except FileNotFoundError:
        print('erro')