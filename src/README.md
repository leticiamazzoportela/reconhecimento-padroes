# Processamento de sinais biológicos
## Descrição
Estes notebooks apresentam as análises para a base de dados [EEG Database Data Set](https://archive.ics.uci.edu/ml/datasets/EEG+Database)

## Estrutura
Para as análises do dataset `EEG Database Data Set`, este repositório foi organizado em 3 notebooks:
1. `load_eeg`: Neste notebook constam os métodos relativos a leitura de toda a base de dados, bem como alguns gráficos com a plotagem desses dados.
2. `pre_processing`: Este notebook apresenta os métodos relativos à etapa de pré-processamento do dataset, onde são aplicados gráficos nos domínios do tempo e da frequência que ajudaram na decisão de qual domínio atuar e qual classificador utilizar.
3. `neural_network`: Com base nas observações realizadas no notebook anterior, optou-se por realizar as análises no domínio do tempo e utilizar uma rede neural artificial como classificador. Dessa forma, este notebook traz os métodos relativos a aplicação da rede neural.