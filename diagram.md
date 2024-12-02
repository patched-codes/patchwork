flowchart TD
    subgraph patchwork/steps
        direction TB
        subgraph GetTypescriptTypeInfo
            GetTypescriptTypeInfo.tsconfig.json["tsconfig.json"]
            GetTypescriptTypeInfo.package.json["package.json"]
            GetTypescriptTypeInfo.pnpm-lock.yaml["pnpm-lock.yaml"]
            GetTypescriptTypeInfo.get_type_info.ts["get_type_info.ts"]
            GetTypescriptTypeInfo.typed.py["typed.py"]
            GetTypescriptTypeInfo.init.py["__init__.py"]
            GetTypescriptTypeInfo.readme.md["README.md"]
            GetTypescriptTypeInfo.GetTypescriptTypeInfo.py["GetTypescriptTypeInfo.py"]
        end

        subgraph ExtractCodeMethodForCommentContexts
            ExtractCodeMethodForCommentContexts.typed.py["typed.py"]
            ExtractCodeMethodForCommentContexts.init.py["__init__.py"]
            ExtractCodeMethodForCommentContexts.readme.md["README.md"]
            ExtractCodeMethodForCommentContexts.ExtractCodeMethodForCommentContexts.py["ExtractCodeMethodForCommentContexts.py"]
        end

        subgraph ScanDepscan
            ScanDepscan.typed.py["typed.py"]
            ScanDepscan.init.py["__init__.py"]
            ScanDepscan.readme.md["README.md"]
            ScanDepscan.ScanDepscan.py["ScanDepscan.py"]
        end

        subgraph PreparePR
            PreparePR.typed.py["typed.py"]
            PreparePR.init.py["__init__.py"]
            PreparePR.readme.md["README.md"]
            PreparePR.PreparePR.py["PreparePR.py"]
        end

        subgraph SimplifiedLLMOnce
            SimplifiedLLMOnce.typed.py["typed.py"]
            SimplifiedLLMOnce.init.py["__init__.py"]
            SimplifiedLLMOnce.readme.md["README.md"]
            SimplifiedLLMOnce.SimplifiedLLMOnce.py["SimplifiedLLMOnce.py"]
        end

        subgraph ExtractCode
            ExtractCode.typed.py["typed.py"]
            ExtractCode.init.py["__init__.py"]
            ExtractCode.readme.md["README.md"]
            ExtractCode.ExtractCode.py["ExtractCode.py"]
        end

        subgraph ModifyCodeOnce
            ModifyCodeOnce.typed.py["typed.py"]
            ModifyCodeOnce.init.py["__init__.py"]
            ModifyCodeOnce.readme.md["README.md"]
            ModifyCodeOnce.ModifyCodeOnce.py["ModifyCodeOnce.py"]
        end

        subgraph AnalyzeImpact
            AnalyzeImpact.typed.py["typed.py"]
            AnalyzeImpact.init.py["__init__.py"]
            AnalyzeImpact.readme.md["README.md"]
            AnalyzeImpact.AnalyzeImpact.py["AnalyzeImpact.py"]
        end

        subgraph SimplifiedLLM
            SimplifiedLLM.typed.py["typed.py"]
            SimplifiedLLM.init.py["__init__.py"]
            SimplifiedLLM.readme.md["README.md"]
            SimplifiedLLM.SimplifiedLLM.py["SimplifiedLLM.py"]
        end

        subgraph Combine
            Combine.typed.py["typed.py"]
            Combine.init.py["__init__.py"]
            Combine.readme.md["README.md"]
            Combine.Combine.py["Combine.py"]
        end

        subgraph ExtractPackageManagerFile
            ExtractPackageManagerFile.typed.py["typed.py"]
            ExtractPackageManagerFile.init.py["__init__.py"]
            ExtractPackageManagerFile.readme.md["README.md"]
            ExtractPackageManagerFile.TestExtractPackageManagerFile.py["TestExtractPackageManagerFile.py"]
            ExtractPackageManagerFile.ExtractPackageManagerFile.py["ExtractPackageManagerFile.py"]
        end

        subgraph CallAPI
            CallAPI.typed.py["typed.py"]
            CallAPI.init.py["__init__.py"]
            CallAPI.readme.md["README.md"]
            CallAPI.CallAPI.py["CallAPI.py"]
        end

        subgraph ReadFile
            ReadFile.typed.py["typed.py"]
            ReadFile.init.py["__init__.py"]
            ReadFile.readme.md["README.md"]
            ReadFile.ReadFile.py["ReadFile.py"]
        end

        subgraph QueryEmbeddings
            QueryEmbeddings.typed.py["typed.py"]
            QueryEmbeddings.init.py["__init__.py"]
            QueryEmbeddings.readme.md["README.md"]
            QueryEmbeddings.QueryEmbeddings.py["QueryEmbeddings.py"]
        end

        subgraph GenerateCodeRepositoryEmbeddings
            GenerateCodeRepositoryEmbeddings.typed.py["typed.py"]
            GenerateCodeRepositoryEmbeddings.init.py["__init__.py"]
            GenerateCodeRepositoryEmbeddings.readme.md["README.md"]
            GenerateCodeRepositoryEmbeddings.filter_lists.py["filter_lists.py"]
            GenerateCodeRepositoryEmbeddings.GenerateCodeRepositoryEmbeddings.py["GenerateCodeRepositoryEmbeddings.py"]
        end

        subgraph CreateIssueComment
            CreateIssueComment.typed.py["typed.py"]
            CreateIssueComment.init.py["__init__.py"]
            CreateIssueComment.readme.md["README.md"]
            CreateIssueComment.CreateIssueComment.py["CreateIssueComment.py"]
        end

        subgraph ExtractModelResponse
            ExtractModelResponse.typed.py["typed.py"]
            ExtractModelResponse.init.py["__init__.py"]
            ExtractModelResponse.readme.md["README.md"]
            ExtractModelResponse.ExtractModelResponse.py["ExtractModelResponse.py"]
        end

        subgraph ReadPRDiffs
            ReadPRDiffs.typed.py["typed.py"]
            ReadPRDiffs.init.py["__init__.py"]
            ReadPRDiffs.readme.md["README.md"]
            ReadPRDiffs.ReadPRDiffs.py["ReadPRDiffs.py"]
        end

        subgraph FilterBySimilarity
            FilterBySimilarity.typed.py["typed.py"]
            FilterBySimilarity.init.py["__init__.py"]
            FilterBySimilarity.readme.md["README.md"]
            FilterBySimilarity.FilterBySimilarity.py["FilterBySimilarity.py"]
        end

        subgraph CreateIssue
            CreateIssue.typed.py["typed.py"]
            CreateIssue.init.py["__init__.py"]
            CreateIssue.readme.md["README.md"]
            CreateIssue.CreateIssue.py["CreateIssue.py"]
        end

        subgraph PR
            PR.typed.py["typed.py"]
            PR.init.py["__init__.py"]
            PR.readme.md["README.md"]
            PR.PR.py["PR.py"]
        end

        subgraph JoinList
            JoinList.typed.py["typed.py"]
            JoinList.init.py["__init__.py"]
            JoinList.readme.md["README.md"]
            JoinList.JoinList.py["JoinList.py"]
        end

        subgraph ExtractCodeContexts
            ExtractCodeContexts.typed.py["typed.py"]
            ExtractCodeContexts.init.py["__init__.py"]
            ExtractCodeContexts.readme.md["README.md"]
            ExtractCodeContexts.ExtractCodeContexts.py["ExtractCodeContexts.py"]
        end

        subgraph CommitChanges
            CommitChanges.typed.py["typed.py"]
            CommitChanges.init.py["__init__.py"]
            CommitChanges.readme.md["README.md"]
            CommitChanges.CommitChanges.py["CommitChanges.py"]
        end

        subgraph ScanSemgrep
            ScanSemgrep.typed.py["typed.py"]
            ScanSemgrep.init.py["__init__.py"]
            ScanSemgrep.readme.md["README.md"]
            ScanSemgrep.ScanSemgrep.py["ScanSemgrep.py"]
        end

        subgraph CallLLM
            CallLLM.typed.py["typed.py"]
            CallLLM.init.py["__init__.py"]
            CallLLM.readme.md["README.md"]
            CallLLM.CallLLM.py["CallLLM.py"]
        end

        subgraph ReadPRs
            ReadPRs.typed.py["typed.py"]
            ReadPRs.init.py["__init__.py"]
            ReadPRs.readme.md["README.md"]
            ReadPRs.ReadPRs.py["ReadPRs.py"]
        end

        subgraph ModifyCode
            ModifyCode.typed.py["typed.py"]
            ModifyCode.init.py["__init__.py"]
            ModifyCode.readme.md["README.md"]
            ModifyCode.ModifyCode.py["ModifyCode.py"]
        end

        subgraph GenerateEmbeddings
            GenerateEmbeddings.typed.py["typed.py"]
            GenerateEmbeddings.init.py["__init__.py"]
            GenerateEmbeddings.readme.md["README.md"]
            GenerateEmbeddings.GenerateEmbeddings.py["GenerateEmbeddings.py"]
        end

        subgraph ReadIssues
            ReadIssues.typed.py["typed.py"]
            ReadIssues.init.py["__init__.py"]
            ReadIssues.readme.md["README.md"]
            ReadIssues.ReadIssues.py["ReadIssues.py"]
        end

        subgraph ExtractDiff
            ExtractDiff.typed.py["typed.py"]
            ExtractDiff.init.py["__init__.py"]
            ExtractDiff.readme.md["README.md"]
            ExtractDiff.ExtractDiff.py["ExtractDiff.py"]
        end

        subgraph LLM
            LLM.typed.py["typed.py"]
            LLM.init.py["__init__.py"]
            LLM.readme.md["README.md"]
            LLM.LLM.py["LLM.py"]
        end

        subgraph CallCode2Prompt
            CallCode2Prompt.typed.py["typed.py"]
            CallCode2Prompt.init.py["__init__.py"]
            CallCode2Prompt.readme.md["README.md"]
            CallCode2Prompt.TestCallCode2Prompt.py["TestCallCode2Prompt.py"]
            CallCode2Prompt.CallCode2Prompt.py["CallCode2Prompt.py"]
        end

        subgraph CreatePRComment
            CreatePRComment.typed.py["typed.py"]
            CreatePRComment.init.py["__init__.py"]
            CreatePRComment.readme.md["README.md"]
            CreatePRComment.CreatePRComment.py["CreatePRComment.py"]
        end

        subgraph SlackMessage
            SlackMessage.typed.py["typed.py"]
            SlackMessage.init.py["__init__.py"]
            SlackMessage.readme.md["README.md"]
            SlackMessage.SlackMessage.py["SlackMessage.py"]
        end

        subgraph CreatePR
            CreatePR.typed.py["typed.py"]
            CreatePR.init.py["__init__.py"]
            CreatePR.readme.md["README.md"]
            CreatePR.CreatePR.py["CreatePR.py"]
        end

        subgraph PreparePrompt
            PreparePrompt.typed.py["typed.py"]
            PreparePrompt.init.py["__init__.py"]
            PreparePrompt.readme.md["README.md"]
            PreparePrompt.PreparePrompt.py["PreparePrompt.py"]
        end

        patchwork.steps.init.py["patchwork/steps/__init__.py"]
        patchwork.steps.readme.md["patchwork/steps/README.md"]
    end

    classDef directory fill:#f9f,stroke:#333,stroke-width:2px;
    classDef module fill:#bbf,stroke:#333,stroke-width:2px;
    classDef file fill:#f96,stroke:#333,stroke-width:2px;

    patchwork/steps init.py,readme.md
    patchwork/steps init.py:::file
    patchwork/steps readme.md:::file

    linkStyle default interpolate basis
