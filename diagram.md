graph TD
subgraph patchwork
  subgraph steps
    patchwork_init["__init__.py"]
    patchwork_readme_md["README.md"]
    
    subgraph ReadPRs
      ReadPRs_py["ReadPRs.py"]
      ReadPRs_init["__init__.py"]
      ReadPRs_typed["typed.py"]
      ReadPRs_readme_md["README.md"]
    end
    
    subgraph ModifyCodeOnce
      ModifyCodeOnce_py["ModifyCodeOnce.py"]
      ModifyCodeOnce_init["__init__.py"]
      ModifyCodeOnce_typed["typed.py"]
      ModifyCodeOnce_readme_md["README.md"]
    end
    
    subgraph ModifyCode
      ModifyCode_py["ModifyCode.py"]
      ModifyCode_init["__init__.py"]
      ModifyCode_typed["typed.py"]
      ModifyCode_readme_md["README.md"]
    end
    
    subgraph LLM
      LLM_py["LLM.py"]
      LLM_init["__init__.py"]
      LLM_typed["typed.py"]
      LLM_readme_md["README.md"]
    end
    
    subgraph CallLLM
      CallLLM_py["CallLLM.py"]
      CallLLM_init["__init__.py"]
      CallLLM_typed["typed.py"]
      CallLLM_readme_md["README.md"]
    end
    
    subgraph ScanSonar
      ScanSonar_py["ScanSonar.py"]
      ScanSonar_init["__init__.py"]
      ScanSonar_typed["typed.py"]
      ScanSonar_readme_md["README.md"]
    end
    
    subgraph ExtractPackageManagerFile
      ExtractPackageManagerFile_init["__init__.py"]
      ExtractPackageManagerFile_typed["typed.py"]
      TestExtractPackageManagerFile["TestExtractPackageManagerFile.py"]
      ExtractPackageManagerFile_py["ExtractPackageManagerFile.py"]
      ExtractPackageManagerFile_readme_md["README.md"]
    end
    
    subgraph FixIssue
      FixIssue_py["FixIssue.py"]
      FixIssue_init["__init__.py"]
      FixIssue_typed["typed.py"]
      FixIssue_readme_md["README.md"]
    end
    
    subgraph ReadIssues
      ReadIssues_py["ReadIssues.py"]
      ReadIssues_init["__init__.py"]
      ReadIssues_typed["typed.py"]
      ReadIssues_readme_md["README.md"]
    end
    
    subgraph CreateIssue
      CreateIssue_py["CreateIssue.py"]
      CreateIssue_init["__init__.py"]
      CreateIssue_typed["typed.py"]
      CreateIssue_readme_md["README.md"]
    end
    
    subgraph GetTypescriptTypeInfo
      tsconfig_json["tsconfig.json"]
      GetTypescriptTypeInfo_py["GetTypescriptTypeInfo.py"]
      package_json["package.json"]
      get_type_info_ts["get_type_info.ts"]
      GetTypescriptTypeInfo_init["__init__.py"]
      GetTypescriptTypeInfo_typed["typed.py"]
      pnpm_lock_yaml["pnpm-lock.yaml"]
      GetTypescriptTypeInfo_readme_md["README.md"]
    end
    
    subgraph FilterBySimilarity
      FilterBySimilarity_init["__init__.py"]
      FilterBySimilarity_typed["typed.py"]
      FilterBySimilarity_py["FilterBySimilarity.py"]
      FilterBySimilarity_readme_md["README.md"]
    end
    
    subgraph ScanDepscan
      ScanDepscan_py["ScanDepscan.py"]
      ScanDepscan_init["__init__.py"]
      ScanDepscan_typed["typed.py"]
      ScanDepscan_readme_md["README.md"]
    end
    
    subgraph QueryEmbeddings
      QueryEmbeddings_py["QueryEmbeddings.py"]
      QueryEmbeddings_init["__init__.py"]
      QueryEmbeddings_typed["typed.py"]
      QueryEmbeddings_readme_md["README.md"]
    end
    
    subgraph ExtractModelResponse
      ExtractModelResponse_init["__init__.py"]
      ExtractModelResponse_typed["typed.py"]
      ExtractModelResponse_py["ExtractModelResponse.py"]
      ExtractModelResponse_readme_md["README.md"]
    end
    
    subgraph SlackMessage
      SlackMessage_py["SlackMessage.py"]
      SlackMessage_init["__init__.py"]
      SlackMessage_typed["typed.py"]
      SlackMessage_readme_md["README.md"]
    end
    
    subgraph SimplifiedLLM
      SimplifiedLLM_py["SimplifiedLLM.py"]
      SimplifiedLLM_init["__init__.py"]
      SimplifiedLLM_typed["typed.py"]
      SimplifiedLLM_readme_md["README.md"]
    end
    
    subgraph CommitChanges
      CommitChanges_py["CommitChanges.py"]
      CommitChanges_init["__init__.py"]
      CommitChanges_typed["typed.py"]
      CommitChanges_readme_md["README.md"]
    end
    
    subgraph JoinList
      JoinList_py["JoinList.py"]
      JoinList_init["__init__.py"]
      JoinList_typed["typed.py"]
      JoinList_readme_md["README.md"]
    end
    
    subgraph CreateIssueComment
      CreateIssueComment_py["CreateIssueComment.py"]
      CreateIssueComment_init["__init__.py"]
      CreateIssueComment_typed["typed.py"]
      CreateIssueComment_readme_md["README.md"]
    end
    
    subgraph ExtractCodeContexts
      ExtractCodeContexts_py["ExtractCodeContexts.py"]
      ExtractCodeContexts_init["__init__.py"]
      ExtractCodeContexts_typed["typed.py"]
      ExtractCodeContexts_readme_md["README.md"]
    end
    
    subgraph CallShell
      CallShell_py["CallShell.py"]
      CallShell_init["__init__.py"]
      CallShell_typed["typed.py"]
    end
    
    subgraph PR
      PR_py["PR.py"]
      PR_init["__init__.py"]
      PR_typed["typed.py"]
      PR_readme_md["README.md"]
    end
    
    subgraph ReadFile
      ReadFile_py["ReadFile.py"]
      ReadFile_init["__init__.py"]
      ReadFile_typed["typed.py"]
      ReadFile_readme_md["README.md"]
    end
    
    subgraph AnalyzeImpact
      AnalyzeImpact_py["AnalyzeImpact.py"]
      AnalyzeImpact_init["__init__.py"]
      AnalyzeImpact_typed["typed.py"]
      AnalyzeImpact_readme_md["README.md"]
    end
    
    subgraph ExtractCode
      ExtractCode_py["ExtractCode.py"]
      ExtractCode_init["__init__.py"]
      ExtractCode_typed["typed.py"]
      ExtractCode_readme_md["README.md"]
    end    
    
    subgraph GenerateCodeRepositoryEmbeddings
      filter_lists_py["filter_lists.py"]
      GenerateCodeRepositoryEmbeddings_py["GenerateCodeRepositoryEmbeddings.py"]
      GenerateCodeRepositoryEmbeddings_init["__init__.py"]
      GenerateCodeRepositoryEmbeddings_typed["typed.py"]
      GenerateCodeRepositoryEmbeddings_readme_md["README.md"]
    end
    
    subgraph ExtractCodeMethodForCommentContexts
      ExtractCodeMethodForCommentContexts_py["ExtractCodeMethodForCommentContexts.py"]
      ExtractCodeMethodForCommentContexts_init["__init__.py"]
      ExtractCodeMethodForCommentContexts_typed["typed.py"]
      ExtractCodeMethodForCommentContexts_readme_md["README.md"]
    end
    
    subgraph SimplifiedLLMOnce
      SimplifiedLLMOnce_py["SimplifiedLLMOnce.py"]
      SimplifiedLLMOnce_init["__init__.py"]
      SimplifiedLLMOnce_typed["typed.py"]
      SimplifiedLLMOnce_readme_md["README.md"]
    end
    
    subgraph PreparePR
      PreparePR_py["PreparePR.py"]
      PreparePR_init["__init__.py"]
      PreparePR_typed["typed.py"]
      PreparePR_readme_md["README.md"]
    end
    
    subgraph ReadPRDiffs
      ReadPRDiffs_py["ReadPRDiffs.py"]
      ReadPRDiffs_init["__init__.py"]
      ReadPRDiffs_typed["typed.py"]
      ReadPRDiffs_readme_md["README.md"]
    end
    
    subgraph CallAPI
      CallAPI_init["__init__.py"]
      CallAPI_typed["typed.py"]
      CallAPI_py["CallAPI.py"]
      CallAPI_readme_md["README.md"]
    end
    
    subgraph GenerateEmbeddings
      GenerateEmbeddings_py["GenerateEmbeddings.py"]
      GenerateEmbeddings_init["__init__.py"]
      GenerateEmbeddings_typed["typed.py"]
      GenerateEmbeddings_readme_md["README.md"]
    end
    
    subgraph AgenticLLM
      AgenticLLM_py["AgenticLLM.py"]
      AgenticLLM_init["__init__.py"]
      AgenticLLM_typed["typed.py"]
    end
    
    subgraph CreatePRComment
      CreatePRComment_py["CreatePRComment.py"]
      CreatePRComment_init["__init__.py"]
      CreatePRComment_typed["typed.py"]
      CreatePRComment_readme_md["README.md"]
    end
    
    subgraph CallSQL
      CallSQL_py["CallSQL.py"]
      CallSQL_init["__init__.py"]
      CallSQL_typed["typed.py"]
    end
    
    subgraph Combine
      Combine_init["__init__.py"]
      Combine_typed["typed.py"]
      Combine_py["Combine.py"]
      Combine_readme_md["README.md"]
    end
    
    subgraph PreparePrompt
      PreparePrompt_py["PreparePrompt.py"]
      PreparePrompt_init["__init__.py"]
      PreparePrompt_typed["typed.py"]
      PreparePrompt_readme_md["README.md"]
    end

    subgraph ExtractDiff
      ExtractDiff_py["ExtractDiff.py"]
      ExtractDiff_init["__init__.py"]
      ExtractDiff_typed["typed.py"]
      ExtractDiff_readme_md["README.md"]
    end
    
    subgraph CreatePR
      CreatePR_py["CreatePR.py"]
      CreatePR_init["__init__.py"]
      CreatePR_typed["typed.py"]
      CreatePR_readme_md["README.md"]
    end
    
    subgraph ScanSemgrep
      ScanSemgrep_py["ScanSemgrep.py"]
      ScanSemgrep_init["__init__.py"]
      ScanSemgrep_typed["typed.py"]
      ScanSemgrep_readme_md["README.md"]
    end
    
    subgraph CallCode2Prompt
      TestCallCode2Prompt["TestCallCode2Prompt.py"]
      CallCode2Prompt_init["__init__.py"]
      CallCode2Prompt_typed["typed.py"]
      CallCode2Prompt_py["CallCode2Prompt.py"]
      CallCode2Prompt_readme_md["README.md"]
    end
  end
end
