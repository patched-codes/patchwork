%%{init: {"themeVariables": {"edgeLabelBackground":"#ffffff", "tertiaryColor":"#E0E0E0"}, "theme":"base", "themeCSS": ".label { font-size: 12px; }"}}%%

graph TD
    subgraph Patchwork
        subgraph Steps
            A[__init__.py] --> B(AgenticLLM)
            A --> C(AgenticLLMV2)
            A --> D(AnalyzeImpact)
            A --> E(BrowserUse)
            A --> F(CallAPI)
            A --> G(CallCode2Prompt)
            A --> H(CallLLM)
            A --> I(CallShell)
            A --> J(CallSQL)
            A --> K(Combine)
            A --> L(CommitChanges)
            A --> M(CreateIssue)
            A --> N(CreateIssueComment)
            A --> O(CreatePR)
            A --> P(CreatePRComment)
            A --> Q(DatabaseAgent)
            A --> R(ExtractCode)
            A --> S(ExtractCodeContexts)
            A --> T(ExtractCodeMethodForCommentContexts)
            A --> U(ExtractDiff)
            A --> V(ExtractModelResponse)
            A --> W(ExtractPackageManagerFile)
            A --> X(FileAgent)
            A --> Y(FilterBySimilarity)
            A --> Z(FixIssue)
            A --> AA(GetTypescriptTypeInfo)
            A --> AB(GitHubAgent)
            A --> AC(JoinList)
            A --> AD(LLM)
            A --> AE(ManageEngineAgent)
            A --> AF(ModifyCode)
            A --> AG(ModifyCodeOnce)
            A --> AH(PreparePR)
            A --> AI(PreparePrompt)
            A --> AJ(PR)
            A --> AK(ReadEmail)
            A --> AL(ReadFile)
            A --> AM(ReadIssues)
            A --> AN(ReadPRDiffs)
            A --> AO(ReadPRs)
            A --> AP(ScanDepscan)
            A --> AQ(ScanSemgrep)
            A --> AR(ScanSonar)
            A --> AS(SendEmail)
            A --> AT(SimplifiedLLM)
            A --> AU(SimplifiedLLMOnce)
            A --> AV(SlackMessage)
            A --> AW(ZohoDeskAgent)
        end
        
        subgraph Common
            B ==> A
            C ==> A
            D ==> A
            E ==> A
            F ==> A
            G ==> A
            H ==> A
            I ==> A
            J ==> A
            K ==> A
            L ==> A
            M ==> A
            N ==> A
            O ==> A
            P ==> A
            Q ==> A
            R ==> A
            S ==> A
            T ==> A
            U ==> A
            V ==> A
            W ==> A
            X ==> A
            Y ==> A
            Z ==> A
            AA ==> A
            AB ==> A
            AC ==> A
            AD ==> A
            AE ==> A
            AF ==> A
            AG ==> A
            AH ==> A
            AI ==> A
            AJ ==> A
            AK ==> A
            AL ==> A
            AM ==> A
            AN ==> A
            AO ==> A
            AP ==> A
            AQ ==> A
            AR ==> A
            AS ==> A
            AT ==> A
            AU ==> A
            AV ==> A
            AW ==> A
        end
    end
