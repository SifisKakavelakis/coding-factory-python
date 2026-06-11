def get_http_error(error_code):
    error_messages = {
        200: "OK",
        400: "Bad Request",
        404: "Not Found"
    }
    return error_messages.get(error_code, "Unknown Error")

def main():
    pass

if __name__ == "__main__":
    main()