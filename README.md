<div align="center">
    <h1>Github Trending API</h1>
    <i>🔗 API para o Trending Tops do Github</i>
</div>
<br/>

<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-%5E3.8-green" />
  <img alt="Framework" src="https://img.shields.io/badge/Framework-Flask-blue" />
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green" />
</div>
<br/>

---

### :electric_plug: Como rodar localmente

Clone o repositorio:

```sh
 git clone https://github.com/iorjunior/github_trending_api.git
```

Abra a pasta, e instale as dependencias:

```sh
 pip install requiriments.txt
```

Se estiver usando Poetry:

```sh
 poetry install
```

Rode usando:

```sh
 gunicorn "application:create_app()"
```

---

### :globe_with_meridians: Como fazer Deploy no Heroku

Instale a <a href="https://devcenter.heroku.com/articles/heroku-cli">CLI</a> do heroku, depois faço login:

```sh
 heroku login
```

Crie um novo projeto com:

```sh
 heroku create Nome_Da_Sua_Aplicacao
```

Adicione Python ao seu projeto:

```sh
 heroku buildpacks:add heroku/python
```

Envio o codigo para o heroku:

```sh
 git push heroku main
```

Observe o final do log, lá estara o link para sua aplicação.

✅ Deploy concluido 🎊 🎉.

---

### :blue_book: Documentação

Atualmente a API tem 2 endpoints e aceita a query: `since`:

| Endpoints             | Retorno                                   |
| --------------------- | ----------------------------------------- |
| /                     | Retorna o trending geral do Dia           |
| /?since=weekly        | Retorna o trending geral da Semana        |
| /python               | Retorna o trending da linguagem na Semana |
| /python?since=monthly | Retorna o trendind da linguagem no Mês    |

Exemplo de retorno:

```json
 [
    {
    "author": "public-apis",
    "avatar_url": "https://github.com/public-apis.png",
    "description": "A collective list of free APIs",
    "forks": 20506,
    "full_name": "public-apis/public-apis",
    "repo_name": "public-apis",
    "repo_url": "https://github.com/public-apis/public-apis",
    "stars": 178065
  },
  ...
 ]
```

---

### 📂 Sobre

O projeto surgiu da ausencia da API do Github de retornar dados da parte de Trending Tops.
Esta sendo usado `Requests` e `BeautifulSoup` para parte de Raspagem de dados e `Flask` para a API.

Se esse projeto te ajudou de alguma maneira deixe um ⭐ , sinta-se avontade para Contribuir!!

Nota: Esta não é uma API oficial do GitHub.
