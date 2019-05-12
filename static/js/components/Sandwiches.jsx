import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import SimpleTable from './SimpleTable';

const styles = theme => ({
    root: {
      display: 'flex',
    },
    appBarSpacer: theme.mixins.toolbar,
    content: {
      flexGrow: 1,
      padding: theme.spacing.unit * 3,
      height: '100vh',
      overflow: 'auto',
    },
    chartContainer: {
      marginLeft: -22,
    },
    tableContainer: {
      height: 320,
    },
    h5: {
      marginBottom: theme.spacing.unit * 2,
    },
  });


class Sandwiches extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            isLoaded: false,
            err: null,
            data: [],
        }
    }

    componentDidMount() {
      let url = '/api/v1/bars/1/sandwiches/';
      fetch(url)
      .then(response => response.json())
      .then(
          (result) => {
              this.setState({isLoaded: true, data: result});
          },
          (err) => {
              this.setState({isLoaded: false, err: err});
          }
      )
    }

    render() {
        const { classes } = this.props;
        const { isLoaded, data } = this.state;
        return (
            <main className={classes.content}>
                <div className={classes.appBarSpacer} />
                <Typography variant="h4" gutterBottom component="h2">
                Sandwiches
                </Typography>
                <div className={classes.tableContainer}>
                    <Paper className={classes.root}>
                    {isLoaded ?            
                        <SimpleTable
                            name={"Sandwiches"}
                            cols={["name", "price"]}
                            data={data}
                        />
                        :
                        <div></div>
                    }
                    </Paper>
                </div>
            </main>
        );
    }
}

Sandwiches.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Sandwiches);
