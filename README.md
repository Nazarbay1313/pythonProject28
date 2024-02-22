<h3>Hello! I am instructing you about this project.</h3>
<hr>
<h5>1)Download, then drag and drop the coolsite directory into your project</h5>
<h5>2)Make this directory 'as sourses root'</h5>

## Deployment

To deploy this project run

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
<br>
<h3>About this project: </h3>
<p>This application is a social network with an online sushi delivery store,
          where each user has the opportunity not only to add a product to the cart and complete an order, but also
          create a personal account, express your opinion in the comments about each dish, and participate
          in discussing new dishes!
          The administrator has the ability to control all orders and contact his clients via gmail (smtp).</p>
<br>
<p>This project was developed by me personally! </p>
<br>
<p>If you have questions or suggestions, please contact me through my email @nazik3110@gmail.com</p>

```bash
  npm run deploy
```
