# Server Mirror api for Sap Apps

Url example:

| path             | type |
| ---------------- | ---- |
| /server-mirrors/ | GET  |

**parameters**
| name | type | description       |
| ---- | ---- | ----------------- |
| app  | str  | the MirrorAppName |


**example**
```url
http://<ip or domain>/<prefix if exists>/server-mirrors/?app=AppName
```

This will return a json with data:
```json
{
  "data": [
    {
      "MirrorAppName": "AppName",
      "MirrorDomainName": "domain.com",
      "MirrorId": 1,
      "MirrorIp": "192.168.1.1",
      "MirrorIsActive": true,
      "MirrorName": "App mirror Name",
      "MirrorUrl": null,
      "MirrorUrlPrefix": "/prefix",
      "URL": "https://domain.com/prefix"
    }
  ],
  "message": "Server Mirrors of AppName",
  "status": 1
}
```