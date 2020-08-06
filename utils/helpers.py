def export_routes(src, dst):
    """ Export all the routes to route.txt file when starting a program
    Args:
        src (str): file main.py or app.py
        dst (str): where to save the file
    """

    routes = []
    with open(src, 'r') as file:
        content = file.readlines()
        for element in content:
            element = element.rstrip()
            if "@app.route" in element:
                routes.append(element)

    with open(dst, 'w') as file:
        for element in routes:
            file.write(element + '\r\n')


def export_sockets(src, dst):
    """  Export all the sockets to socket.txt file when starting a program
    Args:
        src (str): file main.py or app.py
        dst (str): where to save the file
    """

    sockets = []
    with open(src, 'r') as file:
        content = file.readlines()
        for element in content:
            element = element.rstrip()
            if "@socketio.on" in element:
                sockets.append(element)

    with open(dst, 'w') as file:
        for element in sockets:
            file.write(element + '\r\n')
