**POST:**`url/api/v1/challenges`<br>
**body:**
```
{
  startRange: <int>,
  endRange: <int>
}
```
returns summary of challenges from `startRange` to `endRange`.
```
{
  challengesSummary:[
    {
      ID: <int>,
      subject: <str>,
      text: <str>,
      percentOfCorrectAnswers: <int>,
      authorName: <str>,
    }
  ]
}
```

<hr>

**POST:**`url/api/v1/challenge`<br>
**body:**
```
{
  ID: <int>,
}
```
returns summary of challenges from `startRange` to `endRange`.
```
{
  ID: <int>,
  subject: <str>,
  text: <str>,
  percentOfCorrectAnswers: <int>,
  choices: []
  authorName: <str>,
}
```
<hr>

**POST**: `url/api/auth/signup`
<br>
**body:**:
```
{
    username: <str emailAddr>
    password: <str encrypted>
    name: <str>
}
```
<hr>

**POST**: `url/api/auth/signin`
<br>
**body:**:
```
{
    username: <str emailAddr>
    password: <str encrypted>
}
```
