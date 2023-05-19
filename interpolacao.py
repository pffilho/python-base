email_tmpl = """
    Olá, %(nome)s
    Tem interesse em comprar %(produto)s?
    Este produto é ótimo para resolver %(texto)s
    Apenas %(quantidade)d disponíveis!
    Preço promocional %(preco).2f
"""

clientes = ["Paulo", "Daniana", "Gabriella"]

for cliente in clientes:
    print(
            email_tmpl
            %{
                "nome": cliente,
                "produto": "Shampoo",
                "texto":"Deixar os cabelos lisos e soltos",
                "quantidade":1,
                "preco":18.76
             }
        )
   
   