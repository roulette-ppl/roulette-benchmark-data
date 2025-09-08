# README
## You can view the latest Benchmark results summary [here](https://roulette-ppl.github.io/roulette-benchmark-data/)


# workflow diagram

```mermaid
graph TD
  %% Nodes
  U([User]):::actor
  RC[roulette-copy]:::repo
  RBD[roulette-benchmark-data]:::repo
  GP[[GitHub Pages]]:::web

  A1((Generate JSON results)):::action
  A2((Generate plots + Scribble docs)):::action
  A3((Deploy site)):::action

  %% Flows
  U -- commit --> RC
  RC -- on commit --> A1 --> RBD
  RBD -- on commit --> A2 --> RBD
  RBD -- on success --> A3 --> GP

  %% Legend
  subgraph Legend
    L1([Actor]):::actor
    L2[Repository]:::repo
    L3((Action)):::action
    L4[[Website]]:::web
  end

  %% Styles
  classDef actor fill:#1f77b4,color:#fff,stroke:#333,stroke-width:2px
  classDef repo fill:#444,color:#fff,stroke:#000,stroke-width:2px
  classDef action fill:#999,color:#fff,stroke:#222,stroke-dasharray: 3 3
  classDef web fill:#228B22,color:#fff,stroke:#000

```