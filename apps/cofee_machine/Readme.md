## Coffee Machine Simulator App

> This django app simulates an automatic coffee machine. It allows users to customize their coffee preferences and produces a string representation of the resulting coffee based on their choices.

### The virtual coffee machine application includes the following features:

## Gathering user input for the following choices:

>- Whether to add milk or not
>- The strength of the coffee (1, 2, or 3)
>- Whether to froth the milk or not

# Internal management of ingredients stored in containers within the virtual coffee machine:
>- Milk (250ml)
>- Water (750ml)
>- Coffee beans (250g)

>Combining all the ingredients in a virtual coffee cup (200ml) before reporting successful completion of a fresh cup of coffee.

## Changes for Adding Tea Option

In the event that the manufacturer of the virtual coffee machine decides to include tea as an option, the following changes would be required:

>- Modify the user input gathering to include an additional choice for selecting coffee or tea.
>- Update the ingredient management system to include containers for tea leaves and hot water.
>- Adjust the logic for generating the string representation of the resulting beverage to account for tea-specific parameters such as steeping time, infusion strength, etc.



### How to Use the App

To use the app, follow these steps:

> - Access [page] (http://localhost:8000/coffee/order) here 
> - Select how much strength from 1 to the
> - You can add milk
> - You can froth the milk


### Assumptions and Constraints
While building the application:

> - I assemed that I just put togther different combinations of strings depending on the user input, keeping track didn't matter
> - I thought the user interface for the virtual coffee machine doesn't have to be an html page. I thought to just write a python console app
> - The application assumes a single user operating the coffee machine at a time.

### Collaboration and Team Thought Implementation

The design of this application supports team collaboration on the program implementation through:

> - Encapsulation: The code is organized into classes and functions, making it modular and allowing team members to work on different components independently.

> - Clear Separation of Concerns: The application is structured into logical components such as forms, views, and models, making it easier for team members to focus on specific areas of the application.

> - Documentation: The inclusion of docstrings and comments in the code helps team members understand the purpose and functionality of each component, facilitating collaboration and troubleshooting.

### Future Features

Some potential future features that could be added to enhance the coffee machine simulator app include

> - Multiple user support: Allow multiple users to place orders and track their preferences separately
> - Customizable cup size: Enable users to choose their desired cup size.
> - Ingredient management: Implement a feature to track ingredient levels, 
> - User profiles: Allow users to create profiles and save their favorite coffee preferences for easy ordering in the future.

### Conclusion

> The coffee machine simulator app provides a simulated experience of an automatic coffee machine, allowing users to customize their coffee preferences and generating a string representation of the resulting coffee.The application's design supports team collaboration by employing modular code organization, clear separation of concerns, version control, and documentation. With potential future features and enhancements, the coffee machine simulator app can provide an even more immersive and customizable user experience.