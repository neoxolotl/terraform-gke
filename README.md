# terraform-gke

Crear un script bash o makefile, que acepte parámetros (CREATE, DESTROY y OUTPUT) 

## Requerimientos

- Terraform versión v0.12.26.
- Cuenta en GCP.
- Crear una cuenta de servicios y crear una clave del tipo JSON.

### Cuenta de Servicio 

- gcr: correspondiente al container registry GCP
- gke: Modulo de kubernetes engine GCP


## Modo de Uso

1. Descargue al raiz de este proyecto su archivo su archivo de clave JSON 
2. Ejecute el script con los siguientes parametros 

./start CREATE credentials project_id gcp_region

Ejemplos: 

Para crear cluster 

./start CREATE archivo_del_proyecto1122 proyecto1122 us-central1 

Para destruir cluster 

./start DESTROY 

Para ver su salida 

./start OUTPUT http://Ip_del_Cluster  (tendra una salida "Hello World")

./start OUTPUT http://Ip_del_Cluster/square/2 (tendrá como resultado el cuadrado del numero 2)

./start OUTPUT http://Ip_del_Cluster/greetings (tendrá hello World + Hostname) 

## Configuración

Los siguientes parámetros son los que se pueden usar en el flujo.

  *Todos son obligatorios*

Parámetro | Descripción
--------- | -----------
`project_id` | ID del proyecto en GCP
`gcp_region` | Region de GCP en la que se va a trabajar
`credentials` | Indica nombre del archivo .JSON de credenciales 