graph LR
    subgraph Patchwork Steps
        direction TB
        subgraph Init
            A[[__init__.py]]
            direction LR
            S(A) -->|import| T(B)
            C(A) -->|import| F(B)
        end
        
        subgraph LLM
            B[[LLM.py]]
            D[[typed.py]]
            E[[README.md]]
            B --> D
        end
        
        subgraph CallCode2Prompt
            F[[CallCode2Prompt.py]]
            G[[TestCallCode2Prompt.py]]
            H[[typed.py]]
            I[[README.md]]
            F --> H
        end
        
        subgraph GenerateCodeRepositoryEmbeddings
            J[[GenerateCodeRepositoryEmbeddings.py]]
            K[[typed.py]]
            L[[filter_lists.py]]
            M[[README.md]]
            J --> K
        end
        
        subgraph ScanSemgrep
            N[[ScanSemgrep.py]]
            O[[typed.py]]
            P[[README.md]]
            N --> O
        end
        
        subgraph GetTypescriptTypeInfo
            Q[[get_type_info.ts]]
            R[[GetTypescriptTypeInfo.py]]
            S[[tsconfig.json]]
            T[[typed.py]]
            U[[pnpm-lock.yaml]]
            V[[package.json]]
            W[[README.md]]
            U -.-> R
            V -.-> Q
            W --> Q
        end
        
        subgraph ExtractCodeMethodForCommentContexts
            X[[ExtractCodeMethodForCommentContexts.py]]
            Y[[typed.py]]
            Z[[README.md]]
            X --> Y
        end
        
        subgraph ExtractModelResponse
            AA[[ExtractModelResponse.py]]
            AB[[typed.py]]
            AC[[README.md]]
            AA --> AB
        end
        
        subgraph GenerateEmbeddings
            AD[[GenerateEmbeddings.py]]
            AE[[typed.py]]
            AF[[README.md]]
            AD --> AE
        end
        
        subgraph PR
            AG[[PR.py]]
            AH[[typed.py]]
            AI[[README.md]]
            AG --> AH
        end
        
        subgraph SlackMessage
            AJ[[SlackMessage.py]]
            AK[[typed.py]]
            AL[[README.md]]
            AJ --> AK
        end
        
        subgraph PreparePR
            AM[[PreparePR.py]]
            AN[[typed.py]]
            AO[[README.md]]
            AM --> AN
        end
        
        subgraph ModifyCodeOnce
            AP[[ModifyCodeOnce.py]]
            AQ[[typed.py]]
            AR[[README.md]]
            AP --> AQ
        end
        
        subgraph CreatePRComment
            AS[[CreatePRComment.py]]
            AT[[typed.py]]
            AU[[README.md]]
            AS --> AT
        end
        
        subgraph CallShell
            AV[[CallShell.py]]
            AW[[typed.py]]
            AX[[README.md]]
            AV --> AW
        end
        
        subgraph FixIssue
            AY[[FixIssue.py]]
            AZ[[typed.py]]
            BA[[README.md]]
            AY --> AZ
        end
        
        subgraph ScanSonar
            BB[[ScanSonar.py]]
            BC[[typed.py]]
            BD[[README.md]]
            BB --> BC
        end
        
        subgraph CreateIssue
            BE[[CreateIssue.py]]
            BF[[typed.py]]
            BG[[README.md]]
            BE --> BF
        end
        
        subgraph FilterBySimilarity
            BH[[FilterBySimilarity.py]]
            BI[[typed.py]]
            BJ[[README.md]]
            BH --> BI
        end
        
        subgraph ReadPRDiffs
            BK[[ReadPRDiffs.py]]
            BL[[typed.py]]
            BM[[README.md]]
            BK --> BL
        end
        
        subgraph AgenticLLM
            BN[[AgenticLLM.py]]
            BO[[typed.py]]
            BP[[README.md]]
            BN --> BO
        end
        
        subgraph CommitChanges
            BQ[[CommitChanges.py]]
            BR[[typed.py]]
            BS[[README.md]]
            BQ --> BR
        end
        
        subgraph SimplifiedLLMOnce
            BT[[SimplifiedLLMOnce.py]]
            BU[[typed.py]]
            BV[[README.md]]
            BT --> BU
        end
        
        subgraph ExtractPackageManagerFile
            BW[[ExtractPackageManagerFile.py]]
            BX[[TestExtractPackageManagerFile.py]]
            BY[[typed.py]]
            BZ[[README.md]]
            BW --> BY
        end
        
        subgraph ModifyCode
            CA[[ModifyCode.py]]
            CB[[typed.py]]
            CC[[README.md]]
            CA --> CB
        end
        
        subgraph JoinList
            CD[[JoinList.py]]
            CE[[typed.py]]
            CF[[README.md]]
            CD --> CE
        end
        
        subgraph CallAPI
            CG[[CallAPI.py]]
            CH[[typed.py]]
            CI[[README.md]]
            CG --> CH
        end
        
        subgraph CreatePR
            CJ[[CreatePR.py]]
            CK[[typed.py]]
            CL[[README.md]]
            CJ --> CK
        end
        
        subgraph ReadIssues
            CM[[ReadIssues.py]]
            CN[[typed.py]]
            CO[[README.md]]
            CM --> CN
        end
        
        subgraph ReadFile
            CP[[ReadFile.py]]
            CQ[[typed.py]]
            CR[[README.md]]
            CP --> CQ
        end
        
        subgraph CallLLM
            CS[[CallLLM.py]]
            CT[[typed.py]]
            CU[[README.md]]
            CS --> CT
        end
        
        subgraph CallSQL
            CV[[CallSQL.py]]
            CW[[typed.py]]
            CX[[README.md]]
            CV --> CW
        end
        
        subgraph ScanDepscan
            CY[[ScanDepscan.py]]
            CZ[[typed.py]]
            DA[[README.md]]
            CY --> CZ
        end
        
        subgraph ExtractDiff
            DB[[ExtractDiff.py]]
            DC[[typed.py]]
            DD[[README.md]]
            DB --> DC
        end
        
        subgraph QueryEmbeddings
            DE[[QueryEmbeddings.py]]
            DF[[typed.py]]
            DG[[README.md]]
            DE --> DF
        end
        
        subgraph SendEmail
            DH[[SendEmail.py]]
            DI[[typed.py]]
            DJ[[README.md]]
            DH --> DI
        end
        
        subgraph Combine
            DK[[Combine.py]]
            DL[[typed.py]]
            DM[[README.md]]
            DK --> DL
        end
        
        subgraph SimplifiedLLM
            DN[[SimplifiedLLM.py]]
            DO[[typed.py]]
            DP[[README.md]]
            DN --> DO
        end
        
        subgraph ReadPRs
            DQ[[ReadPRs.py]]
            DR[[typed.py]]
            DS[[README.md]]
            DQ --> DR
        end
        
        subgraph ExtractCodeContexts
            DT[[ExtractCodeContexts.py]]
            DU[[typed.py]]
            DV[[README.md]]
            DT --> DU
        end
        
        subgraph AnalyzeImpact
            DW[[AnalyzeImpact.py]]
            DX[[typed.py]]
            DY[[README.md]]
            DW --> DX
        end
        
        subgraph PreparePrompt
            DZ[[PreparePrompt.py]]
            EA[[typed.py]]
            EB[[README.md]]
            DZ --> EA
        end
        
        subgraph CreateIssueComment
            EC[[CreateIssueComment.py]]
            ED[[typed.py]]
            EE[[README.md]]
            EC --> ED
        end
        
        subgraph ExtractCode
            EF[[ExtractCode.py]]
            EG[[typed.py]]
            EH[[README.md]]
            EF --> EG
        end
    end
