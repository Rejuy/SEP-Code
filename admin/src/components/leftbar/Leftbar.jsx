import {
  Person,
  Restaurant,
  School,
  Terrain,
  TrendingUp,
} from "@mui/icons-material";
import { Button, Container, styled, Typography } from "@mui/material";
import React from "react";
import { Link } from "react-router-dom";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  backgroundColor: theme.palette.primary.main,
  height: "100vh",
  width: "15%",
  color: "white",
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  position: "fixed",
}));

const Item = styled(Button)(({ theme }) => ({
  fontSize: "30px",
  color: "white",
  width: "100%",
  marginBottom: theme.spacing(3),
  paddingTop: theme.spacing(2),
  paddingBottom: theme.spacing(2),
}));

export default function Leftbar() {
  return (
    <CustomContainer>
      <Link to="/" style={{ width: "100%" }}>
        <Item size="large" startIcon={<TrendingUp />}>
          <Typography>Analytics</Typography>
        </Item>
      </Link>
      <Link to="/users" style={{ width: "100%" }}>
        <Item size="large" startIcon={<Person />}>
          <Typography>Users</Typography>
        </Item>
      </Link>
      <Link to="/courses" style={{ width: "100%" }}>
        <Item size="large" startIcon={<School />}>
          <Typography>Courses</Typography>
        </Item>
      </Link>
      <Link to="/foods" style={{ width: "100%" }}>
        <Item size="large" startIcon={<Restaurant />}>
          <Typography>Food</Typography>
        </Item>
      </Link>
      <Link to="/places" style={{ width: "100%" }}>
        <Item size="large" startIcon={<Terrain />}>
          <Typography>Places</Typography>
        </Item>
      </Link>
    </CustomContainer>
  );
}
