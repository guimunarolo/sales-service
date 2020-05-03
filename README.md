# sales-service

[![CircleCI](https://circleci.com/gh/guimunarolo/sales-service.svg?style=shield)](https://circleci.com/gh/guimunarolo/sales-service)
[![codecov](https://codecov.io/gh/guimunarolo/sales-service/branch/master/graph/badge.svg)](https://codecov.io/gh/guimunarolo/sales-service)

Serviço simples feito em Fast API para controle de vendas com lógica de cashback.


## Instalação

Com o `pipenv` já instalado e seu ambiente já iniciado:

```bash
$ pipenv install --dev
$ cp local.env .env
```


## Iniciando o Serviço

Basta rodar o comando abaixo substituindo o valor do token:

```bash
$ EXTERNAL_API_TOKEN={token} make run
```

> O valor do token pode ser substituido no arquivo .env

Agora você tem seu serviço rodando em [http://localhost:8000](http://localhost:8000)


## Documentação

Com o serviço instanciado em sua máquina, basta acessar [http://localhost:8000/docs](http://localhost:8000/docs)


## Rodando os testes

```bash
$ make test
```
