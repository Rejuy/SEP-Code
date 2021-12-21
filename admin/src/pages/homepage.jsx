import { styled, Container, Grid } from "@mui/material";
import React from "react";
import UserChangePlot from "../components/userChangePlot/UserchangePlot";
import UserChange from "../components/userchange/Userchange";
import Timeonline from "../components/timeOnline/Timeonline";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: "100vh",
}));

const CustomGrid = styled(Grid)(({ theme }) => ({
  marginBottom: theme.spacing(5),
}));

function Homepage() {
  return (
    <CustomContainer>
      <CustomGrid container spacing={4}>
        <Grid item sm={4}>
          <UserChange></UserChange>
        </Grid>
        <Grid item sm={4}>
          <Timeonline />
        </Grid>
        <Grid item sm={4}>
          <UserChange />
        </Grid>
      </CustomGrid>
      <CustomGrid>
        <UserChangePlot />
      </CustomGrid>
    </CustomContainer>
  );
}

export default Homepage;
