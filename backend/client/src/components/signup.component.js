import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class extends Component {
  render() {
    return (
      <div className="signin-container">
        <form className="form-signin" autocomplte="off" action="/sign-in" method="post">
          <h1>성공의 자세 🪑</h1>
          <h3>Posture of Success</h3>
          <input type="text" id="inputUsername" className="form-control" placeholder="Username" required="" autoFocus=""></input><br></br>
          <input type="email" id="inputEmail" className="form-control" placeholder="Email address" required=""></input><br></br>
          <input type="password" id="inputPassword" className="form-control" placeholder="Password" required=""></input><br></br>
          <button className="button primary-button" type="submit">Submit</button>
          <Link to="sign-in">
            <button className="button secondary-button" type="submit">Back</button>
          </Link>
        </form>
      </div>
    )
  }
}