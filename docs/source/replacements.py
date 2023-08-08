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
    # spaces matter in some indents, so ensure they match if you use a '\n'
    "{SHEBANG}" : "#!/usr/bin/env bash \n    set -e",  # used in all the example jobscripts

}


def setup(app):
    app.add_config_value('variable_replacements', {}, True)
    app.connect('source-read', variableReplace)
