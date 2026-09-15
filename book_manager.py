"""
Módulo de gerenciamento de livros - código inicial
Prática de leitura e escrita de JSON e criação de testes unitários.
Nenhuma dependência externa é necessária (apenas a biblioteca padrão do Python).
"""

import json
from typing import List, Dict, Any, Optional


def load_books(filepath: str) -> List[Dict[str, Any]]:
    """
    Carrega uma lista de livros a partir de um arquivo JSON.

    Args:
    filepath: Caminho para o arquivo JSON.

    Returns:
    Lista de dicionários de livros.

    Raises:
    FileNotFoundError: Se o arquivo não existir.
    json.JSONDecodeError: Se o arquivo não for um JSON válido.
    ValueError: Se os dados JSON do nível superior não forem uma lista.

    """
    # TODO 1: Abra o arquivo usando encoding="utf-8" e um gerenciador de contexto.
    # TODO 2: Analise o conteúdo JSON usando json.load().
    # TODO 3: Verifique se os dados carregados são uma lista; caso contrário, lance ValueError("Catalog must be a list").
    # TODO 4: Retorne a lista de livros.


    # 1. Abre o arquivo para leitura usando UTF-8
    with open(filepath, "r", encoding="utf-8") as f:
        
        # 2. Carrega o conteúdo JSON
        data = json.load(f)

    # 3. Verifica se o conteúdo é uma lista
    if not isinstance(data, list):
        raise ValueError("Catalog must be a list")

    # 4. Retorna a lista de livros
    return data



def save_books(filepath: str, books: List[Dict[str, Any]], indent: int = 4) -> None:
    """
    Salva uma lista de livros em um arquivo JSON.

    Args:
    filepath: Caminho onde o arquivo JSON será gravado.
    books: Lista de dicionários de livros a serem serializados.
    indent: Nível de indentação para formatação do arquivo (padrão 4).

    Raises:
    TypeError: Se books não for uma lista.
    """
    # TODO 1: Verifique se books é uma instância de list. Caso contrário, lance TypeError("books must be a list").
    # TODO 2: Abra o arquivo para escrita usando encoding="utf-8" e um gerenciador de contexto.
    # TODO 3: Escreva os livros no arquivo usando json.dump(..., indent=indent).

    if not isinstance(books, list):
        raise TypeError("books must be a list")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=indent)

def add_book(
    books: List[Dict[str, Any]],
    book_id: int,
    title: str,
    author: str,
    year: int,
    genres: List[str],
    is_available: bool = True
) -> Dict[str, Any]:
    """
    Adiciona um novo livro à lista de livros.

    Args:
        books: Lista existente de dicionários de livros.
        book_id: ID inteiro e único do livro.
        title: Título do livro.
        author: Nome do autor.
        year: Ano de publicação.
        genres: Lista de gêneros.
        is_available: Status de disponibilidade (padrão True).

    Returns:
        O dicionário do livro recém-criado.

    Raises:
        ValueError: Se já existir um livro com book_id ou se o título estiver vazio.
    """
    # TODO 1: Verifique se title está vazio ou contém apenas espaços em branco. Nesse caso, lance ValueError("Title cannot be empty").
    # TODO 2: Verifique se algum livro em books já possui o book_id informado. Nesse caso, lance ValueError(f"Book with ID {book_id} already exists").
    # TODO 3: Construa o dicionário do livro com as chaves: "id", "title", "author", "year", "genres", "is_available".
    # TODO 4: Adicione o novo livro a books e retorne o dicionário do livro.
    
    if not title.strip():
        raise ValueError("Title cannot be empty")

    if any(book.get("id") == book_id for book in books):
        raise ValueError(f"Book with ID {book_id} already exists")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year,
        "genres": genres,
        "is_available": is_available,
    }
    books.append(book)
    return book


def find_books_by_genre(books: List[Dict[str, Any]], genre: str) -> List[Dict[str, Any]]:
    """
    Encontra todos os livros que pertencem a um gênero específico (sem diferenciar maiúsculas de minúsculas).

    Args:
        books: Lista de dicionários de livros.
        genre: Nome do gênero usado como filtro.

    Returns:
        Lista de dicionários dos livros correspondentes.
    """
    # TODO 1: Filtre a lista de livros em que algum gênero de book["genres"] corresponde
    #  a `genre` (comparação sem diferenciar maiúsculas de minúsculas).
    # TODO 2: Retorne a lista de livros correspondentes.
    normalized_genre = genre.casefold()
    return [
        book
        for book in books
        if any(book_genre.casefold() == normalized_genre for book_genre in book["genres"])
    ]


def calculate_average_year(books: List[Dict[str, Any]]) -> float:
    """
    Calcula o ano médio de publicação dos livros da lista.

    Args:
        books: Lista de dicionários de livros.

    Returns:
        Ano médio de publicação como um número de ponto flutuante. Retorna 0.0 se a lista estiver vazia.
    """
    # TODO 1: Se books estiver vazia, retorne 0.0.
    if not books:
        return 0.0
    # TODO 2: Calcule a soma do atributo "year" de todos os livros e divida pela quantid
    # ade.
    total_years = sum(book["year"] for book in books)

    year_average = float(total_years / len(books))
    # TODO 3: Retorne a média como um número de ponto flutuante.
    return year_average
