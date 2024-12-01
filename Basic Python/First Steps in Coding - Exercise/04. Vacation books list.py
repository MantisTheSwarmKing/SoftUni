

book_pages = int(input())
hour_page_finish = int(input())
days_needed_to_finish_the_book = int(input())

total_reading_time = int( book_pages / hour_page_finish)
days_needed_to_read = int (total_reading_time / days_needed_to_finish_the_book)

print(days_needed_to_read)