class PaginationGenerator:

    ELLIPSIS = "..."

    def generate_pagination(self, current_page, total_pages, boundaries, around):
        result_list = []

        self.validate_input(current_page, total_pages, boundaries, around)

        if boundaries * 2 >= total_pages or around * 2 >= total_pages:
            pagination = " ".join(map(str, range(1, total_pages + 1)))
            print(pagination)
            return pagination

        (
            boundaries_start_last_page,
            boundaries_end_first_page,
            around_current_page_list
        ) = self.get_base_values(current_page, total_pages, boundaries, around)

        start = self.generate_start(
            current_page,
            around,
            boundaries_start_last_page,
            around_current_page_list,
            boundaries
        )

        end = self.generate_end(
            current_page,
            around,
            boundaries_end_first_page,
            around_current_page_list,
            total_pages
        )

        result_list.extend(start)
        result_list.extend(end)

        pagination = " ".join(map(str, result_list))
        print(pagination)
        return pagination

    @staticmethod
    def validate_input(current_page, total_pages, boundaries, around):
        all_arguments = [current_page, total_pages, boundaries, around]

        for argument in all_arguments:
            if not type(argument) is int:
                raise TypeError(
                    f"All variables must be integers. "
                    f" {argument} is not an integer.")
        if total_pages <= 0:
            raise ValueError("Total pages must be positive number")
        if current_page <= 0:
            raise ValueError("Current page must be positive number")
        if current_page > total_pages:
            raise ValueError("Current page must be in range of total pages")
        if boundaries < 0:
            raise ValueError("Boundaries must be non-negative number")
        if around < 0:
            raise ValueError("Around must be non-negative number")

    @staticmethod
    def get_base_values(current_page, total_pages, boundaries, around):
        boundaries_start_last_page = boundaries
        boundaries_end_first_page = total_pages - boundaries + 1

        around_current_page_start = (
            current_page - around 
            if current_page - around > 0 
            else 1
        )
        around_current_page_end = (
            current_page + around 
            if current_page + around < total_pages 
            else total_pages
        )

        around_current_page_list = range(
            around_current_page_start, around_current_page_end + 1)
        return (
            boundaries_start_last_page,
            boundaries_end_first_page,
            around_current_page_list,
        )

    def generate_start(
        self,
        current_page,
        around,
        boundaries_start_last_page,
        around_current_page_list,
        boundaries,
    ):
        result_list = []

        if boundaries == 0 and around_current_page_list[0] == 1:
            result_list.extend(around_current_page_list)

        elif current_page - around > boundaries_start_last_page:
            result_list.extend(range(1, boundaries_start_last_page + 1))
            result_list.append(self.ELLIPSIS)
            result_list.extend(around_current_page_list)

        elif current_page - around <= boundaries_start_last_page:
            result_list.extend(range(1, around_current_page_list[0]))
            result_list.extend(around_current_page_list)

        return result_list

    def generate_end(
        self,
        current_page,
        around,
        boundaries_end_first_page,
        around_current_page_list,
        total_pages,
    ):
        result_list = []

        if boundaries_end_first_page - around_current_page_list[-1] <= 1:
            result_list.extend(
                range(around_current_page_list[-1] + 1, total_pages + 1)
            )
            return " ".join(map(str, result_list))

        elif current_page + around < boundaries_end_first_page:
            result_list.append(self.ELLIPSIS)
            result_list.extend(
                range(boundaries_end_first_page, total_pages + 1)
            )

        return result_list
