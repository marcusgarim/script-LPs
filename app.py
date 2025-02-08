from playwright.sync_api import sync_playwright
import os
import requests
from urllib.parse import urlparse, urljoin

# Define a pasta principal de saída
user_folder = os.path.expanduser("~")
main_output_dir = os.path.join(user_folder, "OneDrive - Nelogica", "Documentos", "Outros", "Traning", "swipe", "LPs-all-assets")
os.makedirs(main_output_dir, exist_ok=True)

# Lista de URLs para capturar
urls = [
    "https://lp.nelogica.com.br/pr-trf-lp-aws-profit",
    "https://lp.nelogica.com.br/cbt-nelogica",
    "https://lp.nelogica.com.br/pr-capt-lp-smart-summit"
]

def sanitize_filename(url):
    # Gera um nome de pasta seguro para Windows a partir da URL
    name = urlparse(url).netloc.replace(".", "_") + "_" + urlparse(url).path.strip("/").replace("/", "_")
    return "".join(c for c in name if c not in '<>:"/\\|?*')

def download_images(page, images_folder):
    # Encontra e baixa todas as imagens da página
    os.makedirs(images_folder, exist_ok=True)
    image_elements = page.query_selector_all("img")

    for idx, img in enumerate(image_elements):
        src = img.get_attribute("src")
        if not src:
            continue

        # Converte URLs relativas para absolutas
        src = urljoin(page.url, src)

        try:
            response = requests.get(src, stream=True, timeout=10)
            if response.status_code == 200:
                img_path = os.path.join(images_folder, f"image_{idx+1}.png")
                with open(img_path, "wb") as f:
                    f.write(response.content)
                print(f"Image saved: {img_path}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {src}: {e}")

def capture_page_data(url, browser):
    # Captura de tela, código-fonte e imagens de uma página da web
    page = browser.new_page()

    # Define a viewport para 1920x1080
    page.set_viewport_size({"width": 1920, "height": 1080})

    # Vai para a página e espera que ela carregue completamente
    page.goto(url, timeout=60000, wait_until="networkidle")

    # Espera tempo extra para elementos dinâmicos (opcional)
    page.wait_for_timeout(6000)  # 6 segundos

    # Cria uma subpasta para este site
    site_folder = os.path.join(main_output_dir, sanitize_filename(url))
    os.makedirs(site_folder, exist_ok=True)

    # Salva captura de tela de página inteira
    screenshot_path = os.path.join(site_folder, "screenshot.png")
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"Screenshot saved: {screenshot_path}")

    # Salva o código-fonte completo
    source_code_path = os.path.join(site_folder, "source.html")
    with open(source_code_path, "w", encoding="utf-8") as f:
        f.write(page.content())
    print(f"Source code saved: {source_code_path}")

    # Baixa todas as imagens
    images_folder = os.path.join(site_folder, "images")
    download_images(page, images_folder)

    page.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Executa totalmente em segundo plano
    for url in urls:
        capture_page_data(url, browser)
    browser.close()

print(f"All files saved inside {main_output_dir}")