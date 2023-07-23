# a replaceall function to replace a word without using the replace() method


def replace_all(target_string, find_string, replace_string):
    return replace_string.join(target_string.split(find_string))
