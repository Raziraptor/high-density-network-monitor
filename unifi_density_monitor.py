import json
import datetime
import logging

# Configuración básica de logs para registrar eventos
logging.basicConfig(
    filename='network_monitor.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_unifi_ap_data():
    """
    Simula una petición GET a la API del controlador UniFi de Ubiquiti.
    En un entorno real de evento, esto usaría la librería 'requests' con autenticación.
    """
    # Simulamos el JSON que regresa la API con el estado de los equipos
    return [
        {"ap_name": "AP-MainStage-01", "ip": "10.0.1.15", "clients": 145, "status": "Connected", "model": "UAP-AC-HD"},
        {"ap_name": "AP-MainStage-02", "ip": "10.0.1.16", "clients": 215, "status": "Warning_High_Load", "model": "UAP-AC-HD"},
        {"ap_name": "AP-VIP-Zone", "ip": "10.0.1.20", "clients": 45, "status": "Connected", "model": "UAP-AC-PRO"},
        {"ap_name": "AP-AccessGate", "ip": "10.0.1.25", "clients": 0, "status": "Disconnected", "model": "UAP-AC-M"}
    ]

def analyze_network_density(ap_data, client_threshold=150):
    """
    Analiza la densidad de clientes y el estado del hardware.
    """
    print(f"[{datetime.datetime.now()}] Iniciando análisis de telemetría de red...")
    
    for ap in ap_data:
        # Revisión de desconexión crítica (Hardware failure o caída de cable)
        if ap['status'] == "Disconnected":
            alert_msg = f"CRÍTICO: Equipo {ap['ap_name']} ({ap['ip']}) está fuera de línea."
            print(alert_msg)
            logging.error(alert_msg)
            # Aquí se podría integrar un envío de SMS o mensaje a Slack/Teams
            continue

        # Revisión de saturación de clientes (Alta densidad)
        if ap['clients'] >= client_threshold:
            warning_msg = f"ALERTA DE SATURACIÓN: {ap['ap_name']} superó el umbral ({ap['clients']} clientes). Considere balanceo de carga."
            print(warning_msg)
            logging.warning(warning_msg)
        else:
            info_msg = f"OK: {ap['ap_name']} operando con {ap['clients']} clientes."
            logging.info(info_msg)

if __name__ == "__main__":
    try:
        # 1. Obtener telemetría de los equipos Ubiquiti
        network_data = fetch_unifi_ap_data()
        
        # 2. Analizar y emitir alertas si es necesario (Umbral: 150 usuarios por antena)
        analyze_network_density(network_data, client_threshold=150)
        
    except Exception as e:
        print(f"Error en el sistema de monitoreo: {str(e)}")
        logging.critical(f"Falla del script: {str(e)}")
