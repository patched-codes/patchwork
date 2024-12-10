graph TD
    subgraph Patchwork Steps
        subgraph GetTypescriptTypeInfo
            A1[package.json]
            A2[typed.py]
            A3[GetTypescriptTypeInfo.py]
            A4[tsconfig.json]
            A5[__init__.py]
            A6[README.md]
            A7[get_type_info.ts]
            A8[pnpm-lock.yaml]
        end
        subgraph ExtractCodeMethodForCommentContexts
            B1[typed.py]
            B2[ExtractCodeMethodForCommentContexts.py]
            B3[__init__.py]
            B4[README.md]
        end
        subgraph ScanDepscan
            C1[typed.py]
            C2[__init__.py]
            C3[ScanDepscan.py]
            C4[README.md]
        end
        subgraph PreparePR
            D1[typed.py]
            D2[PreparePR.py]
            D3[__init__.py]
            D4[README.md]
        end
        subgraph SimplifiedLLMOnce
            E1[typed.py]
            E2[__init__.py]
            E3[README.md]
            E4[SimplifiedLLMOnce.py]
        end
        subgraph ExtractCode
            F1[typed.py]
            F2[ExtractCode.py]
            F3[__init__.py]
            F4[README.md]
        end
        subgraph ModifyCodeOnce
            G1[typed.py]
            G2[ModifyCodeOnce.py]
            G3[__init__.py]
            G4[README.md]
        end
        subgraph AnalyzeImpact
            H1[typed.py]
            H2[AnalyzeImpact.py]
            H3[__init__.py]
            H4[README.md]
        end
        subgraph SimplifiedLLM
            I1[typed.py]
            I2[__init__.py]
            I3[README.md]
            I4[SimplifiedLLM.py]
        end
        subgraph Combine
            J1[typed.py]
            J2[Combine.py]
            J3[__init__.py]
            J4[README.md]
        end
        subgraph ExtractPackageManagerFile
            K1[typed.py]
            K2[TestExtractPackageManagerFile.py]
            K3[__init__.py]
            K4[README.md]
            K5[ExtractPackageManagerFile.py]
        end
        subgraph CallAPI
            L1[typed.py]
            L2[__init__.py]
            L3[CallAPI.py]
            L4[README.md]
        end
        subgraph ReadFile
            M1[typed.py]
            M2[ReadFile.py]
            M3[__init__.py]
            M4[README.md]
        end
        subgraph QueryEmbeddings
            N1[typed.py]
            N2[__init__.py]
            N3[QueryEmbeddings.py]
            N4[README.md]
        end
        subgraph FixIssue
            O1[typed.py]
            O2[FixIssue.py]
            O3[__init__.py]
            O4[README.md]
        end
        subgraph GenerateCodeRepositoryEmbeddings
            P1[typed.py]
            P2[__init__.py]
            P3[README.md]
            P4[filter_lists.py]
            P5[GenerateCodeRepositoryEmbeddings.py]
        end
        subgraph CreateIssueComment
            Q1[typed.py]
            Q2[CreateIssueComment.py]
            Q3[__init__.py]
            Q4[README.md]
        end
        subgraph ExtractModelResponse
            R1[typed.py]
            R2[__init__.py]
            R3[ExtractModelResponse.py]
            R4[README.md]
        end
        subgraph ReadPRDiffs
            S1[typed.py]
            S2[ReadPRDiffs.py]
            S3[__init__.py]
            S4[README.md]
        end
        subgraph FilterBySimilarity
            T1[typed.py]
            T2[FilterBySimilarity.py]
            T3[__init__.py]
            T4[README.md]
        end
        subgraph CreateIssue
            U1[CreateIssue.py]
            U2[typed.py]
            U3[__init__.py]
            U4[README.md]
        end
        subgraph PR
            V1[typed.py]
            V2[__init__.py]
            V3[README.md]
            V4[PR.py]
        end
        subgraph JoinList
            W1[typed.py]
            W2[__init__.py]
            W3[README.md]
            W4[JoinList.py]
        end
        subgraph ExtractCodeContexts
            X1[typed.py]
            X2[ExtractCodeContexts.py]
            X3[__init__.py]
            X4[README.md]
        end
        subgraph CommitChanges
            Y1[typed.py]
            Y2[__init__.py]
            Y3[README.md]
            Y4[CommitChanges.py]
        end
        subgraph ScanSemgrep
            Z1[typed.py]
            Z2[ScanSemgrep.py]
            Z3[__init__.py]
            Z4[README.md]
        end
        subgraph CallLLM
            AA1[typed.py]
            AA2[__init__.py]
            AA3[README.md]
            AA4[CallLLM.py]
        end
        subgraph ReadPRs
            AB1[typed.py]
            AB2[__init__.py]
            AB3[README.md]
            AB4[ReadPRs.py]
        end
        subgraph ModifyCode
            AC1[typed.py]
            AC2[__init__.py]
            AC3[ModifyCode.py]
            AC4[README.md]
        end
        subgraph GenerateEmbeddings
            AD1[typed.py]
            AD2[__init__.py]
            AD3[README.md]
            AD4[GenerateEmbeddings.py]
        end
        subgraph ReadIssues
            AE1[typed.py]
            AE2[__init__.py]
            AE3[README.md]
            AE4[ReadIssues.py]
        end
        subgraph ExtractDiff
            AF1[typed.py]
            AF2[ExtractDiff.py]
            AF3[__init__.py]
            AF4[README.md]
        end
        subgraph LLM
            AG1[typed.py]
            AG2[LLM.py]
            AG3[__init__.py]
            AG4[README.md]
        end
        subgraph CallCode2Prompt
            AH1[typed.py]
            AH2[TestCallCode2Prompt.py]
            AH3[__init__.py]
            AH4[README.md]
            AH5[CallCode2Prompt.py]
        end
        subgraph CreatePRComment
            AI1[typed.py]
            AI2[__init__.py]
            AI3[CreatePRComment.py]
            AI4[README.md]
        end
        subgraph SlackMessage
            AJ1[typed.py]
            AJ2[__init__.py]
            AJ3[README.md]
            AJ4[SlackMessage.py]
        end
        subgraph CreatePR
            AK1[typed.py]
            AK2[CreatePR.py]
            AK3[__init__.py]
            AK4[README.md]
        end
        subgraph PreparePrompt
            AL1[typed.py]
            AL2[__init__.py]
            AL3[README.md]
            AL4[PreparePrompt.py]
        end
    end
    patchwork --> Patchwork Steps
