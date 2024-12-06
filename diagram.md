%%{init : {"theme" : "base", "themeVariables": { "primaryColor": "#ffcc00", "edgeLabelBackground":"#ffffff", "tertiaryColor": "#fff700", "primaryBorderColor": "#d9d9d9"}}}%%
graph TB
  %% Define modules and files
  subgraph patchwork
    subgraph steps
      direction TB
      A1[__init__.py]
      A2[README.md]
      subgraph GetTypescriptTypeInfo
        B1[typed.py]
        B2[package.json]
        B3[GetTypescriptTypeInfo.py]
        B4[tsconfig.json]
        B5[__init__.py]
        B6[README.md]
        B7[get_type_info.ts]
        B8[pnpm-lock.yaml]
      end
      subgraph ExtractCodeMethodForCommentContexts
        C1[typed.py]
        C2[ExtractCodeMethodForCommentContexts.py]
        C3[__init__.py]
        C4[README.md]
      end
      subgraph ScanDepscan
        D1[typed.py]
        D2[__init__.py]
        D3[ScanDepscan.py]
        D4[README.md]
      end
      subgraph PreparePR
        E1[typed.py]
        E2[PreparePR.py]
        E3[__init__.py]
        E4[README.md]
      end
      subgraph SimplifiedLLMOnce
        F1[typed.py]
        F2[__init__.py]
        F3[README.md]
        F4[SimplifiedLLMOnce.py]
      end
      subgraph ExtractCode
        G1[typed.py]
        G2[ExtractCode.py]
        G3[__init__.py]
        G4[README.md]
      end
      subgraph ModifyCodeOnce
        H1[typed.py]
        H2[ModifyCodeOnce.py]
        H3[__init__.py]
        H4[README.md]
      end
      subgraph AnalyzeImpact
        I1[typed.py]
        I2[AnalyzeImpact.py]
        I3[__init__.py]
        I4[README.md]
      end
      subgraph SimplifiedLLM
        J1[typed.py]
        J2[__init__.py]
        J3[README.md]
        J4[SimplifiedLLM.py]
      end
      subgraph Combine
        K1[typed.py]
        K2[Combine.py]
        K3[__init__.py]
        K4[README.md]
      end
      subgraph ExtractPackageManagerFile
        L1[typed.py]
        L2[TestExtractPackageManagerFile.py]
        L3[__init__.py]
        L4[README.md]
        L5[ExtractPackageManagerFile.py]
      end
      subgraph CallAPI
        M1[typed.py]
        M2[__init__.py]
        M3[CallAPI.py]
        M4[README.md]
      end
      subgraph ReadFile
        N1[typed.py]
        N2[ReadFile.py]
        N3[__init__.py]
        N4[README.md]
      end
      subgraph QueryEmbeddings
        O1[typed.py]
        O2[__init__.py]
        O3[QueryEmbeddings.py]
        O4[README.md]
      end
      subgraph FixIssue
        P1[typed.py]
        P2[FixIssue.py]
        P3[__init__.py]
        P4[README.md]
      end
      subgraph GenerateCodeRepositoryEmbeddings
        Q1[typed.py]
        Q2[__init__.py]
        Q3[README.md]
        Q4[filter_lists.py]
        Q5[GenerateCodeRepositoryEmbeddings.py]
      end
      subgraph CreateIssueComment
        R1[typed.py]
        R2[CreateIssueComment.py]
        R3[__init__.py]
        R4[README.md]
      end
      subgraph ExtractModelResponse
        S1[typed.py]
        S2[__init__.py]
        S3[ExtractModelResponse.py]
        S4[README.md]
      end
      subgraph ReadPRDiffs
        T1[typed.py]
        T2[ReadPRDiffs.py]
        T3[__init__.py]
        T4[README.md]
      end
      subgraph FilterBySimilarity
        U1[typed.py]
        U2[FilterBySimilarity.py]
        U3[__init__.py]
        U4[README.md]
      end
      subgraph CreateIssue
        V1[CreateIssue.py]
        V2[typed.py]
        V3[__init__.py]
        V4[README.md]
      end
      subgraph PR
        W1[typed.py]
        W2[__init__.py]
        W3[README.md]
        W4[PR.py]
      end
      subgraph JoinList
        X1[typed.py]
        X2[__init__.py]
        X3[README.md]
        X4[JoinList.py]
      end
      subgraph ExtractCodeContexts
        Y1[typed.py]
        Y2[ExtractCodeContexts.py]
        Y3[__init__.py]
        Y4[README.md]
      end
      subgraph CommitChanges
        Z1[typed.py]
        Z2[__init__.py]
        Z3[README.md]
        Z4[CommitChanges.py]
      end
      subgraph ScanSemgrep
        AA1[typed.py]
        AA2[ScanSemgrep.py]
        AA3[__init__.py]
        AA4[README.md]
      end
      subgraph CallLLM
        BB1[typed.py]
        BB2[__init__.py]
        BB3[README.md]
        BB4[CallLLM.py]
      end
      subgraph ReadPRs
        CC1[typed.py]
        CC2[__init__.py]
        CC3[README.md]
        CC4[ReadPRs.py]
      end
      subgraph ModifyCode
        DD1[typed.py]
        DD2[__init__.py]
        DD3[ModifyCode.py]
        DD4[README.md]
      end
      subgraph GenerateEmbeddings
        EE1[typed.py]
        EE2[__init__.py]
        EE3[README.md]
        EE4[GenerateEmbeddings.py]
      end
      subgraph ReadIssues
        FF1[typed.py]
        FF2[__init__.py]
        FF3[README.md]
        FF4[ReadIssues.py]
      end
      subgraph ExtractDiff
        GG1[typed.py]
        GG2[ExtractDiff.py]
        GG3[__init__.py]
        GG4[README.md]
      end
      subgraph LLM
        HH1[typed.py]
        HH2[LLM.py]
        HH3[__init__.py]
        HH4[README.md]
      end
      subgraph CallCode2Prompt
        II1[typed.py]
        II2[TestCallCode2Prompt.py]
        II3[__init__.py]
        II4[README.md]
        II5[CallCode2Prompt.py]
      end
      subgraph CreatePRComment
        JJ1[typed.py]
        JJ2[__init__.py]
        JJ3[CreatePRComment.py]
        JJ4[README.md]
      end
      subgraph SlackMessage
        KK1[typed.py]
        KK2[__init__.py]
        KK3[README.md]
        KK4[SlackMessage.py]
      end
      subgraph CreatePR
        LL1[typed.py]
        LL2[CreatePR.py]
        LL3[__init__.py]
        LL4[README.md]
      end
      subgraph PreparePrompt
        MM1[typed.py]
        MM2[__init__.py]
        MM3[README.md]
        MM4[PreparePrompt.py]
      end
    end
  end

  %% Define dependencies
  A1 --> A2

  B1 --> B2
  B1 --> B3
  B1 --> B4
  B1 --> B5
  B1 --> B6
  B1 --> B7
  B1 --> B8

  C1 --> C2
  C1 --> C3
  C1 --> C4

  D1 --> D2
  D1 --> D3
  D1 --> D4

  E1 --> E2
  E1 --> E3
  E1 --> E4

  F1 --> F2
  F1 --> F3
  F1 --> F4

  G1 --> G2
  G1 --> G3
  G1 --> G4

  H1 --> H2
  H1 --> H3
  H1 --> H4

  I1 --> I2
  I1 --> I3
  I1 --> I4

  J1 --> J2
  J1 --> J3
  J1 --> J4

  K1 --> K2
  K1 --> K3
  K1 --> K4

  L1 --> L2
  L1 --> L5
  L2 --> L3
  L2 --> L4

  M1 --> M3
  M1 --> M4
  M2 --> M3

  N1 --> N2
  N1 --> N3
  N1 --> N4

  O1 --> O2
  O1 --> O3
  O1 --> O4

  P1 --> P2
  P1 --> P3
  P1 --> P4

  Q1 --> Q2
  Q1 --> Q3
  Q1 --> Q4
  Q1 --> Q5

  R1 --> R2
  R1 --> R3
  R1 --> R4

  S1 --> S2
  S1 --> S3
  S1 --> S4

  T1 --> T2
  T1 --> T3
  T1 --> T4

  U1 --> U2
  U1 --> U3
  U1 --> U4

  V1 --> V2
  V1 --> V3
  V1 --> V4

  W1 --> W2
  W1 --> W3
  W1 --> W4

  X1 --> X2
  X1 --> X3
  X1 --> X4

  Y1 --> Y2
  Y1 --> Y3
  Y1 --> Y4

  Z1 --> Z2
  Z1 --> Z3
  Z1 --> Z4

  AA1 --> AA2
  AA1 --> AA3
  AA1 --> AA4

  BB1 --> BB2
  BB1 --> BB3
  BB1 --> BB4

  CC1 --> CC2
  CC1 --> CC3
  CC1 --> CC4

  DD1 --> DD2
  DD1 --> DD3
  DD1 --> DD4

  EE1 --> EE2
  EE1 --> EE3
  EE1 --> EE4

  FF1 --> FF2
  FF1 --> FF3
  FF1 --> FF4

  GG1 --> GG2
  GG1 --> GG3
  GG1 --> GG4

  HH1 --> HH2
  HH1 --> HH3
  HH1 --> HH4

  II1 --> II2
  II1 --> II3
  II1 --> II4
  II1 --> II5

  JJ1 --> JJ2
  JJ1 --> JJ3
  JJ1 --> JJ4

  KK1 --> KK2
  KK1 --> KK3
  KK1 --> KK4

  LL1 --> LL2
  LL1 --> LL3
  LL1 --> LL4

  MM1 --> MM2
  MM1 --> MM3
  MM1 --> MM4
