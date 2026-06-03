class UsqlError(Exception):
    """Exception de base Usql"""
    pass


class ConnectionError(UsqlError):
    """Erreur de connexion"""
    pass


class AdapterError(UsqlError):
    """Adaptateur non supporté"""
    pass