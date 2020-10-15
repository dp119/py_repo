



# <h3> Logstash Intro

- Different input and different outputs

- Manipulate Data

- Plugins - receive, manipulate, ship data
	Built in, community, custom plugins 

- Pipeline = input + (filter) + output

- Handles logs, XML, CSV, JSON

- Decoupled architecture
	Centralized Event processing
	
	
- To run logstash

		bin\logstash -e "input { stdin { } } output { stdout { } }"

------------------

# <h3> Basics of Logstash

Curl Command to send HTTP request

	curl -XPUT -H "Content-Type: application/json" -d "{ \"amount\": 7, \"quantity\": 3 }" http://localhost:8080


HTTP Filter for input
File filter for output

		input{
			stdin {
				codec => json
			}
			http {
				host => "127.0.0.1"
				port => 8080
			}
		}
		output{
			stdout {
				codec => rubydebug
			}
			file {
				path => "output.txt"
			}
		}
		
------------------

# <h3> Filtering Events

Example below to convert quantity value to integer with mutate plugin

		input{
			stdin {
				codec => json
			}
			http {
				host => "127.0.0.1"
				port => 8080
			}
		}
		filter{
			mutate{
				convert => { "quantity" => "integer"}
			}
		}
		output{
			stdout {
				codec => rubydebug
			}
			file {
				path => "output.txt"
			}
		}

------------------

# <h3> Logstash Execution Model

	![ansible1](/images/ansible_on_docker/logstashExecutionModel.png) 
	
	
