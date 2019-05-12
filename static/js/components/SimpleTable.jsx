import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

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


class SimpleTable extends React.Component {

  render() {
      const { classes } = this.props;
      const { name, data, cols } = this.props;
      return (           
        <Table className={classes.table}>
            <TableHead>
            <TableRow>
                {cols.map((col, id) => (
                  <TableCell key={`col_${id}`}>{col}</TableCell>
                ))}
            </TableRow>
            </TableHead>
            <TableBody>
            {data.map(n => {
              return (
                <TableRow key={n.id}>
                    {cols.map((col, j) => (
                      <TableCell key={`${n.id}_${j}`}>{n[col]}</TableCell>
                    ))}
                </TableRow>
              );
            })}
            </TableBody>
        </Table>
      );
  }
}

SimpleTable.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SimpleTable);
