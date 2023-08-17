# functions using lichess api

# gather response from api request
def gather_rating(api_response, type_rating):
    if api_response.status_code == 200:
        json_return = api_response.json()
        print(json_return)
        print(json_return['id'])
        format_data(type_rating, json_return)
    else:
        print("NIE OK")


# format data to be sent by sms
def format_data(rating_type, json_info):
    rating_text = ''

    # add greeting for user
    rating_text += f"Hello {json_info['username']}!\n"

    # parsing json into strings to put them in a message
    if rating_type == 'all':
        for type in json_info['perfs']:
            try:
                rating_text += f"{type.title()} rating: {json_info['perfs'][type]['rating']}, progress: {json_info['perfs'][type]['prog']}.\n"
            except:
                pass
        print(rating_text)
    else:
        for type in rating_type:
            try:
                rating_text += f"{type.title()} rating: {json_info['perfs'][type]['rating']}, progress: {json_info['perfs'][type]['prog']}.\n"
            except:
                print(f'Wrong name of type. {type.title()} does not exist in your lichess account.')

        print("Printujemy tylko kilka")

        # print test sms message
        print(rating_text)
