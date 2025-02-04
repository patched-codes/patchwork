flowchart TB
    subgraph patchwork
        subgraph steps
            subgraph ReadPRs
                direction TB
                ReadPRs_py[ReadPRs.py]
                ReadPRs_init[__init__.py]
                ReadPRs_typed[typed.py]
            end
            subgraph ModifyCodeOnce
                direction TB
                ModifyCodeOnce_py[ModifyCodeOnce.py]
                ModifyCodeOnce_init[__init__.py]
                ModifyCodeOnce_typed[typed.py]
            end
            subgraph ModifyCode
                direction TB
                ModifyCode_py[ModifyCode.py]
                ModifyCode_init[__init__.py]
                ModifyCode_typed[typed.py]
            end
            subgraph LLM
                direction TB
                LLM_py[LLM.py]
                LLM_init[__init__.py]
                LLM_typed[typed.py]
            end
            subgraph CallLLM
                direction TB
                CallLLM_py[CallLLM.py]
                CallLLM_init[__init__.py]
                CallLLM_typed[typed.py]
            end
            subgraph ScanSonar
                direction TB
                ScanSonar_py[ScanSonar.py]
                ScanSonar_init[__init__.py]
                ScanSonar_typed[typed.py]
            end
            subgraph ExtractPackageManagerFile
                direction TB
                ExtractPackageManagerFile_py[ExtractPackageManagerFile.py]
                ExtractPackageManagerFile_init[__init__.py]
                ExtractPackageManagerFile_typed[typed.py]
                TestExtractPackageManagerFile_py[TestExtractPackageManagerFile.py]
            end
            subgraph FixIssue
                direction TB
                FixIssue_py[FixIssue.py]
                FixIssue_init[__init__.py]
                FixIssue_typed[typed.py]
            end
            subgraph ReadIssues
                direction TB
                ReadIssues_py[ReadIssues.py]
                ReadIssues_init[__init__.py]
                ReadIssues_typed[typed.py]
            end
            subgraph CreateIssue
                direction TB
                CreateIssue_py[CreateIssue.py]
                CreateIssue_init[__init__.py]
                CreateIssue_typed[typed.py]
            end
            subgraph GetTypescriptTypeInfo
                direction TB
                GetTypescriptTypeInfo_py[GetTypescriptTypeInfo.py]
                tsconfig[tsconfig.json]
                package[package.json]
                get_type_info[get_type_info.ts]
                GetTypescriptTypeInfo_init[__init__.py]
                GetTypescriptTypeInfo_typed[typed.py]
                pnpm_lock[pnpm-lock.yaml]
            end
            subgraph FilterBySimilarity
                direction TB
                FilterBySimilarity_py[FilterBySimilarity.py]
                FilterBySimilarity_init[__init__.py]
                FilterBySimilarity_typed[typed.py]
            end
            subgraph ScanDepscan
                direction TB
                ScanDepscan_py[ScanDepscan.py]
                ScanDepscan_init[__init__.py]
                ScanDepscan_typed[typed.py]
            end
            subgraph QueryEmbeddings
                direction TB
                QueryEmbeddings_py[QueryEmbeddings.py]
                QueryEmbeddings_init[__init__.py]
                QueryEmbeddings_typed[typed.py]
            end
            subgraph ExtractModelResponse
                direction TB
                ExtractModelResponse_py[ExtractModelResponse.py]
                ExtractModelResponse_init[__init__.py]
                ExtractModelResponse_typed[typed.py]
            end
            subgraph SlackMessage
                direction TB
                SlackMessage_py[SlackMessage.py]
                SlackMessage_init[__init__.py]
                SlackMessage_typed[typed.py]
            end
            subgraph SimplifiedLLM
                direction TB
                SimplifiedLLM_py[SimplifiedLLM.py]
                SimplifiedLLM_init[__init__.py]
                SimplifiedLLM_typed[typed.py]
            end
            subgraph CommitChanges
                direction TB
                CommitChanges_py[CommitChanges.py]
                CommitChanges_init[__init__.py]
                CommitChanges_typed[typed.py]
            end
            subgraph JoinList
                direction TB
                JoinList_py[JoinList.py]
                JoinList_init[__init__.py]
                JoinList_typed[typed.py]
            end
            subgraph CreateIssueComment
                direction TB
                CreateIssueComment_py[CreateIssueComment.py]
                CreateIssueComment_init[__init__.py]
                CreateIssueComment_typed[typed.py]
            end
            subgraph ExtractCodeContexts
                direction TB
                ExtractCodeContexts_py[ExtractCodeContexts.py]
                ExtractCodeContexts_init[__init__.py]
                ExtractCodeContexts_typed[typed.py]
            end
            subgraph CallShell
                direction TB
                CallShell_py[CallShell.py]
                CallShell_init[__init__.py]
                CallShell_typed[typed.py]
            end
            subgraph PR
                direction TB
                PR_py[PR.py]
                PR_init[__init__.py]
                PR_typed[typed.py]
            end
            subgraph ReadFile
                direction TB
                ReadFile_py[ReadFile.py]
                ReadFile_init[__init__.py]
                ReadFile_typed[typed.py]
            end
            subgraph AnalyzeImpact
                direction TB
                AnalyzeImpact_py[AnalyzeImpact.py
