graph TD;
    subgraph Patchwork/Steps
        A[README.md]
        B[init.py]
        subgraph ScanSemgrep
            B1[typed.py]
            B2[README.md]
            B3[init.py]
            B4[ScanSemgrep.py]
        end
        subgraph ModifyCode
            C1[typed.py]
            C2[README.md]
            C3[init.py]
            C4[ModifyCode.py]
        end
        subgraph PreparePrompt
            D1[typed.py]
            D2[README.md]
            D3[init.py]
            D4[PreparePrompt.py]
        end
        subgraph CallLLM
            E1[typed.py]
            E2[README.md]
            E3[init.py]
            E4[CallLLM.py]
        end
        subgraph Combine
            F1[typed.py]
            F2[Combine.py]
            F3[README.md]
            F4[init.py]
        end
        subgraph CreateIssueComment
            G1[typed.py]
            G2[README.md]
            G3[init.py]
            G4[CreateIssueComment.py]
        end
        subgraph CommitChanges
            H1[typed.py]
            H2[README.md]
            H3[CommitChanges.py]
            H4[init.py]
        end
        subgraph PreparePR
            I1[typed.py]
            I2[README.md]
            I3[PreparePR.py]
            I4[init.py]
        end
        subgraph ReadPRs
            J1[typed.py]
            J2[README.md]
            J3[init.py]
            J4[ReadPRs.py]
        end
        subgraph GetTypescriptTypeInfo
            K1[typed.py]
            K2[pnpm-lock.yaml]
            K3[README.md]
            K4[init.py]
            K5[package.json]
            K6[get_type_info.ts]
            K7[tsconfig.json]
            K8[GetTypescriptTypeInfo.py]
        end
        subgraph QueryEmbeddings
            L1[typed.py]
            L2[QueryEmbeddings.py]
            L3[README.md]
            L4[init.py]
        end
        subgraph ExtractCodeContexts
            M1[typed.py]
            M2[README.md]
            M3[init.py]
            M4[ExtractCodeContexts.py]
        end
        subgraph GenerateCodeRepositoryEmbeddings
            N1[GenerateCodeRepositoryEmbeddings.py]
            N2[typed.py]
            N3[README.md]
            N4[filter_lists.py]
            N5[init.py]
        end
        subgraph ExtractDiff
            O1[typed.py]
            O2[README.md]
            O3[init.py]
            O4[ExtractDiff.py]
        end
        subgraph FixIssue
            P1[typed.py]
            P2[README.md]
            P3[init.py]
            P4[FixIssue.py]
        end
        subgraph CallCode2Prompt
            Q1[typed.py]
            Q2[CallCode2Prompt.py]
            Q3[README.md]
            Q4[init.py]
            Q5[TestCallCode2Prompt.py]
        end
        subgraph SimplifiedLLMOnce
            R1[typed.py]
            R2[README.md]
            R3[init.py]
            R4[SimplifiedLLMOnce.py]
        end
        subgraph CreatePRComment
            S1[typed.py]
            S2[CreatePRComment.py]
            S3[README.md]
            S4[init.py]
        end
        subgraph ReadPRDiffs
            T1[typed.py]
            T2[README.md]
            T3[init.py]
            T4[ReadPRDiffs.py]
        end
        subgraph AnalyzeImpact
            U1[typed.py]
            U2[AnalyzeImpact.py]
            U3[README.md]
            U4[init.py]
        end
        subgraph FilterBySimilarity
            V1[typed.py]
            V2[README.md]
            V3[init.py]
            V4[FilterBySimilarity.py]
        end
        subgraph ExtractCode
            W1[typed.py]
            W2[README.md]
            W3[init.py]
            W4[ExtractCode.py]
        end
        subgraph CreatePR
            X1[typed.py]
            X2[CreatePR.py]
            X3[README.md]
            X4[init.py]
        end
        subgraph LLM
            Y1[typed.py]
            Y2[LLM.py]
            Y3[README.md]
            Y4[init.py]
        end
        subgraph PR
            Z1[typed.py]
            Z2[README.md]
            Z3[PR.py]
            Z4[init.py]
        end
        subgraph ExtractCodeMethodForCommentContexts
            AA1[typed.py]
            AA2[README.md]
            AA3[init.py]
            AA4[ExtractCodeMethodForCommentContexts.py]
        end
        subgraph CreateIssue
            AB1[typed.py]
            AB2[README.md]
            AB3[init.py]
            AB4[CreateIssue.py]
        end
        subgraph ModifyCodeOnce
            AC1[typed.py]
            AC2[ModifyCodeOnce.py]
            AC3[README.md]
            AC4[init.py]
        end
        subgraph ExtractModelResponse
            AD1[typed.py]
            AD2[ExtractModelResponse.py]
            AD3[README.md]
            AD4[init.py]
        end
        subgraph JoinList
            AE1[typed.py]
            AE2[JoinList.py]
            AE3[README.md]
            AE4[init.py]
        end
        subgraph SimplifiedLLM
            AF1[typed.py]
            AF2[README.md]
            AF3[init.py]
            AF4[SimplifiedLLM.py]
        end
        subgraph CallAPI
            AG1[typed.py]
            AG2[README.md]
            AG3[init.py]
            AG4[CallAPI.py]
        end
        subgraph ExtractPackageManagerFile
            AH1[typed.py]
            AH2[README.md]
            AH3[init.py]
            AH4[ExtractPackageManagerFile.py]
            AH5[TestExtractPackageManagerFile.py]
        end
        subgraph ReadIssues
            AI1[typed.py]
            AI2[README.md]
            AI3[init.py]
            AI4[ReadIssues.py]
        end
        subgraph ReadFile
            AJ1[typed.py]
            AJ2[README.md]
            AJ3[init.py]
            AJ4[ReadFile.py]
        end
        subgraph ScanSonar
            AK1[typed.py]
            AK2[README.md]
            AK3[ScanSonar.py]
            AK4[init.py]
        end
        subgraph GenerateEmbeddings
            AL1[typed.py]
            AL2[GenerateEmbeddings.py]
            AL3[README.md]
            AL4[init.py]
        end
        subgraph ScanDepscan
            AM1[typed.py]
            AM2[README.md]
            AM3[init.py]
            AM4[ScanDepscan.py]
        end
        subgraph SlackMessage
            AN1[typed.py]
            AN2[SlackMessage.py]
            AN3[README.md]
            AN4[init.py]
        end
    end
