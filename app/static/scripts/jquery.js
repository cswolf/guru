$(function() {

	$(".addButton").click(function() {
		var searchTerm = $(".searchInput").val();
    if (!searchTerm) {
      alert('Please enter some text before adding a department or course.');
      return;
    }
    searchTerm = searchTerm.replace(" ", "");
    var invalidLength = searchTerm.length != 7;
    if (invalidLength) {
    	alert('Please enter a valid 7-character course code (e.g. CPSC110).');
    	return;
    }
    var course = searchTerm.slice(0,4);
    var number = searchTerm.slice(4);
    console.log(course);
    console.log(number);
    $.ajax({
    	url: "search/?course="+course+"&number="+number,
    	type: "GET",
    	success: function (data) {
    		alert("hey");
    	},
      error: function (xhr, errmsg, err) {
        alert("yo");
      }
    });
	});
  
  // $(".searchType div").click(function() {
  //   if (!$(this).hasClass("selected")) {
  //     $(".searchType div").toggleClass("selected");
  //   }
  // });

});
