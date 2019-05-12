import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import ShopDay from './ShopDay';
import Bars from './Bars';
import Sandwiches from './Sandwiches';
import NavBar from './NavBar';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

const drawerWidth = 240;

const styles = theme => ({
  root: {
    display: 'flex',
  }
});

class App extends React.Component {

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        <CssBaseline />
        <NavBar />

        <Router>
          <Route path="/shop-day/" component={ShopDay} />
          <Route path="/bars/" component={Bars} />
          <Route path="/sandwiches/" component={Sandwiches} />
        </Router>
      </div>
    );
  }
}

App.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(App);
