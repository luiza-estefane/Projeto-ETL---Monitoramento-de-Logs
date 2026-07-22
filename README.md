Monitoramento de Logs e Dasboard de observabilidade.

Objetivo do Projeto

Este projeto visa aprendizagem de ferramentas ETL desenhadado para simular, processar e monitorar logs de um sistema em tempo real. Capturando dados bruto para aplicação de regras de separação por nível de severidade do Erro dos Logs e os disponibilizando  para consumo de um dashboard interativo.


O fluxo dos dados foi estruturado em 4 etapas principais:

1. Script para gerar logs em volume para simular um ambiente real de um sistema em Python.
2. banco de dados em container recebe a carga inicial, como se fosse um rascunho. (PostgreSQL)
3. Utilizando o Pentaho no processo de ETL para  aplicar as regras condicionais para identificação de alertas críticos e carregamento as informações nas tabelas finais.
4. Conectado diretamente ao Database, construção de um painel de observabilidade dos logs, contendo indicadores de volume de dados e KPIs das quantidades de logs. 

Para mais informações do projeto acesse a documentação em pdf do Projeto no Repositório. 



