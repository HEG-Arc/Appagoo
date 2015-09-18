from __future__ import absolute_import
from config.celery import app
from models import Application, Category, Content, Downloads

@app.task
def appsupdater():
    has_next = True
    page = 1
    params = {'access_token': '56c33c0815e8ee29e75b7848c81d07741ab1c8cc', 'page': page}
    query = {
        "query": {
            "_id": "54366fbaea9e191f2273c679",
            "name": "AllUpdate",
            "platform": "android",
            "query_params": {
                "sort": "title.caseinsensitive",
                "from": 0,
                "num": 100,
                "set_order": "asc",
                "content_rating": [],
                "cat_int": [],
                "downloads_lte": "",
                "downloads_gte": "",
                "only_english": True,
                "market_update_dynamic": "last_week"
            }
        }
    }
    mattersapi = requests.post("https://42matters.com/api/1/apps/query.json", params=params, data=json.dumps(query))
    print(mattersapi.url)
    mattersapi_response = mattersapi.json()
    has_next = mattersapi_response["has_next"]
    for result in mattersapi_response["results"]:
        existing_app = Application.objects.filter(package=result["package_name"])
        if existing_app is None:
            print('INSERT ' + result["package_name"])
            app = Application.create(
                package=result["package_name"],
                name=result["title"],
                version=result["version"],
                size=result["size"],
                created=result["created"],
                updated=result["updated"],
                price=result["price"],
                currency=result["currency"],
                evaluation=result["rating"],
                number_evaluations=result["number_ratings"],
                developer=result["developer"],
                iap=result["iap"],
                training=False,
                icon=result["icon"],
                market_url=result["market_url"],
                permissions=result["rating"],
                category=Category.objects.get(label=result["category"]),
                content=Content.objects.get(label=result["content_rating"]),
                downloads=Downloads.objects.get(label=result["downloads"])
            )
            app.save()
            desc = Description.create(
                text=result["description"],
                application=app.id
            )
            desc.save()
            playstoreapi = requests.post(
                "https://api.playstoreapi.com/v1.1/apps/" + app.package + "?key=753ff7a00b0acfddb2f800ac70a761a8")
            print(playstoreapi.url)
            playstoreapi_response = playstoreapi.json()

        else:
            print('UPDATE' + result["package_name"])