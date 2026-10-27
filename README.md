# Alien Invasion (Game2D)

Jogo 2D arcade desenvolvido em Python com **Pygame** para a disciplina de **Alta Qualidade em Software (AQS)**.

---

## 🎮 Como Jogar

Execute no terminal:

```powershell
cd Game2D\JogoAlien
python src/alien_invasion.py
```

### Controles
* **Setas (ou A / D):** Move a nave
* **Espaço:** Dispara projéteis
* **Q:** Sai do jogo

---

## 🧪 Testes e Relatórios

Estando na pasta `Game2D\JogoAlien`:

* **Rodar os testes:**
  ```powershell
  pytest
  ```

* **Gerar relatório HTML de testes:**
  ```powershell
  pytest --html=relatorio.html
  ```

* **Gerar relatório de cobertura (Coverage):**
  ```powershell
  coverage run -m pytest
  coverage html
  ```
  *(O relatório visual fica em `htmlcov/index.html`)*
