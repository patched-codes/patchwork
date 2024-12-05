%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#ffcc00', 'edgeLabelBackground':'#ffffff', 'tertiaryColor': '#F0F1F2'}}}%%
graph TD
    subgraph patchwork
    direction TB
    steps["/steps"]
    end
    
    steps --> init_py["__init__.py"]
    init_py --> |"imports"| AnalyzeImpact
    init_py --> |"imports"| CallAPI
    init_py --> |"imports"| CallCode2Prompt
    init_py --> |"imports"| CallLLM
    init_py --> |"imports"| Combine
    init_py --> |"imports"| CommitChanges
    init_py --> |"imports"| CreateIssue
    init_py --> |"imports"| CreateIssueComment
    init_py --> |"imports"| CreatePR
    init_py --> |"imports"| CreatePRComment
    init_py --> |"imports"| ExtractCode
    init_py --> |"imports"| ExtractCodeContexts
    init_py --> |"imports"| ExtractCodeMethodForCommentContexts
    init_py --> |"imports"| ExtractDiff
    init_py --> |"imports"| ExtractModelResponse
    init_py --> |"imports"| ExtractPackageManagerFile
    init_py --> |"imports"| FilterBySimilarity
    init_py --> |"imports"| FixIssue
    init_py --> |"imports"| GenerateCodeRepositoryEmbeddings
    init_py --> |"imports"| GenerateEmbeddings
    init_py --> |"imports"| GetTypescriptTypeInfo
    init_py --> |"imports"| JoinList
    init_py --> |"imports"| LLM
    init_py --> |"imports"| ModifyCode
    init_py --> |"imports"| ModifyCodeOnce
    init_py --> |"imports"| PR
    init_py --> |"imports"| PreparePR
    init_py --> |"imports"| PreparePrompt
    init_py --> |"imports"| QueryEmbeddings
    init_py --> |"imports"| ReadFile
    init_py --> |"imports"| ReadIssues
    init_py --> |"imports"| ReadPRDiffs
    init_py --> |"imports"| ReadPRs
    init_py --> |"imports"| ScanDepscan
    init_py --> |"imports"| ScanSemgrep
    init_py --> |"imports"| SimplifiedLLM
    init_py --> |"imports"| SimplifiedLLMOnce
    init_py --> |"imports"| SlackMessage

    subgraph steps
    direction TB
        subgraph AnalyzeImpact
        direction TB
            AI_init["__init__.py"]
            AI_inputs["typed.py"]
            AI_analyzeImpact["AnalyzeImpact.py"]
            AI_readme["README.md"]
        end
        subgraph CallAPI
        direction TB
            API_init["__init__.py"]
            API_inputs["typed.py"]
            API_callAPI["CallAPI.py"]
            API_readme["README.md"]
        end
        subgraph CallCode2Prompt
        direction TB
            C2P_init["__init__.py"]
            C2P_inputs["typed.py"]
            C2P_callCode2Prompt["CallCode2Prompt.py"]
            C2P_testCallCode2Prompt["TestCallCode2Prompt.py"]
            C2P_readme["README.md"]
        end
        subgraph CallLLM
        direction TB
            LLM_init["__init__.py"]
            LLM_inputs["typed.py"]
            LLM_callLLM["CallLLM.py"]
            LLM_readme["README.md"]
        end
        subgraph Combine
        direction TB
            Combine_init["__init__.py"]
            Combine_inputs["typed.py"]
            Combine_combine["Combine.py"]
            Combine_readme["README.md"]
        end
        subgraph CommitChanges
        direction TB
            CC_init["__init__.py"]
            CC_inputs["typed.py"]
            CC_commitChanges["CommitChanges.py"]
            CC_readme["README.md"]
        end
        subgraph CreateIssue
        direction TB
            CI_init["__init__.py"]
            CI_inputs["typed.py"]
            CI_createIssue["CreateIssue.py"]
            CI_readme["README.md"]
        end
        subgraph CreateIssueComment
        direction TB
            CIC_init["__init__.py"]
            CIC_inputs["typed.py"]
            CIC_createIssueComment["CreateIssueComment.py"]
            CIC_readme["README.md"]
        end
        subgraph CreatePR
        direction TB
            CPR_init["__init__.py"]
            CPR_inputs["typed.py"]
            CPR_createPR["CreatePR.py"]
            CPR_readme["README.md"]
        end
        subgraph CreatePRComment
        direction TB
            CPRC_init["__init__.py"]
            CPRC_inputs["typed.py"]
            CPRC_createPRComment["CreatePRComment.py"]
            CPRC_readme["README.md"]
        end
        subgraph ExtractCode
        direction TB
            EC_init["__init__.py"]
            EC_inputs["typed.py"]
            EC_extractCode["ExtractCode.py"]
            EC_readme["README.md"]
        end
        subgraph ExtractCodeContexts
        direction TB
            ECC_init["__init__.py"]
            ECC_inputs["typed.py"]
            ECC_extractCodeContexts["ExtractCodeContexts.py"]
            ECC_readme["README.md"]
        end
        subgraph ExtractCodeMethodForCommentContexts
        direction TB
            ECMCC_init["__init__.py"]
            ECMCC_inputs["typed.py"]
            ECMCC_extract["ExtractCodeMethodForCommentContexts.py"]
            ECMCC_readme["README.md"]
        end
        subgraph ExtractDiff
        direction TB
            ED_init["__init__.py"]
            ED_inputs["typed.py"]
            ED_extractDiff["ExtractDiff.py"]
            ED_readme["README.md"]
        end
        subgraph ExtractModelResponse
        direction TB
            EMR_init["__init__.py"]
            EMR_inputs["typed.py"]
            EMR_extractModelResponse["ExtractModelResponse.py"]
            EMR_readme["README.md"]
        end
        subgraph ExtractPackageManagerFile
        direction TB
            EPMF_init["__init__.py"]
            EPMF_inputs["typed.py"]
            EPMF_extractPackageManagerFile["ExtractPackageManagerFile.py"]
            EPMF_testExtractPackageManagerFile["TestExtractPackageManagerFile.py"]
            EPMF_readme["README.md"]
        end
        subgraph FilterBySimilarity
        direction TB
            FBS_init["__init__.py"]
            FBS_inputs["typed.py"]
            FBS_filterBySimilarity["FilterBySimilarity.py"]
            FBS_readme["README.md"]
        end
        subgraph FixIssue
        direction TB
            FI_init["__init__.py"]
            FI_inputs["typed.py"]
            FI_fixIssue["FixIssue.py"]
            FI_readme["README.md"]
        end
        subgraph GenerateCodeRepositoryEmbeddings
        direction TB
            GCRE_init["__init__.py"]
            GCRE_inputs["typed.py"]
            GCRE_generate["GenerateCodeRepositoryEmbeddings.py"]
            GCRE_filterLists["filter_lists.py"]
            GCRE_readme["README.md"]
        end
        subgraph GenerateEmbeddings
        direction TB
            GE_init["__init__.py"]
            GE_inputs["typed.py"]
            GE_generateEmbeddings["GenerateEmbeddings.py"]
            GE_readme["README.md"]
        end
        subgraph GetTypescriptTypeInfo
        direction TB
            GTI_init["__init__.py"]
            GTI_inputs["typed.py"]
            GTI_getTypescriptTypeInfo["GetTypescriptTypeInfo.py"]
            GTI_tsconfig["tsconfig.json"]
            GTI_package["package.json"]
            GTI_ts["get_type_info.ts"]
            GTI_pnpmLock["pnpm-lock.yaml"]
            GTI_readme["README.md"]
        end
        subgraph JoinList
        direction TB
            JL_init["__init__.py"]
            JL_inputs["typed.py"]
            JL_joinList["JoinList.py"]
            JL_readme["README.md"]
        end
        subgraph LLM
        direction TB
            LLM_init["__init__.py"]
            LLM_inputs["typed.py"]
            LLM_llm["LLM.py"]
            LLM_readme["README.md"]
        end
        subgraph ModifyCode
        direction TB
            MC_init["__init__.py"]
            MC_inputs["typed.py"]
            MC_modifyCode["ModifyCode.py"]
            MC_readme["README.md"]
        end
        subgraph ModifyCodeOnce
        direction TB
            MCO_init["__init__.py"]
            MCO_inputs["typed.py"]
            MCO_modifyCodeOnce["ModifyCodeOnce.py"]
            MCO_readme["README.md"]
        end
        subgraph PR
        direction TB
            PR_init["__init__.py"]
            PR_inputs["typed.py"]
            PR_pr["PR.py"]
            PR_readme["README.md"]
        end
        subgraph PreparePR
        direction TB
            PPR_init["__init__.py"]
            PPR_inputs["typed.py"]
            PPR_preparePR["PreparePR.py"]
            PPR_readme["README.md"]
        end
        subgraph PreparePrompt
        direction TB
            PP_init["__init__.py"]
            PP_inputs["typed.py"]
            PP_preparePrompt["PreparePrompt.py"]
            PP_readme["README.md"]
        end
        subgraph QueryEmbeddings
        direction TB
            QE_init["__init__.py"]
            QE_inputs["typed.py"]
            QE_queryEmbeddings["QueryEmbeddings.py"]
            QE_readme["README.md"]
        end
        subgraph ReadFile
        direction TB
            RF_init["__init__.py"]
            RF_inputs["typed.py"]
            RF_readFile["ReadFile.py"]
            RF_readme["README.md"]
        end
        subgraph ReadIssues
        direction TB
            RI_init["__init__.py"]
            RI_inputs["typed.py"]
            RI_readIssues["ReadIssues.py"]
            RI_readme["README.md"]
        end
        subgraph ReadPRDiffs
        direction TB
            RPD_init["__init__.py"]
            RPD_inputs["typed.py"]
            RPD_readPRDiffs["ReadPRDiffs.py"]
            RPD_readme["README.md"]
        end
        subgraph ReadPRs
        direction TB
            RPR_init["__init__.py"]
            RPR_inputs["typed.py"]
            RPR_readPRs["ReadPRs.py"]
            RPR_readme["README.md"]
        end
        subgraph ScanDepscan
        direction TB
            SD_init["__init__.py"]
            SD_inputs["typed.py"]
            SD_scanDepscan["ScanDepscan.py"]
            SD_readme["README.md"]
        end
        subgraph ScanSemgrep
        direction TB
            SS_init["__init__.py"]
            SS_inputs["typed.py"]
            SS_scanSemgrep["ScanSemgrep.py"]
            SS_readme["README.md"]
        end
        subgraph SimplifiedLLM
        direction TB
            SLLM_init["__init__.py"]
            SLLM_inputs["typed.py"]
            SLLM_simplifiedLLM["SimplifiedLLM.py"]
            SLLM_readme["README.md"]
        end
        subgraph SimplifiedLLMOnce
        direction TB
            SLLMO_init["__init__.py"]
            SLLMO_inputs["typed.py"]
            SLLMO_simplifiedLLMOnce["SimplifiedLLMOnce.py"]
            SLLMO_readme["README.md"]
        end
        subgraph SlackMessage
        direction TB
            SM_init["__init__.py"]
            SM_inputs["typed.py"]
            SM_slackMessage["SlackMessage.py"]
            SM_readme["README.md"]
        end
    end
