graph TD
  subgraph patchwork/steps
    subgraph ExtractCodeMethodForCommentContexts
      direction TB
      typed[typed.py]
      README[README.md]
      ExtractCodeMethodForCommentContexts.py[ExtractCodeMethodForCommentContexts.py]
      init1[__init__.py]
    end
    subgraph PreparePrompt
      direction TB
      typed2[typed.py]
      README2[README.md]
      PreparePrompt.py[PreparePrompt.py]
      init2[__init__.py]
    end
    subgraph ExtractCodeContexts
      direction TB
      typed3[typed.py]
      README3[README.md]
      ExtractCodeContexts.py[ExtractCodeContexts.py]
      init3[__init__.py]
    end
    subgraph ReadPRs
      direction TB
      typed4[typed.py]
      README4[README.md]
      ReadPRs.py[ReadPRs.py]
      init4[__init__.py]
    end
    subgraph SlackMessage
      direction TB
      typed5[typed.py]
      README5[README.md]
      SlackMessage.py[SlackMessage.py]
      init5[__init__.py]
    end
    subgraph CallAPI
      direction TB
      typed6[typed.py]
      README6[README.md]
      CallAPI.py[CallAPI.py]
      init6[__init__.py]
    end
    subgraph SendEmail
      direction TB
      typed7[typed.py]
      README7[README.md]
      SendEmail.py[SendEmail.py]
      init7[__init__.py]
    end
    subgraph CallLLM
      direction TB
      typed8[typed.py]
      README8[README.md]
      CallLLM.py[CallLLM.py]
      init8[__init__.py]
    end
    subgraph ReadFile
      direction TB
      typed9[typed.py]
      README9[README.md]
      ReadFile.py[ReadFile.py]
      init9[__init__.py]
    end
    subgraph AgenticLLM
      direction TB
      typed10[typed.py]
      README10[README.md]
      AgenticLLM.py[AgenticLLM.py]
      init10[__init__.py]
    end
    subgraph LLM
      direction TB
      typed11[typed.py]
      README11[README.md]
      LLM.py[LLM.py]
      init11[__init__.py]
    end
    subgraph ScanSemgrep
      direction TB
      typed12[typed.py]
      README12[README.md]
      ScanSemgrep.py[ScanSemgrep.py]
      init12[__init__.py]
    end
    subgraph Combine
      direction TB
      typed13[typed.py]
      README13[README.md]
      Combine.py[Combine.py]
      init13[__init__.py]
    end
    subgraph ReadIssues
      direction TB
      typed14[typed.py]
      README14[README.md]
      ReadIssues.py[ReadIssues.py]
      init14[__init__.py]
    end
    subgraph FixIssue
      direction TB
      typed15[typed.py]
      README15[README.md]
      FixIssue.py[FixIssue.py]
      init15[__init__.py]
    end
    subgraph FilterBySimilarity
      direction TB
      typed16[typed.py]
      README16[README.md]
      FilterBySimilarity.py[FilterBySimilarity.py]
      init16[__init__.py]
    end
    subgraph ExtractCode
      direction TB
      typed17[typed.py]
      README17[README.md]
      ExtractCode.py[ExtractCode.py]
      init17[__init__.py]
    end
    subgraph AnalyzeImpact
      direction TB
      typed18[typed.py]
      README18[README.md]
      AnalyzeImpact.py[AnalyzeImpact.py]
      init18[__init__.py]
    end
    subgraph ExtractModelResponse
      direction TB
      typed19[typed.py]
      README19[README.md]
      ExtractModelResponse.py[ExtractModelResponse.py]
      init19[__init__.py]
    end
    subgraph CreateIssue
      direction TB
      typed20[typed.py]
      README20[README.md]
      CreateIssue.py[CreateIssue.py]
      init20[__init__.py]
    end
    subgraph ScanSonar
      direction TB
      typed21[typed.py]
      README21[README.md]
      ScanSonar.py[ScanSonar.py]
      init21[__init__.py]
    end
    subgraph PR
      direction TB
      typed22[typed.py]
      README22[README.md]
      PR.py[PR.py]
      init22[__init__.py]
    end
    subgraph CallSQL
      direction TB
      typed23[typed.py]
      README23[README.md]
      CallSQL.py[CallSQL.py]
      init23[__init__.py]
    end
    subgraph ModifyCodeOnce
      direction TB
      typed24[typed.py]
      README24[README.md]
      ModifyCodeOnce.py[ModifyCodeOnce.py]
      init24[__init__.py]
    end
    subgraph GetTypescriptTypeInfo
      direction TB
      pnpm-lock.yaml
      typed25[typed.py]
      README25[README.md]
      tsconfig.json
      package.json
      get_type_info.ts
      GetTypescriptTypeInfo.py[GetTypescriptTypeInfo.py]
      init25[__init__.py]
    end
    subgraph FileAgent
      direction TB
      typed26[typed.py]
      FileAgent.py[FileAgent.py]
      init26[__init__.py]
    end
    subgraph CreateIssueComment
      direction TB
      typed27[typed.py]
      README27[README.md]
      CreateIssueComment.py[CreateIssueComment.py]
      init27[__init__.py]
    end
    subgraph BrowserUse
      direction TB
      typed28[typed.py]
      README28[README.md]
      BrowserUse.py[BrowserUse.py]
      init28[__init__.py]
    end
    subgraph CallCode2Prompt
      direction TB
      typed29[typed.py]
      README29[README.md]
      CallCode2Prompt.py[CallCode2Prompt.py]
      TestCallCode2Prompt.py[TestCallCode2Prompt.py]
      init29[__init__.py]
    end
    subgraph PreparePR
      direction TB
      typed30[typed.py]
      README30[README.md]
      PreparePR.py[PreparePR.py]
      init30[__init__.py]
    end
    subgraph JoinList
      direction TB
      typed31[typed.py]
      README31[README.md]
      JoinList.py[JoinList.py]
      init31[__init__.py]
    end
    subgraph CreatePR
      direction TB
      typed32[typed.py]
      README32[README.md]
      CreatePR.py[CreatePR.py]
      init32[__init__.py]
    end
    subgraph ScanDepscan
      direction TB
      typed33[typed.py]
      README33[README.md]
      ScanDepscan.py[ScanDepscan.py]
      init33[__init__.py]
    end
    subgraph SimplifiedLLMOnce
      direction TB
      typed34[typed.py]
      README34[README.md]
      SimplifiedLLMOnce.py[SimplifiedLLMOnce.py]
      init34[__init__.py]
    end
    subgraph ModifyCode
      direction TB
      typed35[typed.py]
      README35[README.md]
      ModifyCode.py[ModifyCode.py]
      init35[__init__.py]
    end
    subgraph ManageEngineAgent
      direction TB
      typed36[typed.py]
      README36[README.md]
      ManageEngineAgent.py[ManageEngineAgent.py]
      init36[__init__.py]
    end
    subgraph AgenticLLMV2
      direction TB
      typed37[typed.py]
      README37[README.md]
      AgenticLLMV2.py[AgenticLLMV2.py]
      init37[__init__.py]
    end
    subgraph ExtractDiff
      direction TB
      typed38[typed.py]
      README38[README.md]
      ExtractDiff.py[ExtractDiff.py]
      init38[__init__.py]
    end
    subgraph ReadEmail
      direction TB
      typed39[typed.py]
      README39[README.md]
      ReadEmail.py[ReadEmail.py]
      init39[__init__.py]
    end
    subgraph CreatePRComment
      direction TB
      typed40[typed.py]
      README40[README.md]
      CreatePRComment.py[CreatePRComment.py]
      init40[__init__.py]
    end
    subgraph ReadPRDiffs
      direction TB
      typed41[typed.py]
      README41[README.md]
      ReadPRDiffs.py[ReadPRDiffs.py]
      init41[__init__.py]
    end
    subgraph SimplifiedLLM
      direction TB
      typed42[typed.py]
      README42[README.md]
      SimplifiedLLM.py[SimplifiedLLM.py]
      init42[__init__.py]
    end
    subgraph CallShell
      direction TB
      typed43[typed.py]
      README43[README.md]
      CallShell.py[CallShell.py]
      init43[__init__.py]
    end
    subgraph DatabaseAgent
      direction TB
      typed44[typed.py]
      README44[README.md]
      DatabaseAgent.py[DatabaseAgent.py]
      init44[__init__.py]
    end
    subgraph CommitChanges
      direction TB
      typed45[typed.py]
      README45[README.md]
      CommitChanges.py[CommitChanges.py]
      init45[__init__.py]
    end
    subgraph ZohoDeskAgent
      direction TB
      typed46[typed.py]
      README46[README.md]
      ZohoDeskAgent.py[ZohoDeskAgent.py]
      init46[__init__.py]
    end
    subgraph GitHubAgent
      direction TB
      typed47[typed.py]
      README47[README.md]
      GitHubAgent.py[GitHubAgent.py]
      init47[__init__.py]
    end
    subgraph ExtractPackageManagerFile
      direction TB
      typed48[typed.py]
      README48[README.md]
      ExtractPackageManagerFile.py[ExtractPackageManagerFile.py]
      TestExtractPackageManagerFile.py[TestExtractPackageManagerFile.py]
      init48[__init__.py]
    end  
  end
  READMEAll[patchwork/steps/README.md] --> initAll[patchwork/steps/__init__.py]
  READMEAll --> ExtractCodeMethodForCommentContexts
  READMEAll --> PreparePrompt
  READMEAll --> ExtractCodeContexts
  READMEAll --> ReadPRs
  READMEAll --> SlackMessage
  READMEAll --> CallAPI
  READMEAll --> SendEmail
  READMEAll --> CallLLM
  READMEAll --> ReadFile
  READMEAll --> AgenticLLM
  READMEAll --> LLM
  READMEAll --> ScanSemgrep
  READMEAll --> Combine
  READMEAll --> ReadIssues
  READMEAll --> FixIssue
  READMEAll --> FilterBySimilarity
  READMEAll --> ExtractCode
  READMEAll --> AnalyzeImpact
  READMEAll --> ExtractModelResponse
  READMEAll --> CreateIssue
  READMEAll --> ScanSonar
  READMEAll --> PR
  READMEAll --> CallSQL
  READMEAll --> ModifyCodeOnce
  READMEAll --> GetTypescriptTypeInfo
  READMEAll --> FileAgent
  READMEAll --> CreateIssueComment
  READMEAll --> BrowserUse
  READMEAll --> CallCode2Prompt
  READMEAll --> PreparePR
  READMEAll --> JoinList
  READMEAll --> CreatePR
  READMEAll --> ScanDepscan
  READMEAll --> SimplifiedLLMOnce
  READMEAll --> ModifyCode
  READMEAll --> ManageEngineAgent
  READMEAll --> AgenticLLMV2
  READMEAll --> ExtractDiff
  READMEAll --> ReadEmail
  READMEAll --> CreatePRComment
  READMEAll --> ReadPRDiffs
  READMEAll --> SimplifiedLLM
  READMEAll --> CallShell
  READMEAll --> DatabaseAgent
  READMEAll --> CommitChanges
  READMEAll --> ZohoDeskAgent
  READMEAll --> GitHubAgent
  READMEAll --> ExtractPackageManagerFile
