graph TD
  A["patchwork"] --> |Has Dependency| B["steps"]
  
  subgraph B
    D[README.md]
    E["__init__.py"]
    
    subgraph Overview
      F["README.md"]     
    end

    
    D --> |Document| Overview
    
    subgraph steps
      subgraph ExtractCodeMethodForCommentContexts
        FC["typed.py"]
        FF["README.md"]
        FG["ExtractCodeMethodForCommentContexts.py"]
        FH["__init__.py"]
        
        F[ExtractCodeMethodForCommentContexts] --> FC
        F --> FF
        F --> FG
        F --> FH
      end

      subgraph PreparePrompt
        FZ["typed.py"]
        FD["README.md"]
        FE["__init__.py"]
        FF["PreparePrompt.py"]
        
        F[PreparePrompt] --> FZ
        F --> FD
        F --> FE
        F --> FF
      end

      subgraph ExtractCodeContexts
        FG["typed.py"]
        FH["README.md"]
        FI["ExtractCodeContexts.py"]
        FJ["__init__.py"]
        
        F[ExtractCodeContexts] --> FG
        F --> FH
        F --> FI
        F --> FJ
      end

      subgraph ReadPRs
        FK["typed.py"]
        FL["README.md"]
        FM["__init__.py"]
        FN["ReadPRs.py"]
        
        F[ReadPRs] --> FK
        F --> FL
        F --> FM
        F --> FN
      end

      subgraph SlackMessage
        FO["typed.py"]
        FP["README.md"]
        FQ["__init__.py"]
        FR["SlackMessage.py"]
        
        F[SlackMessage] --> FO
        F --> FP
        F --> FQ
        F --> FR
      end

      subgraph CallAPI
        FS["typed.py"]
        FT["README.md"]
        FU["__init__.py"]
        FV["CallAPI.py"]
        
        F[CallAPI] --> FS
        F --> FT
        F --> FU
        F --> FV
      end

      subgraph SendEmail
        FW["typed.py"]
        FX["README.md"]
        FY["__init__.py"]
        FZ["SendEmail.py"]
        
        F[SendEmail] --> FW
        F --> FX
        F --> FY
        F --> FZ
      end

      subgraph CallLLM
        FZ["typed.py"]
        FA["README.md"]
        FB["__init__.py"]
        FC["CallLLM.py"]
        
        F[CallLLM] --> FZ
        F --> FA
        F --> FB
        F --> FC
      end

      subgraph ReadFile
        FD["typed.py"]
        FE["README.md"]
        FF["__init__.py"]
        FG["ReadFile.py"]
        
        F[ReadFile] --> FD
        F --> FE
        F --> FF
        F --> FG
      end

      subgraph AgenticLLM
        FH["typed.py"]
        FI["README.md"]
        FJ["__init__.py"]
        FK["AgenticLLM.py"]
        
        F[AgenticLLM] --> FH
        F --> FI
        F --> FJ
        F --> FK
      end

      subgraph LLM
        FL["typed.py"]
        FM["README.md"]
        FN["__init__.py"]
        FO["LLM.py"]
        
        F[LLM] --> FL
        F --> FM
        F --> FN
        F --> FO
      end

      subgraph ScanSemgrep
        FP["typed.py"]
        FQ["README.md"]
        FR["ScanSemgrep.py"]
        FS["__init__.py"]
        
        F[ScanSemgrep] --> FP
        F --> FQ
        F --> FR
        F --> FS
      end

      subgraph Combine
        FT["typed.py"]
        FU["README.md"]
        FV["__init__.py"]
        FW["Combine.py"]
        
        F[Combine] --> FT
        F --> FU
        F --> FV
        F --> FW
      end

      subgraph ReadIssues
        FX["typed.py"]
        FY["README.md"]
        FZ["__init__.py"]
        FA["ReadIssues.py"]
        
        F[ReadIssues] --> FX
        F --> FY
        F --> FZ
        F --> FA
      end

      subgraph FixIssue
        FB["typed.py"]
        FC["README.md"]
        FD["__init__.py"]
        FE["FixIssue.py"]
        
        F[FixIssue] --> FB
        F --> FC
        F --> FD
        F --> FE
      end

      subgraph FilterBySimilarity
        FF["typed.py"]
        FG["README.md"]
        FH["__init__.py"]
        FI["FilterBySimilarity.py"]
        
        F[FilterBySimilarity] --> FF
        F --> FG
        F --> FH
        F --> FI
      end

      subgraph ExtractCode
        FJ["typed.py"]
        FK["README.md"]
        FL["__init__.py"]
        FM["ExtractCode.py"]
        
        F[ExtractCode] --> FJ
        F --> FK
        F --> FL
        F --> FM
      end

      subgraph AnalyzeImpact
        FN["typed.py"]
        FO["README.md"]
        FP["__init__.py"]
        FQ["AnalyzeImpact.py"]
        
        F[AnalyzeImpact] --> FN
        F --> FO
        F --> FP
        F --> FQ
      end

      subgraph ExtractModelResponse
        FR["typed.py"]
        FS["README.md"]
        FT["__init__.py"]
        FU["ExtractModelResponse.py"]
        
        F[ExtractModelResponse] --> FR
        F --> FS
        F --> FT
        F --> FU
      end

      subgraph CreateIssue
        FV["typed.py"]
        FW["README.md"]
        FX["__init__.py"]
        FY["CreateIssue.py"]
        
        F[CreateIssue] --> FV
        F --> FW
        F --> FX
        F --> FY
      end

      subgraph ScanSonar
        FZ["typed.py"]
        FA["README.md"]
        FB["__init__.py"]
        FC["ScanSonar.py"]
        
        F[ScanSonar] --> FZ
        F --> FA
        F --> FB
        F --> FC
      end

      subgraph PR
        FD["typed.py"]
        FE["README.md"]
        FF["__init__.py"]
        FG["PR.py"]
        
        F[PR] --> FD
        F --> FE
        F --> FF
        F --> FG
      end

      subgraph CallSQL
        FH["typed.py"]
        FI["README.md"]
        FJ["__init__.py"]
        FK["CallSQL.py"]
        
        F[CallSQL] --> FH
        F --> FI
        F --> FJ
        F --> FK
      end

      subgraph ModifyCodeOnce
        FL["typed.py"]
        FM["README.md"]
        FN["__init__.py"]
        FO["ModifyCodeOnce.py"]
        
        F[ModifyCodeOnce] --> FL
        F --> FM
        F --> FN
        F --> FO
      end

      subgraph GetTypescriptTypeInfo
        FP["typed.py"]
        FQ["README.md"]
        FR["__init__.py"]
        FS["GetTypescriptTypeInfo.py"]
        FT["get_type_info.ts"]
        FZ["tsconfig.json"]
        FG["package.json"]
        FH["pnpm-lock.yaml"]
        
        F[GetTypescriptTypeInfo] --> FP
        F --> FQ
        F --> FR
        F --> FS
        F --> FT
        F --> FZ
        F --> FG
        F --> FH
      end

      subgraph CreateIssueComment
        FI["typed.py"]
        FJ["README.md"]
        FK["__init__.py"]
        FL["CreateIssueComment.py"]
        
        F[CreateIssueComment] --> FI
        F --> FJ
        F --> FK
        F --> FL
      end

      subgraph BrowserUse
        FM["typed.py"]
        FN["README.md"]
        FO["__init__.py"]
        FP["BrowserUse.py"]
        
        F[BrowserUse] --> FM
        F --> FN
        F --> FO
        F --> FP
      end

      subgraph CallCode2Prompt
        FQ["typed.py"]
        FR["README.md"]
        FI["__init__.py"]
        FS["CallCode2Prompt.py"]
        FT["TestCallCode2Prompt.py"]
        
        F[CallCode2Prompt] --> FQ
        F --> FR
        F --> FI
        F --> FS
        F --> FT
      end

      subgraph PreparePR
        FV["typed.py"]
        FW["README.md"]
        FX["__init__.py"]
        FY["PreparePR.py"]
        
        F[PreparePR] --> FV
        F --> FW
        F --> FX
        F --> FY
      end

      subgraph JoinList
        FZ["typed.py"]
        FA["README.md"]
        FB["__init__.py"]
        FC["JoinList.py"]
        
        F[JoinList] --> FZ
        F --> FA
        F --> FB
        F --> FC
      end

      subgraph CreatePR
        FD["typed.py"]
        FE["README.md"]
        FF["__init__.py"]
        FG["CreatePR.py"]
        
        F[CreatePR] --> FD
        F --> FE
        F --> FF
        F --> FG
      end

      subgraph ScanDepscan
        FH["typed.py"]
        FI["README.md"]
        FJ["__init__.py"]
        FK["ScanDepscan.py"]
        
        F[ScanDepscan] --> FH
        F --> FI
        F --> FJ
        F --> FK
      end

      subgraph SimplifiedLLMOnce
        FL["typed.py"]
        FM["README.md"]
        FN["__init__.py"]
        FO["SimplifiedLLMOnce.py"]
        
        F[SimplifiedLLMOnce] --> FL
        F --> FM
        F --> FN
        F --> FO
      end

      subgraph ModifyCode
        FP["typed.py"]
        FQ["README.md"]
        FR["__init__.py"]
        FS["ModifyCode.py"]
        
        F[ModifyCode] --> FP
        F --> FQ
        F --> FR
        F --> FS
      end

      subgraph ManageEngineAgent
        FT["typed.py"]
        FU["__init__.py"]
        FV["ManageEngineAgent.py"]
        
        F[ManageEngineAgent] --> FT
        F --> FU
        F --> FV
      end

      subgraph AgenticLLMV2
        FW["typed.py"]
        FX["README.md"]
        FY["__init__.py"]
        FZ["AgenticLLMV2.py"]
        
        F[AgenticLLMV2] --> FW
        F --> FX
        F --> FY
        F --> FZ
      end

      subgraph ExtractDiff
        FG["typed.py"]
        FH["README.md"]
        FI["__init__.py"]
        FJ["ExtractDiff.py"]
        
        F[ExtractDiff] --> FG
        F --> FH
        F --> FI
        F --> FJ
      end

      subgraph ReadEmail
        FK["typed.py"]
        FL["README.md"]
        FM["__init__.py"]
        FN["ReadEmail.py"]
        
        F[ReadEmail] --> FK
        F --> FL
        F --> FM
        F --> FN
      end

      subgraph CreatePRComment
        FO["typed.py"]
        FP["README.md"]
        FQ["__init__.py"]
        FR["CreatePRComment.py"]
        
        F[CreatePRComment] --> FO
        F --> FP
        F --> FQ
        F --> FR
      end

      subgraph ReadPRDiffs
        FS["typed.py"]
        FT["README.md"]
        FU["__init__.py"]
        FV["ReadPRDiffs.py"]
        
        F[ReadPRDiffs] --> FS
        F --> FT
        F --> FU
        F --> FV
      end

      subgraph SimplifiedLLM
        FW["typed.py"]
        FX["README.md"]
        FY["__init__.py"]
        FZ["SimplifiedLLM.py"]
        
        F[SimplifiedLLM] --> FW
        F --> FX
        F --> FY
        F --> FZ
      end

      subgraph CallShell
        FG["typed.py"]
        FH["README.md"]
        FI["__init__.py"]
        FJ["CallShell.py"]
        
        F[CallShell] --> FG
        F --> FH
        F --> FI
        F --> FJ
      end

      subgraph CommitChanges
        FK["typed.py"]
        FL["README.md"]
        FM["__init__.py"]
        FN["CommitChanges.py"]
        
        F[CommitChanges] --> FK
        F --> FL
        F --> FM
        F --> FN
      end

      subgraph GitHubAgent
        FO["typed.py"]
        FP["__init__.py"]
        FQ["GitHubAgent.py"]
        
        F[GitHubAgent] --> FO
        F --> FP
        F --> FQ
      end

      subgraph ExtractPackageManagerFile
        FR["typed.py"]
        FS["README.md"]
        FT["__init__.py"]
        FU["TestExtractPackageManagerFile.py"]
        FV["ExtractPackageManagerFile.py"]
        
        F[ExtractPackageManagerFile] --> FR
        F --> FS
        F --> FT
        F --> FU
        F --> FV
      end

    end
  end
