import { styled, Container, Grid, Typography } from "@mui/material";
import React from "react";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: "100vh",
}));

const CustomGrid = styled(Grid)(({ theme }) => ({
  marginBottom: theme.spacing(5),
}));

function NotFound() {
  return (
    <CustomContainer>
      <Typography
        variant="h2"
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-around",
        }}
      >
        Page Not Found
      </Typography>
    </CustomContainer>
  );
}

export default NotFound;
