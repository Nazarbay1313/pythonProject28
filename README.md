<h2>Hello! I am instructing you about this project.</h3>
<h3>Description and capabilities: </h3>
<p>This application is a network with an online sushi delivery store, where each user has the opportunity not only to add a product to the cart, adjust its quantity and place an order, but also to create a personal account, express their opinion in the comments on each dish and participate in discussions of new dishes! The administrator has the ability to control all orders and contact my clients via Gmail (smtp).
<br>
<p>Also, in this project I added an API section.
Through POSTMAN you can receive database objects.
Of course, I added my access rights there.
Get a token and perform operations to create/delete/update objects.</p> 
<hr>
<h3>Installation</h3>
<p>1)Download, then drag and drop the coolsite directory into your project</h4>
<p>2)Make this directory 'as sourses root'</p>
<hr>

```bash
  pip install -r requirements.txt
```
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```
```bash
  python manage.py createsuperuser
```
```bash
  python manage.py loaddata product/fixtures/tags.json
```
```bash
  python manage.py loaddata product/fixtures/products.json
```
*Make sure redis is working correctly and play with it
```bash
redis-cli ping
```
*Make sure celery is working correctly by writing the command
```bash
celery -A coolsite worker -l INFO
```
<h5>*In this project, the celery’s work involves communicating with the client by mail (on behalf of the administrator)</h5>
<hr>
<p>This project was developed by me personally! </p>
<hr>
<p>If you have questions or suggestions, please contact me through my email <b>@nazik3110@gmail.com</b></p>


