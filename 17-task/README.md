Write python script to get user ids from web site “https://jsonplaceholder.typicode.com/posts".

Script must accept three arguments:
- obligatory argument "url"
- obligatory argument "destination"
- non obligatory argument --verbose

Using library "requests" script retrieves json with users information from web site passed with argument “url", get field
"userId" from it and write it to the file from "destination" argument in json format, like:
```
{
	"User 1": "1",
	"User 2": "2",
	...
}
```
If flag --verbose is set, than script must log response from site and every userId it get from json

## Script usage:

`python main.py [-h] url destination [--verbose]`

**Example:**

`python main.py  https://jsonplaceholder.typicode.com/posts file.json --verbose`

##Screenshots:
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/32343ab3-302b-404e-b989-26d450563fe2)
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/e7c2c56d-90a0-4436-9ece-2c56576f8171)
