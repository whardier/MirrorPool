import settings
from utils import module_loader

module_loader(__name__, settings.PROXIES)
