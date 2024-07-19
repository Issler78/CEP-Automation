import pandas as pd

# Dados fictícios de 50 pessoas
nomes = [
    'João Silva', 'Maria Oliveira', 'Pedro Santos', 'Ana Costa', 'Lucas Pereira', 'Fernanda Lima', 'Carlos Alves', 'Juliana Souza', 
    'Paulo Gonçalves', 'Mariana Ferreira', 'Bruno Rodrigues', 'Tatiana Mendes', 'Eduardo Campos', 'Bianca Moreira', 
    'Rodrigo Cardoso', 'Gabriela Barbosa', 'Marcelo Teixeira', 'Renata Martins', 'Ricardo Dias', 'Luana Rocha', 
    'Antonio Ramos', 'Camila Nogueira', 'Felipe Almeida', 'Carolina Azevedo', 'Roberto Pinto', 'Larissa Borges', 
    'Gustavo Moura', 'Débora Vieira', 'Sérgio Macedo', 'Adriana Silva', 'Rafael Lopes', 'Patrícia Cardoso', 'Daniel Ribeiro', 
    'Vanessa Duarte', 'Bruno Nascimento', 'Beatriz Melo', 'Fábio Fernandes', 'Lorena Carvalho', 'André Lima', 'Priscila Castro', 
    'Thiago Almeida', 'Luciana Campos', 'Miguel Azevedo', 'Sofia Martins', 'Renato Lima', 'Lara Souza', 'Leonardo Gomes', 
    'Isabela Santos', 'Vitor Costa', 'Carla Oliveira'
]

enderecos = [
    'Rua A, 123', 'Av. B, 456', 'Travessa C, 789', 'Praça D, 101', 'Rua E, 234', 'Av. F, 567', 'Rua G, 890', 'Praça H, 111', 
    'Rua I, 222', 'Av. J, 333', 'Travessa K, 444', 'Praça L, 555', 'Rua M, 666', 'Av. N, 777', 'Rua O, 888', 'Praça P, 999', 
    'Rua Q, 1010', 'Av. R, 1111', 'Rua S, 1212', 'Praça T, 1313', 'Rua U, 1414', 'Av. V, 1515', 'Travessa W, 1616', 
    'Praça X, 1717', 'Rua Y, 1818', 'Av. Z, 1919', 'Rua AA, 2020', 'Praça BB, 2121', 'Rua CC, 2222', 'Av. DD, 2323', 
    'Rua EE, 2424', 'Praça FF, 2525', 'Rua GG, 2626', 'Av. HH, 2727', 'Travessa II, 2828', 'Praça JJ, 2929', 'Rua KK, 3030', 
    'Av. LL, 3131', 'Rua MM, 3232', 'Praça NN, 3333', 'Rua OO, 3434', 'Av. PP, 3535', 'Rua QQ, 3636', 'Praça RR, 3737', 
    'Rua SS, 3838', 'Av. TT, 3939', 'Rua UU, 4040', 'Praça VV, 4141', 'Rua WW, 4242', 'Rua S, 3403'
]

ceps = [
    '01001-000', '02002-000', '03003-000', '04004-000', '05005-000', '06006-000', '07007-000', '08008-000', 
    '09009-000', '10010-000', '11011-000', '12012-000', '13013-000', '14014-000', '15015-000', '16016-000', 
    '17017-000', '18018-000', '19019-000', '20020-000', '21021-000', '22022-000', '23023-000', '24024-000', 
    '25025-000', '26026-000', '27027-000', '28028-000', '29029-000', '30030-000', '31031-000', '32032-000', 
    '33033-000', '34034-000', '35035-000', '36036-000', '37037-000', '38038-000', '39039-000', '40040-000', 
    '41041-000', '42042-000', '43043-000', '44044-000', '45045-000', '46046-000', '47047-000', '48048-000', 
    '49049-000', '50050-000'
]

# Criação do DataFrame
dados = {
    'Nome': nomes,
    'Endereço': enderecos,
    'CEP': ceps
}

df = pd.DataFrame(dados)

# Salvar a planilha Excel
df.to_excel('enderecos.xlsx', index=False)
