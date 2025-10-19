# MD5 CRacker

> Projeto muito simples em Python para tentar encontrar a senha original dado um hash MD5 usando uma wordlist. Feito apenas para fins educacionais, testes forenses em ambientes autorizados e recuperação de senhas em arquivos de autoria própria.

---

# Visão geral

Script em Python que percorre uma lista de palavras (`wordlist.txt`) e compara o MD5 de cada palavra com um hash alvo informado pelo usuário. Se encontrar correspondência, exibe a senha descoberta.

**Objetivos:**

* Projeto didático para aprender sobre hashing e técnicas básicas de *brute-force* com wordlists.
* Ferramenta minimalista para recuperação de senhas próprias em casos autorizados.
* Escalonar o projeto com o tempo, conforme necessidade.

---

# Pré-requisitos

* Python 3.8 ou superior.
* Sistema com memória e CPU compatíveis com o tamanho da sua wordlist.
* `wordlist.txt` no mesmo diretório do script ou modifique o caminho e nome no código.

Nenhuma dependência externa é necessária para o script fornecido, pois necessita apenas da biblioteca padrão (`hashlib`).

---

# Argumentos

Segue a lista de argumentos e parâmetros para utilizar no terminal:

> **--wordlist**: Caminho do arquivo de wordlist, por padrão o valor é "wordlist.txt"  
> **--encoding**: Tipo de codificação para leitura do arquivo da wordlist, por padrão o valor é "utf-8"

---

# Como estender / suportar outros hashes

O script atual usa `hashlib.md5(...)`. Para suportar SHA256 ou outro algoritmo, substitua pela função apropriada:

**Exemplo para SHA-256:**

```python
import hashlib

hashlib.sha256(palavra.encode(encoding)).hexdigest()
```

**Ou, de forma genérica usando `hashlib.new()`:**

```python
alg = "sha256"  # ou "md5", "sha1", ...
digest = hashlib.new(alg, palavra.encode(encoding)).hexdigest()
```

Se estender, também é recomendável:

* Validar o comprimento/formatos do hash alvo.
* Fornecer `--alg` como argumento de linha de comando.
