
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


Get your ipV4 address or your WSL ipv4 address(if you have Windows like OS) with :

```bash
  ipconfig
```

Change host value in the app/helper/.env file by your ipv4 address 

After you must build the python container with the next command (don't forget the "." at the end of the command) :

```bash
  docker build -t sneakerwolf --rm .
```

and launch it with :

```bash
  docker run -it --name sneakerwolf --rm sneakerwolf
```


RUNNING THE APP
To run the code simply run the main.py code which can be
found in the repository folder.
The settings.py initialises a connection with the data base
and sets the cnx as a global variable shared across all files.
Please make sure to only initialise the pre-fabricated inputs
to fill the database once or constraints will be violated.