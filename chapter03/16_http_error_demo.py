def get_http_error(error_code):
    result = ''
    match error_code:
        case 200:
            result = "OK"
        case 400:
            result = "Bad Request"
        case 404:
            result = "Not Found"
        case _:
            result = "Unknown Error"

    return result

def main():
    pass

if __name__ == "__main__":
    main()