"# MLOps_Assignment-2 #" 

To login Azure:
az login

To run and test Azure Function locally: 
func host start

To deploy application in “Azure Function app”: 
az functionapp deployment source config-zip --resource-group <resource-group> --name <function-app-name> --src <path-to-zip-file>

To publish the application using Azure Function Core Tools:
func azure functionapp publish <FunctionAppName>
