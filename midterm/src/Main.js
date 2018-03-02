import React, { Component } from 'react';
import {
	BrowserRouter as Router,
	Route,
	Link
} from 'react-router-dom'
import Contact from './Contact';
import ToDo from './ToDo';
import Home from './Home';

class Main extends Component{

	render(){
		return (
			<Router>
				<div>
					<ul>
						<li><Link to="/">Home</Link></li>
						<li><Link to="/contact">Contact</Link></li>
						<li><Link to="/todo">ToDo</Link></li>
					</ul>

					<hr/>
						
					<Route exact path="/" component={Home}/>
					<Route path="/contact" component={Contact}/>
					<Route path="/todo" component={ToDo}/>
				</div>
			</Router>
		);
	}
}

export default Main;