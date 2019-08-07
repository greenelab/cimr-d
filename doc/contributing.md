
# Table of Contents

- [Contributing data with a yaml file](#contributing-data-with-a-yaml-file)

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
  - [eQTL upload yaml file example](#eqtl-upload-yaml-file-example)
  - [GWAS bulk upload yaml file example](#gwas-bulk-upload-yaml-file-example)

- [Frequently asked questions](#frequently-asked-questions)



# Contributing data with a yaml file


_cimr-d_ uses a version control system, [git](https://github.com), to 
track different versions of code and data. Experienced git users 
may skip the following section and just move on to the 
[example yaml files](#examples).

In order to contribute new data to _cimr-d_, please follow these steps:



### 0. Make a github account.

Create a github [account](https://github.com), GitHub allows 
unlimited public repositories. Git also offers 
[discounts for academics](https://education.github.com/discount_requests/new).

If you need more detailed guides, here is 
[a tutorial on using git and github for revision control](https://www.melbournebioinformatics.org.au/tutorials/tutorials/using_git/Using_Git/), 


### 1. Prepare data

Details are in the following 
[section](#preparing-a-file-for-data-contribution).

Here is an example GWAS file:

```
rsnum	variant_id	pvalue	effect_size	odds_ratio	standard_error	zscore	tss_distance	effect_allele	non_effect_allele	frequency	imputation_status	sample_size	n_cases	build
rs12565286	chr1_785910_G_C_b38	0.06295	-0.03250	NA	0.01940	-1.85954	NA	C	G	0.05628	original	54632	NA	b38
```

Any variant-based association files can be similarly formatted. 
The absolute minimum requirement for _cimr-d_ to accept the 
contributed data are following columns:

* variant_id (chrom_position_refallele_altallele_genomebuild)
* pvalue
* effect_size (may be substituted by zscore for imputed data, etc.)
* standard_error
* effect_allele
* sample_size (may be written in the yaml file)
* n_cases (may be written in the yaml file)


### 2. Prepare the contributor yaml file

Some more details are provided 
[below](#writing-a-yaml-file-for-data-contribution). 



### 3. Fork the current _cimr-d_ repository.

Here is [a help article](https://help.github.com/en/articles/fork-a-repo).


### 4. Create a pull request from the forked repository

Here is [a help article](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork)



# Preparing a file for data contribution

## File formatting

Currently _cimr-d_ expects tab-delimited plain text files that 
are compressed by gzip. Column headings may differ from the 
default _cimr-d_ example files. However, in such cases, 
column heading changes must be noted in the 
[yaml file](#conditionally-required-fields). 



# Writing a yaml file for data contribution


## Accepted weblinks

_cimr-d_ accepts data previously uploaded to public archives such as 
[zenodo](https://zenodo.org/) and [figshare](https://figshare.com/). 
_cimr-d_ will as long as the linked data contains all required 
columns and properly formatted yaml pointing to it.

However, we strongly recommend archive services in place of e.g. 
personal storage drive or box accounts, due to various reasons 
including long-term reproducibility and contributor acknowledgement. 



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
See [data_file section](#data_file) for available options. _cimr-d_ 
expects the following information for processing and integrating 
new data:


```
```


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
    citation: 10.1038/ng.2797
    data_source: http://lipidgenetics.org/
    data_type: gwas
    build: b38
    sample_size: 187167
    n_cases: na
    can_be_public: true

method:
    name: linear regression
    tool: PLINK; SNPTEST; EMMAX; Merlin; GENABEL; MMAP
    website: >-
        http://zzz.bwh.harvard.edu/plink/download.shtml; 
        https://mathgen.stats.ox.ac.uk/genetics_software/snptest/snptest.html;
        https://genome.sph.umich.edu/wiki/EMMAX;
        https://csg.sph.umich.edu/abecasis/Merlin/tour/assoc.html;
        http://www.genabel.org/sites/default/files/html_for_import/GenABEL_tutorial_html/GenABEL-tutorial.html;
        https://mmap.github.io/

contributor:
    name: YoSon Park
    github: ypar
    email: cimrroot@gmail.com

```


## eQTL upload yaml file example


Here is an example yaml file for eQTL data submission. This example 
refers to a file linked on a website, GTEx Portal. Since the file 
contains all required columns for _cimr-d_ but have different 
column names, this information has been noted in the `data_file` 
section of the yaml file. 



```yaml
data_file:
    description: >-
        Genotype-Tissue Expression (GTEx) consortium v7 data release 
        for genome-wide expression quantitative trait loci (eQTL) scans
    location:
        url: https://storage.googleapis.com/gtex_analysis_v7/single_tissue_eqtl_data/all_snp_gene_associations/Whole_Blood.allpairs.txt.gz
        md5: 09d0f87289e29f75cd735533472093c3
    columns:
        effect_size: slope
        standard_error: slope_se
        pvalue: pval_nominal
        feature_id: gene_id
        variant_id: variant_id

data_info:
    citation: 10.1038/nature24277
    data_source: http:/gtexportal.org
    data_type: eqtl
    build: b37
    sample_size: 369
    n_cases: na
    can_be_public: true

method:
    name: linear regression
    tool: fastqtl
    website: http://fastqtl.sourceforge.net/

contributor:
    name: YoSon Park
    github: ypar
    email: cimrroot@gmail.com

```


## GWAS bulk upload yaml file example

_cimr-d_ allows bulk uploads, if all data contributed share metadata. 
Specifically, compressed tarfiles are accepted. Bulk file extensions 
can be: 'tar.gz', 'tgz', 'tar.bz2', or 'tar.xz'.

For instance, two different traits, low-density lipid cholesterol and 
high-density lipid cholesterol, have been measured in the same 
cohort of people and analyzed using the same method in the below 
example. In this case, two compressed tab-delimited files may be 
prepared as one tarfile and submitted with one yaml file. 



```yaml
data_file:
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
    citation: 10.1038/ng.2797
    data_source: http://lipidgenetics.org/
    data_type: gwas
    build: b38
    sample_size: 187167
    n_cases: na
    can_be_public: true

method:
    name: linear regression
    tool: PLINK; SNPTEST; EMMAX; Merlin; GENABEL; MMAP
    website: >-
        http://zzz.bwh.harvard.edu/plink/download.shtml; 
        https://mathgen.stats.ox.ac.uk/genetics_software/snptest/snptest.html;
        https://genome.sph.umich.edu/wiki/EMMAX;
        https://csg.sph.umich.edu/abecasis/Merlin/tour/assoc.html;
        http://www.genabel.org/sites/default/files/html_for_import/GenABEL_tutorial_html/GenABEL-tutorial.html;
        https://mmap.github.io/

contributor:
    name: YoSon Park
    github: ypar
    email: cimrroot@gmail.com

```



## Frequently asked questions


### Error messages


Troubleshooting cimr processing based on error messages:



`data type is not recognized`


`no file_name provided; nothing to process`


`data_type or file_name is not recognized; nothing to do`


`no file {file_name} found for processing`


`%s rows in %s are non-numeric' % (numcol, col,)`


`the format of %s is not testable.' % (col,)`


`unknown delimiter used in variant_id`



`chromosome id needs to be checked.`
* chromosome ID contains values other than \[chr\]1-26, X, Y, M or MT.
* data is too big to be processed as a whole. Splited chunks of data
  does not contain all chromosomes


`there are no matching rs ids`


`{col} should only contain values between 0 and 1`


`gene_id column is not provided`


`variant_id column is not provided`


`rsnum column is not provided`



`effect_size column is not provided`


`standard_error column is not provided`



`pvalue column is not provided`


`file {self.outfile} cannot be written`


`no content in {self.file_name}`


`check your data_type`


`check the file link and try again`



`data_type not indicated in dir tree`


`{yaml_file} is not accessible`


`there is no data_type indicated`


`file unavailable`

