import { Container, styled } from "@mui/material";
import React from "react";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: theme.spacing(75),
}));
export default function Analytics() {
  return <CustomContainer>Analytics</CustomContainer>;
}
