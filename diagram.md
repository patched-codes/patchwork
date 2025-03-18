classDiagram
    direction TB
    class Steps {
        +<<abstract>> run()
    }
    class ExtractCodeMethodForCommentContexts {
        <<abstract>>
        +ExtractCodeMethodForCommentContextsInputs
        +ExtractCodeMethodForCommentContextsOutputs
    }
    class ExtractCodeMethodForCommentContexts* {
        
    }
    class PreparePrompt {
        +PreparePromptInputs
        +PreparePromptOutputs
    }
    class ExtractCodeContexts {
        +ExtractCodeContextsInputs
        +ExtractCodeContextsOutputs
    }
    class ReadPRs {
        +ReadPRsInputs
        +ReadPRsOutputs
    }
    class SlackMessage {
        +SlackMessageInputs
        +SlackMessageOutputs
    }
    class CallAPI {
        +CallAPIInputs
        +CallAPIOutputs
    }
    class SendEmail {
        +SendEmailInputs
        +SendEmailOutputs
    }
    class CallLLM {
        +CallLLMInputs
        +CallLLMOutputs
    }
    class ReadFile {
        +ReadFileInputs
        +ReadFileOutputs
    }
    class AgenticLLM {
        +AgenticLLMInputs
        +AgenticLLMOutputs
    }
    class LLM {
        +LLMInputs
        +LLMOutputs
    }
    class ScanSemgrep {
        +ScanSemgrepInputs
        +ScanSemgrepOutputs
    }
    class Combine {
        +CombineInputs
        +CombineOutputs
    }
    class ReadIssues {
        +ReadIssuesInputs
        +ReadIssuesOutputs
    }
    class FixIssue {
        +FixIssueInputs
        +FixIssueOutputs
    }
    class FilterBySimilarity {
        +FilterBySimilarityInputs
        +FilterBySimilarityOutputs
    }
    class ExtractCode {
        +ExtractCodeInputs
        +ExtractCodeOutputs
    }
    class AnalyzeImpact {
        +AnalyzeImpactInputs
        +AnalyzeImpactOutputs
    }
    class ExtractModelResponse {
        +ExtractModelResponseInputs
        +ExtractModelResponseOutputs
    }
    class CreateIssue {
        +CreateIssueInputs
        +CreateIssueOutputs
    }
    class ScanSonar {
        +ScanSonarInputs
        +ScanSonarOutputs
    }
    class PR {
        +PRInputs
        +PROutputs
    }
    class CallSQL {
        +CallSQLInputs
        +CallSQLOutputs
    }
    class ModifyCodeOnce {
        +ModifyCodeOnceInputs
        +ModifyCodeOnceOutputs
    }
    class GetTypescriptTypeInfo {
        +GetTypescriptTypeInfoInputs
        +GetTypescriptTypeInfoOutputs
    }
    class FileAgent {
        +FileAgentInputs
        +FileAgentOutputs
    }
    class CreateIssueComment {
        +CreateIssueCommentInputs
        +CreateIssueCommentOutputs
    }
    class BrowserUse {
        +BrowserUseInputs
        +BrowserUseOutputs
    }
    class CallCode2Prompt {
        +CallCode2PromptInputs
        +CallCode2PromptOutputs
    }
    class PreparePR {
        +PreparePRInputs
        +PreparePROutputs
    }
    class JoinList {
        +JoinListInputs
        +JoinListOutputs
    }
    class CreatePR {
        +CreatePRInputs
        +CreatePROutputs
    }
    class ScanDepscan {
        +ScanDepscanInputs
        +ScanDepscanOutputs
    }
    class SimplifiedLLMOnce {
        +SimplifiedLLMOnceInputs
        +SimplifiedLLMOnceOutputs
    }
    class ModifyCode {
        +ModifyCodeInputs
        +ModifyCodeOutputs
    }
    class ManageEngineAgent {
        +ManageEngineAgentInputs
        +ManageEngineAgentOutputs
    }
    class AgenticLLMV2 {
        +AgenticLLMV2Inputs
        +AgenticLLMV2Outputs
    }
    class ExtractDiff {
        +ExtractDiffInputs
        +ExtractDiffOutputs
    }
    class ReadEmail {
        +ReadEmailInputs
        +ReadEmailOutputs
    }
    class CreatePRComment {
        +CreatePRCommentInputs
        +CreatePRCommentOutputs
    }
    class ReadPRDiffs {
        +ReadPRDiffsInputs
        +ReadPRDiffsOutputs
    }
    class SimplifiedLLM {
        +SimplifiedLLMInputs
        +SimplifiedLLMOutputs
    }
    class CallShell {
        +CallShellInputs
        +CallShellOutputs
    }
    class CommitChanges {
        +CommitChangesInputs
        +CommitChangesOutputs
    }
    class ZohoDeskAgent {
        +ZohoDeskAgentInputs
        +ZohoDeskAgentOutputs
    }
    class GitHubAgent {
        +GitHubAgentInputs
        +GitHubAgentOutputs
    }
    class ExtractPackageManagerFile {
        +ExtractPackageManagerFileInputs
        +ExtractPackageManagerFileOutputs
    }
    
    ExtractCodeMethodForCommentContexts --> ExtractCodeMethodForCommentContexts* : call
    ExtractCodeContexts --> ExtractCodeMethodForCommentContexts
    PreparePrompt --> PR
    PR --> CreatePR
    PreparePR --> CreatePR
    PR --> CommitChanges
    FixIssue --> CommitChanges
    CommitChanges --> PR
    LLM --> CallLLM
    AgenticLLM --> CallLLM
    SimplifiedLLM --> CallLLM
    SimplifiedLLMOnce --> SimplifiedLLM
    ReadPRs --> ReadPRDiffs
    ReadIssues --> FixIssue 
    ExtractModelResponse --> CallLLM
    ReadFile --> ReadEmail
    SendEmail --> ReadEmail
    FileAgent --> ExtractModelResponse
    ManageEngineAgent --> AnalyzeImpact
