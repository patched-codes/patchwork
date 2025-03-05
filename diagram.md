classDiagram
    class Step {
        <<abstract>>
        run() dict
    }
    class ExtractCodeMethodForCommentContexts {
        +__init__(inputs: dict)
        +run() dict
    }
    class PreparePrompt {
        +__init__(inputs: dict)
        +run() dict
    }
    class ExtractCodeContexts {
        +__init__(inputs: dict)
        +run() dict
        +get_positions(max_depth: int)
    }
    class ReadPRs {
        +__init__(inputs: DataPoint)
        +run() DataPoint
    }
    class SlackMessage {
        +__init__(inputs)
        +run()
    }
    class CallAPI {
        +__init__(inputs)
        +run()
    }
    class SendEmail {
        +__init__(inputs)
        +run() dict
    }
    class CallLLM {
        +__init__(inputs: dict)
        +run() dict
    }
    class ReadFile {
        +__init__(inputs)
        +run()
    }
    class AgenticLLM {
        +__init__(inputs)
        +run() dict
    }
    class LLM {
        +__init__(inputs)
        +run() dict
    }
    class ScanSemgrep {
        +__init__(inputs: dict)
        +run() dict
    }
    class Combine {
        +__init__(inputs)
        +run()
    }
    class ReadIssues {
        +__init__(inputs: dict)
        +run() dict
    }
    class FixIssue {
        +__init__(inputs)
        +run() dict
    }
    class FilterBySimilarity {
        +__init__(inputs)
        +run()
    }
    class ExtractCode {
        +__init__(inputs: dict)
        +run() dict
    }
    class AnalyzeImpact {
        +__init__(inputs: dict)
        +run() dict
    }
    class ExtractModelResponse {
        +__init__(inputs: dict)
        +run() dict
    }
    class CreateIssue {
        +__init__(inputs: dict)
        +run() dict
    }
    class ScanSonar {
        +__init__(inputs: dict)
        +run() dict
    }
    class PR {
        +__init__(inputs)
        +run()
    }
    class CallSQL {
        +__init__(inputs: dict)
        +run() dict
    }
    class ModifyCodeOnce {
        +__init__(inputs: dict)
        +run() dict
    }
    class GetTypescriptTypeInfo {
        +__init__(inputs: dict)
        +run() dict
    }
    class CreateIssueComment {
        +__init__(inputs: dict)
        +run() dict
    }
    class BrowserUse {
        +__init__(inputs)
        +run() dict
    }
    class CallCode2Prompt {
        +__init__(inputs: dict)
        +run() dict
    }
    class PreparePR {
        +__init__(inputs: dict)
        +run() dict
    }
    class JoinList {
        +__init__(inputs)
        +run()
    }
    class CreatePR {
        +__init__(inputs: dict)
        +run() dict
    }
    class ScanDepscan {
        +__init__(inputs: dict)
        +run() dict
    }
    class SimplifiedLLMOnce {
        +__init__(inputs)
        +run() dict
    }
    class ModifyCode {
        +__init__(inputs: dict)
        +run() dict
    }
    class AgenticLLMV2 {
        +__init__(inputs)
        +run() dict
    }
    class ExtractDiff {
        +__init__(inputs: dict)
        +run() dict
    }
    class ReadEmail {
        +__init__(inputs: dict)
        +run() dict
    }
    class CreatePRComment {
        +__init__(inputs: dict)
        +run() dict
    }
    class ReadPRDiffs {
        +__init__(inputs: dict)
        +run() dict
    }
    class SimplifiedLLM {
        +__init__(inputs)
        +run() dict
    }
    class CallShell {
        +__init__(inputs: dict)
        +run() dict
    }
    class CommitChanges {
        +__init__(inputs: dict)
        +run() dict
    }
    class GitHubAgent {
        +__init__(inputs)
        +run() dict
    }
    class ExtractPackageManagerFile {
        +__init__(inputs: dict)
        +run() dict
    }
    
    Step <|-- ExtractCodeMethodForCommentContexts
    Step <|-- PreparePrompt
    Step <|-- ExtractCodeContexts
    Step <|-- ReadPRs
    Step <|-- SlackMessage
    Step <|-- CallAPI
    Step <|-- SendEmail
    Step <|-- CallLLM
    Step <|-- ReadFile
    Step <|-- AgenticLLM
    Step <|-- LLM
    Step <|-- ScanSemgrep
    Step <|-- Combine
    Step <|-- ReadIssues
    Step <|-- FixIssue
    Step <|-- FilterBySimilarity
    Step <|-- ExtractCode
    Step <|-- AnalyzeImpact
    Step <|-- ExtractModelResponse
    Step <|-- CreateIssue
    Step <|-- ScanSonar
    Step <|-- PR
    Step <|-- CallSQL
    Step <|-- ModifyCodeOnce
    Step <|-- GetTypescriptTypeInfo
    Step <|-- CreateIssueComment
    Step <|-- BrowserUse
    Step <|-- CallCode2Prompt
    Step <|-- PreparePR
    Step <|-- JoinList
    Step <|-- CreatePR
    Step <|-- ScanDepscan
    Step <|-- SimplifiedLLMOnce
    Step <|-- ModifyCode
    Step <|-- AgenticLLMV2
    Step <|-- ExtractDiff
    Step <|-- ReadEmail
    Step <|-- CreatePRComment
    Step <|-- ReadPRDiffs
    Step <|-- SimplifiedLLM
    Step <|-- CallShell
    Step <|-- CommitChanges
    Step <|-- GitHubAgent
    Step <|-- ExtractPackageManagerFile
