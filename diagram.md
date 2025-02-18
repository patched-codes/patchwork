graph TD
    subgraph Patchwork/Steps
        A[__init__.py] 
        B[README.md] 
        C[LLM]
        subgraph LLM
            C1[__init__.py]
            C2[LLM.py]
            C3[typed.py]
            C4[README.md]
        end
        D[CallCode2Prompt]
        subgraph CallCode2Prompt
            D1[__init__.py]
            D2[CallCode2Prompt.py]
            D3[TestCallCode2Prompt.py]
            D4[typed.py]
            D5[README.md]
        end
        E[GenerateCodeRepositoryEmbeddings]
        subgraph GenerateCodeRepositoryEmbeddings
            E1[__init__.py]
            E2[GenerateCodeRepositoryEmbeddings.py]
            E3[typed.py]
            E4[filter_lists.py]
            E5[README.md]
        end
        F[ScanSemgrep]
        subgraph ScanSemgrep
            F1[__init__.py]
            F2[ScanSemgrep.py]
            F3[typed.py]
            F4[README.md]
        end
        G[GetTypescriptTypeInfo]
        subgraph GetTypescriptTypeInfo
            G1[__init__.py]
            G2[get_type_info.ts]
            G3[GetTypescriptTypeInfo.py]
            G4[tsconfig.json]
            G5[typed.py]
            G6[pnpm-lock.yaml]
            G7[package.json]
            G8[README.md]
        end
        H[ExtractCodeMethodForCommentContexts]
        subgraph ExtractCodeMethodForCommentContexts
            H1[__init__.py]
            H2[ExtractCodeMethodForCommentContexts.py]
            H3[typed.py]
            H4[README.md]
        end
        I[ExtractModelResponse]
        subgraph ExtractModelResponse
            I1[ExtractModelResponse.py]
            I2[__init__.py]
            I3[typed.py]
            I4[README.md]
        end
        J[GenerateEmbeddings]
        subgraph GenerateEmbeddings
            J1[__init__.py]
            J2[GenerateEmbeddings.py]
            J3[typed.py]
            J4[README.md]
        end
        K[PR]
        subgraph PR
            K1[PR.py]
            K2[__init__.py]
            K3[typed.py]
            K4[README.md]
        end
        L[SlackMessage]
        subgraph SlackMessage
            L1[__init__.py]
            L2[typed.py]
            L3[SlackMessage.py]
            L4[README.md]
        end
        M[PreparePR]
        subgraph PreparePR
            M1[__init__.py]
            M2[PreparePR.py]
            M3[typed.py]
            M4[README.md]
        end
        N[ModifyCodeOnce]
        subgraph ModifyCodeOnce
            N1[__init__.py]
            N2[ModifyCodeOnce.py]
            N3[typed.py]
            N4[README.md]
        end
        O[CreatePRComment]
        subgraph CreatePRComment
            O1[__init__.py]
            O2[typed.py]
            O3[CreatePRComment.py]
            O4[README.md]
        end
        P[CallShell]
        subgraph CallShell
            P1[CallShell.py]
            P2[__init__.py]
            P3[typed.py]
        end
        Q[FixIssue]
        subgraph FixIssue
            Q1[__init__.py]
            Q2[typed.py]
            Q3[FixIssue.py]
            Q4[README.md]
        end
        R[ScanSonar]
        subgraph ScanSonar
            R1[ScanSonar.py]
            R2[__init__.py]
            R3[typed.py]
            R4[README.md]
        end
        S[CreateIssue]
        subgraph CreateIssue
            S1[__init__.py]
            S2[CreateIssue.py]
            S3[typed.py]
            S4[README.md]
        end
        T[FilterBySimilarity]
        subgraph FilterBySimilarity
            T1[__init__.py]
            T2[FilterBySimilarity.py]
            T3[typed.py]
            T4[README.md]
        end
        U[ReadPRDiffs]
        subgraph ReadPRDiffs
            U1[__init__.py]
            U2[typed.py]
            U3[ReadPRDiffs.py]
            U4[README.md]
        end
        V[AgenticLLM]
        subgraph AgenticLLM
            V1[__init__.py]
            V2[typed.py]
            V3[AgenticLLM.py]
        end
        W[CommitChanges]
        subgraph CommitChanges
            W1[__init__.py]
            W2[CommitChanges.py]
            W3[typed.py]
            W4[README.md]
        end
        X[SimplifiedLLMOnce]
        subgraph SimplifiedLLMOnce
            X1[SimplifiedLLMOnce.py]
            X2[__init__.py]
            X3[typed.py]
            X4[README.md]
        end
        Y[ExtractPackageManagerFile]
        subgraph ExtractPackageManagerFile
            Y1[__init__.py]
            Y2[TestExtractPackageManagerFile.py]
            Y3[typed.py]
            Y4[ExtractPackageManagerFile.py]
            Y5[README.md]
        end
        Z[ReadEmail]
        subgraph ReadEmail
            Z1[__init__.py]
            Z2[ReadEmail.py]
            Z3[typed.py]
        end
        AA[ModifyCode]
        subgraph ModifyCode
            AA1[__init__.py]
            AA2[typed.py]
            AA3[ModifyCode.py]
            AA4[README.md]
        end
        AB[JoinList]
        subgraph JoinList
            AB1[JoinList.py]
            AB2[__init__.py]
            AB3[typed.py]
            AB4[README.md]
        end
        AC[CallAPI]
        subgraph CallAPI
            AC1[CallAPI.py]
            AC2[__init__.py]
            AC3[typed.py]
            AC4[README.md]
        end
        AD[CreatePR]
        subgraph CreatePR
            AD1[__init__.py]
            AD2[typed.py]
            AD3[README.md]
            AD4[CreatePR.py]
        end
        AE[ReadIssues]
        subgraph ReadIssues
            AE1[ReadIssues.py]
            AE2[__init__.py]
            AE3[typed.py]
            AE4[README.md]
        end
        AF[ReadFile]
        subgraph ReadFile
            AF1[__init__.py]
            AF2[typed.py]
            AF3[README.md]
            AF4[ReadFile.py]
        end
        AG[CallLLM]
        subgraph CallLLM
            AG1[CallLLM.py]
            AG2[__init__.py]
            AG3[typed.py]
            AG4[README.md]
        end
        AH[CallSQL]
        subgraph CallSQL
            AH1[CallSQL.py]
            AH2[__init__.py]
            AH3[typed.py]
        end
        AI[ScanDepscan]
        subgraph ScanDepscan
            AI1[__init__.py]
            AI2[ScanDepscan.py]
            AI3[typed.py]
            AI4[README.md]
        end
        AJ[ExtractDiff]
        subgraph ExtractDiff
            AJ1[__init__.py]
            AJ2[typed.py]
            AJ3[ExtractDiff.py]
            AJ4[README.md]
        end
        AK[QueryEmbeddings]
        subgraph QueryEmbeddings
            AK1[__init__.py]
            AK2[typed.py]
            AK3[QueryEmbeddings.py]
            AK4[README.md]
        end
        AL[SendEmail]
        subgraph SendEmail
            AL1[__init__.py]
            AL2[SendEmail.py]
            AL3[typed.py]
        end
        AM[Combine]
        subgraph Combine
            AM1[__init__.py]
            AM2[Combine.py]
            AM3[typed.py]
            AM4[README.md]
        end
        AN[SimplifiedLLM]
        subgraph SimplifiedLLM
            AN1[SimplifiedLLM.py]
            AN2[__init__.py]
            AN3[typed.py]
            AN4[README.md]
        end
        AO[ReadPRs]
        subgraph ReadPRs
            AO1[__init__.py]
            AO2[ReadPRs.py]
            AO3[typed.py]
            AO4[README.md]
        end
        AP[ExtractCodeContexts]
        subgraph ExtractCodeContexts
            AP1[__init__.py]
            AP2[typed.py]
            AP3[README.md]
            AP4[ExtractCodeContexts.py]
        end
        AQ[AnalyzeImpact]
        subgraph AnalyzeImpact
            AQ1[__init__.py]
            AQ2[AnalyzeImpact.py]
            AQ3[typed.py]
            AQ4[README.md]
        end
        AR[PreparePrompt]
        subgraph PreparePrompt
            AR1[__init__.py]
            AR2[PreparePrompt.py]
            AR3[typed.py]
            AR4[README.md]
        end
        AS[CreateIssueComment]
        subgraph CreateIssueComment
            AS1[__init__.py]
            AS2[typed.py]
            AS3[CreateIssueComment.py]
            AS4[README.md]
        end
        AT[ExtractCode]
        subgraph ExtractCode
            AT1[__init__.py]
            AT2[ExtractCode.py]
            AT3[typed.py]
            AT4[README.md]
        end
    end
