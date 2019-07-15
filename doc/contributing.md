
# upload_data.yml

This is an example yml configuration to upload data to cimr-d:

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



`defined_as` variable indicates whether the contributed data is a
single text file or a tarball containing multiple files.


| argument    | variable    | description             |
|-------------|-------------|-------------------------|
| defined_as  | upload      | single file upload yaml |
| defined_as  | upload_bulk | bulk file upload yaml   |

For `upload_bulk` option, all submitted files need to be archived as 
one of the following file types: `tar`, `tar.gz`, `tar.bz2`, and `tar.xz`.
***Important***: currently, cimr-d only processes tar files with no 
directory trees. 

One may produce a tar file containing all files with suffix `_gwas.txt` within 
the directory as follows:

```bash
tar czvf gwas.tar.gz *_gwas.txt
```



Data contributor needs to provide a set of information regarding the 
submitting data in the `data_file` section. 

| argument    | description             |
|-------------|-------------------------|
| doc
|
|
|


```yaml
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
```

```yaml
contributor:
    name: YoSon Park
    github: ypar
    email: cimrroot@gmail.com
```

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

```yaml
method:
    name: logistic regression
    tool: predixcan
    website: https://github.com/hakyimlab/PrediXcan 
```


