graph TD;
  subgraph patchwork/steps
    A(init.py)
    B(README.md)
    subgraph LLM
      B1(init.py)
      B2(LLM.py)
      B3(typed.py)
      B4(README.md)
    end
    subgraph CallCode2Prompt
      C1(init.py)
      C2(CallCode2Prompt.py)
      C3(TestCallCode2Prompt.py)
      C4(typed.py)
      C5(README.md)
    end
    subgraph GenerateCodeRepositoryEmbeddings
      D1(init.py)
      D2(GenerateCodeRepositoryEmbeddings.py)
      D3(typed.py)
      D4(filter_lists.py)
      D5(README.md)
    end
    subgraph ScanSemgrep
      E1(init.py)
      E2(ScanSemgrep.py)
      E3(typed.py)
      E4(README.md)
    end
    subgraph GetTypescriptTypeInfo
      F1(init.py)
      F2(get_type_info.ts)
      F3(GetTypescriptTypeInfo.py)
      F4(tsconfig.json)
      F5(typed.py)
      F6(pnpm-lock.yaml)
      F7(package.json)
      F8(README.md)
    end
    subgraph ExtractCodeMethodForCommentContexts
      G1(init.py)
      G2(ExtractCodeMethodForCommentContexts.py)
      G3(typed.py)
      G4(README.md)
    end
    subgraph ExtractModelResponse
      H1(init.py)
      H2(ExtractModelResponse.py)
      H3(typed.py)
      H4(README.md)
    end
    subgraph GenerateEmbeddings
      I1(init.py)
      I2(GenerateEmbeddings.py)
      I3(typed.py)
      I4(README.md)
    end
    subgraph PR
      J1(init.py)
      J2(PR.py)
      J3(typed.py)
      J4(README.md)
    end
    subgraph SlackMessage
      K1(init.py)
      K2(SlackMessage.py)
      K3(typed.py)
      K4(README.md)
    end
    subgraph PreparePR
      L1(init.py)
      L2(PreparePR.py)
      L3(typed.py)
      L4(README.md)
    end
    subgraph ModifyCodeOnce
      M1(init.py)
      M2(ModifyCodeOnce.py)
      M3(typed.py)
      M4(README.md)
    end
    subgraph CreatePRComment
      N1(init.py)
      N2(CreatePRComment.py)
      N3(typed.py)
      N4(README.md)
    end
    subgraph CallShell
      O1(init.py)
      O2(CallShell.py)
      O3(typed.py)
      O4(README.md)
    end
    subgraph AgenticLLMV2
      P1(init.py)
      P2(AgenticLLMV2.py)
      P3(typed.py)
      P4(README.md)
    end
    subgraph FixIssue
      Q1(init.py)
      Q2(FixIssue.py)
      Q3(typed.py)
      Q4(README.md)
    end
    subgraph ScanSonar
      R1(init.py)
      R2(ScanSonar.py)
      R3(typed.py)
      R4(README.md)
    end
    subgraph CreateIssue
      S1(init.py)
      S2(CreateIssue.py)
      S3(typed.py)
      S4(README.md)
    end
    subgraph FilterBySimilarity
      T1(init.py)
      T2(FilterBySimilarity.py)
      T3(typed.py)
      T4(README.md)
    end
    subgraph ReadPRDiffs
      U1(init.py)
      U2(ReadPRDiffs.py)
      U3(typed.py)
      U4(README.md)
    end
    subgraph AgenticLLM
      V1(init.py)
      V2(AgenticLLM.py)
      V3(typed.py)
      V4(README.md)
    end
    subgraph CommitChanges
      W1(init.py)
      W2(CommitChanges.py)
      W3(typed.py)
      W4(README.md)
    end
    subgraph SimplifiedLLMOnce
      X1(init.py)
      X2(SimplifiedLLMOnce.py)
      X3(typed.py)
      X4(README.md)
    end
    subgraph ExtractPackageManagerFile
      Y1(init.py)
      Y2(ExtractPackageManagerFile.py)
      Y3(TestExtractPackageManagerFile.py)
      Y4(typed.py)
      Y5(README.md)
    end
    subgraph ReadEmail
      Z1(init.py)
      Z2(ReadEmail.py)
      Z3(typed.py)
      Z4(README.md)
    end
    subgraph ModifyCode
      AA1(init.py)
      AA2(ModifyCode.py)
      AA3(typed.py)
      AA4(README.md)
    end
    subgraph JoinList
      AB1(init.py)
      AB2(JoinList.py)
      AB3(typed.py)
      AB4(README.md)
    end
    subgraph CallAPI
      AC1(init.py)
      AC2(CallAPI.py)
      AC3(typed.py)
      AC4(README.md)
    end
    subgraph CreatePR
      AD1(init.py)
      AD2(CreatePR.py)
      AD3(typed.py)
      AD4(README.md)
    end
    subgraph ReadIssues
      AE1(init.py)
      AE2(ReadIssues.py)
      AE3(typed.py)
      AE4(README.md)
    end
    subgraph ReadFile
      AF1(init.py)
      AF2(ReadFile.py)
      AF3(typed.py)
      AF4(README.md)
    end
    subgraph CallLLM
      AG1(init.py)
      AG2(CallLLM.py)
      AG3(typed.py)
      AG4(README.md)
    end
    subgraph CallSQL
      AH1(init.py)
      AH2(CallSQL.py)
      AH3(typed.py)
      AH4(README.md)
    end
    subgraph ScanDepscan
      AI1(init.py)
      AI2(ScanDepscan.py)
      AI3(typed.py)
      AI4(README.md)
    end
    subgraph ExtractDiff
      AJ1(init.py)
      AJ2(ExtractDiff.py)
      AJ3(typed.py)
      AJ4(README.md)
    end
    subgraph QueryEmbeddings
      AK1(init.py)
      AK2(QueryEmbeddings.py)
      AK3(typed.py)
      AK4(README.md)
    end
    subgraph SendEmail
      AL1(init.py)
      AL2(SendEmail.py)
      AL3(typed.py)
      AL4(README.md)
    end
    subgraph Combine
      AM1(init.py)
      AM2(Combine.py)
      AM3(typed.py)
      AM4(README.md)
    end
    subgraph SimplifiedLLM
      AN1(init.py)
      AN2(SimplifiedLLM.py)
      AN3(typed.py)
      AN4(README.md)
    end
    subgraph ReadPRs
      AO1(init.py)
      AO2(ReadPRs.py)
      AO3(typed.py)
      AO4(README.md)
    end
    subgraph ExtractCodeContexts
      AP1(init.py)
      AP2(ExtractCodeContexts.py)
      AP3(typed.py)
      AP4(README.md)
    end
    subgraph AnalyzeImpact
      AQ1(init.py)
      AQ2(AnalyzeImpact.py)
      AQ3(typed.py)
      AQ4(README.md)
    end
    subgraph PreparePrompt
      AR1(init.py)
      AR2(PreparePrompt.py)
      AR3(typed.py)
      AR4(README.md)
    end
    subgraph CreateIssueComment
      AS1(init.py)
      AS2(CreateIssueComment.py)
      AS3(typed.py)
      AS4(README.md)
    end
    subgraph ExtractCode
      AT1(init.py)
      AT2(ExtractCode.py)
      AT3(typed.py)
      AT4(README.md)
    end
  end

  A --> B
  B --> B1
  B --> C1
  B --> D1
  B --> E1
  B --> F1
  B --> G1
  B --> H1
  B --> I1
  B --> J1
  B --> K1
  B --> L1
  B --> M1
  B --> N1
  B --> O1
  B --> P1
  B --> Q1
  B --> R1
  B --> S1
  B --> T1
  B --> U1
  B --> V1
  B --> W1
  B --> X1
  B --> Y1
  B --> Z1
  B --> AA1
  B --> AB1
  B --> AC1
  B --> AD1
  B --> AE1
  B --> AF1
  B --> AG1
  B --> AH1
  B --> AI1
  B --> AJ1
  B --> AK1
  B --> AL1
  B --> AM1
  B --> AN1
  B --> AO1
  B --> AP1
  B --> AQ1
  B --> AR1
  B --> AS1
  B --> AT1
