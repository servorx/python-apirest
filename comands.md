# comandos para poder usar XAMPP

## instalar XAMPP
esto no se hace de esta forma pero yo lo tengo asi
```bash
sudo ./xampp-linux-*-installer.run
```


## instalar entorno
```bash
python3 -m venv .venv
```

## iniciar 
```bash
sudo /opt/lampp/lampp start
```

### parar
```bash
sudo /opt/lampp/lampp stop
```

## activar el entorno virtual
```bash
source .venv/bin/activate
```
a partir de ahi se puede entrar a los comandos de la terminar de mysql

## para ejecutar fastapi
```bash
uvicorn main:app --reload
```

## entrar a la pagina del api 
```bash
localhost:8000/docs
```