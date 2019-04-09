# Processamento de sinais biológicos
## Descrição
Repositório destinado aos projetos da disciplina de Reconhecimento de Padrões, cujo foco é o processamento de sinais biológicos.
Para as análises, foi utilizada a base de dados [EEG Database Data Set](https://archive.ics.uci.edu/ml/datasets/EEG+Database)

## Instruções
1. Faça o clone deste repositório
2. Execute os comandos:
    ```
    virtualenv -p python3.7 .
    source ./bin/activate
    ```
3. Instale as dependências necessárias no ambiente virtual
    ```
    pip install numpy scipy matplotlib scikit-learn jupyter mne
    ```
4. Inicie o jupyter
    ```
    cd src && jupyter notebook
    ```

6 funcoes
10 trials p/ cada funcao
64 canais de eletrodos p/ cada trial
256 0 a 255 milivolt p/ cada canal
