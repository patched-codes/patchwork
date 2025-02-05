classDiagram
    direction LR

    class patchwork{
    }

    subgraph patchwork
        subgraph steps
            class Readme
            class Init
            class ReadPRs
            class ModifyCodeOnce
            class ModifyCode
            class LLM
            class CallLLM
            class ScanSonar
            class ExtractPackageManagerFile
            class FixIssue
            class ReadIssues
            class CreateIssue
            class GetTypescriptTypeInfo
            class FilterBySimilarity
            class ScanDepscan
            class QueryEmbeddings
            class ExtractModelResponse
            class SlackMessage
            class SimplifiedLLM
            class CommitChanges
            class JoinList
            class CreateIssueComment
            class ExtractCodeContexts
            class CallShell
            class PR
            class ReadFile
            class AnalyzeImpact
            class ExtractCode
            class GenerateCodeRepositoryEmbeddings
            class ExtractCodeMethodForCommentContexts
            class SimplifiedLLMOnce
            class PreparePR
            class ReadPRDiffs
            class CallAPI
            class GenerateEmbeddings
            class AgenticLLM
            class CreatePRComment
            class CallSQL
            class Combine
            class PreparePrompt
            class ExtractDiff
            class CreatePR
            class ScanSemgrep
            class CallCode2Prompt
            
            >>> Init --> ReadPRs
            >>> Init --> ModifyCodeOnce
            >>> Init --> ModifyCode
            >>> Init --> LLM
            >>> Init --> CallLLM
            >>> Init --> ScanSonar
            >>> Init --> ExtractPackageManagerFile
            >>> Init --> FixIssue
            >>> Init --> ReadIssues
            >>> Init --> CreateIssue
            >>> Init --> GetTypescriptTypeInfo
            >>> Init --> FilterBySimilarity
            >>> Init --> ScanDepscan
            >>> Init --> QueryEmbeddings
            >>> Init --> ExtractModelResponse
            >>> Init --> SlackMessage
            >>> Init --> SimplifiedLLM
            >>> Init --> CommitChanges
            >>> Init --> JoinList
            >>> Init --> CreateIssueComment
            >>> Init --> ExtractCodeContexts
            >>> Init --> CallShell
            >>> Init --> PR
            >>> Init --> ReadFile
            >>> Init --> AnalyzeImpact
            >>> Init --> ExtractCode
            >>> Init --> GenerateCodeRepositoryEmbeddings
            >>> Init --> ExtractCodeMethodForCommentContexts
            >>> Init --> SimplifiedLLMOnce
            >>> Init --> PreparePR
            >>> Init --> ReadPRDiffs
            >>> Init --> CallAPI
            >>> Init --> GenerateEmbeddings
            >>> Init --> AgenticLLM
            >>> Init --> CreatePRComment
            >>> Init --> CallSQL
            >>> Init --> Combine
            >>> Init --> PreparePrompt
            >>> Init --> ExtractDiff
            >>> Init --> CreatePR
            >>> Init --> ScanSemgrep
            >>> Init --> CallCode2Prompt
        end
    end
