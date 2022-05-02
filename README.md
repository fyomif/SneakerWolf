
# Sneaker Wolf 

Chain of sneaker shops application.

Mysql it's use like database and python for the applicative layout.



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
