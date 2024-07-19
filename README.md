# Automação de Busca de CEPs com Python

Uma automação feita com Python 3, que irá automatizar uma tarefa repetitiva.
O script irá ler uma tabela excel, e com base nos CEPs que estão nela, irá pesquisar no site https://www2.correios.com.br/sistemas/buscacep/BuscaCepEndereco.cfm e irá salvar os dados de cidade e estado em uma nova tabela excel, além dos dados já presentes na tabela anterior.

### Passo a passo da automação

* Abrir a tabela endereços e selecionar a página onde esta localizado os dados.
* Criar uma nova tabela com os campos: Nome, Endereço, CEP (estes já presentes na tabela anterior), Cidade e Estado.
* Entrar no site https://www2.correios.com.br/sistemas/buscacep/BuscaCepEndereco.cfm para a busca de CEPs.
* Ler os dados da tabela de endereços.
* Para cada endereço na tabela, digitar o cep no campo de busca do site e clicar no botão de busca.
* Salvar os dados de Cidade e Estado do resultado da busca no site e salvá-los na nova tabela com as outras informações.

### Requisitos

* Python 3
* Instalar as bibliotecas **Openpyxl** e **Selenium**.

**No Windows e Linux:**
```sh
pip install openpyxl, selenium
```
**No Mac**
```sh
pip3 install openpyxl, selenium
```
