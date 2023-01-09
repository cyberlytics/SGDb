def escaping_string(title):
    # because the url will be with underscore -> night_reverie -> night reverie
    title = title.replace("_", " ")
    # for database-querys "(" and ")" have to be escaped
    title = title.replace("(", "\\\(")
    title = title.replace(")", "\\\)")
    return title