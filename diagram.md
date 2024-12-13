graph TD
  subgraph Patchwork
    direction TB
    PatchworkStepSteps
    
    PatchworkStepSteps -->|Import| PreparePrompt["PreparePrompt.py"]
    PatchworkStepSteps -->|Import| CallLLM["CallLLM.py"]
    PatchworkStepSteps -->|Import| CreatePR["CreatePR.py"]
    PatchworkStepSteps -->|Import| QueryEmbeddings["QueryEmbeddings.py"]
    PatchworkStepSteps -->|Import| ExtractCode["ExtractCode.py"]
    PatchworkStepSteps -->|Import| GenerateEmbeddings["GenerateEmbeddings.py"]

    subgraph Steps
      direction LR
      subgraph StepModules
        direction TB
        PreparePrompt
        CallLLM
        CreatePR
        QueryEmbeddings
        ExtractCode
        GenerateEmbeddings
      end

      subgraph StepsImportDetails
        direction LR
        ScanSemgrep["ScanSemgrep.py"]
        ModifyCode["ModifyCode.py"]
        PreparePR["PreparePR.py"]
        CreateIssueComment["CreateIssueComment.py"]
        CommitChanges["CommitChanges.py"]
        ReadPRs["ReadPRs.py"]
        GetTypescriptTypeInfo["GetTypescriptTypeInfo.py"]
        ExtractDiff["ExtractDiff.py"]
        FixIssue["FixIssue.py"]
        CallCode2Prompt["CallCode2Prompt.py"]
        SimplifiedLLMOnce["SimplifiedLLMOnce.py"]
        CreatePRComment["CreatePRComment.py"]
        ReadPRDiffs["ReadPRDiffs.py"]
        AnalyzeImpact["AnalyzeImpact.py"]
        FilterBySimilarity["FilterBySimilarity.py"]
        ExtractCodeMethodForCommentContexts["ExtractCodeMethodForCommentContexts.py"]
        CreateIssue["CreateIssue.py"]
        ModifyCodeOnce["ModifyCodeOnce.py"]
        ExtractModelResponse["ExtractModelResponse.py"]
        JoinList["JoinList.py"]
        SimplifiedLLM["SimplifiedLLM.py"]
        CallAPI["CallAPI.py"]
        ExtractPackageManagerFile["ExtractPackageManagerFile.py"]
        ReadIssues["ReadIssues.py"]
        ReadFile["ReadFile.py"]
        ScanDepscan["ScanDepscan.py"]
        SlackMessage["SlackMessage.py"]
      end
    end

    StepModules -->|Uses| StepsImportDetails
  end
