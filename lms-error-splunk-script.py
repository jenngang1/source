SFDC=* NOT SFDC IN ("DC13", "DC25")
(host="*" OR servername="*")
(sourcetype = kube:sac_ois_lms_logs)
ERROR AND NOT INFO AND NOT POST

| rex field=_raw ":\s\[(.*?),(?<instance>.*?),(.*?)\]\s\["
| rex field=_raw "^.*?\]\s([a-z][\.])*(?<component>.*?)\s+:\s\["
| rex field=_raw "^(?:[^\]\n]*\]){2}\s*\[(?<correl>.*?)\]\s*"
| rex field=_raw "^(?:[^\]\n]*\]){3}\s+(?P<error_statement>.+)( -)"

| eval error_statement = case(
    like(_raw, "%500%"), "500 InternalError",
    like(_raw, "%invalid name of function or procedure%"), "invalid name of function or procedure",
    like(_raw, "%ERROR_CODE 42201 Column not found%"), "ERROR_CODE 42201 Column not found",
    like(_raw, "%ERROR_CODE 42420 The aggregation type is invalid%"), "ERROR_CODE 42420 The aggregation type is invalid",
    like(_raw, "%ERROR_CODE 6009 Unsupported dimension name in the query%"), "ERROR_CODE 6009 Unsupported dimension name in the query",
    like(_raw, "%ERROR_CODE5040 Query is not activated and will be deleted%"), "ERROR_CODE5040 Query is not activated and will be deleted",
    like(_raw, "%Migration failed for query%"), "Migration failed for query",
    like(_raw, "%Repository: Encountered an error in repository runtime extension;Model inconsistency.%"), "Repository: Encountered an error in repository runtime extension;Model inconsistency.",
    like(_raw, "%Unhandled error in servlet filter processing.%"), "Unhandled error in servlet filter processing.",
    like(_raw, "%QueryObject creation failed%"), "QueryObject creation failed",
    like(_raw, "%ERROR_CODE : 2048 : SAP DBTech JDBC: [2048]: column store error%"), "ERROR_CODE : 2048 : SAP DBTech JDBC: [2048]: column store error",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 1000002: Allocation failed%"), "ERROR_CODE 42014 Caught exception : exception 1000002: Allocation failed",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42018: Internal error occurred while processing%"), "ERROR_CODE 42014 Caught exception : exception 42018: Internal error occurred while processing",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42111: SQL Error%"), "ERROR_CODE 42014 Caught exception : exception 42111: SQL Error",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42218: The Blending mapping is wrongly defined%"), "ERROR_CODE 42014 Caught exception : exception 42218: The Blending mapping is wrongly defined",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42445: A field name in a filter must be a view column or dimension%"), "ERROR_CODE 42014 Caught exception : exception 42445: A field name in a filter must be a view column or dimension",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42556: Extended dimension processing error%"), "ERROR_CODE 42014 Caught exception : exception 42556: Extended dimension processing error",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70000004: cannot allocate enough memory%"), "ERROR_CODE 42014 Caught exception : exception 70000004: cannot allocate enough memory",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70000339: invalid number%"), "ERROR_CODE 42014 Caught exception : exception 70000339: invalid number",
    like(_raw, "%ERROR_CODE 42218 The Blending mapping is wrongly defined%"), "ERROR_CODE 42218 The Blending mapping is wrongly defined",
    like(_raw, "%ERROR_CODE 42560 Invalid default aggregation type used%"), "ERROR_CODE 42560 Invalid default aggregation type used",
    like(_raw, "%ERROR_CODE 4537 Cannot get tenant connection details%"), "ERROR_CODE 4537 Cannot get tenant connection details",
    like(_raw, "%ERROR_CODE5037\"Column does not exist in calculation View%"), "ERROR_CODE5037\"Column does not exist in calculation View",
    like(_raw, "%Failure in @ExceptionHandler com.sap.orca.remote.qbuilder.rest.exceptions.DefaultExceptionMapper%"), "Failure in @ExceptionHandler com.sap.orca.remote.qbuilder.rest.exceptions.DefaultExceptionMapper",
    like(_raw, "%liquibase.exception.DatabaseException: com.sap.db.jdbc.exceptions.JDBCDriverException: SAP DBTech JDBC: [262]: invalid query name%"), "liquibase.exception.DatabaseException: com.sap.db.jdbc.exceptions.JDBCDriverException: SAP DBTech JDBC: [262]: invalid query name",
    like(_raw, "%TrexUpdate failed%"), "TrexUpdate failed",
    like(_raw, "%Unexpected error occured: com.sap.db.jdbc.exceptions.JDBCDriverException%"), "Unexpected error occured: com.sap.db.jdbc.exceptions.JDBCDriverException",
    like(_raw, "%Unexpected error occured: java.lang.NullPointerException%"), "Unexpected error occured: java.lang.NullPointerException",
    like(_raw, "%Unexpected error occured: org.apache.catalina.connector.ClientAbortException%"), "Unexpected error occured: org.apache.catalina.connector.ClientAbortException",
    like(_raw, "%Unexpected error occured: org.springframework.orm.jpa.JpaSystemException%"), "Unexpected error occured: org.springframework.orm.jpa.JpaSystemException",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42208: Can't read the view%"), "ERROR_CODE 42014 Caught exception : exception 42208: Can't read the view",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42567: Error during formula evaluation%"), "ERROR_CODE 42014 Caught exception : exception 42567: Error during formula evaluation",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70000303: invalid DATE, TIME or TIMESTAMP value%"), "ERROR_CODE 42014 Caught exception : exception 70000303: invalid DATE, TIME or TIMESTAMP value",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70006930: attribute value is not a number%"), "ERROR_CODE 42014 Caught exception : exception 70006930: attribute value is not a number",
    like(_raw, "%ERROR_CODE 42129 Data failed to persist successfully%"), "ERROR_CODE 42129 Data failed to persist successfully",
    like(_raw, "%ERROR_CODE 42208 Can't read the view%"), "ERROR_CODE 42208 Can't read the view",
    like(_raw, "%ERROR_CODE 42227 One of the blending source queries returned an empty result%"), "ERROR_CODE 42227 One of the blending source queries returned an empty result",
    like(_raw, "%ERROR_CODE 42474 The view doesn't contain the measure%"), "ERROR_CODE 42474 The view doesn't contain the measure",
    like(_raw, "%ERROR_CODE5041 Query is not activated and will be reverted%"), "ERROR_CODE5041 Query is not activated and will be reverted",
    like(_raw, "%TrexColumnUpdate failed%"), "TrexColumnUpdate failed",
    like(_raw, "%Unexpected error occured: javax.persistence.PersistenceException: Exception [EclipseLink-4002]%"), "Unexpected error occured: javax.persistence.PersistenceException: Exception [EclipseLink-4002]",
    like(_raw, "%Unexpected error occured: org.springframework.web.client.HttpServerErrorException$ServiceUnavailable%"), "Unexpected error occured: org.springframework.web.client.HttpServerErrorException$ServiceUnavailable", 
    like(_raw, "%401 : \"Wrapper token invalid%"), "401 : \"Wrapper token invalid", 
    like(_raw, "%403 : \"Secret has not initialized%"), "403 : \"Secret has not initialized", 
    like(_raw, "%403 Forbidden: \"SuccessFactors: Forbidden%"), "403 Forbidden: \"SuccessFactors: Forbidden", 
    like(_raw, "%Cannot invoke \"com.google.gson.JsonElement.getAsString%"), "Cannot invoke \"com.google.gson.JsonElement.getAsString", 
    like(_raw, "%Connection to database server lost%"), "Connection to database server lost", 
    like(_raw, "%Error Code : 3112 User authentication service call failed%"), "Error Code : 3112 User authentication service call failed", 
    like(_raw, "%Error from HanaFileAPI: Unknown Status Code%"), "Error from HanaFileAPI: Unknown Status Code", 
    like(_raw, "%Error in GenericRemoteAPI%"), "Error in GenericRemoteAPI", 
    like(_raw, "%Error occured while extracting story execution details from Ina request%"), "Error occured while extracting story execution details from Ina request", 
    like(_raw, "%ERROR_CODE : 430 : SAP DBTech JDBC: [430]: invalidated procedure%"), "ERROR_CODE : 430 : SAP DBTech JDBC: [430]: invalidated procedure", 
    like(_raw, "%ERROR_CODE 3518 Cannot get DB Connection from DataSource%"), "ERROR_CODE 3518 Cannot get DB Connection from DataSource", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42001: Unspecified error%"), "ERROR_CODE 42014 Caught exception : exception 42001: Unspecified error", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42012: The wrong value type was requested%"), "ERROR_CODE 42014 Caught exception : exception 42012: The wrong value type was requested", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42492: The column names are empty%"), "ERROR_CODE 42014 Caught exception : exception 42492: The column names are empty", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70000129: transaction rolled back by an internal error: Allocation failed%"), "ERROR_CODE 42014 Caught exception : exception 70000129: transaction rolled back by an internal error: Allocation failed", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70000260: invalid column name%"), "ERROR_CODE 42014 Caught exception : exception 70000260: invalid column name", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70000391: invalidated view%"), "ERROR_CODE 42014 Caught exception : exception 70000391: invalidated view", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70002620: executor: plan operation failed%"), "ERROR_CODE 42014 Caught exception : exception 70002620: executor: plan operation failed", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70006944: AttributeEngine: overflow in numeric calculation%"), "ERROR_CODE 42014 Caught exception : exception 70006944: AttributeEngine: overflow in numeric calculation", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 70042900: The remote subquery results are larger than the maximum size allowed%"), "ERROR_CODE 42014 Caught exception : exception 70042900: The remote subquery results are larger than the maximum size allowed", 
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 71000591: SQLException exception 1000002: Allocation failed%"), "ERROR_CODE 42014 Caught exception : exception 71000591: SQLException exception 1000002: Allocation failed", 
    like(_raw, "%ERROR_CODE 42024 An expected attribute is missing%"), "ERROR_CODE 42024 An expected attribute is missing", 
    like(_raw, "%ERROR_CODE 42111 SQL Error :  Allocation failed%"), "ERROR_CODE 42111 SQL Error :  Allocation failed", 
    like(_raw, "%ERROR_CODE 42518 Inconsistent state. No corresponding variable in the view detected for variable%"), "ERROR_CODE 42518 Inconsistent state. No corresponding variable in the view detected for variable", 
    like(_raw, "%ERROR_CODE 42554 Invalid custom member : Formula member  uses the not existing member%"), "ERROR_CODE 42554 Invalid custom member : Formula member  uses the not existing member", 
    like(_raw, "%ERROR_CODE 42709 The selection returned more records than the limit in MaxResultRecords%"), "ERROR_CODE 42709 The selection returned more records than the limit in MaxResultRecords", 
    like(_raw, "%ERROR_CODE 6002 We failed to execute the query%"), "ERROR_CODE 6002 We failed to execute the query", 
    like(_raw, "%ERROR_CODE 6016 We found an error while executing the SQL statement.SAP DBTech JDBC: [4]: cannot allocate enough memory%"), "ERROR_CODE 6016 We found an error while executing the SQL statement.SAP DBTech JDBC: [4]: cannot allocate enough memory", 
    like(_raw, "%Exception encountered during context initialization%"), "Exception encountered during context initialization", 
    like(_raw, "%Fail to create a MDSGetResponseExecutor object%"), "Fail to create a MDSGetResponseExecutor object", 
    like(_raw, "%Failed to get the server information%"), "Failed to get the server information", 
    like(_raw, "%PreparedStatementCallback; uncategorized SQLException for SQL%"), "PreparedStatementCallback; uncategorized SQLException for SQL", 
    like(_raw, "%Unexpected error occured: com.sap.db.jdbc.exceptions.InternalReconnectException%"), "Unexpected error occured: com.sap.db.jdbc.exceptions.InternalReconnectException", 
    like(_raw, "%Unexpected error occured: com.sap.db.jdbc.exceptions.SQLNonTransientConnectionExceptionSapDB%"), "Unexpected error occured: com.sap.db.jdbc.exceptions.SQLNonTransientConnectionExceptionSapDB", 
    like(_raw, "%Unexpected error occured: com.sap.db.jdbc.exceptions.SQLTransactionRollbackExceptionSapDB%"), "Unexpected error occured: com.sap.db.jdbc.exceptions.SQLTransactionRollbackExceptionSapDB", 
    like(_raw, "%Unexpected error occured: org.springframework.jdbc.UncategorizedSQLException: PreparedStatementCallback; uncategorized SQLException%"), "Unexpected error occured: org.springframework.jdbc.UncategorizedSQLException: PreparedStatementCallback; uncategorized SQLException", 
    like(_raw, "%Unexpected error occured: org.springframework.web.client.ResourceAccessException: I/O error%"), "Unexpected error occured: org.springframework.web.client.ResourceAccessException: I/O error", 
    like(_raw, "%Unexpected error occured: org.springframework.web.client.UnknownHttpStatusCodeException%"), "Unexpected error occured: org.springframework.web.client.UnknownHttpStatusCodeException", 
    like(_raw, "%Error Code : 4121 We found an error while processing the model%"), "Error Code : 4121 We found an error while processing the model",
    like(_raw, "%404 Not Found%"), "404 Not Found",
    like(_raw, "%503 Service Temporarily Unavailable%"), "503 Service Temporarily Unavailable",
    like(_raw, "%503 We're Sorry...but the server while acting as a gateway or proxy received an invalid response from the upstream server%"), "503 We're Sorry...but the server while acting as a gateway or proxy received an invalid response from the upstream server",
    like(_raw, "%Could not commit JPA transaction%"), "Could not commit JPA transaction",
    like(_raw, "%Data receive failed%"), "Data receive failed",
    like(_raw, "%Error executing SQL%"), "Error executing SQL",
    like(_raw, "%ERROR_CODE 42014 Caught exception : exception 42432: Dimension attribute referenced in view is not defined%"), "ERROR_CODE 42014 Caught exception : exception 42432: Dimension attribute referenced in view is not defined",
    like(_raw, "%ERROR_CODE 42421 The aggregation dimension does not exist in the view%"), "ERROR_CODE 42421 The aggregation dimension does not exist in the view",
    like(_raw, "%ERROR_CODE 42432 Dimension attribute referenced in view is not defined%"), "ERROR_CODE 42432 Dimension attribute referenced in view is not defined",
    like(_raw, "%ERROR_CODE 42581 Invalid sort definition%"), "ERROR_CODE 42581 Invalid sort definition",
    like(_raw, "%ERROR-5016 Source Field learning_user_activity%"), "ERROR-5016 Source Field learning_user_activity",
    like(_raw, "%The request was rejected because the URL contained a potentially malicious String%"), "The request was rejected because the URL contained a potentially malicious String",
    like(_raw, "%while trying to invoke the method com.google.gson.JsonElement.getAsString%"), "while trying to invoke the method com.google.gson.JsonElement.getAsString",
    like(_raw, "%[129]: transaction rolled back by an internal error: Allocation failed%"), "[129]: transaction rolled back by an internal error: Allocation failed",
    1==1, error_statement)

| eval error_statement_256 = if(len(error_statement)>256, substr(error_statement,1,256), error_statement)

| eval error_statement=case(
like(error_statement_256, "%QueryObject creation failed%"), "QueryObject creation failed", 
like(error_statement_256, "%Repository: Encountered an error in repository runtime extension;Model inconsistency.%"), "Repository: Encountered an error in repository runtime extension;Model inconsistency.", 
1==1, error_statement_256)

| eval err_message = if(isnull(error_statement), substr(_raw, 1, 256), error_statement)

| eval err_type=case(
    like(_raw, "%The parallel execution limit per tenant has been exceeded:100%"), "Failed to execute query (Execution limit exceeded)", 
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
    like(_raw, "%403 Forbidden%"), "403 Forbidden", like(_raw, "%500 Internal Server Error:%"), "500 Internal Server Error", 
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
    like(_raw, "%ERROR-5008:%"), "ERROR-5008", like(_raw, "%Translations: NodeSource information not available for%"), "Translations- NodeSource information not available", 
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
    like(_raw, "%Error during processSynchronization.%"), "Error during processSynchronization", 
    like(_raw, "%The selection returned more records than the limit in MaxResultRecords%"), "The selection returned more records than the limit ", 
    like(_raw, "%Unexpected error occured: org.apache.catalina.connector.ClientAbortException: java.io.IOException: Connection reset by peer%"), "IOException: Connection reset by peer", 
    like(_raw, "%QueryObject creation failed for:%"), "QueryObject creation failed", 
    like(_raw, "%java.sql.SQLException: Connection has already been closed.%"), "SQLException: Connection has already been closed", 
    like(_raw, "%Unexpected error occured: org.springframework.orm.jpa.JpaSystemException:%"), "JpaSystemException", 
    like(_raw, "%SAP DBTech JDBC: [258]: insufficient privilege:%"), "insufficient privilege", 
    like(_raw, "%Error while writing csv export response to DB%"), "Error writing csv export response", 
    like(_raw, "%Unexpected error occured: org.springframework.web.client.ResourceAccessException:%"), "Unexpected error occured: ResourceAccessException", 
    like(_raw, "%Failed to execute an InA query:%"), "Failed to execute an InA query", 
    like(_raw, "%Empty root node list.%"), "Empty root node list", 
    1==1, "Unknown Error")

| dedup _time, component, err_message

| eval id=1 | accum id | eval count="1"

| eval date = strftime(_time, "%Y-%m-%d") 
| eval weekday = strftime(_time, "%A") 
| eval time = strftime(_time, "%H:%M") 
| eval hour = "\"" + substr(time,1,2) + "\""
| eval minute = strftime(_time, "%M")
| eval time_2 = strftime(_time + if(minute%2=0,0,(2-minute%2)*60), "%H:%M")
| eval time_3 = strftime(_time + if(minute%3=0,0,(3-minute%3)*60), "%H:%M")
| eval date_2 = strftime(_time + if(time="23:59",86400,0), "%Y-%m-%d")
| eval date_3 = strftime(_time + if(time="23:58" OR time="23:59",86400,0), "%Y-%m-%d")

| eval server = if(servername!="", servername, host)
| eval server_type = if (substr(server, 1, 2) = "pc", "PROD", if (substr(server, 1, 2) = "sc", "PREVIEW", if (substr(server, 1, 2) = "ac", "QA",if (substr(server, 1, 2) = "ps", "SALES DEMO", "OTHER") ) ) ) 

| eval correl = replace (correl, "-" , "")

| rename SFDC AS "dc"

| table id, date, weekday, time, hour, dc, server, server_type, instance, sourcetype, correl, err_type, component, err_message, count, date_2, time_2, date_3, time_3
