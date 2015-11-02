$(function() {
  
  $(".searchType div").click(function() {
    if (!$(this).hasClass("selected")) {
      $(".searchType div").toggleClass("selected");
    }
  });

});