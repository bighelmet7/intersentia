import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import FastFoodIcon from '@material-ui/icons/Fastfood';
import RestaurantIcon from '@material-ui/icons/Restaurant';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import AssignmentIcon from '@material-ui/icons/Assignment';
import { Link } from "react-router-dom";

export const mainListItems = (
  <div>
    <ListItem button>
      <ListItemIcon>
          <ShoppingCartIcon />
      </ListItemIcon>
        <Link to="/shop-day">
          <ListItemText primary="Shop Day" />
        </Link>
    </ListItem>
    <ListItem button>
      <ListItemIcon>
          <RestaurantIcon />
      </ListItemIcon>
        <Link to="/bars">
          <ListItemText primary="Bars" />
        </Link>
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <FastFoodIcon />
      </ListItemIcon>
        <Link to="/sandwiches">
          <ListItemText primary="Sandwiches" />
        </Link>
    </ListItem>
  </div>
);

export const secondaryListItems = (
  <div>
    <ListSubheader inset>Saved reports</ListSubheader>
    <ListItem button>
      <ListItemIcon>
        <AssignmentIcon />
      </ListItemIcon>
      <ListItemText primary="Current month" />
    </ListItem>
  </div>
);