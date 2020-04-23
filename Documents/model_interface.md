User:
```
{
  name: text, default: (some random name, like "USER XSRAT");
  email: text, required: true;
  password: text (encrypted);
  xp: number, default: 0;
  is_admin: boolean, default: false;
}
```  
<hr />

Challenge: 
 ```
 {
  author: int (user ID), required: true;
  title: text, required: true;
  content: text (md format), requried: true;
  choices: array -> ["choice 1", "choice 2", "choice 3"], required: true;
  answers: array -> (index of correct choice) -> [0, 2]
 }
 ```
