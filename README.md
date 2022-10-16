# GUAC
## Google Universal Analytics Conserver
---
On __Jul 1, 2023__ Universal Analytics properties will stop collecting and processing data. Users will still be able to access and interact with their Universal Analytics data for the coming months, however Google will be setting a specific date when existing Universal Analytics properties will no longer be available. After this future date, users will no longer be able to see Universal Analytics reports in the Analytics interface, or access Universal Analytics data via the API (or any other means).

This repository leverages the [Google Analytics Reporting API](https://developers.google.com/analytics/devguides/reporting/core/v4) (v4) as a tool to extract granular views of historical Universal Analytics data.

### GUAC Requirments
* A Google Universal Analytics property
* The Analytics Reporting API v4 [enabled on a Google Cloud Project](https://console.developers.google.com/start/api?id=analyticsreporting.googleapis.com&credential=client_key)
* A Google Cloud Project Service Account
    * _further instructions on configuring the Analytics Reporting API v4 set up can be found [here](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py)_
* `client_secrets.json` file containing the credentials to a Google Cloude Project Service Account
* A `.env` file containing both the PATH to the Service Account credentials as well as the Services Accounts Google Analytics Reporting API scopes