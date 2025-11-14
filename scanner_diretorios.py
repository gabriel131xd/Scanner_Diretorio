import requests
from urllib.parse import urljoin
import threading
from queue import Queue
import sys

URL = ""
ARQUIVO_WORDLIST = "common.txt"
NUMERO_THREADS = 15

cabecalho = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

bloqueio = threading.Lock()
fila = Queue()

def testar_url(url):
    try:
        r = requests.get(url, headers=cabecalho, timeout=7, allow_redirects=True)
        codigo = r.status_code
        
        if codigo in [200, 301, 302, 403]:
            with bloqueio:
                status = "EXISTE" if codigo in [200, 301, 302] else "PROIBIDO"
                print(f"[+] {status} ({codigo}): {url}")
    except:
        pass

def escanear_caminho(caminho):
    caminho = caminho.strip()
    if not caminho:
        return
    
    base = URL.rstrip("/") + "/"
    
    variacoes = []
    
    if '.' in caminho:
        variacoes.append(caminho)
    else:
        variacoes.append(caminho)
        variacoes.append(caminho + "/")
        variacoes.append(caminho.rstrip("/") + "/")
    
    for var in variacoes:
        url = urljoin(base, var)
        fila.put(url)  # Adiciona na fila para teste

def trabalhador():
    while True:
        url = fila.get()
        if url is None:
            break
        testar_url(url)
        fila.task_done()

def iniciar_threads():
    for i in range(NUMERO_THREADS):
        t = threading.Thread(target=trabalhador)
        t.daemon = True
        t.start()

def carregar_wordlist():
    try:
        with open(ARQUIVO_WORDLIST, "r", encoding="utf-8") as f:
            linhas = [l.strip() for l in f if l.strip() and not l.startswith("#")]
        
        print(f"[*] Carregando {len(linhas)} itens da wordlist...")
        
        for caminho in linhas:
            escanear_caminho(caminho)
            
        print(f"[*] {fila.qsize()} URLs na fila para teste.")
        
    except FileNotFoundError:
        print(f"[!] Arquivo '{ARQUIVO_WORDLIST}' não encontrado!")
        sys.exit(1)


if __name__ == "__main__":
    print(f"[*] INICIANDO ANALISE: {URL}\n")
    
    carregar_wordlist()
    iniciar_threads()
    
    fila.join()
    
    for _ in range(NUMERO_THREADS):
        fila.put(None)
    
    print("\n[!] ANALISE CONCLUIDA!")