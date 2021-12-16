import { styled, Container, Grid } from "@mui/material";
import React from "react";
import Chart from "../components/chart/Chart";
import FeaturedInfo from "../components/featuredInfo/FeaturedInfo";

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
          <FeaturedInfo></FeaturedInfo>
        </Grid>
        <Grid item sm={4}>
          <FeaturedInfo></FeaturedInfo>
        </Grid>
        <Grid item sm={4}>
          <FeaturedInfo></FeaturedInfo>
        </Grid>
      </CustomGrid>
      <CustomGrid>
        <Chart />
      </CustomGrid>
      <CustomGrid>
        <Chart />
      </CustomGrid>
    </CustomContainer>
  );
}

export default Homepage;
