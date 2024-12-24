graph TD
  A[patchwork/steps/] --> B[README.md]
  A --> C[__init__.py]
  
  subgraph ScanSemgrep
    D[typed.py]
    E[README.md]
    F[__init__.py]
    G[ScanSemgrep.py]
  end

  subgraph ModifyCode
    H[typed.py]
    I[README.md]
    J[__init__.py]
    K[ModifyCode.py]
  end

  subgraph PreparePrompt
    L[typed.py]
    M[README.md]
    N[__init__.py]
    O[PreparePrompt.py]
  end

  subgraph CallLLM
    P[typed.py]
    Q[README.md]
    R[__init__.py]
    S[CallLLM.py]
  end

  subgraph Combine
    T[typed.py]
    U[Combine.py]
    V[README.md]
    W[__init__.py]
  end

  subgraph CreateIssueComment
    X[typed.py]
    Y[README.md]
    Z[__init__.py]
    AA[CreateIssueComment.py]
  end

  subgraph CommitChanges
    AB[typed.py]
    AC[README.md]
    AD[CommitChanges.py]
    AE[__init__.py]
  end

  subgraph PreparePR
    AF[typed.py]
    AG[README.md]
    AH[PreparePR.py]
    AI[__init__.py]
  end

  subgraph ReadPRs
    AJ[typed.py]
    AK[README.md]
    AL[__init__.py]
    AM[ReadPRs.py]
  end

  subgraph GetTypescriptTypeInfo
    AN[typed.py]
    AO[pnpm-lock.yaml]
    AP[README.md]
    AQ[__init__.py]
    AR[package.json]
    AS[get_type_info.ts]
    AT[tsconfig.json]
    AU[GetTypescriptTypeInfo.py]
  end

  subgraph QueryEmbeddings
    AV[typed.py]
    AW[QueryEmbeddings.py]
    AX[README.md]
    AY[__init__.py]
  end

  subgraph ExtractCodeContexts
    AZ[typed.py]
    BA[README.md]
    BB[__init__.py]
    BC[ExtractCodeContexts.py]
  end

  subgraph GenerateCodeRepositoryEmbeddings
    BD[GenerateCodeRepositoryEmbeddings.py]
    BE[typed.py]
    BF[README.md]
    BG[filter_lists.py]
    BH[__init__.py]
  end

  subgraph ExtractDiff
    BI[typed.py]
    BJ[README.md]
    BK[__init__.py]
    BL[ExtractDiff.py]
  end

  subgraph FixIssue
    BM[typed.py]
    BN[README.md]
    BO[__init__.py]
    BP[FixIssue.py]
  end

  subgraph CallCode2Prompt
    BQ[typed.py]
    BR[CallCode2Prompt.py]
    BS[README.md]
    BT[__init__.py]
    BU[TestCallCode2Prompt.py]
  end

  subgraph SimplifiedLLMOnce
    BV[typed.py]
    BW[README.md]
    BX[__init__.py]
    BY[SimplifiedLLMOnce.py]
  end

  subgraph CreatePRComment
    BZ[typed.py]
    CA[CreatePRComment.py]
    CB[README.md]
    CC[__init__.py]
  end

  subgraph ReadPRDiffs
    CD[typed.py]
    CE[README.md]
    CF[__init__.py]
    CG[ReadPRDiffs.py]
  end

  subgraph AnalyzeImpact
    CH[typed.py]
    CI[AnalyzeImpact.py]
    CJ[README.md]
    CK[__init__.py]
  end

  subgraph FilterBySimilarity
    CL[typed.py]
    CM[README.md]
    CN[__init__.py]
    CO[FilterBySimilarity.py]
  end

  subgraph ExtractCode
    CP[typed.py]
    CQ[README.md]
    CR[__init__.py]
    CS[ExtractCode.py]
  end

  subgraph CreatePR
    CT[typed.py]
    CU[CreatePR.py]
    CV[README.md]
    CW[__init__.py]
  end

  subgraph LLM
    CX[typed.py]
    CY[LLM.py]
    CZ[README.md]
    DA[__init__.py]
  end

  subgraph PR
    DB[typed.py]
    DC[README.md]
    DD[PR.py]
    DE[__init__.py]
  end

  subgraph ExtractCodeMethodForCommentContexts
    DF[typed.py]
    DG[README.md]
    DH[__init__.py]
    DI[ExtractCodeMethodForCommentContexts.py]
  end

  subgraph CreateIssue
    DJ[typed.py]
    DK[README.md]
    DL[__init__.py]
    DM[CreateIssue.py]
  end

  subgraph ModifyCodeOnce
    DN[typed.py]
    DO[ModifyCodeOnce.py]
    DP[README.md]
    DQ[__init__.py]
  end

  subgraph ExtractModelResponse
    DR[typed.py]
    DS[ExtractModelResponse.py]
    DT[README.md]
    DU[__init__.py]
  end

  subgraph JoinList
    DV[typed.py]
    DW[JoinList.py]
    DX[README.md]
    DY[__init__.py]
  end

  subgraph SimplifiedLLM
    DZ[typed.py]
    EA[README.md]
    EB[__init__.py]
    EC[SimplifiedLLM.py]
  end

  subgraph CallAPI
    ED[typed.py]
    EE[README.md]
    EF[__init__.py]
    EG[CallAPI.py]
  end

  subgraph ExtractPackageManagerFile
    EH[typed.py]
    EI[README.md]
    EJ[ExtractPackageManagerFile.py]
    EK[__init__.py]
    EL[TestExtractPackageManagerFile.py]
  end

  subgraph ReadIssues
    EM[typed.py]
    EN[README.md]
    EO[__init__.py]
    EP[ReadIssues.py]
  end

  subgraph ReadFile
    EQ[typed.py]
    ER[README.md]
    ES[__init__.py]
    ET[ReadFile.py]
  end

  subgraph ScanSonar
    EU[typed.py]
    EV[README.md]
    EW[ScanSonar.py]
    EX[__init__.py]
  end

  subgraph GenerateEmbeddings
    EY[typed.py]
    EZ[GenerateEmbeddings.py]
    FA[README.md]
    FB[__init__.py]
  end

  subgraph ScanDepscan
    FC[typed.py]
    FD[README.md]
    FE[__init__.py]
    FF[ScanDepscan.py]
  end

  subgraph SlackMessage
    FG[typed.py]
    FH[SlackMessage.py]
    FI[README.md]
    FJ[__init__.py]
  end

  B -.-> C
  C -.-> D
  D -.-> E
  E -.-> F
  F -.-> G
  G -.-> H
  H -.-> I
  I -.-> J
  J -.-> K
  K -.-> L
  L -.-> M
  M -.-> N
  N -.-> O
  O -.-> P
  P -.-> Q
  Q -.-> R
  R -.-> S
  S -.-> T
  T -.-> U
  U -.-> V
  V -.-> W
  W -.-> X
  X -.-> Y
  Y -.-> Z
  Z -.-> AA
  AA -.-> AB
  AB -.-> AC
  AC -.-> AD
  AD -.-> AE
  AF -.-> AG
  AG -.-> AH
  AH -.-> AI
  AJ -.-> AK
  AK -.-> AL
  AL -.-> AM
  AN -.-> AO
  AO -.-> AP
  AP -.-> AQ
  AQ -.-> AR
  AR -.-> AS
  AS -.-> AT
  AT -.-> AU
  AU -.-> AV
  AV -.-> AW
  AW -.-> AX
  AX -.-> AY
  AZ -.-> BA
  BA -.-> BB
  BB -.-> BC
  BD -.-> BE
  BE -.-> BF
  BF -.-> BG
  BG -.-> BH
  BI -.-> BJ
  BJ -.-> BK
  BK -.-> BL
  BM -.-> BN
  BN -.-> BO
  BO -.-> BP
  BQ -.-> BR
  BR -.-> BS
  BS -.-> BT
  BT -.-> BU
  BV -.-> BW
  BW -.-> BX
  BX -.-> BY
  BZ -.-> CA
  CA -.-> CB
  CB -.-> CC
  CD -.-> CE
  CE -.-> CF
  CF -.-> CG
  CH -.-> CI
  CI -.-> CJ
  CJ -.-> CK
  CL -.-> CM
  CM -.-> CN
  CN -.-> CO
  CP -.-> CQ
  CQ -.-> CR
  CR -.-> CS
  CT -.-> CU
  CU -.-> CV
  CV -.-> CW
  CX -.-> CY
  CY -.-> CZ
  CZ -.-> DA
  DB -.-> DC
  DC -.-> DD
  DD -.-> DE
  DF -.-> DG
  DG -.-> DH
  DH -.-> DI
  DJ -.-> DK
  DK -.-> DL
  DL -.-> DM
  DN -.-> DO
  DO -.-> DP
  DP -.-> DQ
  DR -.-> DS
  DS -.-> DT
  DT -.-> DU
  DV -.-> DW
  DW -.-> DX
  DX -.-> DY
  DZ -.-> EA
  EA -.-> EB
  EB -.-> EC
  ED -.-> EE
  EE -.-> EF
  EF -.-> EG
  EH -.-> EI
  EI -.-> EJ
  EJ -.-> EK
  EK -.-> EL
  EM -.-> EN
  EN -.-> EO
  EO -.-> EP
  EQ -.-> ER
  ER -.-> ES
  ES -.-> ET
  EU -.-> EV
  EV -.-> EW
  EW -.-> EX
  EY -.-> EZ
  EZ -.-> FA
  FA -.-> FB
  FC -.-> FD
  FD -.-> FE
  FE -.-> FF
  FG -.-> FH
  FH -.-> FI
  FI -.-> FJ
