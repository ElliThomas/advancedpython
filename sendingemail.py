import requests

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxd92460e91e874e62bcf8077332cfbb4a.mailgun.org/messages",
		auth=("api", "key-026c95969d156839a4191e0ef42dce66"),
		data={"from": "Excited User <mailgun@sandboxd92460e91e874e62bcf8077332cfbb4a.mailgun.org>",
				"to": ["elli.thomas@gmail.com", "daniel.hough@gmail.com"], 
				"subject": "Hi!",
				"text": "Hi! I'm sending this through mailgun. How amazing! Massively love you. Mwah"})
