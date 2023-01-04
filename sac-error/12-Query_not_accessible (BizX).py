SFDC=* NOT SFDC IN ("DC13", "DC25")
splunk_server_group = *_indexers
(host="*" OR servername="*")
sourcetype = server_log_bizx
LogLevel = ERROR 
 
"Repository: Encountered an error in repository runtime extension;Model inconsistency." OR
"Error occurred during execution of Table Function and PickList view Creation Task" OR
"Error in creating/updating" OR
"Dependent object not found: SqlScript;(.*?)PICKLIST_VIEW: symbol not found" OR
"Dependentobjectnotfound:SqlScript;(.*?)LOCALIZATION_VIEW:symbolnotfound"

| rex field=_raw "^([0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3})\s(ERROR)\s\[(?<err_class>.*?)\]\s\[(?<err_no>.*?)\]\s"
| rex field=_raw "^(.*)\[(?<GID>[0-9a-f\-]{32,})\]"
| rex field=_raw "^(.*)\[(?<instance>.*?)\,.*?\,.*?\,.*?\,.*?\,.*?\,.*?\]"
| rex field=_raw "^(?<skip>(?:[^\]\n]*\]){3})\s*(?P<err_message>.+)" 

| eval type = "Query_not_accessible"  

| rex field=err_message "(?<err_category1>Error in creating\/updating\s.*?)\s"
| rex field=err_message "\"errorCode\":(.*?),\"errorMsg\":\"(?<err_category2>.*?(:.*?,)*)"
| rex field=err_message "(?<err_category3>Error occurred during Table Function and PickList view Creation Task)"
| rex field=err_message "(?<err_category4>Error while creating\/updating.*)"
| rex field=err_message "(?<err_category5>Exception in creating scope filter)"
| rex field=err_message "(?<err_category6>Failed to create table function)"

| eval err_class=if(isnull(err_class), "Unassigned", trim(err_class))
| eval err_class=if(len(err_class)>256, substr(err_class,1,256), err_class)

| eval err_category=case(NOT isnull(err_category1), err_category1, NOT isnull(err_category2), err_category2, NOT isnull(err_category3), err_category3, NOT isnull(err_category4), err_category4, NOT isnull(err_category5), err_category5, NOT isnull(err_category6), err_category6, 1==1, null())
| eval err_category=if(isnull(err_category), "Unassigned", trim(err_category))
| eval err_category=if(len(err_category)>256, substr(err_category,1,256), err_category)

| eval date = strftime(_time, "%Y-%m-%d") 
| eval weekday = strftime(_time, "%A") 
| eval time = strftime(_time, "%H:%M") 
| eval hour = "\"" + substr(time,1,2) + "\""
| eval minute = strftime(_time, "%M")

| eval server = ifnull(servername, host, servername)
| eval server_type = if (substr(server, 1, 2) = "pc", "PROD", if (substr(server, 1, 2) = "sc", "PREVIEW", if (substr(server, 1, 2) = "ac", "QA",if (substr(server, 1, 2) = "ps", "SALES DEMO", "OTHER") ) ) ) 
| eval GID=replace(GID, "\-" , "")
| eval id=1 | accum id | eval count=1

| rename SFDC AS "dc", GID AS "correl", err_class AS "errorClass", err_category as "errorCategory" 

| table id, type, sourcetype, dc, host, servername, server, server_type, instance, date, time, hour, "Error (number)", "System (url)", class, correl, errorClass, errorCategory, count