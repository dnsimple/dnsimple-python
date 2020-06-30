def return_list_of(cls, data):
    """
    Returns a list of instances of the class type found in the response.

    :param cls: class
        The class type we want to instantiate
    :param data: list
        The data containing the list of the dictionaries we want to return as objects
    :return:
        A list of objects of the type specified found in the response
    """
    return [cls(x) for x in data]


def attach_attributes_to(obj: object, data: object) -> object:
    """
    Attaches attributes to an object

    :param obj: object
        The object (class) to attach the attributes to
    :param data: dict
        A dictionary (taken from the 'data' attribute in the json payload coming from the response) with the
        attributes and their values.
    :return: None
    """
    for index, attribute in enumerate(list(data)):
        setattr(obj, str(attribute), data[attribute])


def prepare_params(sort=None, filter=None, params=None):
    """
    Prepares the different parameters we want to send as the query in a request

    :param sort: str
        The sorting (used in list commands issued to the DNSimple API)
    :param filter: dict
        The filtering (used in list commands issued to the DNSimple API)
    :param params: dict
        Any other params we want to send in the query
    :return:
    """
    if params is None:
        params = {}
    if sort is not None:
        params = {**params, **{'sort': sort}}
    if filter is not None:
        params = {**params, **filter}
    return params
