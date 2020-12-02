from django.http import HttpResponse
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=["localhost:9200"])

res = es.get(index="test_receipe", doc_type='_doc', id=1)


def index(request):
    #return HttpResponse("Elasticsearch client version: {}".format(es.info()["version"]))
    html = "<html><body>Przepis na <b> %s.</b></br></br><p><b>Składniki:</b></p><p>%s.</p><p>%s.</p><p>%s.</p></body></html>" % (res["_source"]["receipe name"], res["_source"]["ingredient one"], res["_source"]["ingredient two"], res["_source"]["receipe"])
    return HttpResponse(html)



