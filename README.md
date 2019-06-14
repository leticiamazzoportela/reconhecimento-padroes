# Processamento de sinais biológicos
## Descrição
Repositório destinado aos projetos da disciplina de Reconhecimento de Padrões, cujo foco é o processamento de sinais biológicos.

## Instruções
1. Faça o clone deste repositório
2. Execute os comandos:
    ```
    virtualenv -p python3.7 .
    source ./bin/activate
    ```
3. Instale as dependências necessárias no ambiente virtual
    ```
    pip install numpy scipy matplotlib scikit-learn jupyter mne keras pandas
    ```
4. Inicie o jupyter
    ```
    cd src && jupyter notebook
    ```

## Estrutura do repositório
1. `eeg_dataset`: Notebooks com as análises para a base de dados [EEG Database Data Set](https://archive.ics.uci.edu/ml/datasets/EEG+Database)
2. `evocation_alpha`: Notebooks com as análises para os datasets com evocação do ritmo _alpha_