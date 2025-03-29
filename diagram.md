graph TD
    subgraph patchwork ["patchwork"]
        direction TB
        subgraph steps ["steps"]
            direction TB
            init(steps/__init__.py)
            README1(steps/README.md)
            ExtractCodeMethodForCommentContexts [ExtractCodeMethodForCommentContexts]
            PreparePrompt [PreparePrompt]
            ExtractCodeContexts [ExtractCodeContexts]
            ReadPRs [ReadPRs]
            SlackMessage [SlackMessage]
            CallAPI [CallAPI]
            SendEmail [SendEmail]
            CallLLM [CallLLM]
            ReadFile [ReadFile]
            AgenticLLM [AgenticLLM]
            LLM [LLM]
            ScanSemgrep [ScanSemgrep]
            Combine [Combine]
            ReadIssues [ReadIssues]
            FixIssue [FixIssue]
            FilterBySimilarity [FilterBySimilarity]
            ExtractCode [ExtractCode]
            AnalyzeImpact [AnalyzeImpact]
            ExtractModelResponse [ExtractModelResponse]
            CreateIssue [CreateIssue]
            ScanSonar [ScanSonar]
            PR [PR]
            CallSQL [CallSQL]
            ModifyCodeOnce [ModifyCodeOnce]
            subgraph GetTypescriptTypeInfo [GetTypescriptTypeInfo]
                direction TB
                pnpm-lock.yaml
                tsconfig.json
                package.json
                get_type_info.ts
            end
            CreateIssueComment [CreateIssueComment]
            BrowserUse [BrowserUse]
            CallCode2Prompt [CallCode2Prompt]
            PreparePR [PreparePR]
            JoinList [JoinList]
            CreatePR [CreatePR]
            ScanDepscan [ScanDepscan]
            SimplifiedLLMOnce [SimplifiedLLMOnce]
            ModifyCode [ModifyCode]
            ManageEngineAgent [ManageEngineAgent]
            AgenticLLMV2 [AgenticLLMV2]
            ExtractDiff [ExtractDiff]
            ReadEmail [ReadEmail]
            CreatePRComment [CreatePRComment]
            ReadPRDiffs [ReadPRDiffs]
            SimplifiedLLM [SimplifiedLLM]
            CallShell [CallShell]
            CommitChanges [CommitChanges]
            GitHubAgent [GitHubAgent]
            ExtractPackageManagerFile [ExtractPackageManagerFile]
            README1 --> |Documentation| steps
            init --> |Initialization| steps
            ExtractCodeMethodForCommentContexts --> ExtractCodeMethodForCommentContexts.ts
        
            PreparePrompt --> PreparePrompt.ts
        
            ExtractCodeContexts --> ExtractCodeContexts.ts
        
            ReadPRs --> ReadPRs.ts
        
            SlackMessage --> SlackMessage.ts
        
            CallAPI --> CallAPI.ts
        
            SendEmail --> SendEmail.ts
        
            CallLLM --> CallLLM.ts
        
            ReadFile --> ReadFile.ts
        
            AgenticLLM --> AgenticLLM.ts
        
            LLM --> LLM.ts
        
            ScanSemgrep --> ScanSemgrep.ts
        
            Combine --> Combine.ts
        
            ReadIssues --> ReadIssues.ts
        
            FixIssue --> FixIssue.ts
        
            FilterBySimilarity --> FilterBySimilarity.ts
        
            ExtractCode --> ExtractCode.ts
        
            AnalyzeImpact --> AnalyzeImpact.ts
        
            ExtractModelResponse --> ExtractModelResponse.ts
        
            CreateIssue --> CreateIssue.ts
        
            ScanSonar --> ScanSonar.ts
        
            PR --> PR.ts
        
            CallSQL --> CallSQL.ts
        
            ModifyCodeOnce --> ModifyCodeOnce.ts
        
            CreateIssueComment --> CreateIssueComment.ts
        
            BrowserUse --> BrowserUse.ts
        
            CallCode2Prompt --> CallCode2Prompt.ts
        
            PreparePR --> PreparePR.ts
        
            JoinList --> JoinList.ts
        
            CreatePR --> CreatePR.ts
        
            ScanDepscan --> ScanDepscan.ts
        
            SimplifiedLLMOnce --> SimplifiedLLMOnce.ts
        
            ModifyCode --> ModifyCode.ts
        
            ManageEngineAgent --> ManageEngineAgent.ts
        
            AgenticLLMV2 --> AgenticLLMV2.ts
        
            ExtractDiff --> ExtractDiff.ts
        
            ReadEmail --> ReadEmail.ts
        
            CreatePRComment --> CreatePRComment.ts
        
            ReadPRDiffs --> ReadPRDiffs.ts
        
            SimplifiedLLM --> SimplifiedLLM.ts
        
            CallShell --> CallShell.ts
        
            CommitChanges --> CommitChanges.ts
        
            GitHubAgent --> GitHubAgent.ts
        
            ExtractPackageManagerFile --> ExtractPackageManagerFile.ts
        
        end
    end
