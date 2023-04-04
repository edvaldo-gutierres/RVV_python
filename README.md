Projeto de Banco de Dados em Um Sistema de Remuneração Variável do Setor de Vendas de Eletrônicos

Resumo
Este relatório apresenta o projeto do banco de dados em um sistema de Remuneração Variável do Setor de Vendas de Eletrônicos. Contém no relatório atividades de especificação do minimundo. Conterá a análise de requisitos, projeto conceitual, projeto lógico e projeto físico proposto.

1 Introdução
Atualmente, temos uma expansão de mercado no seguimento de eletrônicos com uma maior demanda e fluxo de funcionários. Isso se deve, principalmente, ao desenvolvimento acelerado da tecnologia de informação e comunicação, além do aumento da conectividade da população com o uso de computadores/tablets e telefonia. Portanto, com o objetivo de tornar o gerenciamento empresarial mais prático, sobretudo de estabelecimentos de varejo de equipamentos tecnológicos, foi criado um sistema de remuneração variável através de um banco de dados relacional.

Dessa maneira, o presente trabalho tem como intuito facilitar o controle de comissionamento dos funcionários dentro da organização através de um banco de dados contendo apenas 7 entidades. Para aplicação do sistema de remuneração variável (RVV), o atual projeto dispõe-se de uma especificação de minimundo, contemplando de forma textual o conceito lógico do banco de dados proposto. Além disso, foram realizados as Análises de Requisitos, Projeto Conceitual apresentando a modelagem dos dados e graficamente o diagrama entidade-relacionamento (DER), o Projeto Lógico de banco de dados, incluindo diagrama relacional que representa forma gráfica as definições dos objetos para implementação do banco de dados, e, por fim o Projeto Físico apresentando todos os script’s necessários para materialização do banco de dados.

2 Especificação do Minimundo
Essa seção apresenta a descrição textual de minimundo do RVV (v1.0), um banco de dados para um sistema de gerenciamento de cálculo de remuneração variável de vendas (RVV) em empresas de vendas, considerando como pilares de cálculos a meta e o realizado de indicadores estratégicos conforme a visão de negócio proposta por sua diretoria comercial.

A priori os indicadores e suas metas são categorizados por departamento e cargos, onde o departamento são lotados por funcionários vendedores que atendem a um tipo de varejo (key account, mercado interno e e-commerce), e os cargos classificador por senioridades (sênior, pleno e júnior). Os indicadores são identificados por sequencia numérica exclusiva (id) e contem os atributos código e descrição dos departamentos e cargos, e suas datas de início e fim de vigência.

Os funcionários são identificados por seu número de exclusivo de matrícula e contém
os atributos nome, CPF, sexo, departamento, data de nascimento, cargo e salário. Cada
vendedor será lotado em apenas um departamento e estará relacionando em apenas um
cargo.
A comissão será calculada com base nos indicadores, onde o índice de produtividade
(I.P.) será medido pela divisão do realizado pela meta. O valor da comissão se dará pelo
produto do I.P. e a base de cálculo. A base de cálculo é categorizada por cargos de gestão
e operacional, onde a definição se dá por percentual do salário e percentual do faturamento
bruto, respectivamente.

2.1 Requisitos Funcionais
Vários usuários chaves demandarão diversas operações de manipulação de dados
sobre diferentes procedimentos do banco de dados. O usuário Diretor demandará consulta
de recuperação de dados dos cálculos da comissão de supervisores e vendedores.
O usuário Gerente demandará atualização e recuperação de dados de metas e
resultado de vendas dos supervisores, bem como a inclusão e/ou exclusão de cadastro de
novos colaboradores.
O usuário Supervisor demandará atualização e recuperação de dados de metas, e
resultado e cálculo da RVV (comissão) e de seus vendedores subordinados
O usuário administrativo demandará a inclusão e/ou exclusão de cadastro de novos
colaboradores, atualização dos registros de funcionários, além da manipulação do cálculo
para a RVV.
O usuário vendedor poderá visualizar as metas e os seus resultados, além dos cálculos
da remuneração variável.
O usuário Geral poderá visualizar os cálculos da remuneração variável.