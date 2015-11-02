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
    $.ajax({
    	url: "search?course="+course+"&number="+number,
    	method: "GET",
    	success: function (data) {
    		alert("hey");
    	}
    });
	});
  
  // $(".searchType div").click(function() {
  //   if (!$(this).hasClass("selected")) {
  //     $(".searchType div").toggleClass("selected");
  //   }
  // });

});
