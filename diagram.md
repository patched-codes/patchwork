graph TD
    A[patchwork/steps] --> B[README.md]
    A --> C[__init__.py]
    A --> D[ExtractCodeMethodForCommentContexts]
    A --> E[PreparePrompt]
    A --> F[ExtractCodeContexts]
    A --> G[ReadPRs]
    A --> H[SlackMessage]
    A --> I[CallAPI]
    A --> J[SendEmail]
    A --> K[CallLLM]
    A --> L[FileAgent]
    A --> M[AnalyzeImpact]
    A --> N[ExtractModelResponse]
    A --> O[CreateIssue]
    A --> P[ScanSemgrep]
    A --> Q[PR]
    A --> R[CallSQL]
    A --> S[ModifyCodeOnce]
    A --> T[GetTypescriptTypeInfo]
    A --> U[BrowserUse]
    A --> V[CreateIssueComment]
    A --> W[ReadPRDiffs]
    A --> X[SimplifiedLLM]
    A --> Y[CommitChanges]
    A --> Z[ZohoDeskAgent]
    A --> AA[ExtractPackageManagerFile]

    %% ExtractCodeMethodForCommentContexts Section
    D --> D1[__init__.py]
    D --> D2[typed.py]
    D --> D3[README.md]
    D --> D4[ExtractCodeMethodForCommentContexts.py]
    
    %% PreparePrompt Section
    E --> E1[__init__.py]
    E --> E2[typed.py]
    E --> E3[README.md]
    E --> E4[PreparePrompt.py]

    %% ExtractCodeContexts Section
    F --> F1[__init__.py]
    F --> F2[typed.py]
    F --> F3[README.md]
    F --> F4[ExtractCodeContexts.py]

    %% ReadPRs Section
    G --> G1[__init__.py]
    G --> G2[typed.py]
    G --> G3[README.md]
    G --> G4[ReadPRs.py]

    %% SlackMessage Section
    H --> H1[__init__.py]
    H --> H2[typed.py]
    H --> H3[README.md]
    H --> H4[SlackMessage.py]
    
    %% CallAPI Section
    I --> I1[__init__.py]
    I --> I2[typed.py]
    I --> I3[README.md]
    I --> I4[CallAPI.py]

    %% SendEmail Section
    M --> M1[__init__.py]
    M --> M2[typed.py]
    M --> M3[README.md]
    M --> M4[SendEmail.py]

    %% CallLLM Section
    P --> P1[__init__.py]
    P --> P2[typed.py]
    P --> P3[README.md]
    P --> P4[CallLLM.py]

    %% ReadFile Section
    F --> D1
    F --> E2
    F --> G4

    %% AnalyzeImpact Section
    M --> M5[typed.py]
    M --> M6[README.md]
    M --> M7[AnalyzeImpact.py]

    %% ExtractModelResponse Section
    N --> N8[typed.py]
    N --> N9[README.md]
    N --> N1

    %% CreateIssue Section
    O --> M1
    O --> D5[typed.py]
    O --> G1

    %% ScanSemgrep Section
    P --> P9

    %% PreparePR Section
    Q --> Q5[typed.py]
    Q --> R9
    Q --> J3

    %% ReadIssues Section
    R --> M7
    U --> U8[typed.py]
    T --> T10[tsconfig.json]
    T --> T11[package.json]
    T --> T12[get_type_info.ts]
    H --> H13

    %% PreparePR Section
    U --> U8
    P --> P3

