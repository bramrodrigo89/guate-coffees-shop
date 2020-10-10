$( document ).ready(function() {

    // Country Preselection when page loads
    var countryInput = $("#update-delivery-info-form").find(".select-dropdown");
    var countryPreSelected = $("#update-delivery-info-form").find(".select-dropdown").val();

    // Hidden ul list with country options 
    var countryList = $("#update-delivery-info-form").find(".dropdown-content");
    var allCountryOptions = countryList.children();

    // Color change when value is already preselected when page is loaded
    if(countryPreSelected !== "Please select") {
        countryInput.css("color", "black");
    } else {
        countryInput.css("color", "#d9d9d9");
    }

    // Color changes triggered when one option is selected from countries list 
    $(allCountryOptions).on("click", function(){
        var countrySelected = countryList.find(".selected").find("span").html();
        if(countrySelected !== "Please select") {
            $(countryInput).css("color", "black");
            $(countryInput).addClass("green-bottom-triggered");
        } else {
            $(countryInput).css("color", "#d9d9d9");
            $(countryInput).removeClass("green-bottom-triggered");
        }
    });
});