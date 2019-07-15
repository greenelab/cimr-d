
# Table of Contents

- [Preparing a file for data contribution](#preparing-a-file-for-data-contribution)

- [Writing a yaml file for data contribution](#writing-a-yaml-file-for-data-contribution)

- [Arguments](#arguments)
  - [defined_as](#defined-as)
  - [data_file](#data-file)
  - [contributor](#contributor)
  - [data_info](#data-info)
  - [method](#method)

- [Examples](#examples)
  - [TWAS upload example](#twas-upload-example)
  - [GWAS upload example](#gwas-upload-example)

- [Frequently asked questions](#frequently-asked-questions)



# Preparing a file for data contribution




# Writing a yaml file for a weblink-based data contribution

_cimr-d_ accepts data previously uploaded to public archives such as 
[zenodo](https://zenodo.org/).




# Arguments

## defined_as

`defined_as` variable indicates whether the contributed data is a
single text file or a tarball containing multiple files.


| argument    | description             |
|-------------|-------------------------|
| upload      | single file upload yaml |
| upload_bulk | bulk file upload yaml   |

For `upload_bulk` option, all submitted files need to be archived as 
one of the following file types: `tar`, `tar.gz`, `tar.bz2`, and `tar.xz`.
***Important***: currently, cimr-d only processes tar files with no 
directory trees. 

One may produce a tar file containing all files with suffix `_gwas.txt` within 
the directory as follows:

```bash
tar czvf gwas.tar.gz *_gwas.txt
```

Then the file must be uploaded to a repository where cimr-d can access.



## data_file

`data_file` variable is a superset of variables describing the dataset. 


| argument                    | description                                   |
|-----------------------------|-----------------------------------------------|
| doc                         | a brief description of data                   | 
| location: url               | link to data                                  |
| location: md5               | md5 sum hash to verify the file size          |
| compression                 | whether the file has been compressed          |
| keep_file_name              | whether the file name should be used          |
| output_name                 | data name, if not indicated as a file name    |
| columns: variant_id         | variant id in the format of
|                             | chromosome:position:ref:alt or 
|                             | chromosome_position_ref_alt  
| columns: variant_chromosome | 
| columns: variant_position   | 
| columns: rsnum              | 
| columns: reference_allele   | 
| columns: alternate_allele   | 
| columns: effect_allele      | 
| columns: effect_size        | 
| columns: standard_error     | 
| columns: statistic          | 
| columns: pvalue             | 
| columns: gene_id            | 
| columns: gene_chromosome    | 
| columns: gene_start         | 
| columns: gene_stop          | 
| columns: comment_0          | 




## contributor

Data contributor needs to provide a set of information regarding the 
submitting data in the `data_file` section. 

| argument    | description             |
|-------------|-------------------------|
| doc
|
|
|

```yaml
contributor:
    name: YoSon Park
    github: ypar
    email: cimrroot@gmail.com
```


## data_info 

```yaml
data_info:
    citation: 10.1016/S2213-2600(19)30055-4
    data_source: https://zenodo.org/record/3248979
    sample_size: 356083
    cases: 37846
    controls: 318237
    data_type: twas
    can_be_public: na
```

## method 


```yaml
method:
    name: logistic regression
    tool: predixcan
    website: https://github.com/hakyimlab/PrediXcan 
```


# Examples


## TWAS example
This is an example yml configuration to upload TWAS data to cimr-d:


```yaml
defined_as: upload

data_file:
    doc: >
        Shared and distinct genetic risk factors for childhood-onset 
        and adult-onset asthma; genome-wide and transcriptome-wide 
        studies using predixcan
    location:
        url: https://zenodo.org/record/3248979/files/asthma_adults.logistic.assoc.tsv.gz
        md5: 358d9ac5a7b70633b6a9028331817c7b
    compression: true
    keep_file_name: false
    output_name: ukb_adult_asthma_predixcan_logistic
    columns:
        variant_id: variant
        variant_chromosome: chr
        variant_genomic_position: pos
        rsnum: rsid
        reference_allele: ref
        alternate_allele: alt
        effect_allele: na
        effect_size: beta
        standard_error: se
        statistic: zstat
        pvalue: pval
        gene_id: na
        gene_chromosome: na
        gene_start: na
        gene_stop: na
        comment_0: converged
        
contributor:
    name: YoSon Park
    github: ypar
    email: cimrroot@gmail.com

data_info:
    citation: 10.1016/S2213-2600(19)30055-4
    data_source: https://zenodo.org/record/3248979
    sample_size: 356083
    cases: 37846
    controls: 318237
    data_type: twas
    can_be_public: na

method:
    name: logistic regression
    tool: predixcan
    website: https://github.com/hakyimlab/PrediXcan 
```



## GWAS example





## Frequently asked questions

