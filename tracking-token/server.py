from sharedicom import Serversharedicom


if __name__ == "__main__":
    server = Serversharedicom('/media/erjulioaguiar/DFE1-F19A/DICOM_TCIA', '10.62.9.185', 5000)

    # Params:
    # hprovider: healthcare provider to register dicom
    # typeExam: Type exam whithin dicom
    #server.registerDicom('USP', 'Radiography')

    # let available server for transfer dicom
    server.start_transfer_dicom()
