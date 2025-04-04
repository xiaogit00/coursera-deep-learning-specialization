def custom_sink(message):
    record = message.record
    function = record['function']
    message = record['message']
    extra = record['extra']
    if extra.get("format") == "function_inputs":
        args_strings = []
        for k, v in extra.items():
            if k == "format": continue
            args_log = f"\n{k}: \n {v} \n"
            args_strings.append(args_log)
        log_message = f"\n-----{message}" + "".join(args_strings)
    else:
        log_message = f"{function}:: {message} \n"
    with open("file.log", "a") as file:
        file.write(log_message)