"# MLOps_Assignment-2" 

To login Azure:
_az login_

To run and test Azure Function locally: 
_func host start_

To deploy application in “Azure Function app”: 
_az functionapp deployment source config-zip --resource-group </resource-group> --name </function-app-name> --src </path-to-zip-file>_

To publish the application using Azure Function Core Tools:
_func azure functionapp publish --</FunctionAppName>_
