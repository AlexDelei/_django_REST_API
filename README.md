##### Django RestAPI
I learned to craeate a rest api from scratch. This is what i understood:
<li>First: Create an endpoint -> url that will return a json response according to the http request</li>
<li>Second: Creating a backend django app for the various manipulation of incoming requests -> in this:</li>

[_backend/api](https://github.com/AlexDelei/_django_REST_API/tree/master/backend/api) : handles token verification and authentication of an endpoint url. i.e Security reasons like valid time, maximum calls for the endpoint, maximum users and the like are handled in this app.

[backend/products](https://github.com/AlexDelei/_django_REST_API/tree/master/backend/products) : performs the CRUD from the endpoint's http request.

[backend/search](https://github.com/AlexDelei/_django_REST_API/tree/master/backend/search) :  implementing a search algorithm using **algolia search**.



**Credit goes to CFE (CodingForEnterpreneurs)**
[DjangoRestAPI youtube tutorial I used](https://youtu.be/c708Nf0cHrs?si=ioePwux3GRph7PZu)
