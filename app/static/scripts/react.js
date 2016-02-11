// // Mock data kept here for now
// var searchTerms = [];
// var results = [ ["CPSC310", 25],
//                 ["MATH307", 20],
//                 ["GENE549", 15],
//                 ["CPSC317", 12],
//                 ["MATH302", 5] ];

// Search Bar
var SearchBar = React.createClass({
  getInitialState: function() {
    return {results: []};
  },
  addSearchTerm: function() {
    var searchTerm = $(".searchInput").val();
    if (!searchTerm) {
      alert('Please enter a course code (e.g. MATH307).');
      return;
    }
    searchTerm = searchTerm.replace(" ", "");
    var invalidLength = searchTerm.length != 7;
    if (invalidLength) {
      alert('Please enter a valid 7-character course code (e.g. MATH307).');
      return;
    }
    var course = searchTerm.slice(0,4);
    var number = searchTerm.slice(4);
    var excl = '0'
    if ($(".exBox").is(":checked")) {
      var excl = '1'
    }
    $.ajax({
      url: "search/?excl="+excl+"&course="+course+"&number="+number,
      type: "GET",
      dataType: "json",
      success: function (data) {
        // console.log(data["course"]);
        if (data["results"].length == 0) {
          alert("Your search returned 0 results. Try another course.");
        }
        if (data["results"][0] == -1) {
          alert("Oops! " + data["course"] + data["number"] + " is not a valid course code. Try another course.");
          this.setState({results: []});
        } else {
          this.setState({results: data["results"]});  
        }
        $(".searchInput").val(data["course"]+data["number"]);
      }.bind(this),
      error: function (xhr, errmsg, err) {
        alert(err);
      }
    });
  },
  handleKeyUp: function(e) {
    if (e.key === 'Enter') {
      this.addSearchTerm();
    }
  },
  render: function() {
    // console.log(this.state.results);
    return (
      <div className="searchBar">
        <input className="searchInput" type="text" placeholder="..." onKeyUp={this.handleKeyUp}/>
        <div className="addButton" onClick={this.addSearchTerm}>
          <p>go</p>
        </div>
        <div className="excludeCS">
          <input className="exBox" type="checkbox"/>
          <div className="exLabel">Exclude CPSC courses</div>
        </div>
        <ResultList results={this.state.results} />
      </div>
    );
  }
});

// Results
var ResultList = React.createClass({
  render: function() {
    var resultNodes = this.props.results.map(function (result) {
      var dept = result[0].replace(/[0-9]/g, '');
      var course = result[0].replace(/\D/g, '');
      var url = "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=3&dept="+dept+"&course="+course;
      return (
        <Result code={result[0]} url={url} count={result[1]}></Result>
      );
    });

    return (
      <div className="resultList">
        <div className="codeHeader">Course code</div>
        <div className="freqHeader">Cosine Similarity</div>
        {resultNodes}
      </div>
    );
  }
});

var Result = React.createClass({
  render: function() {
    var scoreBarWidth = this.props.count * 2000 - 1900;
    var scoreBarStyle = {
      height: "90%",
      width: scoreBarWidth + "px",
      float: "right",
      backgroundColor: "#00C4AA"
    };
    return (
      <div className="result">
        <h4>{this.props.code} &nbsp; (<a href={this.props.url} target="_blank">SSC</a>)</h4>
        <div className="scoreBar" style={scoreBarStyle}></div>
        <p>{this.props.count}</p>
      </div>
    );
  }
});

React.render(
  <SearchBar />,
  document.getElementById('searchBar')
);
