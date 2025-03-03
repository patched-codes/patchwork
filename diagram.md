graph TD
    A[pachwork/steps/README.md]
    subgraph patchwork/steps
        B["patchwork/steps/__init__.py"]
        subgraph ExtractCodeMethodForCommentContexts
            E[typed.py]
            F[README.md]
            G[ExtractCodeMethodForCommentContexts.py]
            H[__init__.py]
        end
        subgraph PreparePrompt
            I[typed.py]
            J[README.md]
            K[PreparePrompt.py]
            L[__init__.py]
        end
        subgraph ExtractCodeContexts
            M[typed.py]
            N[README.md]
            O[ExtractCodeContexts.py]
            P[__init__.py]
        end
        subgraph ReadPRs
            Q[typed.py]
            R[README.md]
            S[ReadPRs.py]
            T[__init__.py]
        end
        subgraph SlackMessage
            U[typed.py]
            V[README.md]
            W[SlackMessage.py]
            X[__init__.py]
        end
        subgraph CallAPI
            Y[typed.py]
            Z[README.md]
            AA[CallAPI.py]
            AB[__init__.py]
        end
        subgraph SendEmail
            AC[SendEmail.py]
            AD[typed.py]
            AE[README.md]
            AF[__init__.py]
        end
        subgraph CallLLM
            AG[typed.py]
            AH[README.md]
            AI[CallLLM.py]
            AJ[__init__.py]
        end
        subgraph ReadFile
            AK[typed.py]
            AL[README.md]
            AM[ReadFile.py]
            AN[__init__.py]
        end
        subgraph AgenticLLM
            AO[typed.py]
            AP[README.md]
            AQ[AgenticLLM.py]
            AR[__init__.py]
        end
        subgraph LLM
            AS[typed.py]
            AT[README.md]
            AU[LLM.py]
            AV[__init__.py]
        end
        subgraph ScanSemgrep
            AW[typed.py]
            AX[README.md]
            AY[ScanSemgrep.py]
            AZ[__init__.py]
        end
        subgraph Combine
            BA[typed.py]
            BB[README.md]
            BC[Combine.py]
            BD[__init__.py]
        end
        subgraph ReadIssues
            BE[typed.py]
            BF[README.md]
            BG[ReadIssues.py]
            BH[__init__.py]
        end
        subgraph FixIssue
            BI[typed.py]
            BJ[README.md]
            BK[FixIssue.py]
            BL[__init__.py]
        end
        subgraph FilterBySimilarity
            BM[typed.py]
            BN[README.md]
            BO[FilterBySimilarity.py]
            BP[__init__.py]
        end
        subgraph ExtractCode
            BQ[typed.py]
            BR[README.md]
            BS[ExtractCode.py]
            BT[__init__.py]
        end
        subgraph AnalyzeImpact
            BU[typed.py]
            BV[README.md]
            BW[AnalyzeImpact.py]
            BX[__init__.py]
        end
        subgraph ExtractModelResponse
            BY[typed.py]
            BZ[README.md]
            CA[ExtractModelResponse.py]
            CB[__init__.py]
        end
        subgraph CreateIssue
            CC[CreateIssue.py]
            CD[typed.py]
            CE[README.md]
            CF[__init__.py]
        end
        subgraph ScanSonar
            CG[ScanSonar.py]
            CH[typed.py]
            CI[README.md]
            CJ[__init__.py]
        end
        subgraph PR
            CK[PR.py]
            CL[typed.py]
            CM[README.md]
            CN[__init__.py]
        end
        subgraph CallSQL
            CO[typed.py]
            CP[README.md]
            CQ[CallSQL.py]
            CR[__init__.py]
        end
        subgraph ModifyCodeOnce
            CS[typed.py]
            CT[README.md]
            CU[ModifyCodeOnce.py]
            CV[__init__.py]
        end
        subgraph GetTypescriptTypeInfo
            CW[pnpm-lock.yaml]
            CX[typed.py]
            CY[README.md]
            CZ[tsconfig.json]
            DA[package.json]
            DB[get_type_info.ts]
            DC[GetTypescriptTypeInfo.py]
            DD[__init__.py]
        end
        subgraph CreateIssueComment
            DE[typed.py]
            DF[README.md]
            DG[CreateIssueComment.py]
            DH[__init__.py]
        end
        subgraph BrowserUse
            DI[typed.py]
            DJ[README.md]
            DK[BrowserUse.py]
            DL[__init__.py]
        end
        subgraph CallCode2Prompt
            DM[typed.py]
            DN[README.md]
            DO[CallCode2Prompt.py]
            DP[__init__.py]
            DQ[TestCallCode2Prompt.py]
        end
        subgraph PreparePR
            DR[typed.py]
            DS[README.md]
            DT[PreparePR.py]
            DU[__init__.py]
        end
        subgraph JoinList
            DV[typed.py]
            DW[README.md]
            DX[JoinList.py]
            DY[__init__.py]
        end
        subgraph CreatePR
            DZ[CreatePR.py]
            EA[typed.py]
            EB[README.md]
            EC[__init__.py]
        end
        subgraph ScanDepscan
            ED[typed.py]
            EE[README.md]
            EF[ScanDepscan.py]
            EG[__init__.py]
        end
        subgraph SimplifiedLLMOnce
            EH[typed.py]
            EI[README.md]
            EJ[SimplifiedLLMOnce.py]
            EK[__init__.py]
        end
        subgraph ModifyCode
            EL[typed.py]
            EM[README.md]
            EN[ModifyCode.py]
            EO[__init__.py]
        end
        subgraph AgenticLLMV2
            EP[typed.py]
            EQ[README.md]
            ER[AgenticLLMV2.py]
            ES[__init__.py]
        end
        subgraph ExtractDiff
            ET[typed.py]
            EU[README.md]
            EV[ExtractDiff.py]
            EW[__init__.py]
        end
        subgraph ReadEmail
            EX[typed.py]
            EY[README.md]
            EZ[ReadEmail.py]
            FA[__init__.py]
        end
        subgraph CreatePRComment
            FB[typed.py]
            FC[README.md]
            FD[CreatePRComment.py]
            FE[__init__.py]
        end
        subgraph ReadPRDiffs
            FF[typed.py]
            FG[README.md]
            FH[ReadPRDiffs.py]
            FI[__init__.py]
        end
        subgraph SimplifiedLLM
            FJ[typed.py]
            FK[README.md]
            FL[SimplifiedLLM.py]
            FM[__init__.py]
        end
        subgraph CallShell
            FN[typed.py]
            FO[README.md]
            FP[CallShell.py]
            FQ[__init__.py]
        end
        subgraph CommitChanges
            FR[typed.py]
            FS[README.md]
            FT[CommitChanges.py]
            FU[__init__.py]
        end
        subgraph ExtractPackageManagerFile
            FV[typed.py]
            FW[README.md]
            FX[TestExtractPackageManagerFile.py]
            FY[ExtractPackageManagerFile.py]
            FZ[__init__.py]
        end
    end
    A --> B
    B --> E
    B --> I
    B --> M
    B --> Q
    B --> U
    B --> Y
    B --> AC
    B --> AG
    B --> AK
    B --> AO
    B --> AS
    B --> AW
    B --> BA
    B --> BE
    B --> BI
    B --> BM
    B --> BQ
    B --> BU
    B --> BY
    B --> CC
    B --> CG
    B --> CK
    B --> CO
    B --> CS
    B --> CW
    B --> DE
    B --> DI
    B --> DM
    B --> DR
    B --> DV
    B --> DZ
    B --> ED
    B --> EH
    B --> EL
    B --> EP
    B --> ET
    B --> EX
    B --> FB
    B --> FF
    B --> FJ
    B --> FN
    B --> FR
    B --> FV
