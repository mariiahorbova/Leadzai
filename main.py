def generate_pagination(current_page, total_pages, boundaries, around):
    if total_pages <= 0:
        raise ValueError("Total pages must be non-negative number")
    if current_page <= 0:
        raise ValueError("Current page must be non-negative number")
    if current_page > total_pages:
        raise ValueError("Current page must be in range of total pages")
    if boundaries < 0:
        raise ValueError("Boundaries must be non-negative number")
    if around < 0:
        raise ValueError("Around must be non-negative number")
    hidden_pages = "..."
    pages = [i for i in range(1, total_pages + 1)]
    pages_start = pages[: boundaries]
    pages_end = pages[-boundaries:]
    around_current_page = pages[
        pages.index(current_page) - around: pages.index(current_page) + around + 1
    ]
    result = list(set(pages_start + around_current_page + pages_end))
    previous_page = result[0]
    result_string = str(previous_page)
    for page in result[1:]:
        if page - previous_page == 1:
            result_string += " " + str(page)
        else:
            result_string += " " + hidden_pages + " " + str(page)
        previous_page = page
    print(result_string)
    return result_string
