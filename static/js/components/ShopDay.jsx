import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const drawerWidth = 240;

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


class ShopDay extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            isLoaded: false,
            err: null,
            data: [],
        }
    }

    // TODO: Added filter parameters to the URL ?is_shop_day=true, instead of
    // doing the searching here.
    componentDidMount() {
        let url = '/api/v1/bars/';
        fetch(url)
        .then(response => response.json())
        .then(
            (result) => {
                let shopDay = result.filter(bar => bar['is_shop_day'] == true)
                this.setState({isLoaded: true, data: shopDay});
            },
            (err) => {
                this.setState({isLoaded: false, err: err});
            }
        )

    }

    renderObj = (obj) => {
        let results = obj.map(o => {
            return o.name + ': ' + parseFloat(o.price) + ' €';
        });
        return results.join(', ');
    }

    render() {
        const { classes } = this.props;
        const { isLoaded, data } = this.state;
        return (
            <main className={classes.content}>
                <div className={classes.appBarSpacer} />
                <Typography variant="h4" gutterBottom component="h2">
                Shop of the day
                </Typography>
                <div className={classes.tableContainer}>
                    <Paper className={classes.root}>
                    {isLoaded ?            
                        <Table className={classes.table}>
                            <TableHead>
                            <TableRow>
                                <TableCell>Sandwich</TableCell>
                                <TableCell align="right">Price</TableCell>
                                <TableCell align="right">Toppings</TableCell>
                            </TableRow>
                            </TableHead>
                            <TableBody>
                            {data.map((bar, i) => {
                                return (
                                    bar.sandwiches.map((sandwich, j) => (
                                        <TableRow key={`bar_${i}_${j}`}>
                                        <TableCell component="th" scope="row">
                                            {sandwich.name}
                                        </TableCell>
                                        <TableCell align="right">{`${sandwich.price} €`}</TableCell>
                                        <TableCell align="right">{this.renderObj(sandwich.toppings)}</TableCell>
                                        </TableRow>
                                    ))
                                );
                            })}
                            </TableBody>
                        </Table>
                        :
                        <div></div>
                    }
                    </Paper>
                </div>
            </main>
        );
    }
}

ShopDay.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(ShopDay);
