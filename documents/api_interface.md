**GET:**`url/api/v1/challenges`<br>
- job: return all available challenges from database<br>
- response:
```
{
  result: [
  [10 challenges for first page ],
  [ ... for second page ],
  ...
  ]
}
```

<hr>

**GET:**`url/api/v1/challenges<pageNumber>`<br>
- job: return 10 challenges which belongs to first page
 - note: each page contains 10 challenges
- `challenge_content` contains first 100 char
- response:
```
{
  page: <int>,
  data: [
    { challenge 1 }
    { challenge 2 }
    ...
  ]
}
```

- page interface:
```
[
  page: [
    {
      challeng_title: text
      challenge_content: text
      isAnsweredByUser: bool
      challenge_id: number
      xp: number
    }
  ]
]
```

<hr>

**GET:**`url/api/v1/challenges/<challengeID>`<br>
- job: return a single challenge's full detail
- response:
```
{
  challengeID: <int>,
  data: [
    challengTitle: <str>
    challengeContent: <str>
    userAnswer: [<int>,...] # contains more than one number in case of multiple choice challenge
    choices:[<str>,<str>,...]
    correctChoice: [<int>,...]
    author: <str username>
    percentOfCorrectAnswer: <int>
    challenge_id: <int>
    xp: <int>
  ]
}
```

<hr>

**GET:**`url/api/v1/challengeReaction/<challengeID>`<br>
- send answers or likes
- body:
```
{
  answers: [<int>,...]
}
```
- response:
```
{
  message: "200" | "400 ID not found" | "401 answer index not valid"
}
```

<hr>

**GET:**`url/api/v1/challengeReaction/<challengeID>`<br>
- send answers or likes
- body:
```
{
  reaction: "like"
}
```

- response:
```
{
  message: "200" | "400 ID not found" | "401 reaction not valid"
}
```
<hr>

**POST:**`url/api/v1/UserUpdate/<userID>`<br>
- update the user data and return new data
- obviously if no new data is sent, the response will be current user data
body:
```
{
    password: <str encrypted>
    name: <str>
}
```
-response:
```
{
    username: <str emailAddr>
    password: <str encrypted>
    name: <str>
}
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
