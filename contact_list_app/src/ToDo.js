import React, { Component } from 'react';
import ToDoItem from './ToDoItem';

class ToDo extends Component {

	constructor(props) {
		super(props);

		this.state = {
			searchText: "",
			allItems: [],
			currentItems: [],
			text: "",
			cnt: 0,
			priority: 0,
			completed: [],
			isCompleted: false,
		};

		this.searchTextChanged = this.searchTextChanged.bind(this);
		this.searchButtonClicked = this.searchButtonClicked.bind(this);
		this.textChanged = this.textChanged.bind(this);
		this.priorityChanged = this.priorityChanged.bind(this);
    	this.addButtonClicked = this.addButtonClicked.bind(this);
    	this.deleteItem = this.deleteItem.bind(this);
        this.editItem = this.editItem.bind(this);
	}

	searchTextChanged(event){
	    this.setState({
	    	searchText: event.target.value 
	    });
	}

	searchButtonClicked(){

	    this.setState({
	    	currentItems: this.state.allItems.filter((item) => item.text.includes(this.state.searchText)).sort((a, b) => a.priority <= b.priority),
			text: "",
	    });
  	}

	textChanged(event) {
		this.setState({
			text: event.target.value
		});
	}

	priorityChanged(event) {
		this.setState({
			priority: event.target.value
		});
	}

	addButtonClicked(){

		// console.log("add");

		if(this.state.text === "") return;

		let toDoList = this.state.allItems;

		for(let i = 0; i < toDoList.length; ++i){
			if(toDoList[i].text === this.state.text && toDoList[i].priority === this.state.priority && toDoList[i].isCompleted === this.state.isCompleted) return;
		}

		toDoList.push(
			{
				"id": this.state.cnt,
				"text": this.state.text,
				"priority": this.state.priority,
				"isCompleted": false,
			}
		)

	    this.setState({
	    	searchText: "",
			allItems: toDoList.sort((a, b) => a.priority <= b.priority),
			currentItems: toDoList.sort((a, b) => a.priority <= b.priority),
			text: "",
			cnt: this.state.cnt + 1,
			priority: 0,
	    });
	}

	editItem(_cnt, _text, _priority){

		// console.log("editToDo\n");

		let allItems = this.state.allItems;
		let currentItems = this.state.currentItems;

		for(let i = 0; i < allItems.length; ++i){
			if(allItems[i].id === _cnt){
				allItems[i].text = _text;
				allItems[i].priority = _priority;
			}
		}

		for(let i = 0; i < currentItems.length; ++i){
			if(currentItems[i].id === _cnt){
				currentItems[i].text = _text;
				currentItems[i].priority = _priority;
			}
		}

		// console.log(allItems);

		allItems = allItems.sort((a, b) => a.priority <= b.priority);

		// console.log(allItems);
		currentItems = currentItems.sort((a, b) => a.priority <= b.priority);

		this.setState({
			"allItems": allItems,
			"currentItems": currentItems,
		})

	}

	deleteItem(_cnt){

		console.log("deleteToDo");
		// console.log(_cnt);

		let completed = this.state.completed;
		let currentItems = this.state.currentItems;

		for(let i = 0; i < currentItems.length; ++i){
			if(currentItems[i].id === _cnt){
				currentItems[i].isCompleted = true;
				completed.push(currentItems[i]);
			}
		}
	    this.setState({
	    	currentItems: this.state.currentItems.filter((item) => item.id !== _cnt),
	    	allItems: this.state.allItems.filter((item) => item.id !== _cnt),
	    	completed: completed,
	    });
	}

	render() {

		let toDoList = this.state.currentItems
		.sort((a, b) => a.priority <= b.priority)
		.map((item) => (
			<ToDoItem key = {item.id} item = {item}
				deleteItem = {() => this.deleteItem(item.id)}
				editItem = {this.editItem} />
		));

		let completed = this.state.completed
		.map((item) => (
			<ToDoItem key = {item.id} item = {item}
				deleteItem = {() => this.deleteItem(item.id)}
				editItem = {this.editItem} />
		));

		return (
			<div>
				<div>
					<input placeholder="Search" value={this.state.searchText} onChange={this.searchTextChanged} />
					<input type="button" value = "Search" onClick={this.searchButtonClicked}/>
				</div>
				<div>
					<input type="text" placeholder="ToDo" value={this.state.text} onChange={this.textChanged}/>
					<input type="number" placeholder="Priority" value={this.state.priority} onChange={this.priorityChanged}/>
					<input type="button" value = "Add" onClick={this.addButtonClicked}/>
				</div>
				<hr/>
				<h5>ToDo:</h5>
				<ul>
					{toDoList}
				</ul>
				<h5>Completed:</h5>
				<ul>
					{completed}
				</ul>
			</div>
		)
	}
}

export default ToDo;