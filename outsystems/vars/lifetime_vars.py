# Base LT Variables
LIFETIME_HTTP_PROTO = "https"
LIFETIME_API_ENDPOINT = "lifetimeapi/rest"
LIFETIME_API_VERSION = 2

# Applications Endpoint Variables
# Application list specific
APPLICATIONS_ENDPOINT = "applications"
APPLICATIONS_SUCCESS_CODE = 200
APPLICATIONS_EMPTY_CODE = 204
APPLICATIONS_FLAG_FAILED_CODE = 400
APPLICATIONS_FAILED_CODE = 500
# Application specific
APPLICATION_SUCCESS_CODE = 200
APPLICATION_FLAG_FAILED_CODE = 400
APPLICATION_NO_PERMISSION_CODE = 403
APPLICATION_FAILED_CODE = 404
# Application version specific
APPLICATION_VERSIONS_ENDPOINT = "versions"
APPLICATION_VERSIONS_CONTENT = "content"
APPLICATION_VERSION_SUCCESS_CODE = 200
APPLICATION_VERSIONS_EMPTY_CODE = 204
APPLICATION_VERSION_INVALID_CODE = 400
APPLICATION_VERSION_NO_PERMISSION_CODE = 403
APPLICATION_VERSION_FAILED_CODE = 404
APPLICATION_VERSION_FAILED_LIST_CODE = 500

# Deployments Endpoint Variables
# Deployment list specific
DEPLOYMENTS_ENDPOINT = "deployments"
DEPLOYMENTS_SUCCESS_CODE = 200
DEPLOYMENTS_EMPTY_CODE = 204
DEPLOYMENTS_INVALID_CODE = 400
DEPLOYMENTS_NO_PERMISSION_CODE = 403
DEPLOYMENTS_FAILED_CODE = 500
DEPLOYMENT_MESSAGE = "Automated deploy via OutSystems Pipeline"
# Deployment creation specific
DEPLOYMENT_PLAN_V1_API_OPS = "ApplicationVersionKeys"
DEPLOYMENT_PLAN_V2_API_OPS = "ApplicationOperations"
DEPLOYMENT_SUCCESS_CODE = 201
DEPLOYMENT_INVALID_CODE = 400
DEPLOYMENT_NO_PERMISSION_CODE = 403
DEPLOYMENT_NO_ENVIRONMENT_CODE = 404
DEPLOYMENT_FAILED_CODE = 500
# Deployment specific
DEPLOYMENT_GET_SUCCESS_CODE = 200
DEPLOYMENT_GET_NO_PERMISSION_CODE = 403
DEPLOYMENT_GET_NO_DEPLOYMENT_CODE = 404
DEPLOYMENT_GET_FAILED_CODE = 500
# Deployment delete specific
DEPLOYMENT_DELETE_SUCCESS_CODE = 204
DEPLOYMENT_DELETE_IMPOSSIBLE_CODE = 400
DEPLOYMENT_DELETE_NO_PERMISSION_CODE = 403
DEPLOYMENT_DELETE_NO_DEPLOYMENT_CODE = 404
DEPLOYMENT_DELETE_FAILED_CODE = 500
# Deployment status specific
DEPLOYMENT_STATUS_ENDPOINT = "status"
DEPLOYMENT_STATUS_SUCCESS_CODE = 200
DEPLOYMENT_STATUS_NO_PERMISSION_CODE = 403
DEPLOYMENT_STATUS_NO_DEPLOYMENT_CODE = 404
DEPLOYMENT_STATUS_FAILED_CODE = 500
# Deployment execution specific
DEPLOYMENT_START_ENDPOINT = "start"
DEPLOYMENT_ABORT_ENDPOINT = "abort"
DEPLOYMENT_CONTINUE_ENDPOINT = "continue"
DEPLOYMENT_ACTION_SUCCESS_CODE = 202
DEPLOYMENT_ACTION_IMPOSSIBLE_CODE = 400
DEPLOYMENT_ACTION_NO_PERMISSION_CODE = 403
DEPLOYMENT_ACTION_NO_DEPLOYMENT_CODE = 404
DEPLOYMENT_ACTION_FAILED_CODE = 500

# Environments Endpoint Variables
# Environment list specific
ENVIRONMENTS_ENDPOINT = "environments"
ENVIRONMENTS_SUCCESS_CODE = 200
ENVIRONMENTS_NOT_FOUND_CODE = 204
ENVIRONMENTS_FAILED_CODE = 500
# Environment application list specific
ENVIRONMENT_APPLICATIONS_ENDPOINT = "applications"
ENVIRONMENT_APP_SUCCESS_CODE = 200
ENVIRONMENT_APP_NOT_STATUS_CODE = 400
ENVIRONMENT_APP_NO_PERMISSION_CODE = 403
ENVIRONMENT_APP_NOT_FOUND = 404
ENVIRONMENT_APP_FAILED_CODE = 500
