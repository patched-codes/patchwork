classDiagram
    class Step {
    }

    class ExtractCodeMethodForCommentContexts {
        +ExtractCodeMethodForCommentContexts.py
        +typed.py
    }

    class PreparePrompt {
        +PreparePrompt.py
        +typed.py
    }

    class ExtractCodeContexts {
        +ExtractCodeContexts.py
        +typed.py
    }

    class ReadPRs {
        +ReadPRs.py
        +typed.py
    }

    class SlackMessage {
        +SlackMessage.py
        +typed.py
    }

    class CallAPI {
        +CallAPI.py
        +typed.py
    }

    class SendEmail {
        +SendEmail.py
        +typed.py
    }

    class CallLLM {
        +CallLLM.py
        +typed.py
    }

    class ReadFile {
        +ReadFile.py
        +typed.py
    }

    class AgenticLLM {
        +AgenticLLM.py
        +typed.py
    }

    class LLM {
        +LLM.py
        +typed.py
    }

    class ScanSemgrep {
        +ScanSemgrep.py
        +typed.py
    }

    class Combine {
        +Combine.py
        +typed.py
    }

    class ReadIssues {
        +ReadIssues.py
        +typed.py
    }

    class FixIssue {
        +FixIssue.py
        +typed.py
    }

    class FilterBySimilarity {
        +FilterBySimilarity.py
        +typed.py
    }

    class ExtractCode {
        +ExtractCode.py
        +typed.py
    }

    class AnalyzeImpact {
        +AnalyzeImpact.py
        +typed.py
    }

    class ExtractModelResponse {
        +ExtractModelResponse.py
        +typed.py
    }

    class CreateIssue {
        +CreateIssue.py
        +typed.py
    }

    class ScanSonar {
        +ScanSonar.py
        +typed.py
    }

    class PR {
        +PR.py
        +typed.py
    }

    class CallSQL {
        +CallSQL.py
        +typed.py
    }

    class ModifyCodeOnce {
        +ModifyCodeOnce.py
        +typed.py
    }

    class GetTypescriptTypeInfo {
        +GetTypescriptTypeInfo.py
        +typed.py
    }

    class CreateIssueComment {
        +CreateIssueComment.py
        +typed.py
    }

    class CallCode2Prompt {
        +CallCode2Prompt.py
        +typed.py
    }

    class PreparePR {
        +PreparePR.py
        +typed.py
    }

    class JoinList {
        +JoinList.py
        +typed.py
    }

    class CreatePR {
        +CreatePR.py
        +typed.py
    }

    class ScanDepscan {
        +ScanDepscan.py
        +typed.py
    }

    class SimplifiedLLMOnce {
        +SimplifiedLLMOnce.py
        +typed.py
    }

    class ModifyCode {
        +ModifyCode.py
        +typed.py
    }

    class AgenticLLMV2 {
        +AgenticLLMV2.py
        +typed.py
    }

    class ExtractDiff {
        +ExtractDiff.py
        +typed.py
    }

    class ReadEmail {
        +ReadEmail.py
        +typed.py
    }

    class CreatePRComment {
        +CreatePRComment.py
        +typed.py
    }

    class ReadPRDiffs {
        +ReadPRDiffs.py
        +typed.py
    }

    class SimplifiedLLM {
        +SimplifiedLLM.py
        +typed.py
    }

    class CallShell {
        +CallShell.py
        +typed.py
    }

    class CommitChanges {
        +CommitChanges.py
        +typed.py
    }

    class ExtractPackageManagerFile {
        +ExtractPackageManagerFile.py
        +typed.py
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
    Step <|-- ExtractPackageManagerFile
