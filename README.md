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