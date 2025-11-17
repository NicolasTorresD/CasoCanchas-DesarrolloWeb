#!/bin/bash
# Script para esperar a que MySQL esté disponible antes de iniciar FastAPI

set -e

echo "Esperando a que MySQL esté disponible..."

python -c "
import pymysql
import sys
import time
import os

max_retries = 30
retry_count = 0

while retry_count < max_retries:
    try:
        # Intentar conectar usando las variables de entorno
        db_url = os.getenv('DATABASE_URL', '')
        # Parsear la URL: mysql+pymysql://user:pass@host:port/db
        parts = db_url.split('@')[1].split('/')
        host_port = parts[0].split(':')
        host = host_port[0]
        port = int(host_port[1])
        db_name = parts[1]
        
        user_pass = db_url.split('//')[1].split('@')[0]
        user = user_pass.split(':')[0]
        password = user_pass.split(':')[1]
        
        print(f'Intento {retry_count + 1}/{max_retries}: Conectando a {host}:{port}...')
        
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            connect_timeout=5
        )
        conn.close()
        print('✓ Conexión exitosa a MySQL!')
        sys.exit(0)
    except Exception as e:
        print(f'✗ Error: {e}')
        retry_count += 1
        if retry_count < max_retries:
            time.sleep(2)
        else:
            print('✗ No se pudo conectar a MySQL después de todos los intentos')
            sys.exit(1)
"

if [ $? -eq 0 ]; then
    echo "MySQL está listo - iniciando FastAPI"
    exec uvicorn app.main:app --host 0.0.0.0 --port 8000
else
    echo "Error: No se pudo conectar a MySQL"
    exit 1
fi
