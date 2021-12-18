import {
  alpha,
  AppBar,
  Badge,
  InputBase,
  styled,
  Toolbar,
  Typography,
} from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import React from "react";
import { Mail, Settings } from "@mui/icons-material";

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

export default function Navbar() {
  return (
    <AppBar position="fixed">
      <CustomToolbar>
        <Typography
          variant="h6"
          style={{ display: "flex", alignItems: "center" }}
        >
          Admin
        </Typography>
        <Search>
          <SearchIcon></SearchIcon>
          <CustomInput placeholder="Search.."></CustomInput>
        </Search>
        <CustomUser>
          <Settings></Settings>
          <Badge badgeContent={4} color="secondary">
            <Mail></Mail>
          </Badge>
        </CustomUser>
      </CustomToolbar>
    </AppBar>
  );
}
