# Web Page Capture

Este projeto utiliza o Playwright para capturar telas, códigos-fonte e imagens de páginas da web específicas.

## Requisitos

- Python 3
- Playwright
- Requests

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/marcusgarim/script-LPs.git
    cd script-LPs
    ```

2. Instale as dependências:
    ```sh
    pip install playwright requests
    playwright install
    ```

## Uso

1. Edite a lista de URLs no arquivo [app.py](http://_vscodecontentref_/1) conforme necessário:
    ```python
    urls = [
        "https://lp.nelogica.com.br/pr-trf-lp-aws-profit",
        "https://lp.nelogica.com.br/cbt-nelogica",
        "https://lp.nelogica.com.br/pr-capt-lp-smart-summit"
    ]
    ```

2. Execute o script:
    ```sh
    python app.py
    ```

3. Os arquivos capturados serão salvos na pasta [LPs-all-assets](http://_vscodecontentref_/2) dentro do diretório especificado no script.

## Funcionalidades

- Captura de tela de página inteira
- Salvamento do código-fonte completo
- Download de todas as imagens da página

## Estrutura do Código

- `sanitize_filename(url)`: Gera um nome de pasta seguro para Windows a partir da URL.
- `download_images(page, images_folder)`: Encontra e baixa todas as imagens da página.
- `capture_page_data(url, browser)`: Captura de tela, código-fonte e imagens de uma página da web.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.