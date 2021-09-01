FROM tensorflow/tensorflow:latest-jupyter

MAINTAINER lbertolini <@lbertolini>


USER root

# Install de driver para SQL
RUN set -ex \
    && buildDeps=' \
        freetds-dev \
        libkrb5-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        libpq-dev \
        git'
RUN  apt-get clean 
RUN  apt-get update -yqq && apt-get upgrade -yqq 

RUN apt-get install -yqq  \
        default-libmysqlclient-dev \
        apt-utils \
        nano \
        gnupg \
        gnupg2 \ 
        gnupg1 \
        curl \
        rsync \
        netcat \
        locales \
        unixodbc-dev \
		wget \
        iputils-ping \
		sox 		
RUN apt-get install -yqq unzip
RUN apt-get purge --auto-remove -yqq $buildDeps \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base 
RUN curl https://packages.microsoft.com/keys/microsoft.asc  | tac | tac | apt-key add - 
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list 
RUN apt-get update 
RUN ACCEPT_EULA=Y apt-get install  -yqq msodbcsql17 
RUN ACCEPT_EULA=Y apt-get install  -yqq mssql-tools 
RUN apt-get clean 
RUN ls /opt/mssql-tools/bin/sqlcmd* 
RUN ln -s /opt/mssql-tools/bin/sqlcmd /usr/local/bin 
RUN sed -i -E 's/(CipherString\s*=\s*DEFAULT@SECLEVEL=)2/\11/' /etc/ssl/openssl.cnf



# Update de pip
RUN /usr/bin/python3 -m pip install --upgrade pip

# Install black as jupyter linter
RUN jupyter nbextension install "https://github.com/drillan/jupyter-black/archive/master.zip"
RUN jupyter nbextension enable jupyter-black-master/jupyter-black


# Para log al sql con ad
# curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
# sudo curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list
# sudo apt-get remove adutil
# sudo apt-get update
# sudo ACCEPT_EULA=Y apt-get install -y adutil-preview
# kinit privilegeduser@DOMAIN.COM
# adutil user create --name sqluser --distname CN=sqluser,CN=Users,DC=CONTOSO,DC=COM --password 'P@ssw0rd'
# adutil spn addauto -n sqluser -s MSSQLSvc -H sql1.contoso.com -p 5433
# adutil keytab createauto -k /container/sql1/secrets/mssql.keytab -p 5433 -H sql1.contoso.com --password 'P@ssw0rd' -s MSSQLSvc
# adutil keytab create -k /container/sql1/secrets/mssql.keytab -p sqluser --password 'P@ssw0rd!'
# chmod 440 /container/sql1/secrets/mssql.keytab
# https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-containers-ad-auth-adutil-tutorial?view=sql-server-ver15	

# bash instead of dash to use source
RUN ln -snf /bin/bash /bin/sh

# Carpeta para los modelos
RUN mkdir /mlruns
RUN chmod -R a+rwX /mlruns

#Crear usuario
RUN useradd -ms /bin/bash User

USER User
WORKDIR /home/User

# mlflow
RUN pip install --upgrade mlflow
# RUN pip install --upgrade --no-deps git+git://github.com/fchollet/keras.git 
 

# Dependencias del requeriments.txt
COPY ./conf  /home/User/conf
RUN cd /home/User/conf \
 && pip install --no-cache -r requirements.txt

# Carpeta para notebooks
RUN mkdir -p /home/User/work

# Ref: https://github.com/drillan/jupyter-black
RUN jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user
RUN jupyter nbextension enable jupyter-black-master/jupyter-black

# Para exponer el puerto y dejar el notebook sin contraseña.
EXPOSE 8888
CMD jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token= --NotebookApp.allow_origin='*'
