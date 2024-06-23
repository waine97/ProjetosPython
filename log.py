import pdb
import logging

log_format = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(filename='teste.log', level=logging.DEBUG, filemode='w', format = log_format)

log = logging.getLogger()

log.info('Olá')
log.critical('Erro Critico')
log.error('Error nivel 40')
log.debug('Erro Grave')
log.warning('erro aviso')

