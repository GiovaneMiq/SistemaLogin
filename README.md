# SistemaLogin

SistemaLogin é uma aplicação desktop desenvolvida em **Python**, utilizando **CustomTkinter** para a interface gráfica e **SQLite3** para o armazenamento de dados. O projeto é distribuído como um executável para Windows, permitindo sua utilização sem a necessidade de instalar o Python.

## Requisitos

* Sistema operacional Windows.
* Não é necessário instalar dependências adicionais para executar o arquivo disponibilizado na pasta `dist`.

## Instalação

### Clonar o repositório

```bash
git clone https://github.com/GiovaneMiq/SistemaLogin
cd SistemaLogin
```

### Ou baixar o projeto

1. Acesse o repositório no GitHub.
2. Clique em **Code** → **Download ZIP**.
3. Extraia o conteúdo em uma pasta de sua preferência.

## Execução

O executável está localizado na pasta `dist`.

### Pelo Explorador de Arquivos

Abra a pasta `dist` e execute o arquivo `app.exe`.

### Pelo PowerShell

```powershell
cd .\dist\
.\app.exe
```

ou

```powershell
Start-Process .\app.exe
```

## Observações

* O executável foi compilado para o sistema operacional Windows.
* Caso o Windows exiba o aviso **"Windows protected your PC"**, selecione **More info** e, em seguida, **Run anyway**, desde que o arquivo tenha sido obtido diretamente deste repositório.
* Alguns antivírus podem bloquear executáveis gerados com PyInstaller. Se isso ocorrer, verifique se o arquivo foi colocado em quarentena e restaure-o.

## Solução de Problemas

### O programa não inicia

Execute o aplicativo pelo PowerShell para verificar possíveis mensagens de erro:

```powershell
cd .\dist\
.\app.exe
```

### Erro relacionado a DLLs

Em alguns computadores pode ser necessário instalar o **Microsoft Visual C++ Redistributable** para executar aplicações empacotadas com PyInstaller.

### O antivírus removeu o executável

Alguns antivírus podem identificar executáveis gerados com PyInstaller como suspeitos. Caso o arquivo tenha sido obtido diretamente deste repositório, restaure-o e adicione uma exceção no antivírus, se necessário.

## Tecnologias Utilizadas

* Python
* CustomTkinter
* SQLite3
* PyInstaller

## Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado.
