// Mock data kept here for now
var searchTerms = [];
var results = [ {"code": "COGS 300: Understanding and Designing Cognitive Systems",
                  "url": "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=3&dept=COGS&course=300",
                  "desc": "Theory and methods for integrating diverse disciplinary content in cognitive systems."},
                {"code": "COGS 303: Research Methods in Cognitive Systems",
                  "url": "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=3&dept=COGS&course=303",
                  "desc": "Examination and comparison of the research methodologies of different disciplines relevant to cognitive systems."},
                {"code": "COGS 401: Seminar in Cognitive Systems",
                  "url": "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=3&dept=COGS&course=401",
                  "desc": "Interdisciplinary seminar integrating theory, methods, and current research topics."},
                {"code": "PSYC 309: Cognitive Processes",
                  "url": "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=3&dept=PSYC&course=309A",
                  "desc": "Contribution of cognitive processes to perception, attention, and memory; cognitive development, language, thinking, and creativity."},
                {"code": "CPSC 322: Introduction to Artificial Intelligence",
                  "url": "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=3&dept=CPSC&course=322",
                  "desc": "Problem-solving and planning; state/action models and graph searching. Natural language understanding Computational vision. Applications of artificial intelligence."}
                  ];

// Search Bar
// var SearchBar = React.createClass({
//   addSearchTerm: function() {
//     var searchTerm = $(".searchInput").val();
//     if (!searchTerm) {
//       alert('Please enter some text before adding a department or course.');
//       return;
//     }
//     searchTerms.push(searchTerm);
//     console.log(searchTerms);
//     $(".searchInput").val('');
//     React.render(
//       <SearchTermList />,
//       document.getElementById('searchTerms')
//     );
//   },
//   render: function() {
//     return (
//       <div className="searchBar">
//         <input className="searchInput" type="text" placeholder="..." />
//         <div className="addButton" /*onClick={this.addSearchTerm}*/>
//           <p>go</p>
//         </div>
//       </div>
//     );
//   }
// });

// React.render(
//   <SearchBar />,
//   document.getElementById('searchBar')
// );

// Search Terms
var SearchTermList = React.createClass({
  showResults: function() {
    React.render(
      <ResultList />,
      document.getElementById('results')
    );
  },
  render: function() {
    var searchTermNodes = searchTerms.map(function (searchTerm) {
      return (
        <SearchTerm course={searchTerm}></SearchTerm>
      );
    });
    
    return (
      <div className="searchTerms">
        <div className="searchTermList">
          {searchTermNodes}
        </div>
        <div className="goButton" onClick={this.showResults}>
          <p>Go</p>
        </div>
      </div>
    );
  }
});

var SearchTerm = React.createClass({
  render: function() {
    return (
      <div className="searchTerm">
        + {this.props.course}
      </div>
    );
  }
});

React.render(
  <SearchTermList />,
  document.getElementById('searchTerms')
);

// Results
var ResultList = React.createClass({
  render: function() {
    var resultNodes = results.map(function (result) {
      return (
        <Result code={result.code} url={result.url} desc={result.desc}></Result>
      );
    });

    return (
      <div className="resultList">
        {resultNodes}
      </div>
    );
  }
});

var Result = React.createClass({
  render: function() {
    return (
      <div className="result">
        <h4>{this.props.code} (<a href={this.props.url}>SSC</a>)</h4>
        <p>{this.props.desc}</p>
      </div>
    );
  }
});
