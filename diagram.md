graph TD
  A(patchwork/steps/README.md)
  A --> B(patchwork/steps/__init__.py)

  B --> C(ExtractCodeMethodForCommentContexts/typed.py)
  B --> D(ExtractCodeMethodForCommentContexts/README.md)
  B --> E(ExtractCodeMethodForCommentContexts/ExtractCodeMethodForCommentContexts.py)
  B --> F(ExtractCodeMethodForCommentContexts/__init__.py)

  B --> G(PreparePrompt/typed.py)
  B --> H(PreparePrompt/README.md)
  B --> I(PreparePrompt/__init__.py)
  B --> J(PreparePrompt/PreparePrompt.py)

  B --> K(ExtractCodeContexts/typed.py)
  B --> L(ExtractCodeContexts/README.md)
  B --> M(ExtractCodeContexts/ExtractCodeContexts.py)
  B --> N(ExtractCodeContexts/__init__.py)

  B --> O(ReadPRs/typed.py)
  B --> P(ReadPRs/README.md)
  B --> Q(ReadPRs/__init__.py)
  B --> R(ReadPRs/ReadPRs.py)

  B --> S(SlackMessage/typed.py)
  B --> T(SlackMessage/README.md)
  B --> U(SlackMessage/__init__.py)
  B --> V(SlackMessage/SlackMessage.py)

  B --> W(CallAPI/typed.py)
  B --> X(CallAPI/README.md)
  B --> Y(CallAPI/__init__.py)
  B --> Z(CallAPI/CallAPI.py)

  B --> AA(SendEmail/SendEmail.py)
  B --> AB(SendEmail/typed.py)
  B --> AC(SendEmail/README.md)
  B --> AD(SendEmail/__init__.py)

  B --> AE(CallLLM/typed.py)
  B --> AF(CallLLM/README.md)
  B --> AG(CallLLM/CallLLM.py)
  B --> AH(CallLLM/__init__.py)

  B --> AI(ReadFile/typed.py)
  B --> AJ(ReadFile/README.md)
  B --> AK(ReadFile/__init__.py)
  B --> AL(ReadFile/ReadFile.py)

  B --> AM(AgenticLLM/typed.py)
  B --> AN(AgenticLLM/README.md)
  B --> AO(AgenticLLM/__init__.py)
  B --> AP(AgenticLLM/AgenticLLM.py)

  B --> AQ(LLM/typed.py)
  B --> AR(LLM/README.md)
  B --> AS(LLM/__init__.py)
  B --> AT(LLM/LLM.py)

  B --> AU(ScanSemgrep/typed.py)
  B --> AV(ScanSemgrep/README.md)
  B --> AW(ScanSemgrep/ScanSemgrep.py)
  B --> AX(ScanSemgrep/__init__.py)

  B --> AY(Combine/typed.py)
  B --> AZ(Combine/README.md)
  B --> BA(Combine/__init__.py)
  B --> BB(Combine/Combine.py)

  B --> BC(ReadIssues/typed.py)
  B --> BD(ReadIssues/README.md)
  B --> BE(ReadIssues/ReadIssues.py)
  B --> BF(ReadIssues/__init__.py)

  B --> BG(FixIssue/typed.py)
  B --> BH(FixIssue/README.md)
  B --> BI(FixIssue/__init__.py)
  B --> BJ(FixIssue/FixIssue.py)

  B --> BK(FilterBySimilarity/typed.py)
  B --> BL(FilterBySimilarity/README.md)
  B --> BM(FilterBySimilarity/FilterBySimilarity.py)
  B --> BN(FilterBySimilarity/__init__.py)

  B --> BO(ExtractCode/typed.py)
  B --> BP(ExtractCode/README.md)
  B --> BQ(ExtractCode/ExtractCode.py)
  B --> BR(ExtractCode/__init__.py)

  B --> BS(AnalyzeImpact/typed.py)
  B --> BT(AnalyzeImpact/README.md)
  B --> BU(AnalyzeImpact/AnalyzeImpact.py)
  B --> BV(AnalyzeImpact/__init__.py)

  B --> BW(ExtractModelResponse/typed.py)
  B --> BX(ExtractModelResponse/README.md)
  B --> BY(ExtractModelResponse/ExtractModelResponse.py)
  B --> BZ(ExtractModelResponse/__init__.py)

  B --> CA(CreateIssue/CreateIssue.py)
  B --> CB(CreateIssue/typed.py)
  B --> CC(CreateIssue/README.md)
  B --> CD(CreateIssue/__init__.py)

  B --> CE(ScanSonar/ScanSonar.py)
  B --> CF(ScanSonar/typed.py)
  B --> CG(ScanSonar/README.md)
  B --> CH(ScanSonar/__init__.py)

  B --> CI(PR/PR.py)
  B --> CJ(PR/typed.py)
  B --> CK(PR/README.md)
  B --> CL(PR/__init__.py)

  B --> CM(CallSQL/typed.py)
  B --> CN(CallSQL/README.md)
  B --> CO(CallSQL/__init__.py)
  B --> CP(CallSQL/CallSQL.py)

  B --> CQ(ModifyCodeOnce/typed.py)
  B --> CR(ModifyCodeOnce/README.md)
  B --> CS(ModifyCodeOnce/__init__.py)
  B --> CT(ModifyCodeOnce/ModifyCodeOnce.py)

  B --> CU(GetTypescriptTypeInfo/pnpm-lock.yaml)
  B --> CV(GetTypescriptTypeInfo/typed.py)
  B --> CW(GetTypescriptTypeInfo/README.md)
  B --> CX(GetTypescriptTypeInfo/tsconfig.json)
  B --> CY(GetTypescriptTypeInfo/package.json)
  B --> CZ(GetTypescriptTypeInfo/get_type_info.ts)
  B --> DA(GetTypescriptTypeInfo/GetTypescriptTypeInfo.py)
  B --> DB(GetTypescriptTypeInfo/__init__.py)

  B --> DC(FileAgent/typed.py)
  B --> DD(FileAgent/FileAgent.py)
  B --> DE(FileAgent/__init__.py)

  B --> DF(CreateIssueComment/typed.py)
  B --> DG(CreateIssueComment/README.md)
  B --> DH(CreateIssueComment/CreateIssueComment.py)
  B --> DI(CreateIssueComment/__init__.py)

  B --> DJ(BrowserUse/typed.py)
  B --> DK(BrowserUse/README.md)
  B --> DL(BrowserUse/BrowserUse.py)
  B --> DM(BrowserUse/__init__.py)

  B --> DN(CallCode2Prompt/typed.py)
  B --> DO(CallCode2Prompt/README.md)
  B --> DP(CallCode2Prompt/CallCode2Prompt.py)
  B --> DQ(CallCode2Prompt/__init__.py)
  B --> DR(CallCode2Prompt/TestCallCode2Prompt.py)

  B --> DS(PreparePR/typed.py)
  B --> DT(PreparePR/README.md)
  B --> DU(PreparePR/PreparePR.py)
  B --> DV(PreparePR/__init__.py)

  B --> DW(JoinList/typed.py)
  B --> DX(JoinList/README.md)
  B --> DY(JoinList/__init__.py)
  B --> DZ(JoinList/JoinList.py)

  B --> EA(CreatePR/CreatePR.py)
  B --> EB(CreatePR/typed.py)
  B --> EC(CreatePR/README.md)
  B --> ED(CreatePR/__init__.py)

  B --> EE(ScanDepscan/typed.py)
  B --> EF(ScanDepscan/README.md)
  B --> EG(ScanDepscan/ScanDepscan.py)
  B --> EH(ScanDepscan/__init__.py)

  B --> EI(SimplifiedLLMOnce/typed.py)
  B --> EJ(SimplifiedLLMOnce/README.md)
  B --> EK(SimplifiedLLMOnce/__init__.py)
  B --> EL(SimplifiedLLMOnce/SimplifiedLLMOnce.py)

  B --> EM(ModifyCode/typed.py)
  B --> EN(ModifyCode/README.md)
  B --> EO(ModifyCode/ModifyCode.py)
  B --> EP(ModifyCode/__init__.py)

  B --> EQ(ManageEngineAgent/typed.py)
  B --> ER(ManageEngineAgent/ManageEngineAgent.py)

  B --> ES(AgenticLLMV2/typed.py)
  B --> ET(AgenticLLMV2/README.md)
  B --> EU(AgenticLLMV2/AgenticLLMV2.py)
  B --> EV(AgenticLLMV2/__init__.py)

  B --> EW(ExtractDiff/typed.py)
  B --> EX(ExtractDiff/README.md)
  B --> EY(ExtractDiff/ExtractDiff.py)
  B --> EZ(ExtractDiff/__init__.py)

  B --> FA(ReadEmail/typed.py)
  B --> FB(ReadEmail/README.md)
  B --> FC(ReadEmail/ReadEmail.py)
  B --> FD(ReadEmail/__init__.py)

  B --> FE(CreatePRComment/typed.py)
  B --> FF(CreatePRComment/README.md)
  B --> FG(CreatePRComment/CreatePRComment.py)
  B --> FH(CreatePRComment/__init__.py)

  B --> FI(ReadPRDiffs/typed.py)
  B --> FJ(ReadPRDiffs/README.md)
  B --> FK(ReadPRDiffs/ReadPRDiffs.py)
  B --> FL(ReadPRDiffs/__init__.py)

  B --> FM(SimplifiedLLM/typed.py)
  B --> FN(SimplifiedLLM/README.md)
  B --> FO(SimplifiedLLM/__init__.py)
  B --> FP(SimplifiedLLM/SimplifiedLLM.py)

  B --> FQ(CallShell/typed.py)
  B --> FR(CallShell/README.md)
  B --> FS(CallShell/__init__.py)
  B --> FT(CallShell/CallShell.py)

  B --> FU(CommitChanges/typed.py)
  B --> FV(CommitChanges/README.md)
  B --> FW(CommitChanges/CommitChanges.py)
  B --> FX(CommitChanges/__init__.py)

  B --> FY(ZohoDeskAgent/typed.py)
  B --> FZ(ZohoDeskAgent/README.md)
  B --> GA(ZohoDeskAgent/ZohoDeskAgent.py)
  B --> GB(ZohoDeskAgent/__init__.py)

  B --> GC(GitHubAgent/GitHubAgent.py)
  B --> GD(GitHubAgent/typed.py)
  B --> GE(GitHubAgent/__init__.py)

  B --> GF(ExtractPackageManagerFile/typed.py)
  B --> GG(ExtractPackageManagerFile/README.md)
  B --> GH(ExtractPackageManagerFile/TestExtractPackageManagerFile.py)
  B --> GI(ExtractPackageManagerFile/__init__.py)
  B --> GJ(ExtractPackageManagerFile/ExtractPackageManagerFile.py)

