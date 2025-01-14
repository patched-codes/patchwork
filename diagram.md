classDiagram
    direction TB
    class patchwork.steps {
        <<Directory>>
    }
    class ScanSemgrep {
        <<Directory>>
    }
    class ModifyCode {
        <<Directory>>
    }
    class PreparePrompt {
        <<Directory>>
    }
    class CallLLM {
        <<Directory>>
    }
    class Combine {
        <<Directory>>
    }
    class CreateIssueComment {
        <<Directory>>
    }
    class CommitChanges {
        <<Directory>>
    }
    class PreparePR {
        <<Directory>>
    }
    class ReadPRs {
        <<Directory>>
    }
    class GetTypescriptTypeInfo {
        <<Directory>>
    }
    class QueryEmbeddings {
        <<Directory>>
    }
    class ExtractCodeContexts {
        <<Directory>>
    }
    class GenerateCodeRepositoryEmbeddings {
        <<Directory>>
    }
    class ExtractDiff {
        <<Directory>>
    }
    class FixIssue {
        <<Directory>>
    }
    class CallCode2Prompt {
        <<Directory>>
    }
    class SimplifiedLLMOnce {
        <<Directory>>
    }
    class CreatePRComment {
        <<Directory>>
    }
    class ReadPRDiffs {
        <<Directory>>
    }
    class AnalyzeImpact {
        <<Directory>>
    }
    class FilterBySimilarity {
        <<Directory>>
    }
    class ExtractCode {
        <<Directory>>
    }
    class CreatePR {
        <<Directory>>
    }
    class LLM {
        <<Directory>>
    }
    class PR {
        <<Directory>>
    }
    class ExtractCodeMethodForCommentContexts {
        <<Directory>>
    }
    class CreateIssue {
        <<Directory>>
    }
    class ModifyCodeOnce {
        <<Directory>>
    }
    class ExtractModelResponse {
        <<Directory>>
    }
    class JoinList {
        <<Directory>>
    }
    class SimplifiedLLM {
        <<Directory>>
    }
    class CallAPI {
        <<Directory>>
    }
    class ExtractPackageManagerFile {
        <<Directory>>
    }
    class ReadIssues {
        <<Directory>>
    }
    class ReadFile {
        <<Directory>>
    }
    class ScanSonar {
        <<Directory>>
    }
    class GenerateEmbeddings {
        <<Directory>>
    }
    class AgenticLLM {
        <<Directory>>
    }
    class ScanDepscan {
        <<Directory>>
    }
    class SlackMessage {
        <<Directory>>
    }
    patchwork.steps --> ScanSemgrep
    patchwork.steps --> ModifyCode
    patchwork.steps --> PreparePrompt
    patchwork.steps --> CallLLM
    patchwork.steps --> Combine
    patchwork.steps --> CreateIssueComment
    patchwork.steps --> CommitChanges
    patchwork.steps --> PreparePR
    patchwork.steps --> ReadPRs
    patchwork.steps --> GetTypescriptTypeInfo
    patchwork.steps --> QueryEmbeddings
    patchwork.steps --> ExtractCodeContexts
    patchwork.steps --> GenerateCodeRepositoryEmbeddings
    patchwork.steps --> ExtractDiff
    patchwork.steps --> FixIssue
    patchwork.steps --> CallCode2Prompt
    patchwork.steps --> SimplifiedLLMOnce
    patchwork.steps --> CreatePRComment
    patchwork.steps --> ReadPRDiffs
    patchwork.steps --> AnalyzeImpact
    patchwork.steps --> FilterBySimilarity
    patchwork.steps --> ExtractCode
    patchwork.steps --> CreatePR
    patchwork.steps --> LLM
    patchwork.steps --> PR
    patchwork.steps --> ExtractCodeMethodForCommentContexts
    patchwork.steps --> CreateIssue
    patchwork.steps --> ModifyCodeOnce
    patchwork.steps --> ExtractModelResponse
    patchwork.steps --> JoinList
    patchwork.steps --> SimplifiedLLM
    patchwork.steps --> CallAPI
    patchwork.steps --> ExtractPackageManagerFile
    patchwork.steps --> ReadIssues
    patchwork.steps --> ReadFile
    patchwork.steps --> ScanSonar
    patchwork.steps --> GenerateEmbeddings
    patchwork.steps --> AgenticLLM
    patchwork.steps --> ScanDepscan
    patchwork.steps --> SlackMessage
