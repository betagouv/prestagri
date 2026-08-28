---
title: Add Catala rule
description: How catala is included in python
---

Catala 1.2 :

necessary fix :

- list.map(function) => map(function, list)
- fold_left


    def somme(l:List[Money]) -> Money:
    def _somme__1(total:Money, x:Money):
        return (total + x)
    somme__1 = Function(_somme__1)
    return l.fold_left(somme__1, Money('0.00'))


    -> sum(l)
