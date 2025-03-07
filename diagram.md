graph TB
  subgraph patchwork
    subgraph Steps
      directions["ExtractCodeMethodForCommentContexts"]
      preparePrompt["PreparePrompt"]
      extractCodeContexts["ExtractCodeContexts"]
      readPRs["ReadPRs"]
      slackMessage["SlackMessage"]
      callAPI["CallAPI"]
      sendEmail["SendEmail"]
      callLLM["CallLLM"]
      readFile["ReadFile"]
      agenticLLM["AgenticLLM"]
      llm["LLM"]
      scanSemgrep["ScanSemgrep"]
      combine["Combine"]
      readIssues["ReadIssues"]
      fixIssue["FixIssue"]
      filterBySimilarity["FilterBySimilarity"]
      extractCode["ExtractCode"]
      analyzeImpact["AnalyzeImpact"]
      extractModelResponse["ExtractModelResponse"]
      createIssue["CreateIssue"]
      scanSonar["ScanSonar"]
      pr["PR"]
      callSQL["CallSQL"]
      modifyCodeOnce["ModifyCodeOnce"]
      getTypescriptTypeInfo["GetTypescriptTypeInfo"]
      createIssueComment["CreateIssueComment"]
      browserUse["BrowserUse"]
      callCode2Prompt["CallCode2Prompt"]
      preparePR["PreparePR"]
      joinList["JoinList"]
      createPR["CreatePR"]
      scanDepscan["ScanDepscan"]
      simplifiedLLMOnce["SimplifiedLLMOnce"]
      modifyCode["ModifyCode"]
      manageEngineAgent["ManageEngineAgent"]
      agenticLLMV2["AgenticLLMV2"]
      extractDiff["ExtractDiff"]
      readEmail["ReadEmail"]
      createPRComment["CreatePRComment"]
      readPRDiffs["ReadPRDiffs"]
      simplifiedLLM["SimplifiedLLM"]
      callShell["CallShell"]
      commitChanges["CommitChanges"]
      gitHubAgent["GitHubAgent"]
      extractPackageManagerFile["ExtractPackageManagerFile"]
    end
  end

  extractCodeMethodForCommentContexts --> extractCodeContexts
  preparePrompt --> callLLM
  readPRs --> readPRDiffs
  scanDepscan --> extractPackageManagerFile
  modifyCodeOnce --> modifyCode
  simplifiedLLMOnce --> callLLM
  createIssue --> createIssueComment
  createPR --> createPRComment
  agenticLLMV2 --> agenticLLM
  scanSonar --> extractCodeContexts
  readIssues --> fixIssue
  callAPI --> callLLM
  llm --> callLLM
  combine --> combine
  browserUse --> llm
  sendEmail --> readEmail
  callSQL --> readFile
  slackMessage --> readEmail
  manageEngineAgent --> gitHubAgent
  analyzeImpact --> fixIssue
  pr --> preparePR
