graph TD
    subgraph "patchwork/steps"
    
        subgraph ExtractCodeMethodForCommentContexts
            ECT[typed.py]
            ECM[ExtractCodeMethodForCommentContexts.py]
        end

        subgraph PreparePrompt
            PPT[typed.py]
            PPR[README.md]
            PPP[PreparePrompt.py]
        end

        subgraph ExtractCodeContexts
            ECTY[typed.py]
            ECR[README.md]
            ECCP[ExtractCodeContexts.py]
        end

        subgraph ReadPRs
            RPSTY[typed.py]
            RPSR[README.md]
            RPSPY[ReadPRs.py]
        end
      
        subgraph SlackMessage
            SMT[typed.py]
            SMR[README.md]
            SMP[SlackMessage.py]
        end
        
        subgraph CallAPI
            CAT[typed.py]
            CAR[README.md]
            CAP[CallAPI.py]
        end
        
        subgraph SendEmail
            SETY[typed.py]
            SER[README.md]
            SEP[SendEmail.py]
        end

        subgraph CallLLM
            CLT[typed.py]
            CLR[README.md]
            CLP[CallLLM.py]
        end
        
        subgraph ReadFile
            RFTY[typed.py]
            RFR[README.md]
            RFPY[ReadFile.py]
        end

        subgraph AgenticLLM
            ATY[typed.py]
            AR[README.md]
            APY[AgenticLLM.py]
        end

        subgraph LLM
            LTY[typed.py]
            LR[README.md]
            LPY[LLM.py]
        end

        subgraph ScanSemgrep
            SST[typed.py]
            SSR[README.md]
            SSP[ScanSemgrep.py]
        end
        
        subgraph Combine
            CT[typed.py]
            CR[README.md]
            CP[Combine.py]
        end
        
        subgraph ReadIssues
            RIS[typed.py]
            RIR[README.md]
            RIPY[ReadIssues.py]
        end

        subgraph FixIssue
            FIT[typed.py]
            FIR[README.md]
            FIPY[FixIssue.py]
        end
        
        subgraph FilterBySimilarity
            FST[typed.py]
            FSR[README.md]
            FSPY[FilterBySimilarity.py]
        end

        subgraph ExtractCode
            XCT[typed.py]
            XCR[README.md]
            XCP[ExtractCode.py]
        end

        subgraph AnalyzeImpact
            AIT[typed.py]
            AIR[README.md]
            AIPY[AnalyzeImpact.py]
        end

        subgraph ExtractModelResponse
            EMRT[typed.py]
            EMRR[README.md]
            EMRPY[ExtractModelResponse.py]
        end

        subgraph CreateIssue
            CIT[typed.py]
            CIR[README.md]
            CIPY[CreateIssue.py]
        end
        
        subgraph ScanSonar
            SST[typed.py]
            SSR[README.md]
            SSPY[ScanSonar.py]
        end

        subgraph PR
            PRT[typed.py]
            PRR[README.md]
            PRPY[PR.py]
        end

        subgraph CallSQL
            CST[typed.py]
            CSR[README.md]
            CSPY[CallSQL.py]
        end

        subgraph ModifyCodeOnce
            MCT[typed.py]
            MCR[README.md]
            MCPY[ModifyCodeOnce.py]
        end

        subgraph GetTypescriptTypeInfo
            GTTY[typed.py]
            GTR[README.md]
            GTJ[tsconfig.json]
            GTP[package.json]
            GTTS[get_type_info.ts]
            GTTYPI[GetTypescriptTypeInfo.py]
        end

        subgraph FileAgent
            FTY[typed.py]
            FFP[FileAgent.py]
        end

        subgraph CreateIssueComment
            CIT[typed.py]
            CIR[README.md]
            CIPY[CreateIssueComment.py]
        end

        subgraph BrowserUse
            BUTY[typed.py]
            BUR[README.md]
            BUPY[BrowserUse.py]
        end

        subgraph CallCode2Prompt
            CPT[typed.py]
            CPR[README.md]
            CPPY[CallCode2Prompt.py]
            CPTT[TestCallCode2Prompt.py]
        end

        subgraph PreparePR
            PPT[typed.py]
            PPR[README.md]
            PPPY[PreparePR.py]
        end

        subgraph JoinList
            JLT[typed.py]
            JLR[README.md]
            JLPY[JoinList.py]
        end

        subgraph CreatePR
            CPT[typed.py]
            CPR[README.md]
            CPY[CreatePR.py]
        end

        subgraph ScanDepscan
            SDT[typed.py]
            SDR[README.md]
            SDP[ScanDepscan.py]
        end
        
        subgraph SimplifiedLLMOnce
            SLTY[typed.py]
            SLR[README.md]
            SLP[SL.py]
        end

        subgraph ModifyCode
            MCT[typed.py]
            MCR[README.md]
            MCPY[ModifyCode.py]
        end

        subgraph ManageEngineAgent
            MET[typed.py]
            MEP[ManageEngineAgent.py]
        end

        subgraph AgenticLLMV2
            ATV2[typed.py]
            AR2[README.md]
            APY2[AgenticLLMV2.py]
        end

        subgraph ExtractDiff
            EDT[typed.py]
            EDR[README.md]
            EDPY[ExtractDiff.py]
        end

        subgraph ReadEmail
            RET[typed.py]
            RER[README.md]
            REP[ReadEmail.py]
        end

        subgraph CreatePRComment
            CCT[typed.py]
            CCR[README.md]
            CCPY[CreatePRComment.py]
        end

        subgraph ReadPRDiffs
            RDT[typed.py]
            RDR[README.md]
            RDPY[ReadPRDiffs.py]
        end

        subgraph SimplifiedLLM
            SLT[typed.py]
            SLR[README.md]
            SLP[SL.py]
        end

        subgraph CallShell
            CST[typed.py]
            CSR[README.md]
            CSPY[CallShell.py]
        end

        subgraph CommitChanges
            CCT[typed.py]
            CCR[README.md]
            CCPY[CommitChanges.py]
        end

        subgraph ZohoDeskAgent
            ZDAT[typed.py]
            ZDAP[ZohoDeskAgent.py]
        end

        subgraph GitHubAgent
            GHT[typed.py]
            GHP[GitHubAgent.py]
        end

        subgraph ExtractPackageManagerFile
            EPMFT[typed.py]
            EPMFR[README.md]
            EPMFP[ExtractPackageManagerFile.py]
            EPMFTP[TestExtractPackageManagerFile.py]
        end

    end
