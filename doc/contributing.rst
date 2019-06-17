
***************
upload_data.yml
***************

example yml configuration to upload data to cimr-d


>>> upload_data.yml
    # defined_as currently only supports 'upload'
    defined_as: upload
    # data information
    data_file:
        # very brief description of the data
        doc: >
            txt file containing results for coronary artery disease 
            genome-wide association studies of 184305 individuals of 
            mainly European, South Asian and East Asian descent.
        # where cimr-d can load the file(s) from
        location:
            url: https://zenodo.org/path/to/coronary_artery_disease_gwas.txt.gz
            md5: 23mkj312klj
    contributor:
        # name of the contributor; person submitting the data file to cimr-d
        name: YoSon Park
        # github account of the contributor
        github: ypar
        # (optional) email account of the contributor
        email: cimrroot@gmail.com
    data_info:
        # (optional) doi identifier of the published paper, if available
        citation: 10.1038/ng.3396
        # (optional) web link, if data is re-processed from a public source
        data_source: https://www.cardiogramplusc4d.org/data-downloads/
        # sample size for the study
        sample_size: 184305
        # accepted data types include: gwas, eqtl, sqtl, pqtl, tad
        data_type: gwas
        # whether data can be shared when appropriately credited / cited
        can_be_public: yes
    method:
        # method used to generate results
        name: logistic regression
        # name of the tool or programming package used
        tool: plink2
        # website link where descriptions of the tool or the package can be found
        website: https://www.cog-genomics.org/plink/2.0/


In order to submit data, ...