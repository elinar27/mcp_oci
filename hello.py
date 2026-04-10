import oci
from mcp.server.fastmcp import FastMCP

# Inicializar FastMCP
mcp = FastMCP("OCI_Manager")

# Helper para levantar la config local de OCI
def get_oci_config():
    try:
        # Por defecto lee de ~/.oci/config y perfil DEFAULT
        return oci.config.from_file()
    except oci.config.ConfigFileNotFound:
        raise RuntimeError(
            "ERROR: No se encontró la configuración de OCI en ~/.oci/config. "
            "Ponele las credenciales correspondientes antes de usar esto."
        )

@mcp.tool()
def list_compartments(tenant_id: str) -> str:
    """
    Lista los compartimentos dentro de un Tenant (Root Compartment) en OCI.
    Requiere el OCID del tenant.
    """
    config = get_oci_config()
    identity_client = oci.identity.IdentityClient(config)
    try:
        compartments = identity_client.list_compartments(compartment_id=tenant_id).data
        if not compartments:
            return f"No se encontraron compartimentos bajo el tenant {tenant_id}."
            
        result = [f"Compartimentos encontrados ({len(compartments)}):"]
        for c in compartments:
            result.append(f"- {c.name} [Estado: {c.lifecycle_state}] OCID: {c.id}")
        return "\n".join(result)
    except Exception as e:
        return f"Error al listar compartimentos: {str(e)}"

@mcp.tool()
def list_instances(compartment_id: str) -> str:
    """
    Lista las instancias de cómputo (VMs/BareMetal) en un compartimento específico de OCI.
    """
    config = get_oci_config()
    compute_client = oci.core.ComputeClient(config)
    
    try:
        instances = compute_client.list_instances(compartment_id=compartment_id).data
        if not instances:
            return f"No hay instancias en el compartimento {compartment_id}."
            
        result = [f"Instancias encontradas ({len(instances)}):"]
        for instance in instances:
            result.append(f"- {instance.display_name} [Estado: {instance.lifecycle_state}] OCID: {instance.id}")
        return "\n".join(result)
    except Exception as e:
        return f"Error al consultar Compute en OCI: {str(e)}"

if __name__ == "__main__":
    mcp.run()
