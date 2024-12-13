graph TD;
    patchwork["patchwork/steps"]
    patchwork_init[init.py]
    class patchwork_init file

    ScanSemgrep["ScanSemgrep"]
    ScanSemgrep_init[init.py]
    ScanSemgrep_typed[typed.py]
    ScanSemgrep_readme[README.md]
    ScanSemgrep_ScanSemgrep[ScanSemgrep.py]

    patchwork --> ScanSemgrep
    ScanSemgrep --> ScanSemgrep_init
    ScanSemgrep --> ScanSemgrep_typed
    ScanSemgrep --> ScanSemgrep_readme
    ScanSemgrep --> ScanSemgrep_ScanSemgrep

    ModifyCode["ModifyCode"]
    ModifyCode_init[init.py]
    ModifyCode_typed[typed.py]
    ModifyCode_readme[README.md]
    ModifyCode_ModifyCode[ModifyCode.py]

    patchwork --> ModifyCode
    ModifyCode --> ModifyCode_init
    ModifyCode --> ModifyCode_typed
    ModifyCode --> ModifyCode_readme
    ModifyCode --> ModifyCode_ModifyCode

    PreparePrompt["PreparePrompt"]
    PreparePrompt_init[init.py]
    PreparePrompt_typed[typed.py]
    PreparePrompt_readme[README.md]
    PreparePrompt_PreparePrompt[PreparePrompt.py]

    patchwork --> PreparePrompt
    PreparePrompt --> PreparePrompt_init
    PreparePrompt --> PreparePrompt_typed
    PreparePrompt --> PreparePrompt_readme
    PreparePrompt --> PreparePrompt_PreparePrompt

    CallLLM["CallLLM"]
    CallLLM_init[init.py]
    CallLLM_typed[typed.py]
    CallLLM_readme[README.md]
    CallLLM_CallLLM[CallLLM.py]

    patchwork --> CallLLM
    CallLLM --> CallLLM_init
    CallLLM --> CallLLM_typed
    CallLLM --> CallLLM_readme
    CallLLM --> CallLLM_CallLLM

    Combine["Combine"]
    Combine_init[init.py]
    Combine_typed[typed.py]
    Combine_readme[README.md]
    Combine_Combine[Combine.py]

    patchwork --> Combine
    Combine --> Combine_init
    Combine --> Combine_typed
    Combine --> Combine_readme
    Combine --> Combine_Combine

    CreateIssueComment["CreateIssueComment"]
    CreateIssueComment_init[init.py]
    CreateIssueComment_typed[typed.py]
    CreateIssueComment_readme[README.md]
    CreateIssueComment_CreateIssueComment[CreateIssueComment.py]

    patchwork --> CreateIssueComment
    CreateIssueComment --> CreateIssueComment_init
    CreateIssueComment --> CreateIssueComment_typed
    CreateIssueComment --> CreateIssueComment_readme
    CreateIssueComment --> CreateIssueComment_CreateIssueComment

    CommitChanges["CommitChanges"]
    CommitChanges_init[init.py]
    CommitChanges_typed[typed.py]
    CommitChanges_readme[README.md]
    CommitChanges_CommitChanges[CommitChanges.py]

    patchwork --> CommitChanges
    CommitChanges --> CommitChanges_init
    CommitChanges --> CommitChanges_typed
    CommitChanges --> CommitChanges_readme
    CommitChanges --> CommitChanges_CommitChanges

    PreparePR["PreparePR"]
    PreparePR_init[init.py]
    PreparePR_typed[typed.py]
    PreparePR_readme[README.md]
    PreparePR_PreparePR[PreparePR.py]

    patchwork --> PreparePR
    PreparePR --> PreparePR_init
    PreparePR --> PreparePR_typed
    PreparePR --> PreparePR_readme
    PreparePR --> PreparePR_PreparePR

    ReadPRs["ReadPRs"]
    ReadPRs_init[init.py]
    ReadPRs_typed[typed.py]
    ReadPRs_readme[README.md]
    ReadPRs_ReadPRs[ReadPRs.py]

    patchwork --> ReadPRs
    ReadPRs --> ReadPRs_init
    ReadPRs --> ReadPRs_typed
    ReadPRs --> ReadPRs_readme
    ReadPRs --> ReadPRs_ReadPRs

    GetTypescriptTypeInfo["GetTypescriptTypeInfo"]
    GetTypescriptTypeInfo_init[init.py]
    GetTypescriptTypeInfo_typed[typed.py]
    GetTypescriptTypeInfo_readme[README.md]
    GetTypescriptTypeInfo_packagejson[package.json]
    GetTypescriptTypeInfo_pnpm[typed.py]
    GetTypescriptTypeInfo_getTypeScript[get_type_info.ts]
    GetTypescriptTypeInfo_tsconfig[tsconfig.json]
    GetTypescriptTypeInfo_GetTypescriptTypeInfo[GetTypescriptTypeInfo.py]
    
    patchwork --> GetTypescriptTypeInfo
    GetTypescriptTypeInfo --> GetTypescriptTypeInfo_init
    GetTypescriptTypeInfo --> GetTypescriptTypeInfo_typed
    GetTypescriptTypeInfo --> GetTypescriptTypeInfo_readme
    GetTypescriptTypeInfo --> GetTypescriptTypeInfo_packagejson
    GetTypescriptTypeInfo --> GetTypescriptTypeInfo_pnpm
    GetTypescriptTypeInfo --> GetTypescriptTypeInfo_getTypeScript
    GetTypescriptTypeInfo --> GetTypescriptTypeInfo_tsconfig
    GetTypescriptTypeInfo --> GetTypescriptTypeInfo_GetTypescriptTypeInfo

    QueryEmbeddings["QueryEmbeddings"]
    QueryEmbeddings_init[init.py]
    QueryEmbeddings_typed[typed.py]
    QueryEmbeddings_readme[README.md]
    QueryEmbeddings_QueryEmbeddings[QueryEmbeddings.py]

    patchwork --> QueryEmbeddings
    QueryEmbeddings --> QueryEmbeddings_init
    QueryEmbeddings --> QueryEmbeddings_typed
    QueryEmbeddings --> QueryEmbeddings_readme
    QueryEmbeddings --> QueryEmbeddings_QueryEmbeddings

    ExtractCodeContexts["ExtractCodeContexts"]
    ExtractCodeContexts_init[init.py]
    ExtractCodeContexts_typed[typed.py]
    ExtractCodeContexts_readme[README.md]
    ExtractCodeContexts_ExtractCodeContexts[ExtractCodeContexts.py]

    patchwork --> ExtractCodeContexts
    ExtractCodeContexts --> ExtractCodeContexts_init
    ExtractCodeContexts --> ExtractCodeContexts_typed
    ExtractCodeContexts --> ExtractCodeContexts_readme
    ExtractCodeContexts --> ExtractCodeContexts_ExtractCodeContexts

    GenerateCodeRepositoryEmbeddings["GenerateCodeRepositoryEmbeddings"]
    GenerateCodeRepositoryEmbeddings_init[init.py]
    GenerateCodeRepositoryEmbeddings_typed[typed.py]
    GenerateCodeRepositoryEmbeddings_readme[README.md]
    GenerateCodeRepositoryEmbeddings_filter_lists[filter_lists.py]
    GenerateCodeRepositoryEmbeddings_GenerateCodeRepositoryEmbeddings[GenerateCodeRepositoryEmbeddings.py]

    patchwork --> GenerateCodeRepositoryEmbeddings
    GenerateCodeRepositoryEmbeddings --> GenerateCodeRepositoryEmbeddings_init
    GenerateCodeRepositoryEmbeddings --> GenerateCodeRepositoryEmbeddings_typed
    GenerateCodeRepositoryEmbeddings --> GenerateCodeRepositoryEmbeddings_readme
    GenerateCodeRepositoryEmbeddings --> GenerateCodeRepositoryEmbeddings_filter_lists
    GenerateCodeRepositoryEmbeddings --> GenerateCodeRepositoryEmbeddings_GenerateCodeRepositoryEmbeddings

    ExtractDiff["ExtractDiff"]
    ExtractDiff_init[init.py]
    ExtractDiff_typed[typed.py]
    ExtractDiff_readme[README.md]
    ExtractDiff_ExtractDiff[ExtractDiff.py]

    patchwork --> ExtractDiff
    ExtractDiff --> ExtractDiff_init
    ExtractDiff --> ExtractDiff_typed
    ExtractDiff --> ExtractDiff_readme
    ExtractDiff --> ExtractDiff_ExtractDiff

    FixIssue["FixIssue"]
    FixIssue_init[init.py]
    FixIssue_typed[typed.py]
    FixIssue_readme[README.md]
    FixIssue_FixIssue[FixIssue.py]

    patchwork --> FixIssue
    FixIssue --> FixIssue_init
    FixIssue --> FixIssue_typed
    FixIssue --> FixIssue_readme
    FixIssue --> FixIssue_FixIssue

    CallCode2Prompt["CallCode2Prompt"]
    CallCode2Prompt_init[init.py]
    CallCode2Prompt_typed[typed.py]
    CallCode2Prompt_readme[README.md]
    CallCode2Prompt_CallCode2Prompt[CallCode2Prompt.py]
    CallCode2Prompt_TestCallCode2Prompt[TestCallCode2Prompt.py]

    patchwork --> CallCode2Prompt
    CallCode2Prompt --> CallCode2Prompt_init
    CallCode2Prompt --> CallCode2Prompt_typed
    CallCode2Prompt --> CallCode2Prompt_readme
    CallCode2Prompt --> CallCode2Prompt_CallCode2Prompt
    CallCode2Prompt --> CallCode2Prompt_TestCallCode2Prompt

    SimplifiedLLMOnce["SimplifiedLLMOnce"]
    SimplifiedLLMOnce_init[init.py]
    SimplifiedLLMOnce_typed[typed.py]
    SimplifiedLLMOnce_readme[README.md]
    SimplifiedLLMOnce_SimplifiedLLMOnce[SimplifiedLLMOnce.py]

    patchwork --> SimplifiedLLMOnce
    SimplifiedLLMOnce --> SimplifiedLLMOnce_init
    SimplifiedLLMOnce --> SimplifiedLLMOnce_typed
    SimplifiedLLMOnce --> SimplifiedLLMOnce_readme
    SimplifiedLLMOnce --> SimplifiedLLMOnce_SimplifiedLLMOnce

    CreatePRComment["CreatePRComment"]
    CreatePRComment_init[init.py]
    CreatePRComment_typed[typed.py]
    CreatePRComment_readme[README.md]
    CreatePRComment_CreatePRComment[CreatePRComment.py]

    patchwork --> CreatePRComment
    CreatePRComment --> CreatePRComment_init
    CreatePRComment --> CreatePRComment_typed
    CreatePRComment --> CreatePRComment_readme
    CreatePRComment --> CreatePRComment_CreatePRComment

    ReadPRDiffs["ReadPRDiffs"]
    ReadPRDiffs_init[init.py]
    ReadPRDiffs_typed[typed.py]
    ReadPRDiffs_readme[README.md]
    ReadPRDiffs_ReadPRDiffs[ReadPRDiffs.py]

    patchwork --> ReadPRDiffs
    ReadPRDiffs --> ReadPRDiffs_init
    ReadPRDiffs --> ReadPRDiffs_typed
    ReadPRDiffs --> ReadPRDiffs_readme
    ReadPRDiffs --> ReadPRDiffs_ReadPRDiffs

    AnalyzeImpact["AnalyzeImpact"]
    AnalyzeImpact_init[init.py]
    AnalyzeImpact_typed[typed.py]
    AnalyzeImpact_readme[README.md]
    AnalyzeImpact_AnalyzeImpact[AnalyzeImpact.py]

    patchwork --> AnalyzeImpact
    AnalyzeImpact --> AnalyzeImpact_init
    AnalyzeImpact --> AnalyzeImpact_typed
    AnalyzeImpact --> AnalyzeImpact_readme
    AnalyzeImpact --> AnalyzeImpact_AnalyzeImpact

    FilterBySimilarity["FilterBySimilarity"]
    FilterBySimilarity_init[init.py]
    FilterBySimilarity_typed[typed.py]
    FilterBySimilarity_readme[README.md]
    FilterBySimilarity_FilterBySimilarity[FilterBySimilarity.py]

    patchwork --> FilterBySimilarity
    FilterBySimilarity --> FilterBySimilarity_init
    FilterBySimilarity --> FilterBySimilarity_typed
    FilterBySimilarity --> FilterBySimilarity_readme
    FilterBySimilarity --> FilterBySimilarity_FilterBySimilarity

    ExtractCode["ExtractCode"]
    ExtractCode_init[init.py]
    ExtractCode_typed[typed.py]
    ExtractCode_readme[README.md]
    ExtractCode_ExtractCode[ExtractCode.py]

    patchwork --> ExtractCode
    ExtractCode --> ExtractCode_init
    ExtractCode --> ExtractCode_typed
    ExtractCode --> ExtractCode_readme
    ExtractCode --> ExtractCode_ExtractCode

    CreatePR["CreatePR"]
    CreatePR_init[init.py]
    CreatePR_typed[typed.py]
    CreatePR_readme[README.md]
    CreatePR_CreatePR[CreatePR.py]

    patchwork --> CreatePR
    CreatePR --> CreatePR_init
    CreatePR --> CreatePR_typed
    CreatePR --> CreatePR_readme
    CreatePR --> CreatePR_CreatePR

    LLM["LLM"]
    LLM_init[init.py]
    LLM_typed[typed.py]
    LLM_readme[README.md]
    LLM_LLM[LLM.py]

    patchwork --> LLM
    LLM --> LLM_init
    LLM --> LLM_typed
    LLM --> LLM_readme
    LLM --> LLM_LLM

    PR["PR"]
    PR_init[init.py]
    PR_typed[typed.py]
    PR_readme[README.md]
    PR_PR[PR.py]

    patchwork --> PR
    PR --> PR_init
    PR --> PR_typed
    PR --> PR_readme
    PR --> PR_PR

    ExtractCodeMethodForCommentContexts["ExtractCodeMethodForCommentContexts"]
    ExtractCodeMethodForCommentContexts_init[init.py]
    ExtractCodeMethodForCommentContexts_typed[typed.py]
    ExtractCodeMethodForCommentContexts_readme[README.md]
    ExtractCodeMethodForCommentContexts_ExtractCodeMethodForCommentContexts[ExtractCodeMethodForCommentContexts.py]

    patchwork --> ExtractCodeMethodForCommentContexts
    ExtractCodeMethodForCommentContexts --> ExtractCodeMethodForCommentContexts_init
    ExtractCodeMethodForCommentContexts --> ExtractCodeMethodForCommentContexts_typed
    ExtractCodeMethodForCommentContexts --> ExtractCodeMethodForCommentContexts_readme
    ExtractCodeMethodForCommentContexts --> ExtractCodeMethodForCommentContexts_ExtractCodeMethodForCommentContexts

    CreateIssue["CreateIssue"]
    CreateIssue_init[init.py]
    CreateIssue_typed[typed.py]
    CreateIssue_readme[README.md]
    CreateIssue_CreateIssue[CreateIssue.py]

    patchwork --> CreateIssue
    CreateIssue --> CreateIssue_init
    CreateIssue --> CreateIssue_typed
    CreateIssue --> CreateIssue_readme
    CreateIssue --> CreateIssue_CreateIssue

    ModifyCodeOnce["ModifyCodeOnce"]
    ModifyCodeOnce_init[init.py]
    ModifyCodeOnce_typed[typed.py]
    ModifyCodeOnce_readme[README.md]
    ModifyCodeOnce_ModifyCodeOnce[ModifyCodeOnce.py]

    patchwork --> ModifyCodeOnce
    ModifyCodeOnce --> ModifyCodeOnce_init
    ModifyCodeOnce --> ModifyCodeOnce_typed
    ModifyCodeOnce --> ModifyCodeOnce_readme
    ModifyCodeOnce --> ModifyCodeOnce_ModifyCodeOnce

    ExtractModelResponse["ExtractModelResponse"]
    ExtractModelResponse_init[init.py]
    ExtractModelResponse_typed[typed.py]
    ExtractModelResponse_readme[README.md]
    ExtractModelResponse_ExtractModelResponse[ExtractModelResponse.py]

    patchwork --> ExtractModelResponse
    ExtractModelResponse --> ExtractModelResponse_init
    ExtractModelResponse --> ExtractModelResponse_typed
    ExtractModelResponse --> ExtractModelResponse_readme
    ExtractModelResponse --> ExtractModelResponse_ExtractModelResponse

    JoinList["JoinList"]
    JoinList_init[init.py]
    JoinList_typed[typed.py]
    JoinList_readme[README.md]
    JoinList_JoinList[JoinList.py]

    patchwork --> JoinList
    JoinList --> JoinList_init
    JoinList --> JoinList_typed
    JoinList --> JoinList_readme
    JoinList --> JoinList_JoinList

    SimplifiedLLM["SimplifiedLLM"]
    SimplifiedLLM_init[init.py]
    SimplifiedLLM_typed[typed.py]
    SimplifiedLLM_readme[README.md]
    SimplifiedLLM_SimplifiedLLM[SimplifiedLLM.py]

    patchwork --> SimplifiedLLM
    SimplifiedLLM --> SimplifiedLLM_init
    SimplifiedLLM --> SimplifiedLLM_typed
    SimplifiedLLM --> SimplifiedLLM_readme
    SimplifiedLLM --> SimplifiedLLM_SimplifiedLLM

    CallAPI["CallAPI"]
    CallAPI_init[init.py]
    CallAPI_typed[typed.py]
    CallAPI_readme[README.md]
    CallAPI_CallAPI[CallAPI.py]

    patchwork --> CallAPI
    CallAPI --> CallAPI_init
    CallAPI --> CallAPI_typed
    CallAPI --> CallAPI_readme
    CallAPI --> CallAPI_CallAPI

    ExtractPackageManagerFile["ExtractPackageManagerFile"]
    ExtractPackageManagerFile_init[init.py]
    ExtractPackageManagerFile_typed[typed.py]
    ExtractPackageManagerFile_readme[README.md]
    ExtractPackageManagerFile_ExtractPackageManagerFile[ExtractPackageManagerFile.py]
    ExtractPackageManagerFile_TestExtractPackageManagerFile[TestExtractPackageManagerFile.py]

    patchwork --> ExtractPackageManagerFile
    ExtractPackageManagerFile --> ExtractPackageManagerFile_init
    ExtractPackageManagerFile --> ExtractPackageManagerFile_typed
    ExtractPackageManagerFile --> ExtractPackageManagerFile_readme
    ExtractPackageManagerFile --> ExtractPackageManagerFile_ExtractPackageManagerFile
    ExtractPackageManagerFile --> ExtractPackageManagerFile_TestExtractPackageManagerFile

    ReadIssues["ReadIssues"]
    ReadIssues_init[init.py]
    ReadIssues_typed[typed.py]
    ReadIssues_readme[README.md]
    ReadIssues_ReadIssues[ReadIssues.py]

    patchwork --> ReadIssues
    ReadIssues --> ReadIssues_init
    ReadIssues --> ReadIssues_typed
    ReadIssues --> ReadIssues_readme
    ReadIssues --> ReadIssues_ReadIssues

    ReadFile["ReadFile"]
    ReadFile_init[init.py]
    ReadFile_typed[typed.py]
    ReadFile_readme[README.md]
    ReadFile_ReadFile[ReadFile.py]

    patchwork --> ReadFile
    ReadFile --> ReadFile_init
    ReadFile --> ReadFile_typed
    ReadFile --> ReadFile_readme
    ReadFile --> ReadFile_ReadFile

    GenerateEmbeddings["GenerateEmbeddings"]
    GenerateEmbeddings_init[init.py]
    GenerateEmbeddings_typed[typed.py]
    GenerateEmbeddings_readme[README.md]
    GenerateEmbeddings_GenerateEmbeddings[GenerateEmbeddings.py]

    patchwork --> GenerateEmbeddings
    GenerateEmbeddings --> GenerateEmbeddings_init
    GenerateEmbeddings --> GenerateEmbeddings_typed
    GenerateEmbeddings --> GenerateEmbeddings_readme
    GenerateEmbeddings --> GenerateEmbeddings_GenerateEmbeddings

    ScanDepscan["ScanDepscan"]
    ScanDepscan_init[init.py]
    ScanDepscan_typed[typed.py]
    ScanDepscan_readme[README.md]
    ScanDepscan_ScanDepscan[ScanDepscan.py]

    patchwork --> ScanDepscan
    ScanDepscan --> ScanDepscan_init
    ScanDepscan --> ScanDepscan_typed
    ScanDepscan --> ScanDepscan_readme
    ScanDepscan --> ScanDepscan_ScanDepscan

    SlackMessage["SlackMessage"]
    SlackMessage_init[init.py]
    SlackMessage_typed[typed.py]
    SlackMessage_readme[README.md]
    SlackMessage_SlackMessage[SlackMessage.py]

    patchwork --> SlackMessage
    SlackMessage --> SlackMessage_init
    SlackMessage --> SlackMessage_typed
    SlackMessage --> SlackMessage_readme
    SlackMessage --> SlackMessage_SlackMessage
