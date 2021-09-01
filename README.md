# Mlflow + Tensorflow

Prueba de concepto de un entorno para data science.

## Objetivo

* Incorporar buenas prácticas del desarrollo de software en modelos
* Dockerizar el setup, aislar los componentes y lograr encapsular lo que necesitamos
* Dependencias pip instaladas en deploy
* Versionar modelos, parametros y métricas. Lograr procesos repetibles

## Piezas

* Tensorflow
* Mlflow
* MySql
* Jupyter
* Black

## Instrucciones
* docker build --rm -t 	t-jupyter:latest .
* docker tag t-jupyter:latest t-jupyter:1.1
* docker-compose build
* docker-compose up -d --no-deps


## Detalles
* Base:
	* Usuario y contraseña: admin:admin
	* Puerto por defecto 3306
	* Container: db
	* Recomendación para entrar dbeaver	
* Los Modelos se guardan en local, en el container que ejecuta el modelo
* El jupyter tiene incorporado black, linter incluído

## TODO:
- Mejorar el readme
- Test punta a punta
- Hacer un minitutorial y algunas capturas
- Git como servidor estático?
- Subirlo a linkedin para hacer un poco de ruido

## Mejoras

* Login unificado en mlflow y jupyter
	* Posibles camino con NGINX
		* https://groups.google.com/g/mlflow-users/c/E9QW4HdS8a8
		* https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/#config
		* https://stackoverflow.com/questions/58956459/how-to-run-authentication-on-a-mlflow-server
* Porque mlflow y no otro?
* Sacar la base afuera, para tener un deploy más sólido y que pueda llevarse a prod
* Incorporar soporte para active directoy (LDAP)
* Versionado del csv
	* [https://dagshub.com/blog/data-version-control-tools/](Data version tools)
	* DVC: https://dvc.org/doc/user-guide/what-is-dvc
	* Pachyderm, mejor para pipelines? 


## Referencias

* Docker
	* Mini intro
	* Ref y videos (Pelado nerd por ejemplo y alguna cosita así)

* Mlflow: 
	* [https://bytepawn.com/getting-started-with-mlflow.html](Starting with mlflow)
	* [https://www.youtube.com/watch?v=859OxXrt_TI](MLflow: An Open Platform to Simplify the Machine Learning Lifecycle)


## Utils?

* [https://papermill.readthedocs.io/en/latest/](Papermill is a tool for parameterizing and executing Jupyter Notebooks.)
	
	
	
	
	
	
	
	
	
	
	
	
	




