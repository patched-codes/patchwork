graph TD;
    subgraph patchwork/steps
        subgraph "LLM"
            direction LR
            file104["__init__.py"]
            file105["LLM.py"]
            file106["typed.py"]
            file107["README.md"]
        end
        subgraph "CallCode2Prompt"
            direction LR
            file108["__init__.py"]
            file109["CallCode2Prompt.py"]
            file110["TestCallCode2Prompt.py"]
            file111["typed.py"]
            file112["README.md"]
        end
        subgraph "GenerateCodeRepositoryEmbeddings"
            direction LR
            file113["__init__.py"]
            file114["GenerateCodeRepositoryEmbeddings.py"]
            file115["typed.py"]
            file116["filter_lists.py"]
            file117["README.md"]
        end
        subgraph "ScanSemgrep"
            direction LR
            file118["__init__.py"]
            file119["ScanSemgrep.py"]
            file120["typed.py"]
            file121["README.md"]
        end
        subgraph "GetTypescriptTypeInfo"
            direction LR
            file122["__init__.py"]
            file123["get_type_info.ts"]
            file124["GetTypescriptTypeInfo.py"]
            file125["tsconfig.json"]
            file126["typed.py"]
            file127["pnpm-lock.yaml"]
            file128["package.json"]
            file129["README.md"]
        end
        subgraph "ExtractCodeMethodForCommentContexts"
            direction LR
            file130["__init__.py"]
            file131["ExtractCodeMethodForCommentContexts.py"]
            file132["typed.py"]
            file133["README.md"]
        end
        subgraph "ExtractModelResponse"
            direction LR
            file134["ExtractModelResponse.py"]
            file135["__init__.py"]
            file136["typed.py"]
            file137["README.md"]
        end
        subgraph "GenerateEmbeddings"
            direction LR
            file138["__init__.py"]
            file139["GenerateEmbeddings.py"]
            file140["typed.py"]
            file141["README.md"]
        end
        subgraph "PR"
            direction LR
            file142["PR.py"]
            file143["__init__.py"]
            file144["typed.py"]
            file145["README.md"]
        end
        subgraph "SlackMessage"
            direction LR
            file146["__init__.py"]
            file147["typed.py"]
            file148["SlackMessage.py"]
            file149["README.md"]
        end
        subgraph "PreparePR"
            direction LR
            file150["__init__.py"]
            file151["PreparePR.py"]
            file152["typed.py"]
            file153["README.md"]
        end
        subgraph "ModifyCodeOnce"
            direction LR
            file154["__init__.py"]
            file155["ModifyCodeOnce.py"]
            file156["typed.py"]
            file157["README.md"]
        end
        subgraph "CreatePRComment"
            direction LR
            file158["__init__.py"]
            file159["typed.py"]
            file160["CreatePRComment.py"]
            file161["README.md"]
        end
        subgraph "CallShell"
            direction LR
            file162["CallShell.py"]
            file163["__init__.py"]
            file164["typed.py"]
            file165["README.md"]
        end
        subgraph "AgenticLLMV2"
            direction LR
            file166["__init__.py"]
            file167["AgenticLLMV2.py"]
            file168["typed.py"]
            file169["README.md"]
        end
        subgraph "FixIssue"
            direction LR
            file170["__init__.py"]
            file171["typed.py"]
            file172["FixIssue.py"]
            file173["README.md"]
        end
        subgraph "ScanSonar"
            direction LR
            file174["ScanSonar.py"]
            file175["__init__.py"]
            file176["typed.py"]
            file177["README.md"]
        end
        subgraph "CreateIssue"
            direction LR
            file178["__init__.py"]
            file179["CreateIssue.py"]
            file180["typed.py"]
            file181["README.md"]
        end
        subgraph "FilterBySimilarity"
            direction LR
            file182["__init__.py"]
            file183["FilterBySimilarity.py"]
            file184["typed.py"]
            file185["README.md"]
        end
        subgraph "ReadPRDiffs"
            direction LR
            file186["__init__.py"]
            file187["typed.py"]
            file188["ReadPRDiffs.py"]
            file189["README.md"]
        end
        subgraph "AgenticLLM"
            direction LR
            file190["__init__.py"]
            file191["typed.py"]
            file192["AgenticLLM.py"]
            file193["README.md"]
        end
        subgraph "CommitChanges"
            direction LR
            file194["__init__.py"]
            file195["CommitChanges.py"]
            file196["typed.py"]
            file197["README.md"]
        end
        subgraph "SimplifiedLLMOnce"
            direction LR
            file198["SimplifiedLLMOnce.py"]
            file199["__init__.py"]
            file200["typed.py"]
            file201["README.md"]
        end
        subgraph "ExtractPackageManagerFile"
            direction LR
            file202["__init__.py"]
            file203["TestExtractPackageManagerFile.py"]
            file204["typed.py"]
            file205["ExtractPackageManagerFile.py"]
            file206["README.md"]
        end
        subgraph "ReadEmail"
            direction LR
            file207["__init__.py"]
            file208["ReadEmail.py"]
            file209["typed.py"]
            file210["README.md"]
        end
        subgraph "ModifyCode"
            direction LR
            file211["__init__.py"]
            file212["typed.py"]
            file213["ModifyCode.py"]
            file214["README.md"]
        end
        subgraph "JoinList"
            direction LR
            file215["JoinList.py"]
            file216["__init__.py"]
            file217["typed.py"]
            file218["README.md"]
        end
        subgraph "CallAPI"
            direction LR
            file219["CallAPI.py"]
            file220["__init__.py"]
            file221["typed.py"]
            file222["README.md"]
        end
        subgraph "CreatePR"
            direction LR
            file223["__init__.py"]
            file224["typed.py"]
            file225["README.md"]
            file226["CreatePR.py"]
        end
        subgraph "ReadIssues"
            direction LR
            file227["ReadIssues.py"]
            file228["__init__.py"]
            file229["typed.py"]
            file230["README.md"]
        end
        subgraph "ReadFile"
            direction LR
            file231["__init__.py"]
            file232["typed.py"]
            file233["README.md"]
            file234["ReadFile.py"]
        end
        subgraph "CallLLM"
            direction LR
            file235["CallLLM.py"]
            file236["__init__.py"]
            file237["typed.py"]
            file238["README.md"]
        end
        subgraph "CallSQL"
            direction LR
            file239["CallSQL.py"]
            file240["__init__.py"]
            file241["typed.py"]
            file242["README.md"]
        end
        subgraph "ScanDepscan"
            direction LR
            file243["__init__.py"]
            file244["ScanDepscan.py"]
            file245["typed.py"]
            file246["README.md"]
        end
        subgraph "ExtractDiff"
            direction LR
            file247["__init__.py"]
            file248["typed.py"]
            file249["ExtractDiff.py"]
            file250["README.md"]
        end
        subgraph "QueryEmbeddings"
            direction LR
            file251["__init__.py"]
            file252["typed.py"]
            file253["QueryEmbeddings.py"]
            file254["README.md"]
        end
        subgraph "SendEmail"
            direction LR
            file255["__init__.py"]
            file256["SendEmail.py"]
            file257["typed.py"]
            file258["README.md"]
        end
        subgraph "Combine"
            direction LR
            file259["__init__.py"]
            file260["Combine.py"]
            file261["typed.py"]
            file262["README.md"]
        end
        subgraph "SimplifiedLLM"
            direction LR
            file263["SimplifiedLLM.py"]
            file264["__init__.py"]
            file265["typed.py"]
            file266["README.md"]
        end
        subgraph "ReadPRs"
            direction LR
            file267["__init__.py"]
            file268["ReadPRs.py"]
            file269["typed.py"]
            file270["README.md"]
        end
        subgraph "ExtractCodeContexts"
            direction LR
            file271["__init__.py"]
            file272["typed.py"]
            file273["README.md"]
            file274["ExtractCodeContexts.py"]
        end
        subgraph "AnalyzeImpact"
            direction LR
            file275["__init__.py"]
            file276["AnalyzeImpact.py"]
            file277["typed.py"]
            file278["README.md"]
        end
        subgraph "PreparePrompt"
            direction LR
            file279["__init__.py"]
            file280["PreparePrompt.py"]
            file281["typed.py"]
            file282["README.md"]
        end
        subgraph "CreateIssueComment"
            direction LR
            file283["__init__.py"]
            file284["typed.py"]
            file285["CreateIssueComment.py"]
            file286["README.md"]
        end
        subgraph "ExtractCode"
            direction LR
            file287["__init__.py"]
            file288["ExtractCode.py"]
            file289["typed.py"]
            file290["README.md"]
        end
        file102["__init__.py"]
        file103["README.md"]
    end
