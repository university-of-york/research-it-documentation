def variableReplace(app, docname, source):
    """
    Takes the source on rst and replaces all the needed variables declared on
    variable_replacements structure
    """
    result = source[0]
    for key in app.config.variable_replacements:
        result = result.replace(key, app.config.variable_replacements[key])
    source[0] = result


# Add the needed variables to be replaced either on code or on text on the next
# dictionary structure.
variable_replacements = {
    # can have '\n' for multi lines
    # spaces matter in some indents eg  in a 'code-block', so ensure they match if you use a '\n'
    # an indent is '4 spaces'

    # 'shebang' at the start of all the jobscripts
    "{SHEBANG}" : "#!/usr/bin/env bash \n    set -e",  # used in all the example jobscripts

    # modules and versions used in the various jobscript examples for easy updating & consistency
    "{MOD_PYTHON}": "lang/Python/3.10.8-GCCcore-12.2.0",
    "{MOD_COMPILER}": "compiler/GCC/12.2.0",
    "{MOD_R}": "lang/R/4.2.1-foss-2022a",
    "{MOD_AMBER_CPU}": "chem/Amber/22.3-foss-2022b-AmberTools-23.0",
    "{MOD_AMBER_GPU}": "chem/Amber/16-foss-2018a-AmberTools-17-CUDA",
    "{MOD_GAUSSIAN}": "chem/Gaussian/G16a03",
    "{MOD_MATLAB}": "math/MATLAB/2022a",
    "{MOD_MONGODB}": "tools/MongoDB/4.2.3",
    "{MOD_VOXFE}": "bio/VOX-FE/2.0.1-foss-2017b",
    "{MOD_RELION}": "bio/RELION/4.0.1-foss-2021a",
    "{MOD_ALPHAFOLD_CPU}": "bio/AlphaFold/2.1.2-foss-2021a",
    "{MOD_ALPHAFOLD_GPU}": "bio/AlphaFold/2.3.1-foss-2022a-CUDA-11.7.0",
    "{ALPHAFOLD_DB_PATH}": "/mnt/bb/striped/alphafold_db/",
    "{APLHPFOLD_DB_DATE}": "20230518",
    "{MOD_VASP}": "phys/VASP/5.4.4-intel-2019a",
    "{MOD_TOOLCHAIN_FOSS}": "toolchain/foss/2022b",  # used in the AtChem2 example
    "{MOD_CMAKE}": "devel/CMake/3.24.3-GCCcore-12.2.0",  # used in the AtChem2 example
    "{MOD_APPTAINER}": "tools/Singularity/3.5.3",  # has own page
    "{NAME_APPTAINER}": "singularity",

}


def setup(app):
    app.add_config_value('variable_replacements', {}, True)
    app.connect('source-read', variableReplace)
