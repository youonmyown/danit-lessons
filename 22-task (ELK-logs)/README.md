## ELK Stack local machine logging

This repository was used as a basis:
https://github.com/deviantony/docker-elk/

First we need to clone the repository:
```
git clone https://github.com/deviantony/docker-elk.git

cd docker-elk/
```

Then, initialize the Elasticsearch users and groups required by docker-elk by executing the command:
```
docker-compose up setup
```
If everything went well and the setup completed without error, start the other stack components:
```
docker compose up
```
If everything starts without errors, we can execute `docker compose down` and go to the settings:

```
nano logstash/config/logstash.yml
```
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/8b0de516-5229-4ee2-840d-fbc9226ebdae)
```
nano ../pipeline/logstash.conf
```
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/1f639dc5-7c19-487e-baef-e556b5478a52)

Next we need to install Filebit on the local machine by following [these instructions](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation-configuration.html)
After installation we need to change the Filebit configuration file: 
```
nano /etc/filebeat/filebeat.yml
```
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/f2ccc3c5-fbb8-4e0d-99d2-04a29ffd7acf)

Afterwards we need to return to the folder with the cloned repository and run docker compouse:
```
cd /path_to_docker-elk_folder

docker compose up
```
![image](https://github.com/youonmyown/danit-lessons/assets/138362837/6525501f-97a7-4507-b031-71757f211ef3)

After a few minutes we will be able to see the logs that appeared on the local machine in the /var/log directory:

![image](https://github.com/youonmyown/danit-lessons/assets/138362837/43b79ba4-9aa2-4a1f-8af6-7c99aaf05429)

