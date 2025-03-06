stateDiagram
    state Patchwork {
        state Steps {
            [*] --> ExtractCodeMethodForCommentContexts : import
            [*] --> PreparePrompt : import
            [*] --> ExtractCodeContexts : import
            [*] --> ReadPRs : import
            [*] --> SlackMessage : import
            [*] --> CallAPI : import
            [*] --> SendEmail : import
            [*] --> CallLLM : import
            [*] --> ReadFile : import
            [*] --> AgenticLLM : import
            [*] --> LLM : import
            [*] --> ScanSemgrep : import
            [*] --> Combine : import
            [*] --> ReadIssues : import
            [*] --> FixIssue : import
            [*] --> FilterBySimilarity : import
            [*] --> ExtractCode : import
            [*] --> AnalyzeImpact : import
            [*] --> ExtractModelResponse : import
            [*] --> CreateIssue : import
            [*] --> ScanSonar : import
            [*] --> PR : import
            [*] --> CallSQL : import
            [*] --> ModifyCodeOnce : import
            [*] --> GetTypescriptTypeInfo : import
            [*] --> CreateIssueComment : import
            [*] --> BrowserUse : import
            [*] --> CallCode2Prompt : import
            [*] --> PreparePR : import
            [*] --> JoinList : import
            [*] --> CreatePR : import
            [*] --> ScanDepscan : import
            [*] --> SimplifiedLLMOnce : import
            [*] --> ModifyCode : import
            [*] --> ManageEngineAgent : import
            [*] --> AgenticLLMV2 : import
            [*] --> ExtractDiff : import
            [*] --> ReadEmail : import
            [*] --> CreatePRComment : import
            [*] --> ReadPRDiffs : import
            [*] --> SimplifiedLLM : import
            [*] --> CallShell : import
            [*] --> CommitChanges : import
            [*] --> GitHubAgent : import
            [*] --> ExtractPackageManagerFile : import
        }

        ExtractCodeMethodForCommentContexts --> LLM : uses
        PreparePrompt --> LLM : uses
        ExtractCodeContexts --> ExtractCodeMethodForCommentContexts : uses
        ReadPRs --> CallAPI : uses
        Merge : Steps --> Patchwork

        ExtractModelResponse --> LLM : used by
        PreparePR --> PR : uses
        SimplifiedLLM --> SimplifiedLLMOnce : uses
        CallCode2Prompt --> CallLLM : uses
        CallLLM --> LLM : extended by
        ReadPRDiffs --> ReadPRs : extended by
        CreatePRComment --> CreatePR : extended by
        SendEmail --> SlackMessage : dependency
        GitHubAgent --> ManageEngineAgent : dependency
        Dashboard : PR --> Patchwork

        Merge --> Dashboard : uses
    }
