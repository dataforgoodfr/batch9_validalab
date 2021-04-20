from graphio import NodeSet

def upload_abe_infoservice_node(path_of_file):
    '''
    This function is used to upload the list of websites scraped from https://www.abe-infoservice.fr/
    :param path_of_file:
    :return:
    '''
    log.info('Adding the abe_infoservice list of websites to websites Node to the database')

    abe_infoservice_node = NodeSet(['Website'] ,
                            merge_keys=[]),

    # MERGE
                            {'output_uuid': abe_infoservice_node.uuid,
                            'source': 'https://www.abe-infoservice.fr/'})
    abe_infoservice_metadata = ['source: https://www.abe-infoservice.fr/']