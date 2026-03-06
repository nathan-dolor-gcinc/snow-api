from servicenow_api import ServiceNowClient
from requests_oauthlib import OAuth2Session

# ------------------------------------------------------
# Azure AD (v1) OIDC Configuration
# ------------------------------------------------------
OIDC_CLIENT_ID = "53a7fa40-7c04-4baa-828f-8959bd01d92f"
OIDC_CLIENT_SECRET = ""   # ← remains empty as provided
OIDC_SCOPE = ["openid", "profile", "upn", "email", "useraccount"]
OIDC_AUTH_URL = "https://login.microsoftonline.com/39fcdd46-89f1-432e-ba0a-120e1610adf7/oauth2/authorize"
OIDC_TOKEN_URL = "https://login.microsoftonline.com/39fcdd46-89f1-432e-ba0a-120e1610adf7/oauth2/token"
OIDC_REDIRECT_URI = "https://gcinc.service-now.com/oauth_redirect.do"

# ------------------------------------------------------
# Step 1 — OAuth2 Session Setup
# ------------------------------------------------------
oauth = OAuth2Session(
    client_id=OIDC_CLIENT_ID,
    redirect_uri=OIDC_REDIRECT_URI,
    scope=OIDC_SCOPE
)

# Step 2 — Build Authorization URL
authorization_url, state = oauth.authorization_url(
    OIDC_AUTH_URL,
    resource="https://gcinc.service-now.com"  # Required for Azure AD v1
)

print("Go to this URL and authenticate:")
print(authorization_url)

# Step 3 — User pastes the redirect URL after login
auth_response_url = input("Paste the full redirect URL after login: ")

# ------------------------------------------------------
# Step 4 — Fetch OAuth Token
# ------------------------------------------------------
token = oauth.fetch_token(
    token_url=OIDC_TOKEN_URL,
    authorization_response=auth_response_url,
    client_id=OIDC_CLIENT_ID,
    client_secret=OIDC_CLIENT_SECRET  # even if empty
)

print("Token received:")
print(token)

# ------------------------------------------------------
# Step 5 — Connect to ServiceNow using the Access Token
# ------------------------------------------------------
snow = ServiceNowClient(
    instance="gcinc",
    oauth_token=token["access_token"]
)

# ------------------------------------------------------
# Step 6 — Test Request
# ------------------------------------------------------
result = snow.table("incident").get(limit=1)
print(result)