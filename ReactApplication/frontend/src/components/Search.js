import './Search.css';
import axios from 'axios';
import Loader from '../loader.gif';
import {Component, Fragment} from 'react';


class Search extends Component {

	constructor(props) {
		super(props);

		this.state = {
			query: '',
			results: {},
			loading: false,
			message: '',
		};

		this.cancel = '';
	}

	fetchSearchResults = (query) => {
		const searchUrl = `http://localhost:8000/api/getdata/`+query;
		if (this.cancel) {
			this.cancel.cancel();
		}

		this.cancel = axios.CancelToken.source();

		axios.get(searchUrl, {
			cancelToken: this.cancel.token
		})
			.then(res => {
				this.setState({
					results: res.data,
					loading: false
				})
			})
			.catch(error => {
				if (axios.isCancel(error) || error) {
					this.setState({
						loading: false,
						message: 'Failed to fetch the data. Please check network'
					})
				}
			})
	};

	handleOnInputChange = (event) => {
		const query_value = event.target.value;
		this.setState({ query: query_value, message: '' });
	};

	searchAPI = (event) => {
		const query = this.state.query;
		this.fetchSearchResults(query);
	};

	renderSearchResults = () => {
		
		let results = Array.from(this.state.results);
		results = results.slice(1,5);
		console.log(results);
		const search_result = results.map((result, index) => {
			return (
				<div className="card" >
					<div className="card-body">
						<h1 className="card-title">{result._id.medicine_name}</h1>
						<h2 className="card-text">Medicine_Vendor : {result._id.vendor_name} </h2>
						<h2 className="card-text">Manufacturer: {result.medicine_manufacturer} </h2>
						<h4 className="card-text">Price = {result.medicine_price} </h4>
						<h5 className="card-text"><a href= {result.medicine_url}>Site URL </a> </h5>
					</div>
				</div>
			)
		})
		return(
			<div className = "col">
				{search_result}
    		</div>
		  )
	
	};

handleKeyPress(e) {
	if (e.key === 'Enter') {
		this.searchAPI();
	}
}
render() {
	const { query, loading, message } = this.state;

	return (
		<div className="container">
			{/*	Heading*/}
			<h2 className="heading">Search for Medicines for comparison</h2>
			{/* Search Input*/}
			<label className="search-label" htmlFor="search-input">
				<input
					type="text"
					name="query"
					value={query}
					id="search-input"
					placeholder="Enter the medicine name and press enter..."
					onChange={this.handleOnInputChange}
					onKeyUp={this.handleKeyPress.bind(this)}
				/>
				<i className="fa fa-search search-icon" aria-hidden="true" />
			</label>

			{/*	Error Message*/}
			{message && <p className="message">{message}</p>}

			{/*	Loader*/}
			<img src={Loader} className={`search-loading ${loading ? 'show' : 'hide'}`} alt="loader" />

        	<Fragment>
           	<div>
            {this.renderSearchResults()}
			
          	</div>
        	</Fragment>
    
			
		</div>
	)
}
}

export default Search