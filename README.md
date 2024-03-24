# OwlBookstore

Embark on a journey through the captivating world of literature with OwlBookstore - your ultimate destination for all things books and comics! Our platform is meticulously crafted to provide you with an unparalleled experience in discovering, storing, and exploring a vast collection of literary treasures.

Whether you're an avid reader or a casual enthusiast, OwlBookstore is your go-to companion for all your literary adventures. Delve into a diverse array of genres, from gripping novels to thrilling comics, and unlock the magic of storytelling at your fingertips.

Join our vibrant literary community today and immerse yourself in a world of endless possibilities. With our intuitive features and user-friendly interface, navigating through our extensive catalog is a breeze. Uncover hidden gems, rediscover timeless classics, and connect with fellow book lovers who share your passion for reading.

At OwlBookstore, it's not just about selling books and comics; it's about fostering a love for literature and igniting the imagination of readers worldwide. Start your journey with us today and let the pages of our books and comics transport you to new and exciting realms. Happy reading!

![Home Screen](/media/sreenshots_webp/owl_bookstore_responsive.webp)

[OwlBookstore's live website here](https://owl-bookstore-2a747a64a0a9.herokuapp.com/)

---

## Table of Contents

### [User Experience](#user-experience-ux)

- [Project Goals](#project-goals)
- [Agile Methodology](#agile-methodology)
- [Target Audience](#target-audience)
- [First time user](#first-time-user)
- [Registered user](#registered-user)
- [Admin user](#admin-user)

### [Design](#design-1)

- [Color Scheme](#color-scheme)
- [Recipe Images](#recipe-images)
- [Wireframes](#wireframes)
- [Database Scheme](#database-scheme)
- [Data Model](#data-models)
- [User Journey](#user-journey)

### [Security Features](#security-features-1)

- [User Authentication](#user-authentication)
- [LoginRequiredMixin](#loginrequiredmixin)
- [CSRF Protection](#csrf-protection)
- [Custom Views Security Measures](#custom-views-security-measures)
- [Form Validation](#form-validation)

### [Features](#features-1)

- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)

### [Technologies Used](#technologies-used-1)

- [Languages Used](#languages-used)
- [Databases Used](#databases-used)
- [Frameworks Used](#frameworks-used)
- [Programs Used](#programs-used)

### [Deployment and Local development](#deployment-and-local-development-1)

- [Local Development](#local-development)
- [ElephantSQL Database](#elephantsql-database)
- [Cloudinary](#cloudinary)
- [Heroku Deployment](#heroku-deployment)

### [Testing](#testing-1)

### [References](#references-1)

- [Docs](#docs)
- [Content](#content)
- [Acknowledgements](#acknowledgements)

---

## User Experience (UX)

Embark on an immersive literary journey with OwlBookstore's E-commerce Platform, where the world of books and comics awaits your exploration. Our platform offers a seamless and enriching user experience, ensuring effortless browsing, purchasing, and engagement with your favorite reads. Dive into a treasure trove of literary delights, where every click opens the door to new adventures.

OwlBookstore's E-commerce Platform is meticulously designed with user-friendly navigation, providing a visually captivating interface for an enjoyable and hassle-free shopping experience. Whether you're seeking the latest bestseller or a hidden gem, our personalized recommendations and comprehensive information cater to your unique literary preferences, making every purchase a delight.

Browse through a curated selection of books and comics, conveniently categorized for easy navigation. Discover new releases, explore timeless classics, and uncover exclusive offers and discounts tailored to your interests. With our mobile-friendly design, access your wishlist and cart from any device, ensuring a seamless shopping experience wherever you go.

Experience the satisfaction of finding the perfect book or comic, knowing that every purchase supports your passion for reading. Take advantage of exclusive discounts and promotions, including free delivery for orders above $50, ensuring that your literary treasures arrive at your doorstep without any extra cost.

Engage with fellow bookworms in our vibrant community, where you can share recommendations, leave reviews, and connect with like-minded readers. From lively discussions to insightful reviews, OwlBookstore fosters a sense of camaraderie among literary enthusiasts, enriching your reading journey in more ways than one.

OwlBookstore's E-commerce Platform is more than just a bookstore; it's a gateway to a world of literary wonders, where your love for books and comics flourishes. Join us in celebrating the magic of storytelling and indulge in the joy of discovering new adventures within a vibrant and thriving literary community. Happy reading!

### Project Goals

OwlBookstore endeavors to create a comprehensive and user-friendly e-commerce platform tailored to book and comic enthusiasts. The project focuses on:

- Enhanced User Experience: Provide a seamless and intuitive interface for browsing, purchasing, and engaging with a diverse selection of books and comics.

- Community Building: Foster an engaging community where users can interact, share recommendations, and participate in discussions related to their favorite literary works.

- Streamlined Shopping Experience: Simplify the process of finding and purchasing books and comics by offering personalized recommendations, exclusive discounts, and hassle-free checkout.

- Promote Literary Exploration: Encourage users to discover new authors, genres, and titles through curated collections, featured releases, and thematic promotions.

- Accessibility and Convenience: Prioritize accessibility by ensuring the platform is optimized for mobile devices, allowing users to browse, shop, and manage their accounts on the go.

By focusing on these project goals, OwlBookstore aims to create a vibrant and inclusive online community where readers can connect, explore, and celebrate the joy of literature.

### Agile Methodology

Agile Methodology served as the guiding framework for prioritizing and organizing tasks in the Chef's Helper app development process. The workflow included:

- User Story Creation: Utilizing the Agile approach, user stories were meticulously crafted, and a template was established to streamline the process. This allowed for a clear definition of project goals and user requirements.
- Epics Development: Epics, each containing potential user stories, were formulated. These epics served as overarching themes, providing a foundation for the subsequent development of the OwlBookstore e-commerce platform.
- Iterative Progression: User stories were generated by analyzing and refining the epics. Through iterative cycles, the project steadily advanced, ensuring that each user story contributed to the overall development goals.
- Public Project Board on Github: A Project Board, accessible to the public, was implemented on Github. This board acted as a centralized hub for task tracking, employing columns such as Todo, In Progress, and Done.
- Progress Tracking: The Project Board played a pivotal role in tracking the progression of tasks. Issues smoothly transitioned through the different columns, providing a visual representation of the project's status.
- Labeling for Priority: Labels were strategically added to categorize issues based on their importance. This labeling system facilitated a systematic organization of tasks, allowing the team to focus on critical aspects and prioritize accordingly.

In essence, the Agile Methodology, coupled with Github's Project Boards and a structured template for user stories and epics, ensured an efficient and collaborative approach to OwlBookstore's app development. This methodology allowed for flexibility, adaptability, and continuous improvement throughout the project lifecycle.

<details>
<summary> User Stories Template
</summary>

![User Stories, Template](/media/sreenshots_webp/user_story.webp)
</details>

<details>
<summary> User Stories, Issues
</summary>

![User Stories, Issues](/media/sreenshots_webp/issues.webp)
</details>

<details>
<summary> Project Milestones
</summary>

![Project Milestones](/media/sreenshots_webp/milestones.webp)
</details>

<details>
<summary> Project Board
</summary>

![Project Board](/media/sreenshots_webp/project_board.webp)

- <a href="https://github.com/users/ObiOne84/projects/5" target="_blank">Visit project GitHub page here.</a>

- <a href="https://github.com/users/ObiOne84/projects/5/views/1?layout=roadmap" target="_blank">Visit project GitHub roadmap here.</a>

</details>

### User Stories

#### Epics

- Product Viewing and Navigation
- Product Sorting and Searching
- Purchase and Checkout
- Admin and Store Management
- Registration and User Accounts

---

Finished here

---

#### User Stories

1. Project set up

    - Develop wireframes for the user interface of the application.
    - Design Entity-Relationship Diagrams (ERD).
    - Create a new Heroku application.
    - Link the Github repository to the Heroku app.

2. Site Navigation

    - Create a base.html file.
    - Create the Navigation tabs for the site header.
    - Create links for navigation tabs on each page.

3. Social network bar

    - Create the footer
    - Create a link for social sites on each page.

4. User Registration

    - Sign Up page.
    - User registration, log in, log out.
    - Display the users' name.

5. Manage recipes

    - Admin panel.
    - Crud functionality
    - Admin dashboard functionality.

6. Create drafts

    - Add ingredients in the admin panel to the recipe.
    - Recipe can be saved as a draft.

7. Approve reviews

    - Allow admin to approve reviews
    - Allow admin to create reviews through the admin panel

8. Review a recipe

    - Create a form to allow user review the recipe
    - Allow user to rate recipe only once

9. Like a recipe

    - Allow user to like recipe only once

10. View reviews

    - Allow users to view approved reviews.
    - Create a mechanism to calculate the average rating.

11. Add a recipe

    - Create a recipe form
    - Create a recipe template

12. Open a recipe

    - Create a recipe card template

13. Add an ingredient to the recipe

    - Create an ingredient form.

14. View likes

    - Display the like count next to the recipe.

15. Online recipe book

    - Add recipe content to the page.

16. Enhance Frontend Styling and Responsiveness

    - Create a home page.
    - Maintain consistent design.
    - Test responsiveness.

17. Readme file

    - Create comprehensive application's documentation.

Detailed look can be found on the [project board](https://github.com/users/ObiOne84/projects/4)

### Target Audience

- Home Cooks and Chefs: Individuals passionate about cooking, seeking a platform to store, manage, and share their recipes.
- Recipe Enthusiasts: Those who enjoy discovering and trying out new recipes, leaving reviews, and engaging with a culinary community.
- Tech-Savvy Foodies: Users who appreciate a seamless and user-friendly digital experience for managing their culinary creations.
- Mobile Users: Individuals who prefer the convenience of accessing recipe management tools from their mobile devices.
- Community-Driven Individuals: Those interested in engaging with a community of like-minded individuals, sharing culinary tips and inspiration.
- Culinary Creatives: Home cooks, aspiring chefs, and culinary artists looking for a platform to showcase their creativity.
- Families: Families who want to collect and manage their favourite recipes for shared meals and special occasions.
- Healthy Lifestyle Enthusiasts: Individuals interested in maintaining a healthy lifestyle through diverse and nutritious recipes.
Chef's Helper caters to a diverse audience of culinary enthusiasts, providing a hub for creativity, community, and culinary exploration.

### First time user

- Simple and intuitive website navigation for easy exploration and discovery.
- Engaging visuals showcasing the various dishes of public recipes.
- Informative content providing an overview of application functionality and future updates.
- Search bar, to allow user to find their favourite dishes.
- Easy Registration process.

### Registered User

- Seamless login process with a secure and personalized user account.
- Browsing recipe details.
- Printing.
- Adding new recipes.
- Updating own recipes.
- Reviewing, rating and liking recipes.

### Admin user

- Secure and separate login portal for admin users with appropriate access control.
- Access to an admin dashboard for recipes, reviews and ingredients.
- Ability to add, edit, or delete recipes, including ingredients, reviews and likes.
- Management of recipe options, such as adding, updating, or removing ingredients and reviews.
- Ability to delete user accounts, providing the necessary control for managing user data and accounts.
- Management of recipes, including the ability to view, modify, or delete recipes as needed.

## Design

The design of Chef's Helper platform is carefully crafted to provide a visually appealing and user-friendly experience. The design strikes a balance between simplicity and sophistication, ensuring a clean and modern appearance. The light blue background creates a harmonious backdrop for the culinary-focused content. The design emphasizes user interaction, with hover styles applied to key elements such as navigation, social links, and recipe cards. This provides users with a responsive and dynamic experience as they navigate through the platform. The consistent use of the color scheme, fonts, and styling elements across the platform creates a cohesive and unified visual identity. The design of Chef's Helper is tailored to appeal to users seeking a seamless and visually delightful experience while exploring and managing their recipes.

### Color Scheme

- The predominant color is a soothing light blue background ![#cff4fc](https://placehold.co/15x15/cff4fc/cff4fc.png) `#cff4fc` , creating a calm and inviting atmosphere for users.

- The CH logo is elegantly presented in gold letters ![#dfb705](https://placehold.co/15x15/dfb705/dfb705.png) `#dfb705`, adding a touch of sophistication to the overall design.

- The font choice is a classic black ![#000](https://placehold.co/15x15/000/000.png) `#000`, ensuring readability and a timeless aesthetic.

- Navigation elements, including the nav bar and social links, are designed to respond dynamically to user interaction. On hover, the color transitions to a rich burgundy ![#630a0a](https://placehold.co/15x15/630a0a/630a0a.png) `#630a0a`, providing visual feedback.
Recipe Cards:

- Recipe cards are styled with a hover effect to enhance the user's interaction. On hover, the card scales slightly increasing the size for a subtle animation. Additionally, a drop shadow is applied ![#2759fc](https://placehold.co/15x15/2759fc/2759fc.png) `#2759fc` to create depth and highlight the selected card.

### Recipe Images

- Various high-quality images of delectable foods are strategically placed to evoke the essence of culinary delight. These images contribute to an immersive and engaging visual experience. All recipe images were created using [Canva](https://www.canva.com/) software.

### Logo

- Logo was also created using [Canva](https://www.canva.com/) software.

### Typography

- Lato is a modern and versatile sans-serif font. With a clean and friendly appearance, it ensures readability across various platforms. Ideal for paragraphs and body text, Lato provides a contemporary and professional look.

- Roboto Slab is a serif font with a stylish and sophisticated feel. It adds a touch of elegance to headings and subheadings, making it suitable for conveying a sense of formality and structure in your design.

- Pacifico is a lively and casual cursive font that brings a playful and handwritten charm to your special text. Perfect for creating a personalized and whimsical touch, Pacifico adds character and warmth to headings or elements you want to highlight.

### Wireframes

<details>
<summary> Home Page
</summary>

![Home Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703345763/wireframe-home-page_qobymk.png)
</details>

<details>
<summary> User Sign Up Page
</summary>

![User Sign Up Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703345881/wireframe-registration-page_i3wdcc.png)
</details>

<details>
<summary> User Login Page
</summary>

![User Login Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703414612/django-project/login-page_w7ktsc.webp)
</details>

<details>
<summary> Add Recipe Page / Update Recipe Page
</summary>

![Add and Update Recipe Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703346206/wireframe-add-recipe_qj9ury.png)
</details>

<details>
<summary> Recipe Detail View Page
</summary>

![Recipe Detail View Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703346404/wireframe-recipe-view_qjkzsd.png)
</details>

<details>
<summary> Recipe Images Page
</summary>

![Recipe Images Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703346478/wireframe-recipes-page_ovghpm.png)
</details>

### Database Scheme

Entity Relationship Diagram (ERD)

> The current data scheme comprises models essential for the Minimum Viable Product (MVP) of the recipe management system. However, future updates are planned to enhance the application's functionality. The upcoming features include the addition of Categories to recipes, enabling users to better organize and filter recipes by category and allergens. This enhancement ensures that the system accommodates dietary needs and provides nutritional information for each ingredient and meal created using the recipes.
>
> In subsequent phases, the system will introduce a Supplier model to transform the application into a comprehensive tool for the hospitality sector. This addition will facilitate inventory management, catering to the specific needs of commercial users. The planned updates align with a strategic roadmap, progressively expanding the capabilities of the recipe management system to meet evolving user requirements and industry demands.

<details>
<summary> Data Scheme
</summary>

![Data Scheme](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703347474/Database_ER_diagram_crow_s_foot_-_Database_ER_diagram_crow_s_foot_bowogm.png)
</details>

### Data Models

1. Allauth User Model

    - Django Allauth is a third-party Django package that provides a set of authentication, registration, and account management functionality for Django web applications. It's designed to handle various aspects of user authentication, including login, registration, and more.
    - Django Allauth provides the default User model for authentication within the recipe management system.
    - The User etnity has one-to-many relationship with the Recipe entity, allowing each User to create a multiple recipes. Also, each individual recipe is associated with only one User, this means that users can create and manage their own collection of recipes, and each recipe is attributed to a specific user..

2. Recipe Model

    - The Recipe model in the system represents a culinary recipe and encapsulates various attributes, including the recipe's title, author, creation/update timestamps, instructions, ingredients, featured image, and additional details related to preparation and user interactions.

    - Fields:
    - title: CharField for the title of the recipe, ensuring uniqueness.
    - slug: SlugField for a URL-friendly version of the title.
    - author: ForeignKey to the User model, establishing a many-to-one relationship.
    - created_on: DateTimeField for the creation timestamp.
    - updated_on: DateTimeField for the last update timestamp.
    - instructions: TextField for the detailed recipe instructions.
    - ingredients: ManyToManyField to the RecipeIngredient model, forming a many-to-many relationship.
    - featured_image: CloudinaryField for storing images, with a default placeholder image.
    - excerpt: TextField for a brief description or summary (optional).
    - likes: ManyToManyField to the User model, allowing users to express their liking for a recipe.
    - prep_time: IntegerField for the preparation time in minutes (optional).
    - cook_time: IntegerField for the cooking time in minutes (optional).
    - servings: IntegerField for the default number of servings.
    - rating: FloatField for the overall rating, constrained between 1 and 5.
    - total_ratings: IntegerField for the total number of ratings.
    - status: IntegerField with choices representing the status of the recipe (Draft or Published).
    - rated_users: ManyToManyField to the User model, tracking users who have rated the recipe.
    - sum_of_rating: FloatField for the cumulative sum of all ratings.

    - Meta specifies the default ordering based on the recipe title in descending order.

    - Methods:
    - `__str__(self):` Returns the title of the recipe when converted to a string.
    - `number_of_likes(self):` Returns the count of likes for the recipe.
    - `number_of_reviews(self):` Returns the count of reviews for the recipe.
    - `rate_recipe(self, user, user_rating):` Records a user's rating for the recipe, updating the total rating and user rating history.
    - `calculate_average_rating(self):` Calculates and returns the average rating for the recipe.
    - `has_unapproved_reviews(self):` Checks if there are unapproved reviews for the recipe.
    - Custom save method to create a unique slug for each recipe, ensuring a URL-friendly representation.

    - This model empowers the system to manage and present a diverse array of recipes, supporting interactions such as liking, rating, and reviewing. The inclusion of features like unique slugs and status tracking enhances the robustness of the recipe management system.

3. RecipeIngredient Model

    - The RecipeIngredient model represents an individual ingredient used in a recipe. It encapsulates information such as the ingredient's name, quantity, unit of measurement, and the recipe to which it belongs.

    - Fields:
    - name: CharField for the name of the ingredient.
    - quantity: DecimalField for the quantity of the ingredient.
    - unit: CharField for the unit of measurement.
    - recipe: ForeignKey to the Recipe model, establishing a many-to-one relationship.

    - This model serves as a crucial component in the recipe system, allowing for the detailed specification of each ingredient within a recipe. The ForeignKey establishes a link to the associated recipe, facilitating the organization and retrieval of ingredient information when needed. The `__str__` method provides a readable string representation for ease of use and display.

4. Review Model

    - The Review model represents user reviews for a specific recipe within the recipe management system. It includes essential details such as the reviewer's name, email, the content of the review, creation timestamp, and approval status.

    - Fields:

    - recipe: ForeignKey to the Recipe model, establishing a many-to-one relationship.
    - name: CharField for the name of the reviewer.
    - email: EmailField for the email of the reviewer.
    - body: TextField for the content of the review.
    - created_on: DateTimeField for the creation timestamp.
    - approved: BooleanField indicating whether the review has been approved (default is False).

    - Meta specifies the default ordering based on the creation timestamp in ascending order.

    - This model plays a crucial role in collecting and managing user feedback for recipes. The ForeignKey establishes a link to the associated recipe, allowing for easy retrieval and organization of reviews. The approval status (approved) provides a mechanism to control the visibility of reviews, with the default set to False. The `__str__` method ensures a meaningful and readable representation of reviews when converted to a string. The ordering meta attribute ensures that reviews are sorted based on their creation timestamp.

---

### User Journey

![User Journey](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703352336/user-journey_qhdoqh.png)

## Security Features

### User Authentication

- Django Allauth is a powerful and comprehensive third-party package for handling authentication, registration, and account management in Django applications. It provides several security features to help protect user accounts and sensitive information.

### LoginRequiredMixin

- In Django, LoginRequiredMixin is a mixin class provided by the django.contrib.auth.mixins module. It is used in class-based views to require that the user making the request must be authenticated. If the user is not authenticated, the mixin will automatically redirect the user to the login page.

- You can use LoginRequiredMixin by inheriting it in your class-based views. Typically, it's used as the leftmost mixin in the inheritance chain to ensure that authentication checks are performed before any other mixins. If the user is authenticated, the view proceeds as normal. If the user is not authenticated, the LoginRequiredMixin automatically redirects them to the login page.

- Using LoginRequiredMixin helps in enforcing authentication requirements for views where you want to ensure that only authenticated users have access. It simplifies the process of handling authentication checks and redirects in class-based views.

### CSRF Protection

- In Django, CSRF (Cross-Site Request Forgery) protection is implemented using a CSRF token. The CSRF token is a unique value associated with a user's session, and it is used to verify the legitimacy of a form submission. When a user logs in or visits a page with a form, Django generates a unique CSRF token for that user's session. Django provides built-in middleware (django.middleware.csrf.CsrfViewMiddleware) that automatically checks and enforces CSRF protection for all incoming POST requests.
The middleware ensures that each form submission includes a valid CSRF token.
By incorporating these CSRF protection mechanisms, Django helps prevent attackers from executing malicious actions on behalf of authenticated users. The use of unique tokens tied to user sessions adds an additional layer of security, ensuring that form submissions are authorized and originate from legitimate sources.

- When rendering an HTML form, Django includes the CSRF token as a hidden input field within the form. The {% csrf_token %} template tag is used to include the CSRF token in the form. See example below:

```html
<form method="post" action="{% url 'custom_view' %}">
    {% csrf_token %}
    {% form.as_p %}

    <button type="submit">Submit</button>
</form>
```

### Custom Views Security Measures

- Overall, views incorporate authentication checks, form validation, and ownership verification to secure various operations. It's important to note that Django's built-in features, such as the authentication system, contribute to the overall security of the application.
RecipeList:

  - The RecipeDetails view requires authentication (LoginRequiredMixin) to access recipe details. It includes forms for adding reviews and ratings. Security measures include validating user input using Django forms (ReviewForm and RecipeForm), ensuring that only authenticated users can submit reviews and ratings.
  - The RecipeLike view handles user likes for a recipe. It toggles whether a user has liked a recipe. The security measure includes checking if the user is authenticated before allowing them to like or unlike a recipe.
  - The AddRecipeView view allows authenticated users to add new recipes. Security measures include using LoginRequiredMixin to ensure that only authenticated users can add recipes. It also validates user input using Django forms (AddRecipeForm and AddIngredientForm). The view handles both the recipe and its associated ingredients.
  - The UpdateRecipeView view allows authenticated users to update their recipes. It includes security measures such as using LoginRequiredMixin to ensure only authenticated users can update recipes and validating user input using forms (UpdateRecipeForm and AddIngredientForm). It checks if the user trying to update the recipe is the actual owner.
  - The DeleteRecipeView view allows authenticated users to delete their recipes. Security measures include using LoginRequiredMixin to ensure only authenticated users can delete recipes. It checks if the user trying to delete the recipe is the actual owner.

### Form Validation

- ReviewForm and RecipeForm is a basic form, and validation is handled by the default behavior of Django's ModelForm.

- AddIngredientForm uses Django form field types to ensure correct data types for name, quantity, and unit. Also, it specifies the available choices for the unit field and u tilizes attributes to control the appearance of form fields. Moreover, it sets specific constraints on the quantity field, limiting it to positive numbers and defining the maximum and minimum values. Uses the max_digits and decimal_places attributes for the quantity field to handle decimal precision.
AddRecipeForm and UpdateRecipeForm ensure that the title is unique using a custom clean_title method. Also, they set specific constraints on the prep_time, cook_time, and servings fields, limiting them to positive numbers and defining maximum and minimum values. Furthermore, validate the size of the featured_image to ensure it is no larger than 5 MB. Next, customizes the appearance and behavior of form fields using widget attributes. Finally, the form methods checks for the uniqueness of the recipe title to prevent duplicate entries.

## Features

- The home page contains a hero section, with the Join Now button, that allows unregistered users to go directly to the sign-up page. Also, the About section lists the main features of the application's future updates and invites users to register.
- The application consists of a comprehensive list of recipes.
- Users can sign up for an account and log in.
- Once logged in, the user can gain access to:
  - detailed recipe overview
  - add a new recipe
  - update own recipes
  - delete own recipes
  - like the recipes (all - only once, and can change)
  - rate the recipes (all - only once, and cannot change)
  - leave a review (all, unlimited times)
  - print a recipe
- User receives feedback upon completion of the above-listed actions.
- Average recipe rating is displayed for the user underneath the recipe image.
- Total number of likes is displayed for the user underneath the recipe image.
- Total number of reviews and approved reviews are displayed for each recipe, for registered users only.

### Existing Features

- Home Page
  - Displays a navigation bar with logo, main heading, hero section, about section, footer with social links.

![Home Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703355820/home-page_o8kxlx.png)

- Once logged in the Join Now button disappers.

![Logged in User Home Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703356009/django-project/home-page-logged_urehzy.png)

- Logo
  - Logo was also created using [Canva](https://www.canva.com/) software. It is the abbreviation of the Chef's Helper name.

    <details>
    <summary> Logo
    </summary>

    ![Logo](https://res.cloudinary.com/dcrbeonr9/image/upload/v1700595942/favicon_lr4ymg.ico)
    </details>

- Navigation Bar differs for visitors, and logged in users.

  - Navigation bar for a visitor

    <details>
    <summary> Navigation bar for website visitors.
    </summary>

    ![Visitor's Navigation Bar](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703358255/django-project/visitior-nav-bar_vj275d.png)
    </details>

  - Navigation bar for a user

    <details>
    <summary> Navigation bar for logged in users.
    </summary>

    ![User's Navigation Bar](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703414610/django-project/user-nav-bar_lofpwu.webp)
    </details>
  
    - Navigation bar for an admin

    <details>
    <summary> Navigation bar for logged in admin.
    </summary>

    ![Admin's Navigation Bar](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703523109/django-project/admin-navbar_tbgime.webp)
    </detai

- About Section
  - It contains a description of the main function of the application, and future updates.

    <details>
    <summary> About Us Section.
    </summary>

    ![About Us Section](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703358749/django-project/about-us_eusr88.png)
    </details>

- Footer
  - The website contains copyright information, creator details, and social links. The website includes links to the creator's LinkedIn and GitHub profiles. These links serve as a means for users to connect with the creator on professional and collaborative platforms.

    <details>
    <summary> Footer.
    </summary>

    ![About Us Section](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703361653/django-project/footer_jw6gu9.png)
    </details>

- Sign up Page
  - The user can sign up by providing a username, and password and repeating the password again. After successful sign-up, the user will be logged in and redirected to the home page.

    <details>
    <summary> Sign-up page.
    </summary>

    ![Sign Up](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703362666/django-project/sign-up-page_eni0dp.png)
    </details>

    <details>
    <summary> Success message, user logged in after sign-up completed.
    </summary>

    ![Login Message](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703414610/django-project/sign-up-message_pgtcri.webp)
    </details>

- Login Page
  - Once the user successfully completes signing up for the application, the user can safely log into their own account by providing a username and associated password.

    <details>
    <summary> Sign-in page.
    </summary>

    ![Sign In](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703414612/django-project/login-page_w7ktsc.webp)
    </details>

- Browse Available Recipes
  - Visitors, as well as logged-in users, have the ability to browse through our extensive collection of available recipes. The search functionality allows users to find specific recipes by providing either the complete name or a partial name. Each recipe is accompanied by essential information displayed under the recipe image or image placeholder. This information includes the recipe name, the author, the date when the recipe was added or last updated, the number of likes, and the average rating.

  - Additionally, when hovering over a recipe, users can access a short description (if provided), offering a glimpse into what makes each recipe special.

    <details>
    <summary> Recipes page.
    </summary>

    ![Recipes Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703364760/django-project/recipes-page-min_b2yo32.png)
    </details>

    <details>
    <summary> Search results.
    </summary>

    ![Search Results](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703414612/django-project/search-results_vogash.webp)
    </details>

    <details>
    <summary> Recipe description on hover.
    </summary>

    ![Recipe Description](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703365349/django-project/recipe-on-hover_snmqkw.png)
    </details>

- Recipe pagination
  - Recipes are displayed in four columns on large screens, two on medium, and one column on small. The application displays up to eight recipes per page.

    <details>
    <summary> Recipe pagination.
    </summary>

    ![Pagination](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703365689/django-project/pagination_pbqhs4.png)
    </details>

- Logged in User's taskbar
  - Authorised users benefit from a handy taskbar to easily print, add, edit and delete recipes.

    <details>
    <summary> Recipes page taskbar.
    </summary>

    ![Recipes page taskbar](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703414514/django-project/recipes-page-taskbar_u5chos.webp)
    </details>

    <details>
    <summary> Recipe View page taskbar.
    </summary>

    ![Recipe View page taskbar](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703414514/django-project/recipe-view-page-taskbar_xynpa5.webp)
    </details>

- Logout
  - Implementing a confirmation modal before logout ensures users consciously confirm their decision, minimizing accidental logouts. This user-friendly step prevents inadvertent actions, particularly in scenarios where logging out may lead to data loss or workflow disruption. The modal prompts users to confirm their logout choice, enhancing overall user experience by adding a deliberate confirmation step.

    <details>
    <summary> Logout confirmation modal.
    </summary>

    ![Logout Modal](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703416516/django-project/logout-modal_s1xpjm.webp)
    </details>

- Add a recipe
  - Users can create a new recipe by completing all mandatory fields on the "Add Recipe" form.
  - To save a recipe, users must fill in all required fields. They have the option to save the recipe as a draft or publish it.
  - The recipe title must be unique, and at least one cooking instruction, one ingredient, preparation time, cooking time, and the number of servings must be provided.
  - While the recipe description and image are optional, if a user does not provide an image, a standard image placeholder will be inserted.

    <details>
    <summary> Add Recipe page.
    </summary>

    ![Add Recipe Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703416733/django-project/add-recipe_smpc0c.webp)
    </details>

- Edit the recipe
  - Users can update their created recipe by filling in all mandatory fields on the "Update Recipe" form.
  - Similar to the "Add Recipe" page, users can add or remove additional instructions or ingredients during the update process.

    <details>
    <summary> Update Recipe page.
    </summary>

    ![Update Recipe Page](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703417609/django-project/edit-recipe_azyszp.webp)
    </details>

- Rate and review recipe
  - Users have the flexibility to contribute unlimited reviews for a recipe, fostering the exchange of tips and enabling engaging conversations. The inclusion of a rating system not only aids in identifying popular recipes but also enhances community engagement.
  - Ratings are mandatory and submitted alongside the review. Once a user rates a recipe, the rating becomes permanent, and the average rating is automatically recalculated. A confirmation message is provided upon the successful submission of the review.
  - Users can easily view the total number of reviews submitted for a recipe. In cases where there are pending reviews awaiting approval, an informational message is displayed to users, keeping them informed about the status of the reviews.

    <details>
    <summary> Review and rate recipe.
    </summary>

    ![Review and Rate Recipe](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703418351/django-project/reviews-and-rating_zjveby.webp)
    </details>

- Like the recipe and average rating.
  - Users have the option to express their appreciation for a recipe by clicking on the heart icon beneath the recipe image, toggling between like and unlike. The total number of likes is prominently displayed beside the heart icon.
  - Additionally, an average rating score is showcased beside the likes, accompanied by the total number of full-filled golden stars representing the rating. In instances where the average rating is below 0.5, a half-filled golden star is displayed, providing a visual representation of the recipe's overall rating.

    <details>
    <summary> Likes and average rating.
    </summary>

    ![Likes and Average Rating](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703418350/django-project/likes_and_average_rating_vdnklx.webp)
    </details>

- Print Recipe
  - Logged-in users have the capability to print recipes. The print view omits the review section and action buttons, streamlining the printed output for a focused and convenient recipe reference.

    <details>
    <summary> Print recipe.
    </summary>

    ![Print Recipe](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703419641/django-project/print-recipe_wpfk0n.webp)
    </details>

- Delete Recipe
  - Users have the ability to delete their own recipes. To mitigate the risk of accidental deletion, users are required to confirm the action before the deletion process is initiated. It's important to note that this action is irreversible, emphasizing the need for careful consideration before proceeding with the deletion.

    <details>
    <summary> Delete recipe.
    </summary>

    ![Delete Recipe](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703419937/django-project/delete-recipe_tfjos9.webp)
    </details>

- Admin Features
  - Django built in admin panel allows admin control over the website.
  - Admin can access admin panel through his navigation bar
  - Can add, update, delete recipes, ingredients.
  - Can approve reviews.
  - Can read, add, edit and delete users, email and manage social acccounts.

    <details>
    <summary> Admin panel.
    </summary>

    ![Admin Panel](https://res.cloudinary.com/dcrbeonr9/image/upload/v1703523440/django-project/admin-panel_xqgsan.webp)
    </details>

### Features Left to Implement

I. Feature Left to Implement with the next update:

- Shopping List Functionality - *Allow users to add ingredients directly to their shopping list from a recipe.*
Provide an interface for users to manage and view their shopping list.
- Cross-Off Steps and Ingredients - *Enable users to mark off completed steps and ingredients while following a recipe.*
- Dynamic Serving Size Adjustment -*Allow users to adjust the ingredient quantities for a recipe based on the desired number of servings.*
- Uploaded Recipe Image Preview - *Allow users to upload an image preview for their recipes, enhancing the visual appeal.*
- Image Cropping - *Implement image cropping functionality to enhance control over the appearance of uploaded images.*
- Allergen Information - *Include allergen information for each recipe, ensuring users are aware of potential allergens.*
- Recipe Categories - *Implement a categorization system for recipes, enabling better organization and filtering.*
- Nutritional Information - *Provide detailed nutritional information for each ingredient and the overall recipe.*
- Saved Ingredients Library - *Allow users to save and reuse ingredients, streamlining the recipe creation process.*

II. Transformation into Inventory Application:

- Supplier Management - *Enable users to add and manage suppliers for ingredients.*

- Ordering System - *Implement a system for creating and managing ingredient orders.*

- Order Tracking - *Allow users to send and receive orders, with tracking capabilities.*
- Stock Management - *Provide tools to update and monitor current stock levels.*
- Data Analytics - *Offer data analytics features to highlight stock numbers, usage patterns, and order trends.*
- Compatibility with POS Applications - *Ensure compatibility with popular Point of Sale (POS) applications used by restaurants and takeaways.*

By incorporating these features, Chef's Helper will not only enhance the user experience but also position itself as a versatile tool catering to both home cooks and the hospitality sector. The inclusion of advanced inventory management features and compatibility with POS systems will make it a comprehensive solution for the culinary industry.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used

- [ElephantSQL](https://www.elephantsql.com/) - Postgres database
- [Cloudinary](https://cloudinary.com/) - Online static file storage

### Frameworks Used

- [Django](https://www.djangoproject.com/) - Python framework. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source. (Source: [Django](https://www.djangoproject.com/))
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction//) - CSS framework. Bootstrap is a popular open-source front-end framework that provides a collection of tools, styles, and components to simplify the process of designing and building responsive and mobile-first web pages.
- [jQuery 3.7.1](https://code.jquery.com/jquery-3.7.1.js) - jQuery is a fast, small, and feature-rich JavaScript library. It simplifies things like HTML document traversal and manipulation, event handling, and animation for web development. jQuery is open-source and designed to make things like HTML document traversal and manipulation, event handling, and animation much simpler with an easy-to-use API that works across a multitude of browsers. (Source: [jQuery](https://api.jquery.com/))

### Programs Used

- [Github](https://github.com/) - Used for creating application repository, version control, organising workflow utilising agile functionality of GitHub project, issues and milestones.
- [Gitpod](https://www.gitpod.io/) - Used as a coding environment.
- [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
- [Canva](https://www.canva.com/) - Used to create logo, and recipe images.
- [Google Fonts](https://fonts.google.com/) - Used for the typography.
- [Figma](https://www.figma.com/) - Used for creation of wireframes.
- [Lucidchart](https://www.lucidchart.com/pages/) - Used for creation of ERD.
- [Am I Responsive](https://ui.dev/amiresponsive) - Used for obtaining screenshot of the application on various devices.
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine
- [Compress.png](https://compresspng.com/) - Used to reduce the size of images.
- [favicon.io](https://favicon.io/) - Used to convert images into icons.
- [JSHint](https://jshint.com/) - Used to validate JavaScript
- [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML
- [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python

## Deployment and Local Development

### Local Development

#### How to Fork

To fork the repository, follow the steps below:

1. Log in to your [GitHub](https://github.com).
2. Navigate to the repository for this project [Chef's Helper](https://github.com/ObiOne84/django-chefs-helper)
3. In the top right corner of the window, click on the Fork button.
4. The process will start, and you will see the message confirming the start.

Remember that if you forked the repository, none of the updates made to the source repo would be reflected in your forked repo.

#### How to Clone

To bring down project for local development, it is possible to clone a repository by following steps below:

1. Log in(or Sign Up) to [GitHub](https://github.com).
2. Navigate to the repository for this project [Chef's Helper](https://github.com/ObiOne84/django-chefs-helper)
3. Above the list of files, click the green button Code.
4. Select Local tab.
5. Copy to HTTPS code.
6. In your local IDE open terminal, choose the location where you want to clone the directory.
7. Type `git clone` and then paste the URL you copied from GitHub in step 5.
8. Set up a virtual environment (not required if you are using the Code Institute template and GitPod or Codeanywhere - this will be already set up).
9. Press Enter to create the clone.
10. Install packages by running command `pip3 install -r requirements.txt`

### ElephantSQL Database

1. Login to [ElephantSQL](https://www.elephantsql.com/) PostgreSQL Database.
2. Click Create New Instance.
3. Set up your plan:
    - give your plan name - commonly project name
    - select Tiny Turtle (Free) plan
    - you can leave the tags blank
4. Select the Region and data center near you.
5. Click Review.
6. Check your details are correct and then click Create instance.
7. Return to the ElephantSQL dashboard and click the database name you just created.
8. In the URL section, click and copy icon to copy the database URL (you will need this for your **env.py** file)

### Cloudinary

1. Visit [Cloudinary](https://cloudinary.com/) and click on Sing Up For Free.
2. Provide your name, email address and choose a password
3. For Primary interest, you can choose Programmable Media for image and video API
4. Optional: edit your assigned cloud name to something more memorable
5. Click Create Account
5. Verify your email and you will be brought to the dashboard
6. On your Cloudinary Dashboard, you can copy your API key.
7. Add `CLOUDINARY_URL` to **env.py** and Heroku app variables. Make sure that env.py is added to .gitignore to not share you security key.

### Heroku Deployment

* Log into [Heroku](https://www.heroku.com/) account or create an account.
- Click the "New" button at the top right corner and select "Create New App".
- Enter a unique application name
- Select your region
- Click "Create App"

#### Prepare enviroment and settings.py

* In your workspace (GitPod) create an **env.py** file and add it to **.gitignore**
- Add the **DATABASE_URL** value and your chosen **SECRET_KEY** value to the **env.py file**.
- Update the **settings.py** file to import the **env.py** file and add the SECRET-KEY and DATABASE_URL file paths.
    <details>
    <summary> See the code sample
    </summary>

    ```python
    from pathlib import Path
    import os
    import dj_database_url
    if os.path.isfile('env.py'):
        import env
    ```

    </details>

- Comment out the original DATABASES variable and add the code below.

    <details>
    <summary> See the code sample
    </summary>

    ```python
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #     }
    # }
        
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ```

    </details>

- Don't forget to makemigrations and migrate to update your database.
- Add the **CLOUDINARY_URL** to **env.py**
- Add cloudinary to **INSTALLED_APPS** in **settings.py**.

     <details>
    <summary> See the code sample
    </summary>

    ```python
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'blog',
    ]
    ```

    </details>

- Add cloudinary to the static files in settings.py

    <details>
    <summary> See the code sample
    </summary>

    ```python
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ```

    </details>

- Link the file to the templates directory in Heroku.
- Add TEMPLATES_DIR in settings.py

    <details>
    <summary> See the code sample
    </summary>

    ```python
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    ```

    </details>

- Change the templates directory to TEMPLATES_DIR

    <details>
    <summary> See the code sample
    </summary>

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [TEMPLATES_DIR],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

    </details>

- Add Heroku to the ALLOWED_HOSTS in settings.py

    <details>
    <summary> See the code sample
    </summary>

    ```python
    ALLOWED_HOSTS = [
    'your-app-name.herokuapp.com/',
    ]
    ```

    </details>

- Add the following Config Vars in Heroku:
  - `SECRET_KEY` (Any Django random secret key).
  - `CLOUDINARY_URL` (Insert your Cloudinary API key).
  - `PORT` = 8000.
  - `DISABLE_COLLECTSTATIC` = 1 (temporary and can be removed once static files are created).
  - `DATABASE_URL` (paste ElephantSQL database URL here).

- Heroku Additional Files:
  - Create requirements.txt
  - Create Procfile.

    <details>
    <summary> See the code sample (for gunicorn)
    </summary>

    ```python
    web: gunicorn codestar.wsgi
    ```

    </details>

#### Deploy

1. Before deployment change DEBUG = False in the settings.py, to prevent sharing sensitive information with the public.
2. Connect to GitHub in the deploy tab on Heroku app, and find your project repository.
3. At the bottom of the page you can choose Enable Automatic Deploys for automatic deployments or Deploy Branch to deploy manually. Keep in mind that manually deployed branches will need to be re-deployed after each time the GitHub repository is updated.
4. Click 'Open App' to view the deployed live site.

Site is now live

You can visit the deployed application at [Chef's Helper](https://django-chefs-helper-90ca65af05b0.herokuapp.com/)

## Testing

Please see  [TESTING.md](TESTING.md) for all the detailed testing performed.

## References

### Docs

- [jQuery](https://api.jquery.com/)
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Django docs](https://docs.djangoproject.com/en/5.0/)
- [Django Allauth](https://docs.allauth.org/en/latest/)
- [Stack Overflow](https://stackoverflow.com/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/)
- [GitHub Markdown Cheet Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Content

- [Canva](https://www.canva.com/) - all images for the recipes where created with the software utilising available templates and photos.
- [Woodland Whispers Retreat](https://github.com/Thomas-Tomo/woodland-whispers-retreat?tab=readme-ov-file#user-journey) - the structure of the readme file.

### Acknowledgements

- My sincere gratitude goes to my mentor, Mitko Bachvarov, for providing unwavering support and valuable feedback throughout the entire project.
- I extend my heartfelt thanks to my college colleagues for their invaluable feedback on the application, which has been instrumental in its development.