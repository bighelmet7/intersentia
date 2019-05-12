import React from 'react'
import MaterialTable from 'material-table'
import PropTypes from 'prop-types';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';

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

// TODO: AVOID HARDCODED URLS
class Sandwiches extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      columns: [
        { title: 'Name', field: 'name' },
        { title: 'Price', field: 'price' },
      ],
      data: [],
      isLoaded: false,
      err: null,
    }
  }

  componentDidMount() {
    let url = '/api/v1/bars/';
    fetch(url)
    .then(resp => resp.json())
    .then(
      (results) => {
        let res = [];
        let cols = this.state.columns;
        let template = {
          title: 'Bar',
          field: 'barId',
          lookup: {},
        }
        //TODO: BLOODY BAD PERFORMANCE O(n^2)
        for (let bar of results) {
          template.lookup[bar.id] = bar.name;
          for (let sandwich of bar.sandwiches) {
            res.push({
              id: sandwich.id,
              barId: bar.id,
              name: sandwich.name,
              price: sandwich.price
            })
          }
        }
        cols.push(template);
        this.setState({isLoaded: true, data: res, columns: cols});
      },
      (err) => {
        this.setState({isLoaded: true, err: err});
      }
    )
  }

  handleAdd = (data) => {
    let url = '/api/v1/bars/' + data.barId + '/sandwiches/';
    let params = {
      name: data.name,
      price: data.price
    }
    const searchParams = Object.keys(params).map((key) => {
      return encodeURIComponent(key) + '=' + encodeURIComponent(params[key]);
    }).join('&');
    fetch(url, {
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: searchParams
    })
    .then(resp => resp.json())
    .then(
      (result) => {
        const data = this.state.data;
        result['barId'] = data.barId;
        data.push(result);
        this.setState({ data });
      }
    )
  }

  handleDelete = (oldData) => {
    let url = '/api/v1/bars/' + oldData.barId + '/sandwiches/' + oldData.id + '/';
    fetch(url, {
      method: 'DELETE',
    })
    .then(resp => resp.json())
    .then(
      (result) => {
        let data = this.state.data;
        const index = data.indexOf(oldData);
        data.splice(index, 1);
        this.setState({ data });
      }
    )
  }

  handleUpdate = (newData, oldData) => {
    let url = '/api/v1/bars/' + oldData.barId + '/sandwiches/' + oldData.id + '/';
    let params = {
      name: newData.name,
      price: newData.price
    }
    const searchParams = Object.keys(params).map((key) => {
      return encodeURIComponent(key) + '=' + encodeURIComponent(params[key]);
    }).join('&');
    fetch(url, {
      method: 'PUT',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: searchParams
    })
    .then(resp => resp.json())
    .then(
      (result) => {
        const data = this.state.data;
        const index = data.indexOf(oldData);
        data[index] = newData;
        this.setState({ data });
      }
    )
  }

  render() {
    const { classes } = this.props;
    const { isLoaded } = this.state;
    return (
      <main className={classes.content}>
        <div className={classes.appBarSpacer} />
        <Typography variant="h4" gutterBottom component="h2">
        Sandwiches
        </Typography>
            {isLoaded ?
            <MaterialTable
              title="Sandwich Table"
              columns={this.state.columns}
              data={this.state.data}
              editable={{
                onRowAdd: newData =>
                  new Promise((resolve, reject) => {
                    setTimeout(() => {
                      {
                        this.handleAdd(newData);
                      }
                      resolve()
                    }, 1000)
                  }),
                onRowUpdate: (newData, oldData) =>
                  new Promise((resolve, reject) => {
                    setTimeout(() => {
                      {
                        this.handleUpdate(newData, oldData);
                      }
                      resolve()
                    }, 1000)
                  }),
                onRowDelete: oldData =>
                  new Promise((resolve, reject) => {
                    setTimeout(() => {
                      {
                        this.handleDelete(oldData);
                      }
                      resolve()
                    }, 1000)
                  }),
              }}
            />
            :
            <div></div>
            }
      </main>
    )
  }
}

Sandwiches.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Sandwiches);
