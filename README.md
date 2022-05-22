
# Sneaker Wolf 

Chain of sneaker shops application.

Mysql is used for the database and python is used for the applicative layout.



## Deployment and running

To deploy this project run

```bash
  docker-compose up
```

or just 

```bash
  docker-compose up -d
```


RUNNING THE APP
To run the code simply run the main.py code which can be
found in the repository folder.
The settings.py initialises a connection with the data base
and sets the cnx as a global variable shared across all files.
Please make sure to only initialise the pre-fabricated inputs
to fill the database once or constraints will be violated.