"""Motor matemático do Relation Quest — Grupo 08."""

import ast


def ler_entrada(texto_conjunto, texto_relacao):
    """Transforma o que foi digitado em dois conjuntos Python."""
    try:
        valores_a = ast.literal_eval(texto_conjunto.strip())
        valores_r = ast.literal_eval(texto_relacao.strip())
        A = set(valores_a)
        R = set(valores_r)
    except (ValueError, SyntaxError, TypeError):
        raise ValueError("Use A = {1,2,3} e R = {(1,1),(1,2)}. Para vazio, use {}.")

    if any(type(numero) is not int for numero in A):
        raise ValueError("O conjunto A deve conter somente números inteiros.")

    for par in R:
        if not isinstance(par, tuple) or len(par) != 2:
            raise ValueError("Cada elemento de R deve ser um par: (a,b).")
        a, b = par
        if type(a) is not int or type(b) is not int:
            raise ValueError("Os pares de R devem conter números inteiros.")
        if a not in A or b not in A:
            raise ValueError(f"O par ({a},{b}) é inválido: os números precisam estar em A.")

    return A, R


def reflexiva(A, R):
    for a in sorted(A):
        if (a, a) not in R:
            return False, f"Falta o par ({a},{a})."
    return True, "Todos os elementos possuem o par (a,a)."


def simetrica(R):
    for a, b in sorted(R):
        if (b, a) not in R:
            return False, f"Existe ({a},{b}), mas falta ({b},{a})."
    return True, "Todo par possui seu correspondente invertido."


def antissimetrica(R):
    for a, b in sorted(R):
        if a != b and (b, a) in R:
            return False, f"Existem ({a},{b}) e ({b},{a}), com {a} diferente de {b}."
    return True, "Não há pares opostos entre elementos diferentes."


def transitiva(R):
    for a, b in sorted(R):
        for c, d in sorted(R):
            if b == c and (a, d) not in R:
                return False, f"Existem ({a},{b}) e ({c},{d}), mas falta ({a},{d})."
    return True, "Todas as ligações exigidas pela transitividade existem."


def verificar(A, R):
    return {
        "REFLEXIVA": reflexiva(A, R),
        "SIMÉTRICA": simetrica(R),
        "ANTISSIMÉTRICA": antissimetrica(R),
        "TRANSITIVA": transitiva(R),
    }


if __name__ == "__main__":
    A = {1, 2, 3}
    R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
    for nome, (resultado, motivo) in verificar(A, R).items():
        print(f"{nome}: {'SIM' if resultado else 'NÃO'} - {motivo}")
