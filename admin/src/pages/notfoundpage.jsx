import { styled, Container, Typography } from "@mui/material";
import React from "react";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: "100vh",
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
