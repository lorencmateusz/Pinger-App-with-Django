
"""
Parse ping command results and save to database
"""


def output_parser(cmd_output):
    print(cmd_output)
    next_word_index = 2
    new_output = {"hostname": "", "connected": "", "time": ""}
    output_list = cmd_output.split(" ")
    print(output_list)
    new_output["hostname"] = output_list[1]
    if int(output_list[output_list.index('Received') + next_word_index][0]) > 0:
        new_output["connected"] = True
        new_output["time"] = output_list[output_list.index("Average") + next_word_index][0]
    else:
        new_output["connected"] = False
        new_output["time"] = "n/a"
    # save_results_to_db(new_output)
    return new_output


# def save_results_to_db(ping_results):
#     db.session.add(Ping(hostname=ping_results["hostname"], connected=ping_results["connected"],
#                         avg_time=ping_results["time"], date=date.today()))
#     db.session.commit()
