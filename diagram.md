graph TD;
  subgraph patchwork/steps
    INIT[__init__.py]
    TOC[README.md]
    subgraph ExtractCodeMethodForCommentContexts
      ECMFCtyped[typed.py]
      ECMFCREADME[README.md]
      ECMFC[ExtractCodeMethodForCommentContexts.py]
      ECMFC_INIT[__init__.py]
    end
    subgraph PreparePrompt
      PPtyped[typed.py]
      PPREADME[README.md]
      PP_INIT[__init__.py]
      PP[PreparePrompt.py]
    end
    subgraph ExtractCodeContexts
      ECCtyped[typed.py]
      ECCREADME[README.md]
      ECC[ExtractCodeContexts.py]
      ECC_INIT[__init__.py]
    end
    subgraph ReadPRs
      RPRtyped[typed.py]
      RPRREADME[README.md]
      RPR_INIT[__init__.py]
      RPR[ReadPRs.py]
    end
    subgraph SlackMessage
      SMtyped[typed.py]
      SMREADME[README.md]
      SM_INIT[__init__.py]
      SM[SlackMessage.py]
    end
    subgraph CallAPI
      CAtyped[typed.py]
      CAREADME[README.md]
      CA_INIT[__init__.py]
      CA[CallAPI.py]
    end
    subgraph SendEmail
      SE[SendEmail.py]
      SEtyped[typed.py]
      SEREADME[README.md]
      SE_INIT[__init__.py]
    end
    subgraph CallLLM
      CLLtyped[typed.py]
      CLLREADME[README.md]
      CLL[CallLLM.py]
      CLL_INIT[__init__.py]
    end
    subgraph ReadFile
      RFtyped[typed.py]
      RFREADME[README.md]
      RF_INIT[__init__.py]
      RF[ReadFile.py]
    end
    subgraph AgenticLLM
      ATLtyped[typed.py]
      ATLREADME[README.md]
      ATL_INIT[__init__.py]
      ATL[AgenticLLM.py]
    end
    subgraph LLM
      LLMtyped[typed.py]
      LLMREADME[README.md]
      LLM_INIT[__init__.py]
      LLM[LLM.py]
    end
    subgraph ScanSemgrep
      SSTyped[typed.py]
      SSREADME[README.md]
      SS[ScanSemgrep.py]
      SS_INIT[__init__.py]
    end
    subgraph Combine
      CTyped[typed.py]
      CREADME[README.md]
      C_INIT[__init__.py]
      C[Combine.py]
    end
    subgraph ReadIssues
      RITyped[typed.py]
      RIREADME[README.md]
      RI[ReadIssues.py]
      RI_INIT[__init__.py]
    end
    subgraph FixIssue
      FITyped[typed.py]
      FIREADME[README.md]
      FI_INIT[__init__.py]
      FI[FixIssue.py]
    end
    subgraph FilterBySimilarity
      FBS[FilterBySimilarity.py]
      FBSTyped[typed.py]
      FBSREADME[README.md]
      FBS_INIT[__init__.py]
    end
    subgraph ExtractCode
      ECTyped[typed.py]
      ECREADME[README.md]
      EC[ExtractCode.py]
      EC_INIT[__init__.py]
    end
    subgraph AnalyzeImpact
      AITyped[typed.py]
      AIREADME[README.md]
      AI[AnalyzeImpact.py]
      AI_INIT[__init__.py]
    end
    subgraph ExtractModelResponse
      EMRTyped[typed.py]
      EMRREADME[README.md]
      EMR[ExtractModelResponse.py]
      EMR_INIT[__init__.py]
    end
    subgraph CreateIssue
      CITyped[typed.py]
      CIREADME[README.md]
      CI_INIT[__init__.py]
      CI[CreateIssue.py]
    end
    subgraph ScanSonar
      ScanSonar[ScanSonar.py]
      ScanSonarTyped[typed.py]
      ScanSonarREADME[README.md]
      ScanSonar_INIT[__init__.py]
    end
    subgraph PR
      PR[PR.py]
      PRTyped[typed.py]
      PRREADME[README.md]
      PR_INIT[__init__.py]
    end
    subgraph CallSQL
      CallSQLTyped[typed.py]
      CallSQLREADME[README.md]
      CallSQL[CallSQL.py]
      CallSQL_INIT[__init__.py]
    end
    subgraph ModifyCodeOnce
      MCO[ModifyCodeOnce.py]
      MCOtyped[typed.py]
      MCOREADME[README.md]
      MCO_INIT[__init__.py]
    end
    subgraph GetTypescriptTypeInfo
      gt_typed[typed.py]
      gtREADME[README.md]
      pkg[package.json]
      get_type[get_type_info.ts]
      get_init[__init__.py]
      tsconfig[tsconfig.json]
      pnpm[pnpm-lock.yaml]
    end
    subgraph FileAgent
      FATyped[typed.py]
      FA[FileAgent.py]
      FA_INIT[__init__.py]
    end
    subgraph CreateIssueComment
      CIC[CreateIssueComment.py]
      CICTyped[typed.py]
      CICTREADME[README.md]
      CIC_INIT[__init__.py]
    end
    subgraph BrowserUse
      BUBrowserUse[BrowserUse.py]
      BUTyped[typed.py]
      BUREADME[README.md]
      BU_INIT[__init__.py]
    end
    subgraph CallCode2Prompt
      CCPCallCode2Prompt[CallCode2Prompt.py]
      CCPTyped[typed.py]
      CCPREADME[README.md]
      CCPTest[TestCallCode2Prompt.py]
      CCP_INIT[__init__.py]
    end
    subgraph PreparePR
      PrP_PreparePR[PreparePR.py]
      PrPTyped[typed.py]
      PrPREADME[README.md]
      PrP_INIT[__init__.py]
    end
    subgraph JoinList
      JLJoinList[JoinList.py]
      JLTyped[typed.py]
      JLREADME[README.md]
      JL_INIT[__init__.py]
    end
    subgraph CreatePR
      cr_pr_createpr[CreatePR.py]
      cr_pr_typed[typed.py]
      cr_pr_readme[README.md]
      cr_pr_init[__init__.py]
    end
    subgraph ScanDepscan
      SDTyped[typed.py]
      SDREADME[README.md]
      SD[ScanDepscan.py]
      SD_INIT[__init__.py]
    end
    subgraph SimplifiedLLMOnce
      SSL[SSLOnce.py]
      SSLTyped[typed.py]
      SSLREADME[README.md]
      SSL_INIT[__init__.py]
    end
    subgraph ModifyCode
      MCTyped[typed.py]
      MCREADME[README.md]
      MC[ModifyCode.py]
      MC_INIT[__init__.py]
    end
    subgraph ManageEngineAgent
      MEA[ManageEngineAgent.py]
      MEATyped[typed.py]
    end
    subgraph AgenticLLMV2
      AVLTyped[typed.py]
      AVLREADME[README.md]
      AVL[AgenticLLMV2.py]
      AVL_INIT[__init__.py]
    end
    subgraph ExtractDiff
      EDTyped[typed.py]
      EDREADME[README.md]
      ED[ExtractDiff.py]
      ED_INIT[__init__.py]
    end
    subgraph ReadEmail
      RETyped[typed.py]
      REREADME[README.md]
      RE[ReadEmail.py]
      RE_INIT[__init__.py]
    end
    subgraph CreatePRComment
      CPCIC[CreatePRComment.py]
      CPCTyped[typed.py]
      CPCREADME[README.md]
      CPC_INIT[__init__.py]
    end
    subgraph ReadPRDiffs
      RPDF[ReadPRDiffs.py]
      RPDFTyped[typed.py]
      RPDFREADME[README.md]
      RPDFF_INIT[__init__.py]
    end
    subgraph SimplifiedLLM
      SLTyped[typed.py]
      SLREADME[README.md]
      SL[SSL.py]
      SL_INIT[__init__.py]
    end
    subgraph CallShell
      CShTyped[typed.py]
      CShREADME[README.md]
      CSh[CallShell.py]
      CSh_INIT[__init__.py]
    end
    subgraph CommitChanges
      CCTyped[typed.py]
      CCREADME[README.md]
      CC[CommitChanges.py]
      CC_INIT[__init__.py]
    end
    subgraph GitHubAgent
      GitHub[GHA.py]
      GTHTyped[typed.py]
      GHA_INIT[__init__.py]
    end
    subgraph ExtractPackageManagerFile
      EPMF[ExtractPackageManagerFile.py]
      EPMFTyped[typed.py]
      EPMFREADME[README.md]
      EPMFTest[TestExtractPackageManagerFile.py]
      EPMF_INIT[__init__.py]
    end
  end

  INIT --> TOC
  ECMFCtyped --> ECMFC
  ECMFCREADME --> ECMFC
  PPtyped --> PP
  PPREADME --> PP
  ECCtyped --> ECC
  ECCREADME --> ECC
  RPRtyped --> RPR
  RPRREADME --> RPR
  SMtyped --> SM
  SMREADME --> SM
  CAtyped --> CA
  CAREADME --> CA
  SEtyped --> SE
  SEREADME --> SE
  CLLtyped --> CLL
  CLLREADME --> CLL
  RFtyped --> RF
  RFREADME --> RF
  ATLtyped --> ATL
  ATLREADME --> ATL
  LLMtyped --> LLM
  LLMREADME --> LLM
  SSTyped --> SS
  SSREADME --> SS
  CTyped --> C
  CREADME --> C
  RITyped --> RI
  RIREADME --> RI
  FITyped --> FI
  FIREADME --> FI
  FBSTyped --> FBS
  FBSREADME --> FBS
  ECTyped --> EC
  ECREADME --> EC
  AITyped --> AI
  AIREADME --> AI
  EMRTyped --> EMR
  EMRREADME --> EMR
  CITyped --> CI
  CIREADME --> CI
  ScanSonarTyped --> ScanSonar
  ScanSonarREADME --> ScanSonar
  PRTyped --> PR
  PRREADME --> PR
  CallSQLTyped --> CallSQL
  CallSQLREADME --> CallSQL
  MCOtyped --> MCO
  MCOREADME --> MCO
  gt_typed --> get_type
  gtREADME --> get_init
  FATyped --> FA
  CICTyped --> CIC
  CICTREADME --> CIC
  BUTyped --> BUBrowserUse
  BUREADME --> BUBrowserUse
  CCPTyped --> CCPTest
  CCPREADME --> CCPTest
  CCPTest --> CCPCallCode2Prompt
  PrPTyped --> PrP_PreparePR
  PrPREADME --> PrP_PreparePR
  JLTyped --> JLJoinList
  JLREADME --> JLJoinList
  cr_pr_typed --> cr_pr_createpr
  cr_pr_readme --> cr_pr_createpr
  SDTyped --> SD
  SDREADME --> SD
  SSLTyped --> SSL
  SSLREADME --> SSL
  MCTyped --> MC
  MCREADME --> MC
  MEATyped --> MEA
  AVLTyped --> AVL
  AVLREADME --> AVL
  EDTyped --> ED
  EDREADME --> ED
  RETyped --> RE
  REREADME --> RE
  CPCTyped --> CPCIC
  CPCREADME --> CPCIC
  RPDFTyped --> RPDF
  RPDFREADME --> RPDF
  SLTyped --> SL
  SLREADME --> SL
  CShTyped --> CSh
  CShREADME --> CSh
  CCTyped --> CC
  CCREADME --> CC
  GTHTyped --> GitHub
  EPMFTyped --> EPMF
  EPMFREADME --> EPMF
  EPMFTest --> EPMF
