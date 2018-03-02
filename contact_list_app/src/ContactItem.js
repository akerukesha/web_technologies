import React, { Component } from 'react';

class ContactItem extends Component {

	constructor(props) {
        super(props);

        this.state = {
            "id": this.props.contact.id,
            "name": this.props.contact.name,
            "number": this.props.contact.number,
        }
    }

    render() {
        return (
            <div>
                <i class="fa fa-user"></i>
                <div>
                    <p>{this.props.contact.name}</p>
                    <p>{this.props.contact.number}</p>
                </div>
                <input type="button" value = "Delete" onClick = {this.props.deleteItem}/>
            </div>
        );
    }
}

export default ContactItem;