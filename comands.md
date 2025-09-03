# comandos para poder usar XAMPP

## iniciar 
```bash
sudo /opt/lampp/lampp start
```

### parar
```bash
sudo /opt/lampp/lampp stop
```

## activar el entorno virtual
```Zbash
source venv/bin/activate
```

## Entrada con MySQL
```bash
/opt/lampp/bin/mysql -u root -p
```
a partir de ahi se puede entrar a los comandos de la terminar de mysql

## conectar fastapi a la base de datos
se necesita instalar el driver de MySQL:
```bash
pip install mysqlclient
# o tambien se puede usar:
pip install pymysql
```

### instalar dependencias
```python
pip install fastapi uvicorn sqlalchemy pymysql python-jose passlib[bcrypt] pydantic
```