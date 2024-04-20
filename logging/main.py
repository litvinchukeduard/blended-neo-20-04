import logging
# import mylib
logger = logging.getLogger(__name__)
FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(filename='myapp.log', level=logging.INFO, format=FORMAT)


def main():
    value_one = int(input(">>>"))
    value_two = int(input(">>>"))
    try:
        value_one / value_two
    except ZeroDivisionError:
        logger.error("Zero division")
    logger.info(value_one / value_two)
    logger.info('Finished')

if __name__ == '__main__':
    main()