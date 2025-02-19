graph TB
    subgraph patchwork/steps
        subgraph LLM
            LLM.py
            typed.py
            init.py
            README.md
        end
        subgraph CallCode2Prompt
            CallCode2Prompt.py
            TestCallCode2Prompt.py
            typed.py
            init.py
            README.md
        end
        subgraph GenerateCodeRepositoryEmbeddings
            GenerateCodeRepositoryEmbeddings.py
            filter_lists.py
            typed.py
            init.py
            README.md
        end
        subgraph ScanSemgrep
            ScanSemgrep.py
            typed.py
            init.py
            README.md
        end
        subgraph GetTypescriptTypeInfo
            get_type_info.ts
            GetTypescriptTypeInfo.py
            tsconfig.json
            package.json
            pnpm-lock.yaml
            typed.py
            init.py
            README.md
        end
        subgraph ExtractCodeMethodForCommentContexts
            ExtractCodeMethodForCommentContexts.py
            typed.py
            init.py
            README.md
        end
        subgraph ExtractModelResponse
            ExtractModelResponse.py
            typed.py
            init.py
            README.md
        end
        subgraph GenerateEmbeddings
            GenerateEmbeddings.py
            typed.py
            init.py
            README.md
        end
        subgraph PR
            PR.py
            typed.py
            init.py
            README.md
        end
        subgraph SlackMessage
            SlackMessage.py
            typed.py
            init.py
            README.md
        end
        subgraph PreparePR
            PreparePR.py
            typed.py
            init.py
            README.md
        end
        subgraph ModifyCodeOnce
            ModifyCodeOnce.py
            typed.py
            init.py
            README.md
        end
        subgraph CreatePRComment
            CreatePRComment.py
            typed.py
            init.py
            README.md
        end
        subgraph CallShell
            CallShell.py
            typed.py
            init.py
            README.md
        end
        subgraph FixIssue
            FixIssue.py
            typed.py
            init.py
            README.md
        end
        subgraph ScanSonar
            ScanSonar.py
            typed.py
            init.py
            README.md
        end
        subgraph CreateIssue
            CreateIssue.py
            typed.py
            init.py
            README.md
        end
        subgraph FilterBySimilarity
            FilterBySimilarity.py
            typed.py
            init.py
            README.md
        end
        subgraph ReadPRDiffs
            ReadPRDiffs.py
            typed.py
            init.py
            README.md
        end
        subgraph AgenticLLM
            AgenticLLM.py
            typed.py
            init.py
            README.md
        end
        subgraph CommitChanges
            CommitChanges.py
            typed.py
            init.py
            README.md
        end
        subgraph SimplifiedLLMOnce
            SimplifiedLLMOnce.py
            typed.py
            init.py
            README.md
        end
        subgraph ExtractPackageManagerFile
            ExtractPackageManagerFile.py
            TestExtractPackageManagerFile.py
            typed.py
            init.py
            README.md
        end
        subgraph ReadEmail
            ReadEmail.py
            typed.py
            init.py
            README.md
        end
        subgraph ModifyCode
            ModifyCode.py
            typed.py
            init.py
            README.md
        end
        subgraph JoinList
            JoinList.py
            typed.py
            init.py
            README.md
        end
        subgraph CallAPI
            CallAPI.py
            typed.py
            init.py
            README.md
        end
        subgraph CreatePR
            CreatePR.py
            typed.py
            init.py
            README.md
        end
        subgraph ReadIssues
            ReadIssues.py
            typed.py
            init.py
            README.md
        end
        subgraph ReadFile
            ReadFile.py
            typed.py
            init.py
            README.md
        end
        subgraph CallLLM
            CallLLM.py
            typed.py
            init.py
            README.md
        end
        subgraph CallSQL
            CallSQL.py
            typed.py
            init.py
            README.md
        end
        subgraph ScanDepscan
            ScanDepscan.py
            typed.py
            init.py
            README.md
        end
        subgraph ExtractDiff
            ExtractDiff.py
            typed.py
            init.py
            README.md
        end
        subgraph QueryEmbeddings
            QueryEmbeddings.py
            typed.py
            init.py
            README.md
        end
        subgraph SendEmail
            SendEmail.py
            typed.py
            init.py
            README.md
        end
        subgraph Combine
            Combine.py
            typed.py
            init.py
            README.md
        end
        subgraph SimplifiedLLM
            SimplifiedLLM.py
            typed.py
            init.py
            README.md
        end
        subgraph ReadPRs
            ReadPRs.py
            typed.py
            init.py
            README.md
        end
        subgraph ExtractCodeContexts
            ExtractCodeContexts.py
            typed.py
            init.py
            README.md
        end
        subgraph AnalyzeImpact
            AnalyzeImpact.py
            typed.py
            init.py
            README.md
        end
        subgraph PreparePrompt
            PreparePrompt.py
            typed.py
            init.py
            README.md
        end
        subgraph CreateIssueComment
            CreateIssueComment.py
            typed.py
            init.py
            README.md
        end
        subgraph ExtractCode
            ExtractCode.py
            typed.py
            init.py
            README.md
        end
        README.md
        init.py
    end
