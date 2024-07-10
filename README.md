# dataHelper
Creating face dataset

## Configuracoes
- instale o virtual env

`pip install virtualenv`

- se nao tiver um ambiente virtual, crie um:

`python -m venv venv`

- ative o seu ambiente virtual:

(linux): `source venv/bin/activate`

(windows): `\venv\Scripts\activate`

- instale as dependencias

`pip install -r requirements.txt`

## Como usar
- Crie duas pastas. Uma com o nome `faces/` e outra com nome `not_faces/`
- Rode o `gen_py`
- A cada set de fotos, ele tirara 10 fotos.
- Para cada set, voce precisa confirmar clicando qualquer tecla no terminal
- Inicialmente um frame azul ira aparecer na tela, aleatoriamente
- posicione seu rosto nesse frame azul, e espere ficar verde
- assim que ficar verde, ele tirara as 10 fotos em torno de ~5 segundos
- quando o frame ficar vermelho, significa que foi finalizado.
- Repita o processo quantas vezes quiser.

## Consideracoes
- tente fazer varias poses, luzes, caretas, inclinacoes de rostos
- tente em dias diferentes, ambientes diferentes

## Como contribuir
- zip as pastas `faces/` e `not_faces/`
- envie para: `scruz.josecarlos@gmail.com`

## Como irei utilizar
- Sera utilizado para incrementar um conjunto de dados de rostos para 
treianmento da minha rede neural `Kinho`. E futuramente, o modelo treinado
sera disponibilizado como um modulo de visao computacional, gracas a sua ajuda.

## Consideracoes finais
- as imagens serao armazenadas exclusivamente comigo, em meu armazenamento fisico, sem armazenamento em nuvem. E voce pode pedir a qualquer momento a
exclusao dos arquivos!

obrigado <3
