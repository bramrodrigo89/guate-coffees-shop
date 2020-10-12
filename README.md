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
- Product Filters: The All Products section has some useful features to filter products by origin region, order them by price, rating or to view only those products featured as 'NEW'. These filters can be activated on the filter panel using the checkboxes or simply selecting the desired region.

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Animockup](https://animockup.com/)
    - Free animated mockup maker to create custom GIFs for this RedMe file.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
