classDiagram
    class Patchwork {
        -str: base_dir
        +start(): void
    }
    class Step {
        <<abstract>>
        +run(): dict
        +set_status(status, message): void
        +get_status(): tuple(Status, str)
    }
    class LLM extends Step
    class CallLLM extends Step
    class PreparePrompt extends Step
    class CreatePR extends Step
    class CreateIssueComment extends Step
    class Combine extends Step
    class GenerateEmbeddings extends Step
    class AnalyzeImpact extends Step
    class GenerateCodeRepositoryEmbeddings extends Step
    class CallAPI extends Step
    class FixIssue extends Step
    class ExtractPackageManagerFile extends Step
    class ExtractDiff extends Step
    class ExtractModelResponse extends Step
    class ExtractCodeContexts extends Step
    class ExtractCode extends Step
    class SimplifiedLLMOnce extends Step
    class QueryEmbeddings extends Step
    class ModifyCodeOnce extends Step
    class ModifyCode extends Step
    class JoinList extends Step
    class FilterBySimilarity extends Step
    class ReadPRs extends Step
    class ReadPRDiffs extends Step
    class ReadIssues extends Step
    class SlackMessage extends Step
    class CommitChanges extends Step
    class ScanSemgrep extends Step
    class ScanDepscan extends Step
    class ReadFile extends Step
    class CallCode2Prompt extends Step
    class CreatePRComment extends Step
    class SlackMessage
    class CreateIssue
    Patchwork "1" --> "*" Step
    Step <|-- LLM
    Step <|-- CallLLM
    Step <|-- PreparePrompt
    Step <|-- CreatePR
    Step <|-- CreateIssueComment
    Step <|-- Combine
    Step <|-- GenerateEmbeddings
    Step <|-- AnalyzeImpact
    Step <|-- GenerateCodeRepositoryEmbeddings
    Step <|-- CallAPI
    Step <|-- FixIssue
    Step <|-- ExtractPackageManagerFile
    Step <|-- ExtractDiff
    Step <|-- ExtractModelResponse
    Step <|-- ExtractCodeContexts
    Step <|-- ExtractCode
    Step <|-- SimplifiedLLMOnce
    Step <|-- QueryEmbeddings
    Step <|-- ModifyCodeOnce
    Step <|-- ModifyCode
    Step <|-- JoinList
    Step <|-- FilterBySimilarity
    Step <|-- ReadPRs
    Step <|-- ReadPRDiffs
    Step <|-- ReadIssues
    Step <|-- SlackMessage
    Step <|-- CommitChanges
    Step <|-- ScanSemgrep
    Step <|-- ScanDepscan
    Step <|-- ReadFile
    Step <|-- CallCode2Prompt
    Step <|-- CreatePRComment
    Step <|-- CreateIssue
