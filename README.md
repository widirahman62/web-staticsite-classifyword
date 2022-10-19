# Classify Word App :no_entry: [DEPRECATED]

Please note that this project is no longer under active development. If you're interested in this project, please let me know in the issue section.

# Overview
A web based application to identify word type in indonesian language. You can type a few words in input field and the app will classify the word type. This project was inspired from [liyantanto project](https://liyantanto.wordpress.com/2011/06/28/stemming-bahasa-indonesia-dengan-algoritma-nazief-dan-andriani/).

## Features

* Stemminng sentence or word in Indonesian language.
* Identify word type that already exists in the database through REST API integration.


## Usage

This project was created in docker environment. Please setup your [docker](https://docs.docker.com/get-docker/) first before running this project. After that, you can use the following command to run this project.

```shell
docker compose up -d
```

The following apps will be run on some port in your local machine.

```shell
FastAPI app: http://localhost:8081/
Static Web app: http://localhost:8080/
```

## License
Classify Word App is a free and open sourced software under [MIT license]().


