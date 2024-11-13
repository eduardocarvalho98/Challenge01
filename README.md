# Chatbot da Dra. Jô

Este projeto tem como objetivo criar um chatbot utilizando Dialogflow para auxiliar a Dra. Jô no atendimento ao cliente, agendamentos e suporte geral. A solução integra inteligência artificial para processamento de linguagem natural (NLP) e uma arquitetura escalável para garantir segurança e eficiência.

## Integrantes

- Eduardo Carvalho Santos - RM559438
- Gustavo Rocha De Castro - RM5608318
- Jhonatan Salles - RM554190

## Arquitetura da Solução


![Diagrama de Arquitetura](https://i.imgur.com/qHqDIJD.png) <!-- Substitua pelo caminho do arquivo real do diagrama -->

### Descrição dos Componentes

1. **Interface de Usuário (Front-end)**: A interface é integrada com plataformas de mensagens, como WhatsApp, Telegram e site da Dra. Jô, permitindo interação direta dos usuários com o chatbot.
2. **Dialogflow (NLP)**: O Dialogflow atua como o “cérebro” do chatbot, interpretando as mensagens dos usuários e definindo as intenções para responder de forma precisa.
3. **Back-end (Flask)**: O back-end processa as requisições do usuário e integra o chatbot com sistemas adicionais de dados, tratando a lógica de negócio.
4. **Banco de Dados**: Armazena interações, registros de atendimento e dados relevantes para análise e aprimoramento contínuo.
5. **Infraestrutura na Nuvem (Google Cloud)**: Hospeda os serviços e proporciona escalabilidade conforme o volume de interações aumenta.

### Justificativa de Custos

| Componente                | Custo Mensal | Descrição                                              |
|---------------------------|--------------|--------------------------------------------------------|
| Dialogflow                | Gratuito (limite de 1000 interações/mês) | Gratuito para até 1000 interações mensais. |


## Resultados Esperados

Espera-se que a implementação do chatbot melhore o atendimento ao cliente, proporcionando respostas rápidas e automatizadas a dúvidas comuns, otimizando o tempo da equipe. Os benefícios incluem:
- **Agilidade no Atendimento**: Respostas em tempo real para dúvidas frequentes.
- **Economia de Custos**: Redução do tempo de atendimento humano.
- **Satisfação do Cliente**: Atendimento personalizado e imediato.
- **Escalabilidade**: Estrutura preparada para suportar picos de acesso.

## Prova de Funcionamento

Para demonstrar o funcionamento do chatbot, abaixo estão 4 prints de diferentes interações e respostas esperadas do sistema:

![Postman 1](https://i.imgur.com/ZhK8Fxa.png)
![Postman 2](https://i.imgur.com/aWSsX0R.png)
![Postman 3](https://i.imgur.com/mD2mqx4.png)
![Dialogflow Training Phrases](https://i.imgur.com/Ly1FSuo.png)


