var searchTerms = [];

var SearchTermList = React.createClass({
	render: function() {
		var searchTermNodes = this.props.map(function (searchTerm) {
			return (
				<SearchTerm course={searchTerm.course}></SearchTerm>
			);
		});
		
		return (
			<div class="searchTermList">
				{searchTermNodes}
			</div>
		);
	}
});

var SearchTerm = React.createClass({
	render: function() {
		return (
			<div class="searchTerm">
				{this.props.course}
			</div>
		);
	}
});

React.render(
  <CommentBox url="http://127.0.0.1:3000/" pollInterval={2000} />,
  document.getElementById('searchTerms')
);