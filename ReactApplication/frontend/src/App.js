import React from 'react';
import Header from "./components/Header"
import Search from "./components/Search";
class App extends React.Component {
	render() {
		return (
			<div>
				<Header/>
				<Search/>
			</div>
		);
	}
}
export default App;