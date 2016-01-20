// Mock data kept here for now
var searchTerms = [];
var results = [ ["CPSC310", 25],
                ["MATH307", 20],
                ["GENE549", 15],
                ["CPSC317", 12],
                ["MATH302", 5] ];

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
    console.log(course);
    console.log(number);
    $.ajax({
      url: "search/?course="+course+"&number="+number,
      type: "GET",
      dataType: "json",
      success: function (data) {
        if (data["results"].length == 0) {
          alert('Your search returned 0 results. Try another course.');
        }
        this.setState({results: data["results"]});
        $(".searchInput").val(data["course"]+data["number"]);
      }.bind(this),
      error: function (xhr, errmsg, err) {
        alert(err);
      }
    });
  },
  render: function() {
    console.log(this.state.results);
    return (
      <div className="searchBar">
        <input className="searchInput" type="text" placeholder="..." />
        <div className="addButton" onClick={this.addSearchTerm}>
          <p>go</p>
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
      var url = "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=3&dept="+result[0].slice(0,4)+"&course="+result[0].slice(4);
      return (
        <Result code={result[0]} url={url} count={result[1]}></Result>
      );
    });

    return (
      <div className="resultList">
        <div className="codeHeader">Course code</div>
        <div className="freqHeader">Frequency</div>
        {resultNodes}
      </div>
    );
  }
});

var Result = React.createClass({
  render: function() {
    return (
      <div className="result">
        <h4>{this.props.code} &nbsp; (<a href={this.props.url}>SSC</a>)</h4>
        <p>{this.props.count}</p>
      </div>
    );
  }
});

React.render(
  <SearchBar />,
  document.getElementById('searchBar')
);
