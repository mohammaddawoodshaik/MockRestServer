# MockRestServer - Code-less

## Problem:
	In vigorpusly growing agile environments, we always expect developer and QA to work in prarallel(Talking theoritically). But in real-cases if a developer is developing a new API, till then QA has to wait/mock the API for developing his automation scripts. So why are we having this extra effort for QA to write his own Mock - Time consuming isn't it?

## Why it is time consuming?
	Well, which language you need to write your server?
	You chose to write server in Python but other guy is not confortable in it?
	Don't you need to write code to Mock the API?
	Just few from top of my mind.....

## Let's talk business:
	What if I provide you Containerized environment which feast on a JSON contains all the API info you want to Mock?, doesn't this will save the time for you. 
	Does this mean you just need to write some JSON snippet to Mock an API? - Yup, that should do it.
	How does this JSON will look like?
	```
		{
		   "name":"Mock the REST",
		   "context":{
		      "is_secured":false,
		      "is_authenticated":false,
		      "DNS":"1.1.1.1",
		      "proxy":"http://abcd.com:80",
		      "env":{
		         "IP_FAMILY":"ipv4",
		         "PORT":"8080"
		      },
		      "application":{
		         
		      }
		   },
		   "endpoints":[
		      {
		         "path":"/",
		         "method":"GET",
		         "resp":{
		            "status":200,
		            "body":"Simple response!"
		         }
		      }
		   ]
        }
	```