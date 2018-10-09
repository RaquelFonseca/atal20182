# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
            if alist:
                    left = [x for x in alist if x > alist[0]]
                    right = [x for x in alist if x < alist[0]]
                    if len(left) > 1:
                            left = retorna_matriculas_decrescente(left)
                    if len(right) > 1:
                             right = retorna_matriculas_decrescente(right)
                    return left + [alist[0]] * alist.count(alist[0]) + right
            return []

print retorna_matriculas_decrescente([3, 8, 1])
