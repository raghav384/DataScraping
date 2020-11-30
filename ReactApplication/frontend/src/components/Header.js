import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';

const useStyles = makeStyles((theme)=> ({
  AppBar:{
    backgroundColor:"green",
  },

  hero:{
    backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('http://www.pngall.com/wp-content/uploads/2/Medicine-Pills-Free-PNG.png')`,
    height: "500px",
    height: "500px",
    backgroundPosition: "center",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover",
    position: "relative",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    color: "#fff",
    fontSize: "4rem",
    },

   blogsContainer:{
    paddingTop: theme.spacing(3)
   },

   blogtitle:{
    fontWeight: 800,
    paddingBottom: theme.spacing(3)
   },
   card: {
    maxWidth: "100%",
  },
  media: {
    height: 240
  },
  cardActions: {
    display: "flex",
    margin: "0 10px",
    justifyContent: "space-between"
  },

  author: {
    display: "flex"
  },

  paginationContainer: {
    display: "flex",
    justifyContent: "center"
  }
}));


function Header() {

  const classes = useStyles();
  return (
    <div className="Header">
  <Box className={classes.hero}>
    <Box><h1>HealthScroll</h1></Box>  
  </Box>
    </div>
  );
}

export default Header;
