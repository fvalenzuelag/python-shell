# Scripts de Shell en Python

**⚠️ SOLO PARA FINES EDUCATIVOS ⚠️**

Este repositorio contiene scripts de Python que demuestran diferentes tipos de shells. Estos scripts están diseñados únicamente para fines educativos y de aprendizaje en entornos controlados y autorizados.

## Tipos de Shells

### 1. Reverse Shell (`reverse_shell.py`)
El reverse shell establece una conexión desde la máquina objetivo hacia la máquina atacante. Es útil cuando la máquina objetivo está detrás de un firewall o NAT.

**Características:**
- Se conecta a una IP y puerto específicos
- Permite ejecutar comandos remotos
- Ideal para máquinas detrás de firewalls

**Uso:**
1. Modifica la IP (HOST) y puerto (PORT) en el script
2. Ejecuta el script en la máquina objetivo
3. En la máquina atacante, usa: `nc -lvnp 1234`

### 2. Bind Shell (`bind_shell.py`)
El bind shell abre un puerto en la máquina objetivo y espera conexiones entrantes. Es útil cuando tienes acceso directo a la máquina objetivo.

**Características:**
- Escucha en un puerto específico
- Acepta conexiones entrantes
- Permite ejecutar comandos localmente

**Uso:**
1. Modifica el puerto (PORT) si es necesario
2. Ejecuta el script en la máquina objetivo
3. Conéctate usando: `nc <IP_OBJETIVO> 1234`

### 3. Web Shell (`web_shell.py`)
El web shell proporciona una interfaz web para ejecutar comandos. Es útil cuando solo tienes acceso a puertos web.

**Características:**
- Interfaz web amigable
- Ejecuta comandos a través de HTTP
- Muestra resultados formateados

**Uso:**
1. Ejecuta el script en la máquina objetivo
2. Accede desde un navegador: `http://<IP_OBJETIVO>:8000`

## Requisitos
- Python 3.x
- Permisos de administrador (en algunos casos)

## Advertencia
Estos scripts son únicamente para fines educativos y de aprendizaje. No los uses en sistemas no autorizados o en entornos de producción. El uso malicioso de estos scripts puede ser ilegal y resultar en consecuencias legales.

## Responsabilidad
El autor no se hace responsable del uso indebido de estos scripts. El usuario es el único responsable de sus acciones y debe asegurarse de tener los permisos necesarios antes de usar estos scripts. 