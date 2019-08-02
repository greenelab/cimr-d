
# Table of Contents

- [Preparing a file for data contribution](#preparing-a-file-for-data-contribution)

- [Writing a yaml file for data contribution](#writing-a-yaml-file-for-data-contribution)
  - [Accepted weblinks](#accepted-weblinks)
  - [Required fields](#required-fields)
  - [Conditionally required fields](#conditionally-required-fields)
  - [Optional fields](#optional-fields)
  - [Basics on yaml file formatting](#basics-on-yaml-file-formatting)

- [Arguments](#arguments)
  - [data_file](#data_file)
  - [data_info](#data_info)
  - [method](#method)
  - [contributor](#contributor)

- [Examples](#examples)
  - [GWAS upload yaml file example](#gwas-upload-yaml-file-example)
  - [GWAS bulk upload yaml file example](#gwas-bulk-upload-yaml-file-example)

- [Frequently asked questions](#frequently-asked-questions)



# Preparing a file for data contribution


Here is an example GWAS file:

```
rsnum	variant_id	pvalue	effect_size	odds_ratio	standard_error	zscore	tss_distance	effect_allele	non_effect_allele	frequency	imputation_status	sample_size	n_cases	build
rs12565286	chr1_785910_G_C_b38	0.06295	-0.03250	NA	0.01940	-1.85954	NA	C	G	0.05628	original	54632	NA	b38
```




# Writing a yaml file for a weblink-based data contribution


## Accepted weblinks

_cimr-d_ accepts data previously uploaded to public archives such as 
[zenodo](https://zenodo.org/).



## Required fields

Following keys are required for _cimr-d_ processing:

```yaml
data_file:
    location:
        url: https://location.of.contributed.data
        md5: md5sumhashforfile

data_info:
    citation: doinumber
    data_type: datatype
    build: genomebuild
    sample_size: samplesize
    n_cases: ncases
    can_be_public: true

method:
    name: methodname
    tool: toolname
    website: toolreference

```

## Conditionally required fields

`data_file: columns:` fields are required if the submitted data 
contains column names different from the default _cimr_ variables.


## Optional fields

For most non-required fields [as seen in examples below](#examples), 
`na` (as in `not available`) is an acceptible value. Alternatively, 
if there's no information available for a given non-required field, 
such variables may be omitted.


## Basics on yaml file formatting

Example cimr submission files are provided [below](#examples). 
[YAML refers to a human friendly data serialization standard](https://yaml.org/). 
Detailed documentation can be found 
[elsewhere](https://yaml.org/spec/1.2/spec.html). 

YAML uses strict syntactically significant newlines and indentations.
In case of cimr data-submission yaml form, most fields expect values 
of one word or a short string (such as a website link). However, for 
longer lines as in `data_file: description`, multi-line strings can be 
indicated with `>-` next to the key as shown in 
[an example](#gwas-upload-yaml-file-example).


# Arguments


## data_file

`data_file` key is a superset of keys describing the dataset.


| argument                    | description                              |
|-----------------------------|------------------------------------------|
| description                 | a brief description of data              | 
| location: url               | link to data                             |
| location: md5               | md5 sum hash to verify the file size     |
|                             |                                          |
| columns: variant_id         | variant id in the format of              |
|                             | chromosome_position_ref_alt or           |
|                             | chromosome_position_ref_alt_build        |
| columns: variant_chrom      | variant chromosome id                    |
| columns: variant_pos        | variant genomic position                 |
| columns: rsnum              | variant rs id                            |
| columns: ref                | variant reference allele                 |
| columns: alt                | variant alternate allele                 |
| columns: effect_allele      | effect allele for statistic              |
| columns: non_effect_allele  | non-effect allele for statistic          |
| columns: effect_size        | effect size / beta coefficient           |
| columns: standard_error     | standard error of the effect size        |
| columns: zscore             | zscore                                   |
| columns: pvalue             | pvalue                                   |
| columns: feature_id         | feature id, if applicable (e.g. gene)    |
| columns: feature_chrom      | chromosome id, if applicable             |
| columns: feature_start      | starting genomic position, if applicable |
| columns: feature_stop       | stopping genomic position, if applicable |
| columns: imputation_status  | imputation status                        |
| columns: frequency          | effect allele frequency                  |
| columns: tss_distance       | distance to tss                          |
| columns: ma_samples         | count of samples with minor alleles      |
| columns: maf                | minor allele frequency                   |
| columns: comment_0          | other info (e.g. did statistic converge?)|



## data_info 

Data information provided in `data_info` is used to generate citation 
and metadata information used for analyses and acknowledgements.


| argument      | description                                          |
|---------------|------------------------------------------------------|
| citation      | publication or data doi, if applicable               |
| data_source   | (permenant) link to the original data, if applicable |
| sample_size   | sample size of the study                             |
| n_cases       | number of cases, if applicable (e.g. binary trait)   |
| data_type     | data_type (e.g. twas, gwas, eqtl, etc.)              |
| can_be_public | whether the data can be posted publicly via cimr-d   |



## method 

Method details can be listed here.

| argument  | description                    |
|-----------|--------------------------------|
| name      | name of the method used        |
| tool      | name of the tool used          |
| website   | website link for the tool used |




## contributor

Contributor information is optional but recommended.


| argument    | description                         |
|-------------|-------------------------------------|
| name        | name of the contributor             |
| github      | github user name of the contributor |
| email       | e-mail address of the contributor   |




# Examples


## GWAS upload yaml file example
This is an example yml configuration to upload GWAS data to cimr-d:


```yaml
data_file:
    # brief description of the data
    description: >-
        Global Lipid Genetics Consortium GWAS results for high-density 
        cholesterol levels
    # where cimr-d can load the file(s) from
    location:
        url: https://zenodo.org/record/3338180/files/HDL_Cholesterol.txt.gz
        md5: 2b28816a0a363db1a09ad9a6ba1a6620
    columns:
        variant_id: panel_variant_id
        variant_chrom: chromosome
        variant_pos: position
        rsnum: variant_id
        ref: na
        alt: na
        effect_allele: effect_allele
        non_effect_allele: non_effect_allele
        inc_allele: na
        inc_afrq: na
        effect_size: effect_size
        standard_error: standard_error
        zscore: zscore
        pvalue: pvalue
        feature_id: na
        feature_chrom: na
        feature_start: na
        feature_stop: na
        imputation_status: imputation_status
        frequency: na
        tss_distance: na
        ma_samples: na
        maf: na
        comment_0: na

data_info:
    # doi identifier of the published paper, if available
    citation: 10.1038/ng.2797
    # original weblink, if data is re-processed from a public source
    data_source: http://lipidgenetics.org/
    data_type: gwas
    build: b38
    sample_size: 187167
    n_cases: na
    can_be_public: true

method:
    # method used to generate results
    name: linear regression
    # name of the tool or programming package used
    tool: PLINK; SNPTEST; EMMAX; Merlin; GENABEL; MMAP
    # website link where descriptions of the tool or the package can be found
    website: >-
        http://zzz.bwh.harvard.edu/plink/download.shtml; 
        https://mathgen.stats.ox.ac.uk/genetics_software/snptest/snptest.html;
        https://genome.sph.umich.edu/wiki/EMMAX;
        https://csg.sph.umich.edu/abecasis/Merlin/tour/assoc.html;
        http://www.genabel.org/sites/default/files/html_for_import/GenABEL_tutorial_html/GenABEL-tutorial.html;
        https://mmap.github.io/

contributor:
    # name of the contributor; person submitting the data file to cimr-d
    name: YoSon Park
    # github account of the contributor
    github: ypar
    # email account of the contributor
    email: cimrroot@gmail.com

```



## GWAS bulk upload yaml file example


```yaml
data_file:
    # brief description of the data
    description: >-
        Global Lipid Genetics Consortium GWAS results for high-density 
        cholesterol levels
    # where cimr-d can load the file(s) from
    location:
        url: https://zenodo.org/record/3345991/files/gwas_hdl_ldl.tar.gz
        md5: eccbd3b5b6ff87e78063321846b78dfa
    columns:
        variant_id: panel_variant_id
        variant_chrom: chromosome
        variant_pos: position
        rsnum: variant_id
        ref: na
        alt: na
        effect_allele: effect_allele
        non_effect_allele: non_effect_allele
        inc_allele: na
        inc_afrq: na
        effect_size: effect_size
        standard_error: standard_error
        zscore: zscore
        pvalue: pvalue
        feature_id: na
        feature_chrom: na
        feature_start: na
        feature_stop: na
        imputation_status: imputation_status
        frequency: na
        tss_distance: na
        ma_samples: na
        maf: na
        comment_0: na
        
data_info:
    # doi identifier of the published paper, if available
    citation: 10.1038/ng.2797
    # original weblink, if data is re-processed from a public source
    data_source: http://lipidgenetics.org/
    data_type: gwas
    build: b38
    sample_size: 187167
    n_cases: na
    can_be_public: true

method:
    # method used to generate results
    name: linear regression
    # name of the tool or programming package used
    tool: PLINK; SNPTEST; EMMAX; Merlin; GENABEL; MMAP
    # website link where descriptions of the tool or the package can be found
    website: >-
        http://zzz.bwh.harvard.edu/plink/download.shtml; 
        https://mathgen.stats.ox.ac.uk/genetics_software/snptest/snptest.html;
        https://genome.sph.umich.edu/wiki/EMMAX;
        https://csg.sph.umich.edu/abecasis/Merlin/tour/assoc.html;
        http://www.genabel.org/sites/default/files/html_for_import/GenABEL_tutorial_html/GenABEL-tutorial.html;
        https://mmap.github.io/

contributor:
    # name of the contributor; person submitting the data file to cimr-d
    name: YoSon Park
    # github account of the contributor
    github: ypar
    # email account of the contributor
    email: cimrroot@gmail.com

```



## Frequently asked questions

