[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b58288b697964acfbbde51a0fed64935)](https://www.codacy.com/gh/bramrodrigo89/guate-coffees-shop/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bramrodrigo89/guate-coffees-shop&amp;utm_campaign=Badge_Grade)

# Guatemalan Coffees shop

Welcome!

The development of this web application was carried out as my Fourth Milestone Project for the Full-Stack Web Development Diploma from the Code Institute.

This appliction's code was written on my own using the Django Full-Stack Framework, Python, HTML5, CSS3 and JavaScript to demonstrate my personal skills and acquired knowledge from this online program. Some other libraries which are listed later on were used as well to simplify functions and styling.

The application is deployed and available in Heroku and can be accessed here:

[Guatemalan Coffees Shop](https://guatemalan-coffees-shop.herokuapp.com/)

Feel free to use it and reach out for any comments or suggestions that you may have.

**Important!** The Stripe test API is activated for this deployed app. Thus you can use the credit card number 4242-4242-4242-4242 with any expiry date in the future and any CCV to check out and cretae a fictional order.

## UX

The main objective was to create an eCommerce Web application using the Django Full Stack-Framework and a relational database to create an interactive website. The application was developed for a **fictional online commerce store** selling coffee products from Guatemala to users all over the world. Users are able to browse through the store's different products and are exposed to their specific regional facts so they can become more familiar with the country Guatemala and even engaged in supporting the different Guatemalan coffee regions by purcashing the products.

![Guatemalan Coffees Shop Desktop](documentation/images/readme_animation_compressed.gif)
![Guatemalan Coffees Shop Mobile](documentation/images/readme_animation_compressed2.gif)

**DISCLAIMER** The online store from this application is completely fictional and all the products displayed in this eCommerce store were taken from other online shops with similar scopes. The purpose of creating this store is merely for academic reasons and to demonstrate my own personal software development skills.

This application's backend allows users to store and manipulate data records on the domain. The project itself was developed using multiple apps in Django, where each app contains a potentially reusable component in the project.

The importance for this web application was identified through some User Stories like the following:
- "I am an expert coffee consumer and oftenly find myself trying new coffee products from different countries. I prefer to buy my coffee online because it is the only way I can get them more directly from coffee producers, without the commercial chain stores in-between that only sell low quality coffees."
- "I enjoy buying coffee online. To me quality and freshness are the main criteria for buying coffee. I go for those using rare coffee beans from one specific region or plantation with natural fruity cupping tones. Supermarkets nowadays only sell predesigned industrial blends that are even artificially flavored. That is why I prefer to buy them from smaller shops online that do not use artifical flavors."
- "Whenever I buy coffee, I prefer having the choice to chose the grind size myself and not someone else deciding it for me. It all depends on which coffee method I want to use: Espresso, French-press, Aeropress, etc. And whenever I want to store the coffee for a while at home, I prefer of course the whole bean presentation."
- "Sometimes I have heared Guatemala is a quality coffee producing country. I personally do not know much about the country and would be interested to find out how the coffee is produced there: I would like to see some pictures of the plantations, see local people and get to know some regional facts about where my coffee is really coming from. Sometimes people ignore what's behind the coffee that they are drinking but I believe every coffee has its own history and regional character. That's what I want to learn before I buy my coffee!"
- "Online stores websites should be straightforward and easy to use. It is very convenient being able to create an account in order to save my delivery address so I do not have to enter the same information over and over again."
- "Sometimes I find it difficult to select one product among different options. However, it becomes easy by reading some reviews of previous shoppers. It is much easier to make a choice when you can learn from other users' good or bad experiences. Reviews should always be available in any online store."

### Wireframe hosted in LucidChart

The user experience design of this application was first conceived using wireframes on LucidChart. The file is available for visualization under this following URL: 
- [LucidChart Wireframe](https://app.lucidchart.com/invitations/accept/0df8e03c-b9e6-4dc7-b94e-ecc86fe35869)

This is an image of the wireframe that can be accessed with the URL above.
![Wireframe Image](documentation/images/Wireframe.jpeg)

As observed on the wireframe, the concept of creating a base template with header and footer was considered and the extra content in the middle would be producced in different templates in Django. All sections were developed with some minor variations except for the 'Coffee Clubs' section. This remains as undeveloped because it would require many other views, models, templates and Stripe methods that are not necessary for the purpose of submission of this Milestone Project.

### Database ER Diagram

The design of the database was carried out using an Entity Relationship Diagram (ERD). The relationships between the main entities are shown in the following diagram.

![Database ER Diagram](documentation/images/Database_ER_Diagram.jpeg)

Only the main models around this application are displayed in the diagram. Secondary models are the customer inquiry and product image models that were not included directly on the diagram in order to keep a more clear visualization.

## Features
 
This application's backend allows users to store and manipulate data records on the domain. The project itself was developed using multiple apps in Django, where each app contains a potentially reusable component in the project. These are the following features already developed and implemented on this application:
 
### Existing Features
- User Authentication: Users are able to create new accounts with their personal information in order to save their data for future orders, create product reviews or send inquiries to the store.
- Google Account Registration: Users can register to the application using their personal Google accounts to create a more convenient experience. No need to enter name, last name, email address because the data is colelcted directly from the user's Google account.
- Administrator User Features: Some extra features are available only to administrator users like creating new products for the store, edit them or delete them, without having to enter the Django Administration interface.
    - Adding new products: New products can be succesfully added to the store by using the special page. However, only a main image can be added at this point. Additional images to products still have to be added through the Django Administration interface.
- Product Filters: The All Products section has some useful features to filter products by origin region, order them by price, rating or to view only those products featured as 'NEW'. These filters can be activated on the filter panel using the checkboxes or simply selecting the desired region.
- Customer Inquiry: Using the 'Contact' button accessible on every page, registered and non-registered users can send inquiries to the store by filling a short form. When the form is submitted, an email confirmation is sent to the user's email address. When users are registered, the contact information is pre-filled automatically with their contact information.
- Shopping cart: 
    - Users can add items to their shopping cart while browing through the store's products. Data is stored safely in the browser's session data so it remains even if the user closes the browser.
    - The total of the shopping cart is always displayed on top of the page next to the cart icon to remind users how much would be spent.
    - Users can edit or remove items from their cart before moving on to the checkout page.
- Checking-Out: Before doing any payment, users are requested to fill out the checkout form to include the contact information, shipping address and billing information. Registered users have the extra feature to 'Save Info' to their account so they don't need to enter it every time they want to check out.
- Profile Page: Registered users can manually save or edit their profile information for future orders, they can browse through their purchase history and check how many product reviews they have written.
    - Purchase history: On the right side of the page, users can select a previous order and see all the information stored from that order: billing information, delivery address, etc.
    - Profile information: Users are able to edit their own profile information any time on the form and using the 'UPDATE' button to save it.
- Product Reviews: Registered users can additionally rate products using a star rating system (from 1 to 5) and leave a product review about their own personal experince consuming one product. Other users can read those comments and check how the product has been previously rated with the star-rating system.
- Toasts Messagess: After a successful or unsuccessful action, users are notified accordingly with toast messages that temporarily appear on top or botton of the page without any intrusiveness to confirm or alert the user that an action has been caried out, e.g. order has been succesfully placed.
- Product Multiple Images: Products can have additional images to include visual content about the region they are produced in. This was achieved using an additional model called 'ProductImage' which contains a single image file. Products can contain more than one of these models and all the images are displayed on their respective page.
- Search Bar: Products can be searched by using the search icon on top of the page. A search bar shows up and users can enter a related term to query through the different products available. The search term is matched on the backend with any product name, description or region name and the corresponding results are returned on the products page.

In addition, these are the plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

Languages, frameworks, libraries, and other tools used to construct this project.

- HTML5
    - Language used for the different templates structure on front-end.
- Python
    - Language used for the Django framework structure, as well as the different libraries and dependencies used.
- CSS3
    - Language used for providing styles to html elements, including some overridings on MaterializeCSS.
- JavaScript
    - Language used for enhancing the users frontend experience, some form validation and form submissions.
- [Django Framework](https://www.djangoproject.com/)
    - Python-based free and open-source web framework used to building this application following the model-template-views architectural pattern.
- [jQuery](https://jquery.com/)
    - jQuery code was used to simplify HTML DOM tree traversal and manipulation, as well as event handling and CSS animation.
- [Materialize CSS](https://materializecss.com/)
    - The project uses **Materialize** to simplify giving styles and adding JavaScripts to different elements. Also it is found in the navbar construct, display cards, grid-layout, as well as other Javascript driven elements like modals, toasts, forms, etc to complement the application.
- [GitPod](https://www.gitpod.io/)
    - Online IDE for GitHub to develop code of this project.
- [GitHub](https://github.com/bramrodrigo89/)
    - Used to manage the version control of the code for this project.
- [Heroku](https://fontawesome.com/icons?d=gallery)
    - Cloud platform to deploy this application on the internet.
- [Google Material Design Icons](https://material.io/resources/icons/?style=baseline)
    - Imported different icons for different action buttons, links and items.
- [Unsplash Images](https://unsplash.com/)
    - Freely-usable images. Background images were downloaded from this source.
- [Animockup](https://animockup.com/)
    - Free animated mockup maker to create custom GIFs for this ReadMe file.
- [Codacy: Automated code reviews & code analytics](https://www.codacy.com/)
    - Automated code quality tools and static analyzers to ensure that this code maintains high quality.

## Testing

### Testing User Stories

User stories are addressed in a separate file that can be accessed [here](#).

### Problem Solving

During the development phase some bugs have been encountered which had to be solved:

1. **Problem**: Google Authentication API was producing unwanted errors when trying to create a new user while being on development environment. Continous error: 'Local host refused to connect'.
    - **Solution**: Project was deployed to Heroku and Google Auth API credentials were saved in Postgres database. When tried again in production, Google API started to function properly.

Bugs that remain unsolved:

1. **Problem**: When two or more items of the same product ID but different grind size have been added to the cart, the '+' (plus) and '-' (minus) symbols to add or substract quantities does not work properly because there are two items of the same ID, so the Javascript logic needs to be changed to include grind size in the DOM manipulation.
2. **Problem**: Additional images cannot be added when creating a new product in the Product Management feature. Only the main image is being uploaded but not the additional images. Python logic needs to be corrected to accept new images and save them as instances of the 'ProductImage' model. 

### Manual Testing

These are scenarios whose testings have not been automated, thus it is necessary to test the user stories manually:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a toast success message appears.
    5. Check that email confirmation was submitted to entered address with the subject: 'Thank you for contacting us!'.

## Deployment

The project is stored on an external repository on [GitHub](https://github.com/bramrodrigo89/guate-coffees-shop) and deployed on Heroku:
[Guatemalan Coffees Shop](https://guatemalan-coffees-shop.herokuapp.com/)

To deploy the project from its repository to Heroku, the following should be taken:

1. Log in to Heroku and select 'New' to create a new app. 
2. Depending on your location, a specific region should be chosen. On this case, United States was selected. Give a unique name to the application of your choice. Then proceed to click on 'Create App'.
3. Once the app is created, go to Settings to start adding the environmental variables. Go to 'Config Vars' and click on Reveal. 
4. Start adding the configuration variables in Key, Value pairs. In this case, 10 variables are necessary:
    4. AWS_ACCESS_KEY_ID = (edited)
    4. AWS_SECRET_ACCESS_KEY = (edited)
    4. DATABASE_URL = (edited) **Used to access Postgres Database**
    4. EMAIL_HOST_PASS = (edited) **Example: Gmail API Pass**
    4. EMAIL_HOST_USER= Email address, e.g. your_name@gmail.com
    4. SECRET_KEY = (edited) Django Key
    4. STRIPE_PUBLIC_KEY = (edited) Stripe Public Key
    4. STRIPE_SECRET_KEY = (edited) Stripe Secret Key
    4. STRIPE_WH_SECRET = (edited) Stripe Webhook Secret Key
    4. USE_AWS = True
5. Once the environment is set up, go to the 'Deploy' Tab and select 'GitHub' as deploment method. 
6. Now select this repository (bramrodrigo89/guate-coffees-shop) as the main source to connect to. 
7. Select 'Enable Automatic Deploys' on the following section from the 'master' branch. 
8. Now before the first automatic deploy, a requirements.txt file should be added to the project. It can be added by using the pip3 command: ``pip3 freeze --local ->requirements.txt`` This will indicate which are the necessary dependencies to install before the application is run. 
9. Next make sure that a Procfile is created. Simply add a new file on your main directory as 'Procfile' which should contain the command:  ``web: gunicorn guate_coffee_shop.wsgi:application`` This will tell Heroku to initiate weby dynos with the main appplication of this project called guate_coffee_shop.
10. Now it is possible to push the project to GitHub and it will automatically transfer it to Heroku for deployment.
11. Wait for the status 'Build succeeded' in Heroku 'Latest Activity' Section (around 5 minutes). Once the deploment is confirmed, go to 'Open App' to confirm the deployment. The URL can be shared now to access the application. 
12. In case there is an error and the app cannot open, go to View Logs to check the error messages. 

## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
