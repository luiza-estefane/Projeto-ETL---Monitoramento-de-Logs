Monitoramento de Logs e Dasboard de observabilidade.

Objetivo do Projeto

Este projeto visa aprendizagem de ferramentas ETL desenhadado para simular, processar e monitorar logs de um sistema em tempo real. Capturando dados brutos, aplicando regras de separação por nível de severidade do Erro dos Logs e os disponibilizando  para consumo de um dashboard interativo.


O fluxo dos dados foi estruturado em 4 etapas principais:

1. Script para gerar logs em volume para simular um ambiente real de um sistema em Python.
2. banco de dados em container recebe a carga inicial, como se fosse um rascunho. (PostgreSQL)
3. Utilizando o Pentaho no processo de ETL o motor de integração lê os dados iniciais, aplica as regras condicionais para identificação de alertas críticos e carrega as informações nas tabelas finais.
4. Conectado diretamente ao Database, construção de um painel de observabilidade dos logs, contendo indicadores de volume de dados e KPIs das quantidades de logs. 

A infraestrutura deste projeto está estruturada em formato de Containers (Docker).

 Compatibilidade para replicação

Embora todo o desenvolvimento e finalização tenham sido executados nativamente em ambiente **Linux**. É possível executar todo o fluxo em outras OS **Windows** utilizando o Docker Desktop  e acionando o arquivo `Spoon.bat` do Pentaho PDI.

 Como Executar Localmente

 Pré-requisitos
* Docker e Docker Compose instalados.
* Python 3 e pacote `psycopg2-binary`.
* Java (para rodar o Pentaho PDI).
  
 Passo a Passo
1. Clone o repositório e configure as credenciais:
   * Crie um arquivo `.env` na raiz do projeto baseando-se no `.env.example`.
2. Suba a infraestrutura:
   ```bash
   docker-compose up -d
