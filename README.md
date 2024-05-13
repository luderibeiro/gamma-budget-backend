# Repositório para o back-end do projeto Gamma-Budget

Este é o repositório do Backend do grupo 2.3 da turma de 2024/1 do Ricardo Chaim de EPS.

## Sobre o projeto

Este é um projeto feito em Django(5.0) está Dockerizado e segue os princípios da arquitetura limpa (Clean Architecture). Ele utiliza uma estrutura sólida para o desenvolvimento de uma aplicação backend e a API do projeto GammaBudget.

## Como Usar

Siga estes passos para executar o projeto:

1.  **Clonar o Repositório:**

        git clone git@gitlab.com:fga-eps-rmc/fintech/grupo3/fintech-grupo3/back-end.git

    ou com HTTPS:

        git clone https://gitlab.com/fga-eps-rmc/fintech/grupo3/fintech-grupo3/back-end.git

2.  **Configurar o Ambiente:**

-   Crie um arquivo `.env` na pasta dotenv_files do projeto e adicione as configurações necessárias, como chaves de API, configurações de banco de dados, etc.

`obs.: Existe um arquivo .env-example para gruiar o processo.`

1.  **Executar o Docker Compose:**

        docker-compose up --build

`obs.: a tag --build deve ser executada somente a primeira vez que o projeto for instalado ou quando houverem alterações nos arquivos de build.`

5. **Acessar a Aplicação:**
   A aplicação estará disponível em `http://localhost:8000`.
   Caso queira acessar a pagina admin basta acessar `http://localhost:8000/admin/`

**Tratamento de erros**

-   No caso de receber este erro: `PermissionError: [Errno 13] Permission denied: '/data/web/static/admin'`
    Rodar o seguinte comando:

        sudo chown -R user:group data

`obs.: Mude "user" por seu usuário local da máquina e "group" pelo grupo do usuário`

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Basta seguir estes passos:

1. Faça um fork do repositório.
2. Crie um branch para a sua contribuição: `git checkout -b feature/nova-feature`.
3. Faça suas alterações e faça commit: `git commit -m 'Adiciona nova feature'`.
4. Faça push para o branch: `git push origin feature/nova-feature`.
5. Abra um pull request.

**Recomendações**

-   Para contribuição recomendamos que seja criado uma virtualenv na pasta raiz para que te ajude no desenvolvimento.
-
