graph TD
  A[README.md] --> B[__init__.py]

  B --> C[ScanSemgrep]
  B --> D[ModifyCode]
  B --> E[PreparePrompt]
  B --> F[CallLLM]
  B --> G[Combine]
  B --> H[CreateIssueComment]
  B --> I[CommitChanges]
  B --> J[PreparePR]
  B --> K[ReadPRs]
  B --> L[GetTypescriptTypeInfo]
  B --> M[QueryEmbeddings]
  B --> N[ExtractCodeContexts]
  B --> O[GenerateCodeRepositoryEmbeddings]
  B --> P[ExtractDiff]
  B --> Q[FixIssue]
  B --> R[CallCode2Prompt]
  B --> S[SimplifiedLLMOnce]
  B --> T[CreatePRComment]
  B --> U[ReadPRDiffs]
  B --> V[AnalyzeImpact]
  B --> W[FilterBySimilarity]
  B --> X[ExtractCode]
  B --> Y[CreatePR]
  B --> Z[LLM]
  B --> AA[PR]
  B --> AB[ExtractCodeMethodForCommentContexts]
  B --> AC[CreateIssue]
  B --> AD[ModifyCodeOnce]
  B --> AE[ExtractModelResponse]
  B --> AF[JoinList]
  B --> AG[SimplifiedLLM]
  B --> AH[CallAPI]
  B --> AI[ExtractPackageManagerFile]
  B --> AJ[ReadIssues]
  B --> AK[ReadFile]
  B --> AL[ScanSonar]
  B --> AM[GenerateEmbeddings]
  B --> AN[ScanDepscan]
  B --> AO[SlackMessage]

  subgraph ScanSemgrep
    C1[typed.py]
    C2[README.md]
    C3[__init__.py]
    C4[ScanSemgrep.py]
  end

  subgraph ModifyCode
    D1[typed.py]
    D2[README.md]
    D3[__init__.py]
    D4[ModifyCode.py]
  end

  subgraph PreparePrompt
    E1[typed.py]
    E2[README.md]
    E3[__init__.py]
    E4[PreparePrompt.py]
  end

  subgraph CallLLM
    F1[typed.py]
    F2[README.md]
    F3[__init__.py]
    F4[CallLLM.py]
  end

  subgraph Combine
    G1[typed.py]
    G2[README.md]
    G3[__init__.py]
    G4[Combine.py]
  end

  subgraph CreateIssueComment
    H1[typed.py]
    H2[README.md]
    H3[__init__.py]
    H4[CreateIssueComment.py]
  end

  subgraph CommitChanges
    I1[typed.py]
    I2[README.md]
    I3[__init__.py]
    I4[CommitChanges.py]
  end

  subgraph PreparePR
    J1[typed.py]
    J2[README.md]
    J3[PreparePR.py]
    J4[__init__.py]
  end

  subgraph ReadPRs
    K1[typed.py]
    K2[README.md]
    K3[__init__.py]
    K4[ReadPRs.py]
  end

  subgraph GetTypescriptTypeInfo
    L1[typed.py]
    L2[pnpm-lock.yaml]
    L3[README.md]
    L4[__init__.py]
    L5[package.json]
    L6[get_type_info.ts]
    L7[tsconfig.json]
    L8[GetTypescriptTypeInfo.py]
  end

  subgraph QueryEmbeddings
    M1[typed.py]
    M2[QueryEmbeddings.py]
    M3[README.md]
    M4[__init__.py]
  end

  subgraph ExtractCodeContexts
    N1[typed.py]
    N2[README.md]
    N3[__init__.py]
    N4[ExtractCodeContexts.py]
  end

  subgraph GenerateCodeRepositoryEmbeddings
    O1[GenerateCodeRepositoryEmbeddings.py]
    O2[typed.py]
    O3[README.md]
    O4[filter_lists.py]
    O5[__init__.py]
  end

  subgraph ExtractDiff
    P1[typed.py]
    P2[README.md]
    P3[__init__.py]
    P4[ExtractDiff.py]
  end

  subgraph FixIssue
    Q1[typed.py]
    Q2[README.md]
    Q3[__init__.py]
    Q4[FixIssue.py]
  end

  subgraph CallCode2Prompt
    R1[typed.py]
    R2[CallCode2Prompt.py]
    R3[README.md]
    R4[__init__.py]
    R5[TestCallCode2Prompt.py]
  end

  subgraph SimplifiedLLMOnce
    S1[typed.py]
    S2[README.md]
    S3[__init__.py]
    S4[SimplifiedLLMOnce.py]
  end

  subgraph CreatePRComment
    T1[typed.py]
    T2[CreatePRComment.py]
    T3[README.md]
    T4[__init__.py]
  end

  subgraph ReadPRDiffs
    U1[typed.py]
    U2[README.md]
    U3[__init__.py]
    U4[ReadPRDiffs.py]
  end

  subgraph AnalyzeImpact
    V1[typed.py]
    V2[AnalyzeImpact.py]
    V3[README.md]
    V4[__init__.py]
  end

  subgraph FilterBySimilarity
    W1[typed.py]
    W2[README.md]
    W3[__init__.py]
    W4[FilterBySimilarity.py]
  end

  subgraph ExtractCode
    X1[typed.py]
    X2[README.md]
    X3[__init__.py]
    X4[ExtractCode.py]
  end

  subgraph CreatePR
    Y1[typed.py]
    Y2[CreatePR.py]
    Y3[README.md]
    Y4[__init__.py]
  end

  subgraph LLM
    Z1[typed.py]
    Z2[LLM.py]
    Z3[README.md]
    Z4[__init__.py]
  end

  subgraph PR
    AA1[typed.py]
    AA2[README.md]
    AA3[PR.py]
    AA4[__init__.py]
  end

  subgraph ExtractCodeMethodForCommentContexts
    AB1[typed.py]
    AB2[README.md]
    AB3[__init__.py]
    AB4[ExtractCodeMethodForCommentContexts.py]
  end

  subgraph CreateIssue
    AC1[typed.py]
    AC2[README.md]
    AC3[__init__.py]
    AC4[CreateIssue.py]
  end

  subgraph ModifyCodeOnce
    AD1[typed.py]
    AD2[ModifyCodeOnce.py]
    AD3[README.md]
    AD4[__init__.py]
  end

  subgraph ExtractModelResponse
    AE1[typed.py]
    AE2[ExtractModelResponse.py]
    AE3[README.md]
    AE4[__init__.py]
  end

  subgraph JoinList
    AF1[typed.py]
    AF2[JoinList.py]
    AF3[README.md]
    AF4[__init__.py]
  end

  subgraph SimplifiedLLM
    AG1[typed.py]
    AG2[README.md]
    AG3[__init__.py]
    AG4[SimplifiedLLM.py]
  end

  subgraph CallAPI
    AH1[typed.py]
    AH2[README.md]
    AH3[__init__.py]
    AH4[CallAPI.py]
  end

  subgraph ExtractPackageManagerFile
    AI1[typed.py]
    AI2[README.md]
    AI3[__init__.py]
    AI4[ExtractPackageManagerFile.py]
    AI5[TestExtractPackageManagerFile.py]
  end

  subgraph ReadIssues
    AJ1[typed.py]
    AJ2[README.md]
    AJ3[__init__.py]
    AJ4[ReadIssues.py]
  end

  subgraph ReadFile
    AK1[typed.py]
    AK2[README.md]
    AK3[__init__.py]
    AK4[ReadFile.py]
  end

  subgraph ScanSonar
    AL1[typed.py]
    AL2[README.md]
    AL3[ScanSonar.py]
    AL4[__init__.py]
  end

  subgraph GenerateEmbeddings
    AM1[typed.py]
    AM2[GenerateEmbeddings.py]
    AM3[README.md]
    AM4[__init__.py]
  end

  subgraph ScanDepscan
    AN1[typed.py]
    AN2[README.md]
    AN3[__init__.py]
    AN4[ScanDepscan.py]
  end

  subgraph SlackMessage
    AO1[typed.py]
    AO2[SlackMessage.py]
    AO3[README.md]
    AO4[__init__.py]
  end
