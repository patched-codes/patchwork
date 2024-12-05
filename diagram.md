classDiagram
    class Patchwork
    Patchwork: +AnalyzeImpact
    Patchwork: +CallAPI
    Patchwork: +CallCode2Prompt
    Patchwork: +CallLLM
    Patchwork: +Combine
    Patchwork: +CommitChanges
    Patchwork: +CreateIssue
    Patchwork: +CreateIssueComment
    Patchwork: +CreatePR
    Patchwork: +CreatePRComment
    Patchwork: +ExtractCode
    Patchwork: +ExtractCodeContexts
    Patchwork: +ExtractCodeMethodForCommentContexts
    Patchwork: +ExtractDiff
    Patchwork: +ExtractModelResponse
    Patchwork: +ExtractPackageManagerFile
    Patchwork: +FilterBySimilarity
    Patchwork: +FixIssue
    Patchwork: +GenerateCodeRepositoryEmbeddings
    Patchwork: +GenerateEmbeddings
    Patchwork: +GetTypescriptTypeInfo
    Patchwork: +JoinList
    Patchwork: +LLM
    Patchwork: +ModifyCode
    Patchwork: +ModifyCodeOnce
    Patchwork: +PR
    Patchwork: +PreparePR
    Patchwork: +PreparePrompt
    Patchwork: +QueryEmbeddings
    Patchwork: +ReadFile
    Patchwork: +ReadIssues
    Patchwork: +ReadPRDiffs
    Patchwork: +ReadPRs
    Patchwork: +ScanDepscan
    Patchwork: +ScanSemgrep
    Patchwork: +SimplifiedLLM
    Patchwork: +SimplifiedLLMOnce
    Patchwork: +SlackMessage
    Patchwork: +KeyAliasing
    class AnalyzeImpact
    class CallAPI
    class CallCode2Prompt
    class CallLLM
    class Combine
    class CommitChanges
    class CreateIssue
    class CreateIssueComment
    class CreatePR
    class CreatePRComment
    class ExtractCode
    class ExtractCodeContexts
    class ExtractCodeMethodForCommentContexts
    class ExtractDiff
    class ExtractModelResponse
    class ExtractPackageManagerFile
    class FilterBySimilarity
    class FixIssue
    class GenerateCodeRepositoryEmbeddings
    class GenerateEmbeddings
    class GetTypescriptTypeInfo
    class JoinList
    class LLM
    class ModifyCode
    class ModifyCodeOnce
    class PR
    class PreparePR
    class PreparePrompt
    class QueryEmbeddings
    class ReadFile
    class ReadIssues
    class ReadPRDiffs
    class ReadPRs
    class ScanDepscan
    class ScanSemgrep
    class SimplifiedLLM
    class SimplifiedLLMOnce
    class SlackMessage
    Patchwork <|-- AnalyzeImpact
    Patchwork <|-- CallAPI
    Patchwork <|-- CallCode2Prompt
    Patchwork <|-- CallLLM
    Patchwork <|-- Combine
    Patchwork <|-- CommitChanges
    Patchwork <|-- CreateIssue
    Patchwork <|-- CreateIssueComment
    Patchwork <|-- CreatePR
    Patchwork <|-- CreatePRComment
    Patchwork <|-- ExtractCode
    Patchwork <|-- ExtractCodeContexts
    Patchwork <|-- ExtractCodeMethodForCommentContexts
    Patchwork <|-- ExtractDiff
    Patchwork <|-- ExtractModelResponse
    Patchwork <|-- ExtractPackageManagerFile
    Patchwork <|-- FilterBySimilarity
    Patchwork <|-- FixIssue
    Patchwork <|-- GenerateCodeRepositoryEmbeddings
    Patchwork <|-- GenerateEmbeddings
    Patchwork <|-- GetTypescriptTypeInfo
    Patchwork <|-- JoinList
    Patchwork <|-- LLM
    Patchwork <|-- ModifyCode
    Patchwork <|-- ModifyCodeOnce
    Patchwork <|-- PR
    Patchwork <|-- PreparePR
    Patchwork <|-- PreparePrompt
    Patchwork <|-- QueryEmbeddings
    Patchwork <|-- ReadFile
    Patchwork <|-- ReadIssues
    Patchwork <|-- ReadPRDiffs
    Patchwork <|-- ReadPRs
    Patchwork <|-- ScanDepscan
    Patchwork <|-- ScanSemgrep
    Patchwork <|-- SimplifiedLLM
    Patchwork <|-- SimplifiedLLMOnce
    Patchwork <|-- SlackMessage
