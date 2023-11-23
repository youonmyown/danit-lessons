## How to build, run and use:
First you must build your image:
```
docker build -t request-logging:v0.1 .
```
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/d4f7efaf-7876-4551-9414-435c423e6afd)

After the image is built, you need to run it:
```
docker run -v $(pwd)/app:/app -p 8001:8000 request-logging:v0.1
```
As you can see, our container has started:
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/67a7467a-633b-4060-9484-0d46c21ae169)

To check the functionality of our container, we can check the `messages.log` file located on the local machine in the `/app` directory
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/fcaa3af4-7b8f-49f3-9699-749ecf886fd0)

We can also go into the container and check this file in the container:
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/a80db7b5-7649-4105-bc6d-0cd830a9b0b3)
