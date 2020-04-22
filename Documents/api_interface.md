**GET:**`url/api/v1/challenges`<br>
- job: return all available challenges from database<br>
- response: 
```
[
  0: [10 challenge for first page ]
  1: [ ... for second page ]
  ...
]
```

**GET:**`url/api/v1/challenges ? page=1`<br>
- job: return 10 challenges which belongs to first page <br>
 - note: each page contains 10 challenges
- response: 
```
[ 
  0: { ... }
]
```

- page interface: 
```
[
  page: [
    {
      challeng_title: text
      challenge_content: text
      challenge_id: number
      xp: number
    }
  ]
]
```

<hr>

**POST**: `url/api/auth/signup`
<br>
- body:
```
{
    username: <str emailAddr>
    password: <str encrypted>
    name: <str>
}
```
- response: 
```
{
  message: "402 all correct." | "409 conflict"
}
```
 - status codes: 402: all correct, 409: "not correct"


**POST**: `url/api/auth/signin`
<br>
**body:**:
```
{
    username: <str emailAddr>
    password: <str encrypted>
}
```
- response: 
```
{
  message: "402 all correct." | "409 conflict"
}
```
 - status codes: 402: all correct, 409: "not correct"

