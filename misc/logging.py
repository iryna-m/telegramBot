import logging

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)
logger = logging.getLogger()
# level=logging.DEBUG -  Can be changed to an other level
