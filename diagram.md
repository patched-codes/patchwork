graph TD
    subgraph System["patchwork/steps"]
        subgraph ExtractCodeMethodForCommentContexts
            direction TB
            ECTypedpy[typed.py]
            ECREADME[README.md]
            ECExtract[ExtractCodeMethodForCommentContexts.py]
            ECInit[__init__.py]
        end

        subgraph PreparePrompt
            direction TB
            PPTypedpy[typed.py]
            PPREADME[README.md]
            PPPrepare[PreparePrompt.py]
            PPInit[__init__.py]
        end

        subgraph ExtractCodeContexts
            direction TB
            ECCINIT[__init__.py]
            ECCTypedpy[typed.py]
            ECCREADME[README.md]
            ECCExtract[ExtractCodeContexts.py]
        end

        subgraph ReadPRs
            direction TB
            RPTypedpy[typed.py]
            RPREADME[README.md]
            RPInit[__init__.py]
            RPRead[ReadPRs.py]
        end

        subgraph SlackMessage
            direction TB
            SMTypedpy[typed.py]
            SMREADME[README.md]
            SMInit[__init__.py]
            SMSlack[SlackMessage.py]
        end

        subgraph CallAPI
            direction TB
            CAPITypedpy[typed.py]
            CAPIREADME[README.md]
            CAPICall[CallAPI.py]
            CAPInit[__init__.py]
        end

        subgraph SendEmail
            direction TB
            SEMailpy[SendEmail.py]
            SETypedpy[typed.py]
            SEREADME[README.md]
            SEInit[__init__.py]
        end

        subgraph CallLLM
            direction TB
            CLTypedpy[typed.py]
            CLREADME[README.md]
            CLCall[CallLLM.py]
            CLInit[__init__.py]
        end

        subgraph ReadFile
            direction TB
            RFTypedpy[typed.py]
            RFREADME[README.md]
            RFRead[ReadFile.py]
            RFInit[__init__.py]
        end

        subgraph AgenticLLM
            direction TB
            ALTpy[typed.py]
            ALREADME[README.md]
            ALInit[__init__.py]
            ALAgentic[AgenticLLM.py]
        end

        subgraph LLM
            direction TB
            LMTypedpy[typed.py]
            LMREADME[README.md]
            LMInit[__init__.py]
            LLMLlm[LLM.py]
        end

        subgraph ScanSemgrep
            direction TB
            SSTypedpy[typed.py]
            SSReadme[README.md]
            SSScan[ScanSemgrep.py]
            SSInit[__init__.py]
        end

        subgraph Combine
            direction TB
            CTypedpy[typed.py]
            CREadme[README.md]
            CCombine[Combine.py]
            CInit[__init__.py]
        end

        subgraph ReadIssues
            direction TB
            RITypedpy[typed.py]
            RIReadme[README.md]
            RIRead[ReadIssues.py]
            RIInit[__init__.py]
        end

        subgraph FixIssue
            direction TB
            FITypedpy[typed.py]
            FIReadme[README.md]
            FIInit[__init__.py]
            FIFix[FixIssue.py]
        end

        subgraph FilterBySimilarity
            direction TB
            FbySTypedpy[typed.py]
            FbySREADME[README.md]
            FbySFilter[FilterBySimilarity.py]
            FbySInit[__init__.py]
        end

        subgraph ExtractCode
            direction TB
            ECTypedpy[typed.py]
            ECREADME[README.md]
            ECExtract[ExtractCode.py]
            ECInit[__init__.py]
        end

        subgraph AnalyzeImpact
            direction TB
            AITypedpy[typed.py]
            AIREADME[README.md]
            AIAnalyze[AnalyzeImpact.py]
            AIInit[__init__.py]
        end

        subgraph ExtractModelResponse
            direction TB
            EMTypedpy[typed.py]
            EMREADME[README.md]
            EMExtract[ExtractModelResponse.py]
            EMInit[__init__.py]
        end

        subgraph CreateIssue
            direction TB
            CITypedpy[typed.py]
            CIREADME[README.md]
            CIInit[__init__.py]
            CICreate[CreateIssue.py]
        end

        subgraph ScanSonar
            direction TB
            SSTypedpy[typed.py]
            SSREADME[README.md]
            SSScan[ScanSonar.py]
            SSInit[__init__.py]
        end

        subgraph PR
            direction TB
            PRTypedpy[typed.py]
            PRREADME[README.md]
            PRInit[__init__.py]
            PRPr[PR.py]
        end

        subgraph CallSQL
            direction TB
            CSTypedpy[typed.py]
            CSREADME[README.md]
            CSInit[__init__.py]
            CSCall[CallSQL.py]
        end

        subgraph ModifyCodeOnce
            direction TB
            MCOTypedpy[typed.py]
            MCOREADME[README.md]
            MCOInit[__init__.py]
            MCOModify[ModifyCodeOnce.py]
        end

        subgraph GetTypescriptTypeInfo
            direction TB
            GTITypedpy[typed.py]
            GTIREADME[README.md]
            GTIConfig[tsconfig.json]
            GTILock[pnpm-lock.yaml]
            GTIPackage[package.json]
            GTIInfo[get_type_info.ts]
            GTIInit[__init__.py]
            GTIGet[GetTypescriptTypeInfo.py]
        end

        subgraph FileAgent
            direction TB
            FATypedpy[typed.py]
            FAFile[FileAgent.py]
            FAInit[__init__.py]
        end

        subgraph CreateIssueComment
            direction TB
            CITypedpy[typed.py]
            CIREADME[README.md]
            CIInit[__init__.py]
            CICreate[CreateIssueComment.py]
        end

        subgraph BrowserUse
            direction TB
            BUTypedpy[typed.py]
            BUREADME[README.md]
            BUInit[__init__.py]
            BUBrowse[BrowserUse.py]
        end

        subgraph CallCode2Prompt
            direction TB
            CCTypedpy[typed.py]
            CCREADME[README.md]
            CCInit[__init__.py]
            CCCode[CallCode2Prompt.py]
            CCTest[TestCallCode2Prompt.py]
        end

        subgraph PreparePR
            direction TB
            PPPTypedpy[typed.py]
            PPREAdme[README.md]
            PPPPrepare[PreparePR.py]
            PPPInit[__init__.py]
        end

        subgraph JoinList
            direction TB
            JLTpy[typed.py]
            JLREADME[README.md]
            JLJoinList[JoinList.py]
            JLInit[__init__.py]
        end

        subgraph CreatePR
            direction TB
            CPTypedpy[typed.py]
            CPRREADME[README.md]
            CPInit[__init__.py]
            CPCreate[CreatePR.py]
        end

        subgraph ScanDepscan
            direction TB
            SDTypedpy[typed.py]
            SDREADME[README.md]
            SDSan[ScanDepscan.py]
            SDInit[__init__.py]
        end

        subgraph SimplifiedLLMOnce
            direction TB
            SMLTypedpy[typed.py]
            SMLREADME[README.md]
            SMLInit[__init__.py]
            SMLSimplified[SimplifiedLLMOnce.py]
        end

        subgraph ModifyCode
            direction TB
            MCTypedpy[typed.py]
            MCREADME[README.md]
            MCModify[ModifyCode.py]
            MCInit[__init__.py]
        end

        subgraph ManageEngineAgent
            direction TB
            METypedpy[typed.py]
            MEInit[__init__.py]
            MEAgent[ManageEngineAgent.py]
        end

        subgraph AgenticLLMV2
            direction TB
            ALVITypedpy[typed.py]
            ALVIREADME[README.md]
            ALVIInit[__init__.py]
            ALVIAgentic[AgenticLLMV2.py]
        end

        subgraph ExtractDiff
            direction TB
            EDTypedpy[typed.py]
            EDREADME[README.md]
            EDExtract[ExtractDiff.py]
            EDInit[__init__.py]
        end

        subgraph ReadEmail
            direction TB
            RETypedpy[typed.py]
            REREADME[README.md]
            RERead[ReadEmail.py]
            REInit[__init__.py]
        end

        subgraph CreatePRComment
            direction TB
            CPCOMTyped[typed.py]
            CPCOMREADME[README.md]
            CPCOMInit[__init__.py]
            CPCOMCreate[CreatePRComment.py]
        end

        subgraph ReadPRDiffs
            direction TB
            RPTypedpy[typed.py]
            RPREADME[README.md]
            RPInit[__init__.py]
            RPDRead[ReadPRDiffs.py]
        end

        subgraph SimplifiedLLM
            direction TB
            SLTypedpy[typed.py]
            SLREADME[README.md]
            SLInit[__init__.py]
            SLLSimplified[SimplifiedLLM.py]
        end

        subgraph CallShell
            direction TB
            CSHTypedpy[typed.py]
            CSHREADME[README.md]
            CSHInit[__init__.py]
            CSHCall[CallShell.py]
        end

        subgraph DatabaseAgent
            direction TB
            DATypedpy[typed.py]
            DAInit[__init__.py]
            DAgent[DatabaseAgent.py]
        end

        subgraph CommitChanges
            direction TB
            CCTypedpy[typed.py]
            CCREADME[README.md]
            CCOMInit[__init__.py]
            CCOMCommit[CommitChanges.py]
        end

        subgraph ZohoDeskAgent
            direction TB
            ZDTypedpy[typed.py]
            ZDREADME[README.md]
            ZDInit[__init__.py]
            ZDAgent[ZohoDeskAgent.py]
        end

        subgraph GitHubAgent
            direction TB
            GOTypedpy[typed.py]
            GInit[__init__.py]
            GOAgent[GitHubAgent.py]
        end

        subgraph ExtractPackageManagerFile
            direction TB
            EPMFTypedpy[typed.py]
            EPMFREADME[README.md]
            EPMFTest[TestExtractPackageManagerFile.py]
            EPMFInit[__init__.py]
            EPMFExtract[ExtractPackageManagerFile.py]
        end
    end
