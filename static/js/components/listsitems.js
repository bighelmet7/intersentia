import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import FastFoodIcon from '@material-ui/icons/Fastfood';
import RestaurantIcon from '@material-ui/icons/Restaurant';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import GroupIcon from '@material-ui/icons/Group';
import AssignmentIcon from '@material-ui/icons/Assignment';
import { NavLink as Nav } from 'react-router-dom';

export const mainListItems = (
  <div>
    <Nav to="/shop-day/">
      <ListItem button>
        <ListItemIcon>
            <ShoppingCartIcon />
        </ListItemIcon>
          <ListItemText primary="Shop Day" />
      </ListItem>
    </Nav>
    <Nav to="/bars/">
      <ListItem button>
        <ListItemIcon>
            <RestaurantIcon />
        </ListItemIcon>
          <ListItemText primary="Bars" />
      </ListItem>
    </Nav>
    <Nav to="/sandwiches/">
      <ListItem button>
        <ListItemIcon>
          <FastFoodIcon />
        </ListItemIcon>
          <ListItemText primary="Sandwiches" />
      </ListItem>
    </Nav>
    <Nav to="/users/">
      <ListItem button>
        <ListItemIcon>
          <GroupIcon />
        </ListItemIcon>
          <ListItemText primary="Users" />
      </ListItem>
    </Nav>
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