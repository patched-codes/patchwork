flowchart TD
    A[patchwork/steps/README.md]
    B[patchwork/steps/__init__.py]
    C[patchwork/steps/common/utils/step_typing.py]
    
    subgraph ScanSemgrep
        direction TB
        S1[patchwork/steps/ScanSemgrep/typed.py]
        S2[patchwork/steps/ScanSemgrep/README.md]
        S3[patchwork/steps/ScanSemgrep/__init__.py]
        S4[patchwork/steps/ScanSemgrep/ScanSemgrep.py]
    end

    subgraph ModifyCode
        direction TB
        M1[patchwork/steps/ModifyCode/typed.py]
        M2[patchwork/steps/ModifyCode/README.md]
        M3[patchwork/steps/ModifyCode/__init__.py]
        M4[patchwork/steps/ModifyCode/ModifyCode.py]
    end

    subgraph PreparePrompt
        direction TB
        P1[patchwork/steps/PreparePrompt/typed.py]
        P2[patchwork/steps/PreparePrompt/README.md]
        P3[patchwork/steps/PreparePrompt/__init__.py]
        P4[patchwork/steps/PreparePrompt/PreparePrompt.py]
    end

    subgraph CallLLM
        direction TB
        L1[patchwork/steps/CallLLM/typed.py]
        L2[patchwork/steps/CallLLM/README.md]
        L3[patchwork/steps/CallLLM/__init__.py]
        L4[patchwork/steps/CallLLM/CallLLM.py]
    end

    subgraph Combine
        direction TB
        C1[patchwork/steps/Combine/typed.py]
        C2[patchwork/steps/Combine/README.md]
        C3[patchwork/steps/Combine/__init__.py]
        C4[patchwork/steps/Combine/Combine.py]
    end

    subgraph CreateIssueComment
        direction TB
        CIC1[patchwork/steps/CreateIssueComment/typed.py]
        CIC2[patchwork/steps/CreateIssueComment/README.md]
        CIC3[patchwork/steps/CreateIssueComment/__init__.py]
        CIC4[patchwork/steps/CreateIssueComment/CreateIssueComment.py]
    end

    subgraph CommitChanges
        direction TB
        CC1[patchwork/steps/CommitChanges/typed.py]
        CC2[patchwork/steps/CommitChanges/README.md]
        CC3[patchwork/steps/CommitChanges/__init__.py]
        CC4[patchwork/steps/CommitChanges/CommitChanges.py]
    end

    subgraph PreparePR
        direction TB
        PPR1[patchwork/steps/PreparePR/typed.py]
        PPR2[patchwork/steps/PreparePR/README.md]
        PPR3[patchwork/steps/PreparePR/__init__.py]
        PPR4[patchwork/steps/PreparePR/PreparePR.py]
    end

    subgraph ReadPRs
        direction TB
        RPR1[patchwork/steps/ReadPRs/typed.py]
        RPR2[patchwork/steps/ReadPRs/README.md]
        RPR3[patchwork/steps/ReadPRs/__init__.py]
        RPR4[patchwork/steps/ReadPRs/ReadPRs.py]
    end

    subgraph GetTypescriptTypeInfo
        direction TB
        GTI1[patchwork/steps/GetTypescriptTypeInfo/typed.py]
        GTI2[patchwork/steps/GetTypescriptTypeInfo/pnpm-lock.yaml]
        GTI3[patchwork/steps/GetTypescriptTypeInfo/README.md]
        GTI4[patchwork/steps/GetTypescriptTypeInfo/__init__.py]
        GTI5[patchwork/steps/GetTypescriptTypeInfo/package.json]
        GTI6[patchwork/steps/GetTypescriptTypeInfo/get_type_info.ts]
        GTI7[patchwork/steps/GetTypescriptTypeInfo/tsconfig.json]
        GTI8[patchwork/steps/GetTypescriptTypeInfo/GetTypescriptTypeInfo.py]
    end

    subgraph QueryEmbeddings
        direction TB
        QE1[patchwork/steps/QueryEmbeddings/typed.py]
        QE2[patchwork/steps/QueryEmbeddings/README.md]
        QE3[patchwork/steps/QueryEmbeddings/__init__.py]
        QE4[patchwork/steps/QueryEmbeddings/QueryEmbeddings.py]
    end

    subgraph ExtractCodeContexts
        direction TB
        ECC1[patchwork/steps/ExtractCodeContexts/typed.py]
        ECC2[patchwork/steps/ExtractCodeContexts/README.md]
        ECC3[patchwork/steps/ExtractCodeContexts/__init__.py]
        ECC4[patchwork/steps/ExtractCodeContexts/ExtractCodeContexts.py]
    end

    subgraph GenerateCodeRepositoryEmbeddings
        direction TB
        GCRE1[patchwork/steps/GenerateCodeRepositoryEmbeddings/typed.py]
        GCRE2[patchwork/steps/GenerateCodeRepositoryEmbeddings/README.md]
        GCRE3[patchwork/steps/GenerateCodeRepositoryEmbeddings/__init__.py]
        GCRE4[patchwork/steps/GenerateCodeRepositoryEmbeddings/filter_lists.py]
        GCRE5[patchwork/steps/GenerateCodeRepositoryEmbeddings/GenerateCodeRepositoryEmbeddings.py]
    end

    subgraph ExtractDiff
        direction TB
        ED1[patchwork/steps/ExtractDiff/typed.py]
        ED2[patchwork/steps/ExtractDiff/README.md]
        ED3[patchwork/steps/ExtractDiff/__init__.py]
        ED4[patchwork/steps/ExtractDiff/ExtractDiff.py]
    end

    subgraph FixIssue
        direction TB
        FI1[patchwork/steps/FixIssue/typed.py]
        FI2[patchwork/steps/FixIssue/README.md]
        FI3[patchwork/steps/FixIssue/__init__.py]
        FI4[patchwork/steps/FixIssue/FixIssue.py]
    end
    
    subgraph CallCode2Prompt
        direction TB
        CCP1[patchwork/steps/CallCode2Prompt/typed.py]
        CCP2[patchwork/steps/CallCode2Prompt/README.md]
        CCP3[patchwork/steps/CallCode2Prompt/__init__.py]
        CCP4[patchwork/steps/CallCode2Prompt/CallCode2Prompt.py]
        CCP5[patchwork/steps/CallCode2Prompt/TestCallCode2Prompt.py]
    end

    subgraph SimplifiedLLMOnce
        direction TB
        SLL1[patchwork/steps/SimplifiedLLMOnce/typed.py]
        SLL2[patchwork/steps/SimplifiedLLMOnce/README.md]
        SLL3[patchwork/steps/SimplifiedLLMOnce/__init__.py]
        SLL4[patchwork/steps/SimplifiedLLMOnce/SimplifiedLLMOnce.py]
    end

    subgraph CreatePRComment
        direction TB
        CP1[patchwork/steps/CreatePRComment/typed.py]
        CP2[patchwork/steps/CreatePRComment/README.md]
        CP3[patchwork/steps/CreatePRComment/__init__.py]
        CP4[patchwork/steps/CreatePRComment/CreatePRComment.py]
    end

    subgraph ReadPRDiffs
        direction TB
        RPD1[patchwork/steps/ReadPRDiffs/typed.py]
        RPD2[patchwork/steps/ReadPRDiffs/README.md]
        RPD3[patchwork/steps/ReadPRDiffs/__init__.py]
        RPD4[patchwork/steps/ReadPRDiffs/ReadPRDiffs.py]
    end

    subgraph AnalyzeImpact
        direction TB
        AI1[patchwork/steps/AnalyzeImpact/typed.py]
        AI2[patchwork/steps/AnalyzeImpact/README.md]
        AI3[patchwork/steps/AnalyzeImpact/__init__.py]
        AI4[patchwork/steps/AnalyzeImpact/AnalyzeImpact.py]
    end
    
    subgraph FilterBySimilarity
        direction TB
        FBS1[patchwork/steps/FilterBySimilarity/typed.py]
        FBS2[patchwork/steps/FilterBySimilarity/README.md]
        FBS3[patchwork/steps/FilterBySimilarity/__init__.py]
        FBS4[patchwork/steps/FilterBySimilarity/FilterBySimilarity.py]
    end
    
    subgraph ExtractCode
        direction TB
        EC1[patchwork/steps/ExtractCode/typed.py]
        EC2[patchwork/steps/ExtractCode/README.md]
        EC3[patchwork/steps/ExtractCode/__init__.py]
        EC4[patchwork/steps/ExtractCode/ExtractCode.py]
    end

    subgraph CreatePR
        direction TB
        CPR1[patchwork/steps/CreatePR/typed.py]
        CPR2[patchwork/steps/CreatePR/README.md]
        CPR3[patchwork/steps/CreatePR/__init__.py]
        CPR4[patchwork/steps/CreatePR/CreatePR.py]
    end

    subgraph LLM
        direction TB
        LLM1[patchwork/steps/LLM/typed.py]
        LLM2[patchwork/steps/LLM/README.md]
        LLM3[patchwork/steps/LLM/__init__.py]
        LLM4[patchwork/steps/LLM/LLM.py]
    end

    subgraph PR
        direction TB
        PR1[patchwork/steps/PR/typed.py]
        PR2[patchwork/steps/PR/README.md]
        PR3[patchwork/steps/PR/__init__.py]
        PR4[patchwork/steps/PR/PR.py]
    end

    subgraph ExtractCodeMethodForCommentContexts
        direction TB
        ECM1[patchwork/steps/ExtractCodeMethodForCommentContexts/typed.py]
        ECM2[patchwork/steps/ExtractCodeMethodForCommentContexts/README.md]
        ECM3[patchwork/steps/ExtractCodeMethodForCommentContexts/__init__.py]
        ECM4[patchwork/steps/ExtractCodeMethodForCommentContexts/ExtractCodeMethodForCommentContexts.py]
    end

    subgraph CreateIssue
        direction TB
        CI1[patchwork/steps/CreateIssue/typed.py]
        CI2[patchwork/steps/CreateIssue/README.md]
        CI3[patchwork/steps/CreateIssue/__init__.py]
        CI4[patchwork/steps/CreateIssue/CreateIssue.py]
    end

    subgraph ModifyCodeOnce
        direction TB
        MCO1[patchwork/steps/ModifyCodeOnce/typed.py]
        MCO2[patchwork/steps/ModifyCodeOnce/README.md]
        MCO3[patchwork/steps/ModifyCodeOnce/__init__.py]
        MCO4[patchwork/steps/ModifyCodeOnce/ModifyCodeOnce.py]
    end

    subgraph ExtractModelResponse
        direction TB
        EMR1[patchwork/steps/ExtractModelResponse/typed.py]
        EMR2[patchwork/steps/ExtractModelResponse/README.md]
        EMR3[patchwork/steps/ExtractModelResponse/__init__.py]
        EMR4[patchwork/steps/ExtractModelResponse/ExtractModelResponse.py]
    end

    subgraph JoinList
        direction TB
        JL1[patchwork/steps/JoinList/typed.py]
        JL2[patchwork/steps/JoinList/README.md]
        JL3[patchwork/steps/JoinList/__init__.py]
        JL4[patchwork/steps/JoinList/JoinList.py]
    end

    subgraph SimplifiedLLM
        direction TB
        SLLM1[patchwork/steps/SimplifiedLLM/typed.py]
        SLLM2[patchwork/steps/SimplifiedLLM/README.md]
        SLLM3[patchwork/steps/SimplifiedLLM/__init__.py]
        SLLM4[patchwork/steps/SimplifiedLLM/SimplifiedLLM.py]
    end

    subgraph CallAPI
        direction TB
        CA1[patchwork/steps/CallAPI/typed.py]
        CA2[patchwork/steps/CallAPI/README.md]
        CA3[patchwork/steps/CallAPI/__init__.py]
        CA4[patchwork/steps/CallAPI/CallAPI.py]
    end

    subgraph ExtractPackageManagerFile
        direction TB
        EPM1[patchwork/steps/ExtractPackageManagerFile/typed.py]
        EPM2[patchwork/steps/ExtractPackageManagerFile/README.md]
        EPM3[patchwork/steps/ExtractPackageManagerFile/__init__.py]
        EPM4[patchwork/steps/ExtractPackageManagerFile/TestExtractPackageManagerFile.py]
        EPM5[patchwork/steps/ExtractPackageManagerFile/ExtractPackageManagerFile.py]
    end

    subgraph ReadIssues
        direction TB
        RI1[patchwork/steps/ReadIssues/typed.py]
        RI2[patchwork/steps/ReadIssues/README.md]
        RI3[patchwork/steps/ReadIssues/__init__.py]
        RI4[patchwork/steps/ReadIssues/ReadIssues.py]
    end

    subgraph ReadFile
        direction TB
        RF1[patchwork/steps/ReadFile/typed.py]
        RF2[patchwork/steps/ReadFile/README.md]
        RF3[patchwork/steps/ReadFile/__init__.py]
        RF4[patchwork/steps/ReadFile/ReadFile.py]
    end
    
    subgraph ScanSonar
        direction TB
        SS1[patchwork/steps/ScanSonar/typed.py]
        SS2[patchwork/steps/ScanSonar/README.md]
        SS3[patchwork/steps/ScanSonar/__init__.py]
        SS4[patchwork/steps/ScanSonar/ScanSonar.py]
    end

    subgraph GenerateEmbeddings
        direction TB
        GE1[patchwork/steps/GenerateEmbeddings/typed.py]
        GE2[patchwork/steps/GenerateEmbeddings/README.md]
        GE3[patchwork/steps/GenerateEmbeddings/__init__.py]
        GE4[patchwork/steps/GenerateEmbeddings/GenerateEmbeddings.py]
    end

    subgraph ScanDepscan
        direction TB
        SD1[patchwork/steps/ScanDepscan/typed.py]
        SD2[patchwork/steps/ScanDepscan/README.md]
        SD3[patchwork/steps/ScanDepscan/__init__.py]
        SD4[patchwork/steps/ScanDepscan/ScanDepscan.py]
    end

    subgraph SlackMessage
        direction TB
        SM1[patchwork/steps/SlackMessage/typed.py]
        SM2[patchwork/steps/SlackMessage/README.md]
        SM3[patchwork/steps/SlackMessage/__init__.py]
        SM4[patchwork/steps/SlackMessage/SlackMessage.py]
    end

    B --> S4
    B --> M4
    B --> P4
    B --> L4
    B --> C4
    B --> CIC4
    B --> CC4
    B --> PPR4
    B --> RPR4
    B --> GTI8
    B --> QE4
    B --> ECC4
    B --> GCRE5
    B --> ED4
    B --> FI4
    B --> CCP4
    B --> SLL4
    B --> CP4
    B --> RPD4
    B --> AI4
    B --> FBS4
    B --> EC4
    B --> CPR4
    B --> LLM4
    B --> PR4
    B --> ECM4
    B --> CI4
    B --> MCO4
    B --> EMR4
    B --> JL4
    B --> SLLM4
    B --> CA4
    B --> EPM5
    B --> RI4
    B --> RF4
    B --> SS4
    B --> GE4
    B --> SD4
    B --> SM4
