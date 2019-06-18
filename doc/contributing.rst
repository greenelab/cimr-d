
***************
upload_data.yml
***************

This is an example yml configuration to upload data to cimr-d::

    defined_as: upload
    data_file:
        doc: >
            txt file containing results for coronary artery disease 
            genome-wide association studies of 184305 individuals of 
            mainly European, South Asian and East Asian descent.
        location:
            url: https://zenodo.org/path/to/coronary_artery_disease_gwas.txt.gz
            md5: 23mkj312klj
    contributor:
        name: YoSon Park
        github: ypar
        email: cimrroot@gmail.com
    data_info:
        citation: 10.1038/ng.3396
        data_source: https://www.cardiogramplusc4d.org/data-downloads/
        sample_size: 184305
        data_type: gwas
        can_be_public: yes
    method:
        name: logistic regression
        tool: plink2
        website: https://www.cog-genomics.org/plink/2.0/

