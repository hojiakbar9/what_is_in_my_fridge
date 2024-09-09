document.addEventListener("DOMContentLoaded", function() {
  // Get references to the input field, search button, and error message container
  var ingredientInput = document.getElementById("ingredientInput");
  var searchButton = document.getElementById("searchButton");
  var infoMessage = document.getElementById("infoMessage");

  // Add a click event listener to the search button
  searchButton.addEventListener("click", function(event) {
      // Get the user input from the input field
      var userInput = ingredientInput.value;
      
      // Check if the input is empty
      if (userInput === "") {
          // Show the error message container
          infoMessage.style.display = "block";
          event.preventDefault();
      } else {
          // Hide the error message container (if it's visible)
          infoMessage.style.display = "none";
          
          // Here you can proceed with your search functionality
          // For example, you can make an AJAX call to your Flask backend to retrieve recipes
          // Replace the code below with your actual functionality
      }
  });
});
