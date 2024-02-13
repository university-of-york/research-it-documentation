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
    "{SHEBANG}" : "#!/usr/bin/env bash",  # used in all the example jobscripts

    # modules and versions used in the various jobscript examples for easy updating & consistency
    "{MOD_PYTHON}": "Python/3.11.3-GCCcore-12.3.0",
    "{MOD_COMPILER}": "GCC/12.3.0",
    "{MOD_R}": "R/4.2.1-foss-2022a",
    "{MOD_AMBER_CPU}": "Amber/22.3-foss-2022b-AmberTools-23.0",
    "{MOD_AMBER_GPU}": "Amber/22.4-foss-2022a-AmberTools-22.5-CUDA-11.7.0",
    "{MOD_GAUSSIAN}": "Gaussian/G16a03",
    "{MOD_MATLAB}": "MATLAB/2023b",
    "{MOD_MONGODB}": "MongoDB/4.2.3",
    "{MOD_VOXFE}": "VOX-FE/1.0-foss-2019b-Python-3.7.4",  # need to update the OpenMPI on same page
    "{MOD_RELION}": "RELION/4.0.1-foss-2021a",
    "{MOD_ALPHAFOLD_CPU}": "AlphaFold/2.3.1-foss-2022a",
    "{MOD_ALPHAFOLD_GPU}": "AlphaFold/2.3.1-foss-2022a-CUDA-11.7.0",
    "{ALPHAFOLD_DB_PATH}": "/mnt/scratch/projects/alphafold-db/",
    "{APLHPFOLD_DB_DATE}": "latest",
    "{MOD_VASP}": "VASP/5.4.4-intel-2023a",
    "{MOD_TOOLCHAIN_FOSS}": "foss/2023a",  # used in the AtChem2 example
    "{MOD_CMAKE}": "CMake/3.26.3-GCCcore-12.3.0",  # used in the AtChem2 example
    "{MOD_APPTAINER}": "Apptainer/latest",  # has own page
    "{MOD_MINICONDA}": "Miniconda3/23.5.2-0",
    "{MOD_RCLONE}": "rclone",
    "{MOD_JUPYTER}": "JupyterLab/3.1.6-GCCcore-11.2.0",
    "{MOD_MATHEMATICA}": "Mathematica/13.3.1-GCCcore-11.3.0",
    "{MOD_GUROBI}": "Gurobi/10.0.1-GCCcore-12.2.0",

}


def setup(app):
    app.add_config_value('variable_replacements', {}, True)
    app.connect('source-read', variableReplace)
