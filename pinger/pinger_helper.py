
"""
Parse ping command results and save to database
"""
from pinger.models import Ping
from datetime import date


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
    return new_output


def save_results_to_db(cmd_results):
    new_ping = Ping(hostname=cmd_results["hostname"], connected=cmd_results["connected"],
                    avg_time=cmd_results["time"], date=date.today())
    new_ping.save()

