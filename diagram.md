graph TD
  subgraph patchwork/steps
    subgraph ExtractCodeMethodForCommentContexts
      ECMTyped --> ECMPy
      ECMPy --> ECMReadMe
    end
    subgraph PreparePrompt
      PPTyped --> PPPy
      PPPy --> PPReadMe
    end
    subgraph ExtractCodeContexts
      ECCTyped --> ECCPy
      ECCPy --> ECCReadMe
    end
    subgraph ReadPRs
      RPReadME --> RPinit
      RPinit --> RPpy
      RPpy --> RPtyped      
    end
    subgraph SlackMessage
      SMReadME --> SMinit
      SMinit --> SMPy
      SMPy --> SMtyped
    end
    subgraph CallAPI
      CAPy --> CAinit
      CAinit --> CAtyped
      CAtyped --> CAreadme
    end
    subgraph SendEmail
      SEPpy --> SEinit
      SEinit --> SEtyped
      SEtyped --> SEREADME
    end
    subgraph CallLLM
      CLTyped --> CLInit
      CLInit --> CLReadme.py
      CLPy --> CLTyped
    end
    subgraph ReadFile
      RFtyped --> RFpy
      RFpy --> RFinit
      RFinit --> RFreadme
    end
    subgraph AgenticLLM
      AGLTyped --> AGLInit
      AGLInit --> AGLReadme
      AGLLPy --> AGLTyped
    end
    subgraph LLM
      LLMReadme --> LLMPy
      LLMPy --> LLMinit
      LLMinit --> LLMtyped
    end
    subgraph ScanSemgrep
      ScanTyped.py --> ScanPy
      ScanPy --> ScanInit
      ScanReadme --> ScanTyped
    end
    subgraph Combine
      CTA --> CTtyped
      CTtyped --> CTPy
    end
    subgraph ReadIssues
      README --> RItyped
      RItyped --> RInint
    end
    subgraph FixIssue
      FIpy --> FItyped
      FItyped --> FInnit
    end
    subgraph FilterBySimilarity
      FtSimread--> FtSimPy
      FtSimPy --> FtSimTyped
      FtSimTyped --> FtSiminit
    end
    subgraph ExtractCode
      ECR --> ECPy
      ECPy --> ECtyped
    end
    subgraph AnalyzeImpact
      AITable --> AIPy
      AIPy --> AIreadme
    end
    subgraph ExtractModelResponse
      EMRTyped --> EMRPY
      EMRPY --> EMR -->
    end
    subgraph CreateIssue
      CIreadme --> CIpy
      CIpy --> CIinit
    end
    subgraph ScanSonar
      SSReadme --> SSInit
      SSPy --> SSReadMe
    end
    AllINIT --> PRpy
    subgraph CallSQL
      SCtyped--> SCinit
      SCinit --> CLreadme
    end
    subgraph ModifyCodeOnce
      MCTyped --> MCrelease
    end
    subgraph FileAgent
      FAtyped --> FArelease
    end
    subgraph CreateIssueComment
      FAtest --> FAinit
    end
    subgraph BrowserUse
      BUseTyped --> BUseleaveService
    end
    subgraph CallCode2Prompt
      CCPTyped --> Call2py
    end
    subgraph PreparePR
      PPRtyped-->PPRinit
    end
    subgraph JoinList
      JLTpy --> JLInit
    end
    subgraph CreatePR
      Createinit --> CreatePy
    end
    subgraph ScanDepscan
      Depinit -->Depreadme
    end
    subgraph SimplifiedLLMOnce
      NonesenseTyped --> NoneSense
    end
    subgraph ModifyCode
      NonsenseTyped --> NoneSenseReadMe
    end
    subgraph ManageEngineAgent
      MEAtyped --> MEAPrent
    end
    subgraph AgenticLLMV2
      InputNodeTyped --> testFile
    end
    subgraph ExtractDiff
      resultTyped --> testfile
    end
    subgraph ReadEmail
      OutputTyped--> tableFile    
    end
    subgraph CreatePRComment
      Outputtyped --> tableMap    
    end
    subgraph BrowserUse 
      Botyped --> mailto
    end
    subgraph CallShell
      SHtyped --> shprep
    end
    subgraph DatabaseAgent
      returnTyped --> finalTyped
    end
    subgraph CommitChanges
      CommitTyped --> prepination
    end
    subgraph ZohoDeskAgent
      TypedFunction --> someFuncs
    end
    subgraph GitHubAgent
      resultAgent --> githubPy
    end
    subgraph ExtractPackageManagerFile
      resultRPMF --> finalReport
    end
  end
