
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

