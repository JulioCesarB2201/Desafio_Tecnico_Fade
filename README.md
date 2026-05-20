# Desafio Técnico-Fade
Processo seletivo Fade-UFPE

# Lesson Plan Manager API

API REST para gerenciamento de planos de aula com geração assistida por IA.

---

# Funcionalidades

- CRUD completo de planos de aula
- Geração automática de planos com IA
- Documentação Swagger
- Suporte com Docker
- Testes automatizados com Pytest
- Banco de dados SQLite
- Arquitetura em camadas

---

# Tecnologias Utilizadas

- Python
- Flask
- SQLAlchemy
- SQLite
- Pytest
- Docker
- Swagger / Flasgger
- OpenRouter API

---

# Estrutura do Projeto

```txt
app/
├── ai/
├── config/
├── database/
├── errors/
├── models/
├── repositories/
├── routes/
├── services/
```

---

# Instalação

## Clonar repositório

```bash
git clone <url_repositorio>
cd lesson-plan-manager/backend
```

---

## Criar ambiente virtual

```bash
python -m venv venv
```

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Variáveis de Ambiente

Crie um arquivo:

```txt
.env
```

Exemplo:

```env
DATABASE_URL=sqlite:///lesson_plans.db
OPENROUTER_API_KEY=sua_chave
```

---

# Executando a Aplicação

```bash
python run.py
```

API:

```txt
http://127.0.0.1:5000
```

Swagger:

```txt
http://127.0.0.1:5000/apidocs
```

---

# Docker

## Build da aplicação

```bash
docker compose build
```

---

## Executar containers

```bash
docker compose up
```

---

# Executando os Testes

```bash
pytest
```

---

# Principais Endpoints

## Health Check

```http
GET /health
```

---

## Criar plano de aula

```http
POST /plans
```

---

## Buscar todos os planos

```http
GET /plans
```

---

## Buscar plano por ID

```http
GET /plans/<id>
```

---

## Atualizar plano

```http
PUT /plans/<id>
```

---

## Remover plano

```http
DELETE /plans/<id>
```

---

## Gerar plano com IA

```http
POST /plans/generate
```

Exemplo:

```json
{
    "topic": "TCP/IP"
}
```

---

# Integração com IA

A aplicação integra provedores externos de LLM através da OpenRouter API.

Também foi implementado um sistema de fallback mockado para garantir estabilidade durante desenvolvimento e testes, mesmo em casos de indisponibilidade da IA externa.

---

# Melhorias Futuras

- Autenticação JWT
- Paginação
- Deploy em nuvem
- Suporte PostgreSQL
- Tasks assíncronas
- Cache
- Rate limiting

---

# Autor

Julio Cesar Barbosa da Silva