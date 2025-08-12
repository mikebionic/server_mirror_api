# Server Mirror API for Mobile & Desktop Apps

This API provides information about the active server mirrors for a given app. It is **required for mobile and desktop apps** to maintain reliable connectivity.
When one server becomes unreachable, the app automatically fetches the list of working server URLs (mirrors), so it can reconfigure itself without requiring:

* Rebuilding the app,
* Changing hardcoded URLs,
* Releasing app updates,
* Or forcing users to manually update their app.

This system improves reliability and user experience, especially in cases of connectivity loss or regional network issues.

## API Endpoint

| Path               | Method |
| ------------------ | ------ |
| `/server-mirrors/` | GET    |

---

## Query Parameters

| Name | Type   | Description       |
| ---- | ------ | ----------------- |
| app  | string | The MirrorAppName |

---

## Example Request

```http
GET http://<ip_or_domain>/<prefix_if_exists>/server-mirrors/?app=AppName
```

---

## Example Response

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
