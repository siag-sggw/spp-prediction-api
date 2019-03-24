# Stock Price Prediction API
This project was made for Team Project classes at the Faculty of Applied Informatics and Mathematics at the Warsaw University of Life Sciences.

## Building the project
You can build the project as a docker container or just run locally:

1. Local
   - Install requirements from requirements.txt
   - Create a config file from the example below
   - Run `python src/main.py -c <configuration file path>`

2. Docker 
   - Put the configuration file in the folder with Dockerfile (it will be in `/etc/` in your container)
   - Run the build.sh script
   - Run `docker run -it -P --name spp_api spp_api`
   
### Example Configuration file

```javascript
{
    "debug": true,
    "networking": {
        "host": "0.0.0.0",
        "port": 8000,
        "routes": {
            "index": "<your route>",
            "predictions": "<your route>",
            "parametrized_predictions": "<your route>",
            "models": "<your route>"
        }
    }
}
```
