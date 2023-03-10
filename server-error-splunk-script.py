SFDC=* NOT SFDC IN ("DC13", "DC25")
splunk_server_group = *_indexers
(host="*" OR servername="*")
sourcetype = server_log_bizx
LogLevel = ERROR ((CalculationViewGenerationServiceV2 OR GetSACResourceImpl OR SACOEMRestClient))
| rex field=_raw "^([0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3})\s(ERROR)\s\[(?<component>.*?)\]"
| rex field=_raw "^(.*)\[(?<correl>[0-9a-f\-]{32,})\]"
| rex field=_raw "^(.*)\[(?<instance>.*?)\,.*?\,.*?\,.*?\,.*?\,.*?\,.*?\]"
| rex field=_raw "^(?<skip>(?:[^\]\n]*\]){1,})\s*(?P<err_message>.+)" 
| eval err_message=case(
    like(err_message,"DAOException%"),"(DAOException)",
    like(err_message,"Enable SAC in LMS Task Failed with exception%"),"(Enable SAC in LMS Task Failed with exception)",
    like(err_message,"Error caused by import service failure"),"(Error caused by import service failure)",
    like(err_message,"Error encountered while fetching all associated labels%"),"(Error encountered while fetching all associated labels)",
    like(err_message,"Error extracting result from future"),"(Error extracting result from future)",
    like(err_message,"Error in creating OEM Request%"),"(Error in creating OEM Request)",
    like(err_message,"Error occured while getting All SAC artifacts%"),"(Error occured while getting All SAC artifacts)",
    like(err_message,"Error occurred during Table Function and PickList view Creation Task%"),"(Error occurred during Table Function and PickList view Creation Task)",
    like(err_message,"Error while calling SAC Stock HANA User Creation api"),"(Error while calling SAC Stock HANA User Creation api)",
    like(err_message,"Error while checking SAC User%"),"(Error while checking SAC User)",
    like(err_message,"Error while executing the search configuration%"),"(Error while executing the search configuration)",
    like(err_message,"Error while getting deleting the query calc view for the story in OEM%"),"(Error while getting deleting the query calc view for the story in OEM)",
    like(err_message,"Error while getting the widget details%"),"(Error while getting the widget details)",
    like(err_message,"Error while populating the response into share collection%"),"(Error while populating the response into share collection)",
    like(err_message,"Error while processing QueryValidationRequest."),"(Error while processing QueryValidationRequest.)",
    like(err_message,"Exception in getNodeInfo%"),"(Exception in getNodeInfo)",
    like(err_message,"Exception occurred in startTasksUsingThreads"),"(Exception occurred in startTasksUsingThreads)",
    like(err_message,"Exception while getting the grup type to ID maps"),"(Exception while getting the grup type to ID maps)",
    like(err_message,"Exception while updating the SAc Share criteria%"),"(Exception while updating the SAc Share criteria)",like(err_message,"Exception while updating the SAC Story Group Share Criteria%"),"(Exception while updating the SAC Story Group Share Criteria)",
    like(err_message,"ExceptionRootCauseTag=%,ExceptionStackTraceTag=%"),"(ExceptionRootCauseTag=...,ExceptionStackTraceTag=...)",
    like(err_message,"Failed /childnodes/"),"(Failed /childnodes/)",
    like(err_message,"Failed /nodeInfo/"),"(Failed /nodeInfo/)",
    like(err_message,"Failed in /preexecutionmetadata when getting permission details"),"(Failed in /preexecutionmetadata when getting permission details)",
    like(err_message,"Failed to resolve entity%"),"(Failed to resolve entity)",
    like(err_message,"Hit Exception to run APM task%"),"(Hit Exception to run APM task)",
    like(err_message,"Integration Security: Unable to find any oauth configuration%"),"(Integration Security: Unable to find any oauth configuration)",
    like(err_message,"java.lang.RuntimeException%com.successfactors.coengine.error.detail.COEnt%"),"(java.lang.RuntimeException...com.successfactors.coengine.error.detail.COEnt...)",
    like(err_message,"Parsing exception while parsing response string to JSON%"),"(Parsing exception while parsing response string to JSON)",
    like(err_message,"RuntimeException%"),"(RuntimeException)",
    like(err_message,"Service Application Exception%"),"(Service Application Exception)",like(err_message,"SQLException"),"(SQLException)",
    like(err_message,"Validity Check for logical model%failed"),"(Validity Check for logical model...failed)",
    like(err_message,"Error encountered while importing ACN Reports%"),"(Error encountered while importing ACN Reports)",
    like(err_message,"Error occured while performing action%"),"(Error occured while performing action)",
    like(err_message,"Error while fetching Field permission details%"),"(Error while fetching Field permission details)",
    like(err_message,"Error while getting the list of supported formats for the story%"),"(Error while getting the list of supported formats for the story)",
    like(err_message,"Error while getting the prompt filter for the story%"),"(Error while getting the prompt filter for the story)",
    like(err_message,"Error while processing QueryValidationRequest%"),"(Error while processing QueryValidationRequest)",
    like(err_message,"Error while updating the global sys config entry%"),"(Error while updating the global sys config entry)",
    like(err_message,"Error while validating SAC Story Listing API%"),"(Error while validating SAC Story Listing API)",
    like(err_message,"Vault error for api oauth:%Platform getCryptographicKey fail"),"(Vault error for api oauth:...Platform getCryptographicKey fail)",
    like(err_message,"Error caused by export service failure"),"(Error caused by export service failure)",
    like(err_message,"Error create index%error is Access denied%"),"(Error create index...error is Access denied...)",
    like(err_message,"Error encountered while checking Standard Content Import Job Status%"),"(Error encountered while checking Standard Content Import Job Status)",
    like(err_message,"Error encountered while fetching ACN Reports"),"(Error encountered while fetching ACN Reports)",
    like(err_message,"Error encountered while fetching company specific throttling configuration%"),"(Error encountered while fetching company specific throttling configuration)",
    like(err_message,"Error occured while getting All SAC artifacts%"),"(Error occured while getting All SAC artifacts)",
    like(err_message,"Error serializing object due to other Exception%"),"(Error serializing object due to other Exception)",
    like(err_message,"Error while checking SAC Stock HANA UserCreation Status"),"(Error while checking SAC Stock HANA UserCreation Status)",
    like(err_message,"Error while checking SAC User%"),"(Error while checking SAC User)",
    like(err_message,"Error while fetching SAC TenantInfo%"),"(Error while fetching SAC TenantInfo)",like(err_message,"Error while populating the response into share collection%"),"(Error while populating the response into share collection)",
    like(err_message,"Error while retrieving sac report story list from controller%"),"(Error while retrieving sac report story list from controller)",
    like(err_message,"Exception encountered while trying to fetch global configuration%"),"(Exception encountered while trying to fetch global configuration)",
    like(err_message,"Exception getting connection to pool%"),"(Exception getting connection to pool)",
    like(err_message,"Exception in creating LMS live connection%"),"(Exception in creating LMS live connection)",
    like(err_message,"Exception is caught when doing serialization%"),"(Exception is caught when doing serialization)",
    like(err_message,"Exception while updating the SAc Share criteria%"),"(Exception while updating the SAc Share criteria)",
    like(err_message,"Exception while updating the SAC Story Group Share Criteria%"),"(Exception while updating the SAC Story Group Share Criteria)",
    like(err_message,"Failed to execute and process SQL query"),"(Failed to execute and process SQL query)",
    like(err_message,"Got error on getSysConfig()%"),"(Got error on getSysConfig())",
    like(err_message,"%Object Definition is Null for provided Object Type%"),"(Object Definition is Null for provided Object Type)",
    like(err_message,"java.lang.RuntimeException%com.github.scribejava.core.exceptions.OAuthConnectionException%"),"(com.github.scribejava.core.exceptions.OAuthConnectionException)",
    like(err_message,"Job Execution failed%"),"(Job Execution failed)",
    like(err_message,"Parsing exception while parsing response string to JSON%"),"(Parsing exception while parsing response string to JSON)",
    like(err_message,"Passed ParamBean is null%"),"(Passed ParamBean is null)",
    like(err_message,"%GetSACResourceImpl%/provisioning_companies%"),"(GetSACResourceImpl.provisioning_companies)",
    like(err_message,"Error processing /preexecutionmetadata%"),"(Error processing /preexecutionmetadata)",
    like(err_message,"Error occurred while fetching the host and port of the given company"),"(Error occurred while fetching the host and port of the given company)",
    like(err_message,"The domain builder cannot be loaded to engine%"),"(The domain builder cannot be loaded to engine)",
    like(err_message,"Error caused by Delete Service failure%"),"(Error caused by Delete Service failure)",
    like(err_message,"Error fetching reporting artifacts%"),"(Error fetching reporting artifacts)",
    
    like(err_message,"Cannot proceed with making call to OEM Server%Fail to generate access token%"),"(Cannot proceed with making call to OEM Server...Fail to generate access token)",
    like(err_message,"An error occurred while retrieving sac/csrf token%"),"(An error occurred while retrieving sac/csrf token)",
    like(err_message,"Error while processing SACUserRoleFixExecutor%"),"(Error while processing SACUserRoleFixExecutor)",
    like(err_message,"Unknown Exception%"),"(Unknown Exception)",
    like(err_message,"Error in resolve%Entity%"),"(Error in resolve...Entity)",
    like(err_message,"Error while fetching%of SPC Process"),"(Error while fetching...of SPC Process)",
    like(err_message,"Failed /rootnodes/"),"(Failed /rootnodes/)",
    like(err_message,"No permitted%found, returning empty list%"),"(No permitted...found, returning empty list)",
    like(err_message,"Error Occured while invoking SAC health check API"),"(Error Occured while invoking SAC health check API)",
    like(err_message,"Get SAC configuration sets failed%"),"(Get SAC configuration sets failed)",
    like(err_message,"Fetching sub-domain-schema from MDF failed%"),"(Fetching sub-domain-schema from MDF failed)",like(err_message,"Error in fetching TenantUUID"),"(Error in fetching TenantUUID)",
    like(err_message,"Error while submitting execution request for story%"),"(Error while submitting execution request for story)",
    like(err_message,"Error while releasing http connection resource%"),"(Error while releasing http connection resource)",
    like(err_message,"Exception occured while getting db connection details "),"(Exception occured while getting db connection details )",
    like(ignore,"%Cannot proceed with making call to OEM Server%Fail to generate access token%"),"(Cannot proceed with making call to OEM Server...Fail to generate access token)",
    like(ignore,"%com.github.scribejava.core.exceptions.OAuthException: Response body is incorrect%"),"(OAuthException: Response body is incorrect)",
    like(ignore,"%Error getting GDPR Qualifier%"),"(Error getting GDPR Qualifier)",
    like(ignore,"%Unable to get managed connection%"),"(Unable to get managed connection)",
    like(ignore,"%JAXBSerializerException: Error serializing object%"),"(JAXBSerializerException: Error serializing object)",
    like(ignore,"%AnalyticsException: Unable to deserialize%"),"(AnalyticsException: Unable to deserialize)",
    like(ignore,"%NullPointerException: while trying to invoke the method%"),"(NullPointerException: while trying to invoke the method)",
    like(ignore,"%Saving SAC OAuth configuration Failed%"),"(Saving SAC OAuth configuration Failed)",
    like(ignore,"%Error creating bean%"),"(Error creating bean)",
    1==1,err_message)

| eval err_message = substr(err_message,1,256)
| eval date = strftime(_time, "%Y-%m-%d") 
| eval weekday = strftime(_time, "%A") 
| eval time = strftime(_time, "%H:%M") 
| eval hour = "\"" + substr(time,1,2) + "\""
| eval minute = strftime(_time, "%M")
| eval time_2 = strftime(_time + if(minute%2=0,0,(2-minute%2)*60), "%H:%M")
| eval time_3 = strftime(_time + if(minute%3=0,0,(3-minute%3)*60), "%H:%M")
| eval date_2 = strftime(_time + if(time="23:59",86400,0), "%Y-%m-%d")
| eval date_3 = strftime(_time + if(time="23:58" OR time="23:59",86400,0), "%Y-%m-%d") | fields - minute
| eval server = ifnull(servername, host, servername)
| eval server_type = if (substr(server, 1, 2) = "pc", "PROD", if (substr(server, 1, 2) = "sc", "PREVIEW", if (substr(server, 1, 2) = "ac", "QA",if (substr(server, 1, 2) = "ps", "SALES DEMO", "OTHER") ) ) ) 
| eval correl=replace(correl, "\-" , "") | eval component=replace(component, "\[" , "")
| eval id=1 | accum id | eval count=1
| rename SFDC AS "dc" 
| eval time_second = strftime(_time, "%H:%M:%S")
| dedup instance, date, time_second, component | fields - time_second
 
| table id, date, weekday, time, hour, dc, sourcetype, server, server_type, instance, correl, component, err_message, count, date_2, time_2, date_3, time_3