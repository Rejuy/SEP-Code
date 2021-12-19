import {
  alpha,
  AppBar,
  Badge,
  IconButton,
  InputBase,
  styled,
  Toolbar,
  Typography,
} from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import React, { useState } from "react";
import { Mail, Settings } from "@mui/icons-material";
import { Link } from "react-router-dom";
import SettingsPage from "../../pages/settings";

const CustomToolbar = styled(Toolbar)(({ theme }) => ({
  display: "flex",
  justifyContent: "space-between",
}));

const Search = styled("div")(({ theme }) => ({
  backgroundColor: alpha(theme.palette.common.white, 0.15),
  "&:hover": {
    backgroundColor: alpha(theme.palette.common.white, 0.25),
  },
  display: "flex",
  alignItems: "center",
  padding: "0 10px",
  width: "35%",
}));

const CustomInput = styled(InputBase)(({ theme }) => ({
  color: "white",
  marginLeft: "5px",
  [theme.breakpoints.down("sm")]: {
    display: "none",
  },
}));

const CustomUser = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "space-evenly",
  width: "5%",
}));

const CustomLink = styled(Link)(({ theme }) => ({
  textDecoration: "none",
}));

export default function Navbar() {
  const [open, setOpen] = useState(false);

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <AppBar position="fixed">
      <CustomToolbar>
        <CustomLink to="/">
          <Typography
            variant="h6"
            style={{ display: "flex", alignItems: "center", color: "white" }}
          >
            Admin
          </Typography>
        </CustomLink>
        <Search>
          <SearchIcon></SearchIcon>
          <CustomInput placeholder="Search.."></CustomInput>
        </Search>
        <CustomUser>
          <IconButton
            onClick={() => {
              setOpen(true);
            }}
          >
            <Settings style={{ color: "white" }} />
          </IconButton>
          <IconButton>
            <Badge badgeContent={4} color="secondary">
              <Mail style={{ color: "white" }} />
            </Badge>
          </IconButton>
        </CustomUser>
      </CustomToolbar>
      <SettingsPage open={open} handleClose={handleClose} />
    </AppBar>
  );
}
