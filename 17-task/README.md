##Task:
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
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/3394caeb-ef73-4ab5-affd-b6e520f9cec0)
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/c86f5f74-3c1f-48d1-93a1-920af6b38079)
