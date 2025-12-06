# API Descarte Integrador

Este projeto é um serviço web construído com Flask que atua como backend para um aplicativo móvel de descarte consciente de resíduos. Ele fornece informações atualizadas sobre pontos de coleta para que o app possa sincronizar a base de dados local.

Por padrão o servidor roda em `0.0.0.0:5000`. Para desenvolvimento com auto-reload, execute com `debug=True` ou use o Flask CLI em modo de desenvolvimento.

## Instruções

1. **Clonar repositório:**

   ```
   git clone https://github.com/akpizutti/descarte-integrador-server
   cd descarte-integrador-server
   ```

2. **Criar ambiente virtual:**

   ```
   python -m venv venv
   ```

3. **Ativar ambiente virtual:**

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Instalar dependências:**

   ```
   pip install -r requirements.txt
   ```

5. **Executar:**
   ```
   python run.py
   ```

## Endpoints da API

- **GET /api/v1/version**

  - Retorna a versão atual da base de dados (um inteiro/timestamp) que o servidor fornece para os clientes verificarem se precisam atualizar os dados locais.

- **GET /api/v1/locations**

  - Retorna a lista completa de locais de coleta de resíduos (array de objetos). Cada objeto possui os campos: `id`, `nome`, `endereco`, `lat`, `lng` e `tipo`.

## Observações

- O arquivo `locations_data.json` contém a base de dados e deve estar em `app/utils/locations_data.json` por padrão. Se o arquivo não for encontrado ao iniciar o servidor, o serviço exibirá um aviso e carregará uma base vazia.
- Em ambiente de desenvolvimento, ative o auto-reload para ver mudanças no código sem reiniciar manualmente. Alterações no arquivo JSON exigem reinício do servidor, pois o arquivo é carregado na inicialização.
