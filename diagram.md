graph TD
    subgraph Patchwork Steps
        style Patchwork Steps fill:#f9f,stroke:#333,stroke-width:2px;
        ReadMe[patchwork/steps/README.md]
        InitSteps[patchwork/steps/__init__.py]
        InitSteps --> ReadMe

        subgraph ScanSemgrep[patchwork/steps/ScanSemgrep]
            ScanSemgrepTyped(typed.py)
            ScanSemgrepRead(README.md)
            ScanSemgrepInit(__init__.py)
            ScanSemgrepPy(ScanSemgrep.py)
            ScanSemgrepTyped --> ScanSemgrepInit
            ScanSemgrepInit --> ScanSemgrepPy
        end
        InitSteps --> ScanSemgrep

        subgraph ModifyCode[patchwork/steps/ModifyCode]
            ModifyCodeTyped(typed.py)
            ModifyCodeRead(README.md)
            ModifyCodeInit(__init__.py)
            ModifyCodePy(ModifyCode.py)
            ModifyCodeTyped --> ModifyCodeInit
            ModifyCodeInit --> ModifyCodePy
        end
        InitSteps --> ModifyCode

        subgraph PreparePrompt[patchwork/steps/PreparePrompt]
            PreparePromptTyped(typed.py)
            PreparePromptRead(README.md)
            PreparePromptInit(__init__.py)
            PreparePromptPy(PreparePrompt.py)
            PreparePromptTyped --> PreparePromptInit
            PreparePromptInit --> PreparePromptPy
        end
        InitSteps --> PreparePrompt

        subgraph CallLLM[patchwork/steps/CallLLM]
            CallLLMTyped(typed.py)
            CallLLMRead(README.md)
            CallLLMInit(__init__.py)
            CallLLMPy(CallLLM.py)
            CallLLMTyped --> CallLLMInit
            CallLLMInit --> CallLLMPy
        end
        InitSteps --> CallLLM

        subgraph Combine[patchwork/steps/Combine]
            CombineTyped(typed.py)
            CombineRead(README.md)
            CombineInit(__init__.py)
            CombinePy(Combine.py)
            CombineTyped --> CombineInit
            CombineInit --> CombinePy
        end
        InitSteps --> Combine

        subgraph CreateIssueComment[patchwork/steps/CreateIssueComment]
            CreateIssueCommentTyped(typed.py)
            CreateIssueCommentRead(README.md)
            CreateIssueCommentInit(__init__.py)
            CreateIssueCommentPy(CreateIssueComment.py)
            CreateIssueCommentTyped --> CreateIssueCommentInit
            CreateIssueCommentInit --> CreateIssueCommentPy
        end
        InitSteps --> CreateIssueComment

        subgraph CommitChanges[patchwork/steps/CommitChanges]
            CommitChangesTyped(typed.py)
            CommitChangesRead(README.md)
            CommitChangesInit(__init__.py)
            CommitChangesPy(CommitChanges.py)
            CommitChangesTyped --> CommitChangesInit
            CommitChangesInit --> CommitChangesPy
        end
        InitSteps --> CommitChanges

        subgraph PreparePR[patchwork/steps/PreparePR]
            PreparePRTyped(typed.py)
            PreparePRRead(README.md)
            PreparePRInit(__init__.py)
            PreparePRPy(PreparePR.py)
            PreparePRTyped --> PreparePRInit
            PreparePRInit --> PreparePRPy
        end
        InitSteps --> PreparePR

        subgraph ReadPRs[patchwork/steps/ReadPRs]
            ReadPRsTyped(typed.py)
            ReadPRsRead(README.md)
            ReadPRsInit(__init__.py)
            ReadPRsPy(ReadPRs.py)
            ReadPRsTyped --> ReadPRsInit
            ReadPRsInit --> ReadPRsPy
        end
        InitSteps --> ReadPRs

        subgraph GetTypescriptTypeInfo[patchwork/steps/GetTypescriptTypeInfo]
            GTTITyped(typed.py)
            GTTIPnpm(pnpm-lock.yaml)
            GTTIRead(README.md)
            GTTIInit(__init__.py)
            GTTIPackage(package.json)
            GTTIGet(get_type_info.ts)
            GTTITsconfig(tsconfig.json)
            GTTIPy(GetTypescriptTypeInfo.py)
            GTTITyped --> GTTIInit
            GTTIPackage --> GTTIGet
            GTTIGet --> GTTIPy
        end
        InitSteps --> GetTypescriptTypeInfo

        subgraph QueryEmbeddings[patchwork/steps/QueryEmbeddings]
            QueryEmbeddingsTyped(typed.py)
            QueryEmbeddingsRead(README.md)
            QueryEmbeddingsInit(__init__.py)
            QueryEmbeddingsPy(QueryEmbeddings.py)
            QueryEmbeddingsTyped --> QueryEmbeddingsInit
            QueryEmbeddingsInit --> QueryEmbeddingsPy
        end
        InitSteps --> QueryEmbeddings

        subgraph ExtractCodeContexts[patchwork/steps/ExtractCodeContexts]
            ExtractCodeContextsTyped(typed.py)
            ExtractCodeContextsRead(README.md)
            ExtractCodeContextsInit(__init__.py)
            ExtractCodeContextsPy(ExtractCodeContexts.py)
            ExtractCodeContextsTyped --> ExtractCodeContextsInit
            ExtractCodeContextsInit --> ExtractCodeContextsPy
        end
        InitSteps --> ExtractCodeContexts

        subgraph GenerateCodeRepositoryEmbeddings[patchwork/steps/GenerateCodeRepositoryEmbeddings]
            GCREGeneratePy(GenerateCodeRepositoryEmbeddings.py)
            GCRETyped(typed.py)
            GCRERead(README.md)
            GCREFilter(filter_lists.py)
            GCREInit(__init__.py)
            GCREGeneratePy --> GCREInit
        end
        InitSteps --> GenerateCodeRepositoryEmbeddings

        subgraph ExtractDiff[patchwork/steps/ExtractDiff]
            ExtractDiffTyped(typed.py)
            ExtractDiffRead(README.md)
            ExtractDiffInit(__init__.py)
            ExtractDiffPy(ExtractDiff.py)
            ExtractDiffTyped --> ExtractDiffInit
            ExtractDiffInit --> ExtractDiffPy
        end
        InitSteps --> ExtractDiff

        subgraph FixIssue[patchwork/steps/FixIssue]
            FixIssueTyped(typed.py)
            FixIssueRead(README.md)
            FixIssueInit(__init__.py)
            FixIssuePy(FixIssue.py)
            FixIssueTyped --> FixIssueInit
            FixIssueInit --> FixIssuePy
        end
        InitSteps --> FixIssue

        subgraph CallCode2Prompt[patchwork/steps/CallCode2Prompt]
            CallCode2PromptTyped(typed.py)
            CallCode2PromptRead(README.md)
            CallCode2PromptInit(__init__.py)
            CallCode2PromptTest(TestCallCode2Prompt.py)
            CallCode2PromptPy(CallCode2Prompt.py)
            CallCode2PromptTyped --> CallCode2PromptInit
            CallCode2PromptInit --> CallCode2PromptPy
        end
        InitSteps --> CallCode2Prompt

        subgraph SimplifiedLLMOnce[patchwork/steps/SimplifiedLLMOnce]
            SimplifiedLLMOnceTyped(typed.py)
            SimplifiedLLMOnceRead(README.md)
            SimplifiedLLMOnceInit(__init__.py)
            SimplifiedLLMOncePy(SimplifiedLLMOnce.py)
            SimplifiedLLMOnceTyped --> SimplifiedLLMOnceInit
            SimplifiedLLMOnceInit --> SimplifiedLLMOncePy
        end
        InitSteps --> SimplifiedLLMOnce

        subgraph CreatePRComment[patchwork/steps/CreatePRComment]
            CreatePRCommentTyped(typed.py)
            CreatePRCommentRead(README.md)
            CreatePRCommentInit(__init__.py)
            CreatePRCommentPy(CreatePRComment.py)
            CreatePRCommentTyped --> CreatePRCommentInit
            CreatePRCommentInit --> CreatePRCommentPy
        end
        InitSteps --> CreatePRComment

        subgraph ReadPRDiffs[patchwork/steps/ReadPRDiffs]
            ReadPRDiffsTyped(typed.py)
            ReadPRDiffsRead(README.md)
            ReadPRDiffsInit(__init__.py)
            ReadPRDiffsPy(ReadPRDiffs.py)
            ReadPRDiffsTyped --> ReadPRDiffsInit
            ReadPRDiffsInit --> ReadPRDiffsPy
        end
        InitSteps --> ReadPRDiffs

        subgraph AnalyzeImpact[patchwork/steps/AnalyzeImpact]
            AnalyzeImpactTyped(typed.py)
            AnalyzeImpactRead(README.md)
            AnalyzeImpactInit(__init__.py)
            AnalyzeImpactPy(AnalyzeImpact.py)
            AnalyzeImpactTyped --> AnalyzeImpactInit
            AnalyzeImpactInit --> AnalyzeImpactPy
        end
        InitSteps --> AnalyzeImpact

        subgraph FilterBySimilarity[patchwork/steps/FilterBySimilarity]
            FilterBySimilarityTyped(typed.py)
            FilterBySimilarityRead(README.md)
            FilterBySimilarityInit(__init__.py)
            FilterBySimilarityPy(FilterBySimilarity.py)
            FilterBySimilarityTyped --> FilterBySimilarityInit
            FilterBySimilarityInit --> FilterBySimilarityPy
        end
        InitSteps --> FilterBySimilarity

        subgraph ExtractCode[patchwork/steps/ExtractCode]
            ExtractCodeTyped(typed.py)
            ExtractCodeRead(README.md)
            ExtractCodeInit(__init__.py)
            ExtractCodePy(ExtractCode.py)
            ExtractCodeTyped --> ExtractCodeInit
            ExtractCodeInit --> ExtractCodePy
        end
        InitSteps --> ExtractCode

        subgraph CreatePR[patchwork/steps/CreatePR]
            CreatePRTyped(typed.py)
            CreatePRRead(README.md)
            CreatePRInit(__init__.py)
            CreatePRPy(CreatePR.py)
            CreatePRTyped --> CreatePRInit
            CreatePRInit --> CreatePRPy
        end
        InitSteps --> CreatePR

        subgraph LLM[patchwork/steps/LLM]
            LLMTyped(typed.py)
            LLMRead(README.md)
            LLMInit(__init__.py)
            LLMPy(LLM.py)
            LLMTyped --> LLMInit
            LLMInit --> LLMPy
        end
        InitSteps --> LLM

        subgraph PR[patchwork/steps/PR]
            PRTyped(typed.py)
            PRRead(README.md)
            PRInit(__init__.py)
            PRPy(PR.py)
            PRTyped --> PRInit
            PRInit --> PRPy
        end
        InitSteps --> PR

        subgraph CallSQL[patchwork/steps/CallSQL]
            CallSQLTyped(typed.py)
            CallSQLInit(__init__.py)
            CallSQLPy(CallSQL.py)
            CallSQLTyped --> CallSQLInit
            CallSQLInit --> CallSQLPy
        end
        InitSteps --> CallSQL

        subgraph ExtractCodeMethodForCommentContexts[patchwork/steps/ExtractCodeMethodForCommentContexts]
            ECMFCCPy(ExtractCodeMethodForCommentContexts.py)
            ECMFCCTyped(typed.py)
            ECMFCCRead(README.md)
            ECMFCCInit(__init__.py)
            ECMFCCTyped --> ECMFCCInit
            ECMFCCInit --> ECMFCCPy
        end
        InitSteps --> ExtractCodeMethodForCommentContexts

        subgraph CreateIssue[patchwork/steps/CreateIssue]
            CreateIssueTyped(typed.py)
            CreateIssueRead(README.md)
            CreateIssueInit(__init__.py)
            CreateIssuePy(CreateIssue.py)
            CreateIssueTyped --> CreateIssueInit
            CreateIssueInit --> CreateIssuePy
        end
        InitSteps --> CreateIssue

        subgraph ModifyCodeOnce[patchwork/steps/ModifyCodeOnce]
            ModifyCodeOnceTyped(typed.py)
            ModifyCodeOnceRead(README.md)
            ModifyCodeOnceInit(__init__.py)
            ModifyCodeOncePy(ModifyCodeOnce.py)
            ModifyCodeOnceTyped --> ModifyCodeOnceInit
            ModifyCodeOnceInit --> ModifyCodeOncePy
        end
        InitSteps --> ModifyCodeOnce

        subgraph ExtractModelResponse[patchwork/steps/ExtractModelResponse]
            ExtractModelResponseTyped(typed.py)
            ExtractModelResponseRead(README.md)
            ExtractModelResponseInit(__init__.py)
            ExtractModelResponsePy(ExtractModelResponse.py)
            ExtractModelResponseTyped --> ExtractModelResponseInit
            ExtractModelResponseInit --> ExtractModelResponsePy
        end
        InitSteps --> ExtractModelResponse

        subgraph JoinList[patchwork/steps/JoinList]
            JoinListTyped(typed.py)
            JoinListRead(README.md)
            JoinListInit(__init__.py)
            JoinListPy(JoinList.py)
            JoinListTyped --> JoinListInit
            JoinListInit --> JoinListPy
        end
        InitSteps --> JoinList

        subgraph SimplifiedLLM[patchwork/steps/SimplifiedLLM]
            SimplifiedLLMTyped(typed.py)
            SimplifiedLLMRead(README.md)
            SimplifiedLLMInit(__init__.py)
            SimplifiedLLMPy(SimplifiedLLM.py)
            SimplifiedLLMTyped --> SimplifiedLLMInit
            SimplifiedLLMInit --> SimplifiedLLMPy
        end
        InitSteps --> SimplifiedLLM

        subgraph CallAPI[patchwork/steps/CallAPI]
            CallAPITyped(typed.py)
            CallAPIRead(README.md)
            CallAPIInit(__init__.py)
            CallAPIPy(CallAPI.py)
            CallAPITyped --> CallAPIInit
            CallAPIInit --> CallAPIPy
        end
        InitSteps --> CallAPI

        subgraph ExtractPackageManagerFile[patchwork/steps/ExtractPackageManagerFile]
            EPMFTyped(typed.py)
            EPMFRead(README.md)
            EPMFInit(__init__.py)
            EPMFTest(TestExtractPackageManagerFile.py)
            EPMFPy(ExtractPackageManagerFile.py)
            EPMFTyped --> EPMFInit
            EPMFInit --> EPMFPy
        end
        InitSteps --> ExtractPackageManagerFile

        subgraph ReadIssues[patchwork/steps/ReadIssues]
            ReadIssuesTyped(typed.py)
            ReadIssuesRead(README.md)
            ReadIssuesInit(__init__.py)
            ReadIssuesPy(ReadIssues.py)
            ReadIssuesTyped --> ReadIssuesInit
            ReadIssuesInit --> ReadIssuesPy
        end
        InitSteps --> ReadIssues

        subgraph ReadFile[patchwork/steps/ReadFile]
            ReadFileTyped(typed.py)
            ReadFileRead(README.md)
            ReadFileInit(__init__.py)
            ReadFilePy(ReadFile.py)
            ReadFileTyped --> ReadFileInit
            ReadFileInit --> ReadFilePy
        end
        InitSteps --> ReadFile

        subgraph ScanSonar[patchwork/steps/ScanSonar]
            ScanSonarTyped(typed.py)
            ScanSonarRead(README.md)
            ScanSonarInit(__init__.py)
            ScanSonarPy(ScanSonar.py)
            ScanSonarTyped --> ScanSonarInit
            ScanSonarInit --> ScanSonarPy
        end
        InitSteps --> ScanSonar

        subgraph GenerateEmbeddings[patchwork/steps/GenerateEmbeddings]
            GenerateEmbeddingsTyped(typed.py)
            GenerateEmbeddingsRead(README.md)
            GenerateEmbeddingsInit(__init__.py)
            GenerateEmbeddingsPy(GenerateEmbeddings.py)
            GenerateEmbeddingsTyped --> GenerateEmbeddingsInit
            GenerateEmbeddingsInit --> GenerateEmbeddingsPy
        end
        InitSteps --> GenerateEmbeddings

        subgraph AgenticLLM[patchwork/steps/AgenticLLM]
            AgenticLLMTyped(typed.py)
            AgenticLLMInit(__init__.py)
            AgenticLLMPy(AgenticLLM.py)
            AgenticLLMTyped --> AgenticLLMInit
            AgenticLLMInit --> AgenticLLMPy
        end
        InitSteps --> AgenticLLM

        subgraph ScanDepscan[patchwork/steps/ScanDepscan]
            ScanDepscanTyped(typed.py)
            ScanDepscanRead(README.md)
            ScanDepscanInit(__init__.py)
            ScanDepscanPy(ScanDepscan.py)
            ScanDepscanTyped --> ScanDepscanInit
            ScanDepscanInit --> ScanDepscanPy
        end
        InitSteps --> ScanDepscan

        subgraph SlackMessage[patchwork/steps/SlackMessage]
            SlackMessageTyped(typed.py)
            SlackMessageRead(README.md)
            SlackMessageInit(__init__.py)
            SlackMessagePy(SlackMessage.py)
            SlackMessageTyped --> SlackMessageInit
            SlackMessageInit --> SlackMessagePy
        end
        InitSteps --> SlackMessage

        subgraph CallShell[patchwork/steps/CallShell]
            CallShellTyped(typed.py)
            CallShellInit(__init__.py)
            CallShellPy(CallShell.py)
            CallShellTyped --> CallShellInit
            CallShellInit --> CallShellPy
        end
        InitSteps --> CallShell
    end
