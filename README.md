# 🕹️ Jogos em Python com Pygame — Pong & Acerte o Alvo

Repositório com dois jogos desenvolvidos em **Python 3.12** usando **Pygame**:
- **Pong**: clássico de duas raquetes e uma bola.
- **Acerte o Alvo**: clique no alvo que aparece aleatoriamente e some pontos.

> Projeto didático para praticar eventos, colisões, animações e renderização no Pygame.

---

## 📦 Requisitos

- **Python 3.12**
- **Pygame**
  
Instale as dependências:
```bash
pip install pygame
````

> Se quiser, crie um ambiente virtual antes: `python -m venv .venv` e ative:
>
> * Windows: `.venv\Scripts\activate`
> * macOS/Linux: `source .venv/bin/activate`

---

## ▶️ Como executar

Clone este repositório e rode os jogos:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPO.git
cd SEU-REPO
```

### Pong

```bash
python pong.py
```

**Controles**

* Jogador 1: **W / S**
* Jogador 2: **↑ / ↓**
* FPS: 60

### Acerte o Alvo

```bash
python acerte_alvo.py
```

* Clique no alvo branco para somar pontos.
* O alvo muda de posição aleatoriamente a cada acerto.
* Opcional: som de acerto (`efect.wav`) na mesma pasta do script.

> 💡 Se o áudio falhar, o jogo continua normalmente (o código trata a ausência do mixer/arquivo).

---

## 🧱 Estrutura sugerida do repositório

```
📁 SEU-REPO
├── acerte_alvo.py
├── pong.py
├── README.md
└── (opcional) assets/
    ├── imagens/
    │   ├── pong.png
    │   └── acerte_o_alvo.png
    └── sons/
        └── acerto.wav
```

---

## 🖼️ Prints dos jogos

> Substitua as imagens abaixo quando fizer seus prints (salve em `assets/imagens/` ou ajuste os caminhos).

### Pong
<img width="1273" height="646" alt="image" src="https://github.com/user-attachments/assets/b34a4f13-13f6-4766-998b-73292c9aaf23" />


### Acerte o Alvo
<img width="1268" height="602" alt="image" src="https://github.com/user-attachments/assets/0a6db0fc-e10a-42e0-aaa9-b2785385f18c" />


---

## 🧩 Tecnologias & conceitos

* Python 3.12
* Pygame
* Eventos de teclado e mouse
* Colisão (Rect & colliderect)
* Renderização de texto (fonte)
* Loop de jogo, FPS e relógio (`Clock`)
* Organização por classes (Raquete, Bola)

---

## 🛠️ Solução de problemas (FAQ)

* **Nada acontece ao rodar pelo VS Code**
  Use *Run Python File in Terminal* (o `input()`/interação só funciona no **Terminal**, não no painel **Output**).

* **Erro com som no Acerte o Alvo**
  Verifique se `acerto.wav` existe e está na mesma pasta do script ou em `assets/sons/` (e atualize o caminho no código).
  Se o mixer não inicializar, o jogo segue sem som.

* **A janela fecha imediatamente**
  Confira se não há exceções no terminal. Rode via terminal para ver mensagens.

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**.
Sinta-se à vontade para usar, estudar e modificar.

---

## 👤 Autor

**Nando Mendes**
GitHub: [https://github.com/SEU-USUARIO](https://github.com/SEU-USUARIO)
LinkedIn: [https://www.linkedin.com/in/SEU-USUARIO](https://www.linkedin.com/in/SEU-USUARIO)




