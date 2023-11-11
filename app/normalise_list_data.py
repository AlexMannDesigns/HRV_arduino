
def normalise_list_data(my_data: list, outlier_count: int = 3) -> None:
    if len(my_data) < 10:
        return
    for _ in range(outlier_count):
        my_data.remove(max(my_data))
        my_data.remove(min(my_data))
