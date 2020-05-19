from locust import HttpUser, TaskSet, between, task
class ForumPage(TaskSet):
    @task(15)
    def amount(l):
        l.client.get("/amount-raised?slug=netguru-test")

    @task(1)
    def payPal(l):
        l.client.post("/create-transaction", {"email": "test@test.test", "currency": "eur", "campaign": "netguru-test", "amount": 60, "nonce": "/iDEa@g4QbB7o@*Db[82@9}T", "paymentMethod": "paypal"})

    @task(1)
    def stripe(l):
        l.client.post("/create-transaction", {"email": "test@test.com", "currency": "eur", "rememberCard": "false", "campaign": "netguru-test", "amount": 6000, "stripeToken": "%fQco>Tq{Ht}A?qcLQ!426WX", "paymentMethod": "card"})

class WebsiteUser(HttpUser):
    tasks = [ForumPage]
    wait_time = between(5.0, 9.0)
