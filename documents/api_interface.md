## GET: `url/api/v1/challenges`<br>
#### JOB: return all available challenges from database<br>
response object:
```json
{
  "result": [
    [
      {
        "challengeID": 123,
        "challengeTitle": "some text",
        "challengeContent": "some text",
        "choices": ["choice 1", "choice 2"],
        "xp": 100
      },
    ]
  ]
}
```

```python 
for page in pages:
  for challenge in page:
    pass
```

<hr>

## GET: `url/api/v1/challenges/pages/:page_number`<br>
#### JOB: return page with specific number, page contains 10 challenges
- `challenge_content` contains first 100 char
- response object:
```json
{
  "page": 10,
  "challenges": [
      {
        "challengeID": 123,
        "challengeTitle": "some text",
        "challengeContent": "some text",
        "choices": ["choice 1", "choice 2"],
        "xp": 100
      }
  ]
}
```
```python
page = data["page"]

for challenge in data["challenges"]:
  pass
```

<hr>

## GET: `url/api/v1/challenges/:challenge_id`<br>
#### JOB: return a specific challenge, fully detailed data.
- response object:
```json
{
  "challenge_id": 124,
  "challenge_title": "some text",
  "challenge_content": "some text",
  "choices":["some text", "some text"],
  "corrects": [true, false],
  "author": 123123,
  "percent_of_corrects": 12,
  "xp": 100
}
```
```python
for key in challenge:
  item = challenge[key]
  pass
```

<hr>

## GET: `url/api/v1/challenges/answers/:challenge_id`<br>
#### JOB: response with user's answers
- response object:
```
{
  "user_answer": [true, false, false]
}
```
```typescript
type Status = 
 | 200 // all correct, [] for challenge that not answered
 | 400 // invalid ID
 | 403 // user not found - login required
 | 503 // internal error
```

<hr>

## GET: `url/api/v1/challenges/reactions/challenge_id`<br>
#### response object:
```
{
  "reaction": "like"
}
```
```typescript
types Status = 
  | 200 // all correct
  | 400 // invalid id
  | 403 // user not found - login required
  | 503 // internal error
```

<hr>

## POST: `url/api/v1/user/update`<br>
#### JOB: update the user data and return new data
- obviously if no new data is sent, the response will be current user data
- user's data will be taken from Session.
reponse object:
```json
{
    "password": "...",
    "name": "new Name"
}
```
- response:
```json
{
  "messaage": "all correct" | "problematic"
}
```
```typescript
type Status = 
  | 200 // all correct
  | 403 // login requried
  | 503 // internal error
```
#### NOTE: Client-Side should consider re-login

<hr>

## POST: `url/api/user/signup` <br>
#### JOB: add new user.
- POST body: 
```json
{
  "username": "email.com",
  "password": "..."
}
```
- response object:
```json
{
    "username": "email.com"
    "profile_image": "http:// .. /image.png"
    "is_admin": false,
    "xp": 0,
    "name": "User"
}
```
```typescript
type Status = 
  | 200 // all correct
  | 403 // invalid data
  | 503 // internal error
```

## POST: `url/api/user/login`<br>
#### JOB: login with account - update Session
- POST body:
```json
{
    "username": "User"
    "password": ".."
}
```
- response object:
```json
{
    "username": "email.com"
    "profile_image": "http:// .. /image.png"
    "is_admin": false,
    "xp": 0,
    "name": "User"
}
```
```typescript
type Status = 
  | 200 // all correct
  | 403 // nothing is correct
  | 503 // internal error
```
