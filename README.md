# ☁️ FastMCP OCI (Oracle Cloud Infrastructure)

> **⚠️ ADVERTENCIA:** Este es un proyecto de prueba. No usar para nada crítico o en entornos de producción sin revisión previa.

## 📖 Descripción

Este repositorio contiene un servidor **[Model Context Protocol (MCP)](https://modelcontextprotocol.io)** construido con la librería oficial `mcp` (implementación `FastMCP`) administrado vía `uv`. 

Su objetivo principal es exponer los recursos de tu nube en **Oracle Cloud Infrastructure (OCI)** para que puedan ser interrogados y administrados directamente por agentes de inteligencia artificial y LLMs compatibles.

---

## 🛠️ Requisitos Previos

Antes de correr el servidor, necesitás tener dos cosas fundamentales:

1. **Gestor de Paquetes (`uv`)**: Este proyecto usa `uv` de Astral para gestionar sus dependencias ultra rápido. 
2. **Credenciales de OCI**: El servidor usa el SDK de Python de Oracle, por lo que asume que tenés tu archivo de configuración en tu directorio local (`~/.oci/config`). El archivo debe verse algo así:

    ```ini
    [DEFAULT]
    user=ocid1.user.oc1..xxxx
    fingerprint=xx:xx:xx:xx:xx:xx
    tenancy=ocid1.tenancy.oc1..xxxx
    region=us-ashburn-1
    key_file=~/.oci/oci_api_key.pem
    ```

---

## 🚀 Instalación y Ejecución

1. Asegurate de tener las dependencias al día:
    ```bash
    uv sync
    ```

2. **(Opcional) Probar localmente** con el Inspector oficial de MCP:
    ```bash
    npx @modelcontextprotocol/inspector uv run hello.py
    ```

---

## 🧰 Herramientas Configuradas (Tools)

Actualmente, el servidor MCP expone las siguientes herramientas:

- `list_compartments(tenant_id)`: Devuelve la lista de subcompartimentos directos asociados al OCID de tu tenant (o compartimento raíz) con sus estados correspondientes.
- `list_instances(compartment_id)`: Inspecciona un compartimento determinado y lista todas las instancias de Compute Server (VMs y Bare Metal) activas.

---

## 🏗️ Cómo Extenderlo

Para agregar nuevas capacidades (ej: crear VCNs, listar Object Storage, apagar instancias), simplemente agregá una función con decorador `@mcp.tool()` a `hello.py` importando el cliente correspondiente de OCI (`oci.core.VirtualNetworkClient`, `oci.object_storage.ObjectStorageClient`, etc.).
