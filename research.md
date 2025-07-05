### Convention

#### Template

[GET] /api/

- Abstract: Unknown
- Body: Unknown
- Returns: Unknown

#### Example

[GET] /login

- Abstract: Logs in the user
- Body:  { "username": "...", "password": "..." }
- Returns: { "token": "..." }
- Example of a different "Returns":
- Returns: { "example6": [ { "example7": 1, "example8": "example9", ... } ] }

### Research itself

#### Fully unknown endpoints:

[GET]  /api/System/GetPlatformSupportedVersions
[GET]  /api/System/EmergencyMessage
[GET]  /api/Friends/Get
[POST] /api/Accounts/CheckSteamAccount
[POST] /api/Accounts/RefreshUserDetails
[POST] /api/Accounts/GetUserStats
[POST] /api/PlayerStatus/SetPlayerStatus
[POST] /api/Messaging/GetDirectMessagesFor
[POST] /api/Matches/GetMatches

#### Endpoints

[POST] /api/Accounts/Login

- Abstract: provides username and auth token
- Body: Unknown
- Returns: {"payload": {"username": "..."}

#### Custom endpoints

[GET] /api/

- Abstract: allows the client to check if the server exists
- Returns: {"message": "..."}