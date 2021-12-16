import { ArrowUpward } from "@mui/icons-material";
import {
  Button,
  Card,
  CardActions,
  CardContent,
  Typography,
} from "@mui/material";
import React from "react";

export default function FeaturedInfo() {
  return (
    <Card>
      <CardContent>
        <Typography variant="h6" component="div">
          New User Count
        </Typography>
        <span>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            Since Last Month
          </Typography>
        </span>
        <span
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-evenly",
          }}
        >
          <Typography sx={{ fontSize: 30 }} color="text.primary" gutterBottom>
            +{20} Users
          </Typography>
          <span style={{ display: "flex", alignItems: "bottom" }}>
            <ArrowUpward color="success" />
            <Typography sx={{ mb: 1.5 }} color="text.secondary">
              +1.0%
            </Typography>
          </span>
        </span>
      </CardContent>
      <CardActions>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  );
}
