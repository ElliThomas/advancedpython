curl -s --user 'api:key-026c95969d156839a4191e0ef42dce66' \
    https://api.mailgun.net/v3/sandboxd92460e91e874e62bcf8077332cfbb4a.mailgun.org/messages \
    -F from='Excited User <mailgun@sandboxd92460e91e874e62bcf8077332cfbb4a.mailgun.org>' \
    -F to=elli.thomas@gmail.com \
    -F subject='Hello' \
    -F text='Testing some Mailgun awesomness!'
