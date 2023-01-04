SFDC=* NOT SFDC IN ("DC13", "DC25") 
splunk_server_group = *_indexers 
index=hcm_sac_app 
(host="*" OR servername="*")
(sourcetype = app_log_sac)
sac_app_log_level = ERROR 

("Error occured while saving labels to DB" 
OR  "User authentication validation failed due to invalid authentication details." 
OR  "Error retrieving translations from remote API" 
OR  "HDI Deployment active: false" 
OR  "Request: /qbuilder/sap/fpa/remote/qbuilder/GetServerInfo Unable to parse" 
OR  "does not have the correct naming convention!" 
OR  "Error occured while extracting story execution details from Ina request." 
OR  "Language is not set in the inaRequest" 
OR  "Unhandled error in servlet filter processing." 
OR  "Token decryption failed." 
OR  "Unexpected error occured: com.sap.orca.remote.qbuilder.rest.exceptions.ServerErrorException" 
OR  "I/O error on POST request for" 
OR  "GenericRemoteAPI call failed. Request URI:" 
OR  "403 Forbidden" 
OR  "500 Internal Server Error:" 
OR  "Query is not activated and will be deleted" 
OR  "Package name missing" 
OR  "Could not commit JPA transaction" 
OR  "com.sap.db.jdbc.exceptions.JDBCDriverException: SAP DBTech JDBC" 
OR  "ERROR_CODE5037\"Column does not exist in calculation View\"" 
OR  "does not exists in data source" 
OR  "Unexpected error occured: org.apache.catalina.connector.ClientAbortException: java.net.SocketTimeoutException" 
OR  "Unexpected error occured: java.lang.NullPointerException" 
OR  "Cannot forward to error page for request" 
OR  "Unexpected error occured: java.util.MissingResourceException" 
OR  "Unexpected error occured: org.springframework.beans.factory.BeanCreationException:" 
OR  "Rest Client Exception Occurred : org.springframework.web.client.ResourceAccessException" 
OR  "SFSF Metadata child node list is empty." 
OR  "User authentication service call failed" 
OR  "Remote API error: Invalid node Id or error while fetching label" 
OR  "406 Not Acceptable" 
OR  "java.util.MissingResourceException: Could not load any resource bundle by com.sun.org.apache.xerces.internal.impl.msg.XMLSchemaMessages" 
OR  "LogicalModelName is null/empty in logical model" 
OR  "c.s.o.r.q.o.s.q.RuntimeMetadataHandler" 
OR  "PooledConnection has already been closed." 
OR  "File not found:" 
OR  "Failed to get the server information:" 
OR  "ERROR-5018: Source data source" 
OR  "Unexpected error occured: org.apache.catalina.connector.ClientAbortException: java.io.IOException: Broken pipe" 
OR  "VCAP_SERVICES is valid JSON, but not a JSON object" 
OR  "504 Gateway Time-out" 
OR  "Unexpected error occured: com.sap.db.jdbc.exceptions.InternalReconnectException" 
OR  "ERROR-5008:" 
OR  "Translations: NodeSource information not available for" 
OR  "Unable to parse the Accept-Language: en-US,en;q=0.9" 
OR  "Right datasource rd5 is used in two joins" 
OR  "ERROR-5028:" 
OR  "Unexpected error occured: java.lang.ArrayIndexOutOfBoundsException" 
OR  "Could not extract response" 
OR  "com.sap.db.jdbc.ConnectionSapDB._tryReconnect" 
OR  "502 Bad Gateway:" 
OR  "401 Bad credentials" 
OR  "Ljava.lang.StackTraceElement" 
OR  "Unexpected error occured: com.google.gson.JsonSyntaxException: com.google.gson.stream.MalformedJsonException" 
OR  "Query not found." 
OR  "Error Fetching and Building widget List: A server error has occurred" 
OR  "Unable to get data from publicAPI service" 
OR  "Exception while processing variables" 
OR  "Error during processSynchronization." 
OR  "The selection returned more records than the limit in MaxResultRecords" 
OR  "Unexpected error occured: org.apache.catalina.connector.ClientAbortException: java.io.IOException: Connection reset by peer" 
OR  "QueryObject creation failed for:" 
OR  "java.sql.SQLException: Connection has already been closed." 
OR  "Unexpected error occured: org.springframework.orm.jpa.JpaSystemException:" 
OR  "SAP DBTech JDBC: [258]: insufficient privilege:" 
OR  "Error while writing csv export response to DB" 
OR  "Unexpected error occured: org.springframework.web.client.ResourceAccessException:" 
OR  "Failed to execute an InA query:" 
OR  "Empty root node list." 
OR  "We failed to execute the query."
OR  "BadRequestException")

| eval ErrorCategory = case( 
like(_raw, "%BadRequestException%"), "BadRequestException",
like(_raw, "%The parallel execution limit per tenant has been exceeded:%"), "Failed to execute query-Execution limit exceeded",
like(_raw, "%Error occured while saving labels to DB%"), "Save Labels Error", 
like(_raw, "%User authentication validation failed due to invalid authentication details.%"), "Invalid Authentication", 
like(_raw, "%Error retrieving translations from remote API%"), "Remote API Error", 
like(_raw, "%HDI Deployment active: false%"), "HDI Deployment", 
like(_raw, "%Request: /qbuilder/sap/fpa/remote/qbuilder/GetServerInfo Unable to parse%"), "Parse Error", 
like(_raw, "%does not have the correct naming convention!%"), "Package Naming", 
like(_raw, "%Error occured while extracting story execution details from Ina request.%"), "Execution Details Extraction", 
like(_raw, "%Language is not set in the inaRequest%"), "Language Not Set", 
like(_raw, "%Unhandled error in servlet filter processing.%"), "Unhandled Error", 
like(_raw, "%Token decryption failed.%"), "Token Decryption", 
like(_raw, "%Unexpected error occured: com.sap.orca.remote.qbuilder.rest.exceptions.ServerErrorException%"), "Unexpected error occurred", 
like(_raw, "%I/O error on POST request for%"), "I/O Error", 
like(_raw, "%GenericRemoteAPI call failed. Request URI:%"), "GenericRemoteAPI call failed", 
like(_raw, "%403 Forbidden%"), "403 Forbidden", 
like(_raw, "%500 Internal Server Error:%"), "500 Internal Server Error", 
like(_raw, "%Query is not activated and will be deleted%"), "Query is not activated", 
like(_raw, "%Package name missing%"), "Package name missing", 
like(_raw, "%Could not commit JPA transaction%"), "JPA Transaction Commit", 
like(_raw, "%com.sap.db.jdbc.exceptions.JDBCDriverException: SAP DBTech JDBC%"), "JDBCDriverException", 
like(_raw, "%ERROR_CODE5037\"Column does not exist in calculation View\"%"), "Column does not exist", 
like(_raw, "%does not exists in data source%"), "Data source", 
like(_raw, "%Unexpected error occured: org.apache.catalina.connector.ClientAbortException: java.net.SocketTimeoutException%"), "Socket Timeout", 
like(_raw, "%Unexpected error occured: java.lang.NullPointerException%"), "NullPointer", 
like(_raw, "%Cannot forward to error page for request%"), "Error Page forwarding", 
like(_raw, "%Unexpected error occured: java.util.MissingResourceException%"), "MissingResourceException", 
like(_raw, "%Unexpected error occured: org.springframework.beans.factory.BeanCreationException:%"), "BeanCreationException", 
like(_raw, "%Rest Client Exception Occurred : org.springframework.web.client.ResourceAccessException%"), "ResourceAccessException", 
like(_raw, "%SFSF Metadata child node list is empty.%"), "Child Node empty", 
like(_raw, "%User authentication service call failed%"), "User Authentication Service Failure", 
like(_raw, "%Remote API error: Invalid node Id or error while fetching label%"), "Invalid Node Id", 
like(_raw, "%406 Not Acceptable%"), "406 Not Acceptable", 
like(_raw, "%java.util.MissingResourceException: Could not load any resource bundle by com.sun.org.apache.xerces.internal.impl.msg.XMLSchemaMessages%"), "Could not load any resource bundle", 
like(_raw, "%LogicalModelName is null/empty in logical model%"), "Logical Model Null", 
like(_raw, "%c.s.o.r.q.o.s.q.RuntimeMetadataHandler%"), "RuntimeMetadataHandler", 
like(_raw, "%PooledConnection has already been closed.%"), "PooledConnection has already been closed", 
like(_raw, "%File not found:%"), "File not found", 
like(_raw, "%Failed to get the server information:%"), "Failed to get the server information", 
like(_raw, "%ERROR-5018: Source data source%"), "ERROR-5018: Source data source", 
like(_raw, "%Unexpected error occured: org.apache.catalina.connector.ClientAbortException: java.io.IOException: Broken pipe%"), "IOException: Broken pipe", 
like(_raw, "%VCAP_SERVICES is valid JSON, but not a JSON object%"), "VCAP_SERVICES not a valid JSON", 
like(_raw, "%504 Gateway Time-out%"), "504 Gateway Time-out", 
like(_raw, "%Unexpected error occured: com.sap.db.jdbc.exceptions.InternalReconnectException%"), "InternalReconnectException", 
like(_raw, "%ERROR-5008:%"), "ERROR-5008", 
like(_raw, "%Translations: NodeSource information not available for%"), "Translations- NodeSource information not available", 
like(_raw, "%Unable to parse the Accept-Language: en-US,en;q=0.9%"), "Language Parse Error", 
like(_raw, "%Right datasource rd5 is used in two joins%"), "Data source join", 
like(_raw, "%ERROR-5028:%"), "ERROR-5028", 
like(_raw, "%Unexpected error occured: java.lang.ArrayIndexOutOfBoundsException%"), "ArrayIndexOutOfBoundsException", 
like(_raw, "%Could not extract response%"), "Could not extract response", 
like(_raw, "%com.sap.db.jdbc.ConnectionSapDB._tryReconnect%"), "ConnectionSapDB._tryReconnect", 
like(_raw, "%502 Bad Gateway:%"), "502 Bad Gateway:", 
like(_raw, "%401 Bad credentials%"), "401 Bad credentials", 
like(_raw, "%Ljava.lang.StackTraceElement%"), "StackTraceElement", 
like(_raw, "%Unexpected error occured: com.google.gson.JsonSyntaxException: com.google.gson.stream.MalformedJsonException%"), "MalformedJsonException", 
like(_raw, "%Query not found.%"), "Query not found", 
like(_raw, "%Error Fetching and Building widget List: A server error has occurred%"), "Building widget List", 
like(_raw, "%Unable to get data from publicAPI service%"), "Public API Error", 
like(_raw, "%Exception while processing variables%"), "Exception while processing variables", 
like(_raw, "%Error during processSynchronization.%"), "Error during processSynchronization", like(_raw, "%The selection returned more records than the limit in MaxResultRecords%"), "The selection returned more records than the limit ", 
like(_raw, "%Unexpected error occured: org.apache.catalina.connector.ClientAbortException: java.io.IOException: Connection reset by peer%"), "IOException: Connection reset by peer", 
like(_raw, "%QueryObject creation failed for:%"), "QueryObject creation failed", 
like(_raw, "%java.sql.SQLException: Connection has already been closed.%"), "SQLException: Connection has already been closed", 
like(_raw, "%Unexpected error occured: org.springframework.orm.jpa.JpaSystemException:%"), "JpaSystemException", 
like(_raw, "%SAP DBTech JDBC: [258]: insufficient privilege:%"), "insufficient privilege", 
like(_raw, "%Error while writing csv export response to DB%"), "Error writing csv export response", 
like(_raw, "%Unexpected error occured: org.springframework.web.client.ResourceAccessException:%"), "Unexpected error occured: ResourceAccessException", 
like(_raw, "%Failed to execute an InA query:%"), "Failed to execute an InA query", 
like(_raw, "%Empty root node list.%"), "Empty root node list", 
1==1, "Unknow Error") 

| search ErrorCategory="Query is not activated"
| eval type = replace(ErrorCategory," ", "_")

| rex field=_raw "([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}) ERROR (?<err_no>\d+) \S+ \[(?<url>\S+)\] (?<class_name>\S+)\s*\: \[+(?<user_id>\S+)\,(?<instance>\S+)\,(?<other_id>\S+)\]+ \[+(?<GID>\S+)\]+ (?<err_text>\S.*)(\s+(?<err_detail>\S.*)\n(?<err_trace>(\t\S.*\n)*))*" 
| eval err_text = substr(err_text,1,250)
| eval err_detail = substr(err_detail,1,250)
| eval err_trace = substr(err_trace,1,250)
| eval err_text = case(isnull(err_text), "NA", 1==1, err_text)
| eval err_detail = case(isnull(err_detail), "NA", 1==1, err_detail)
| eval err_trace = case(isnull(err_trace), "NA", 1==1, err_trace) 
| rex field=err_text "^(?<err_class>.*)$" 
| rex field=err_detail "^(?<err_category>.*)$" 

| rex field=err_text "^(?<err_class>.*?),\\s+(?<err_category>.*?)\\:(.*)$"
| rex field=err_text "^(?<err_class>.*?)for\\:\\s+(?<err_category>.*\\:.*)\\:(.*)$"

| eval date = strftime(_time, "%Y-%m-%d") 
| eval weekday = strftime(_time, "%A") 
| eval time = strftime(_time, "%H:%M") 
| eval hour = "\"" + substr(time,1,2) + "\""
| eval servername = case(isnull(servername), "NA", 1==1, servername)
| streamstats count as id | eval count = "1"

| eval server = if(servername="NA", host, servername)
| eval server_type = if (substr(server, 1, 2) = "pc", "PROD", if (substr(server, 1, 2) = "sc", "PREVIEW", if (substr(server, 1, 2) = "ac", "QA",if (substr(server, 1, 2) = "ps", "SALES DEMO", "OTHER") ) ) )
| eval GID = replace (GID, "-" , "")

| rename SFDC AS "dc", err_no AS "Error (number)", url AS "System (url)", class_name AS "class", GID AS "correl", err_class AS "errorClass", err_category as "errorCategory" 
| table id, type, sourcetype, dc, host, servername, server, server_type, instance, date, time, hour, "Error (number)", "System (url)", class, correl, errorClass, errorCategory, count