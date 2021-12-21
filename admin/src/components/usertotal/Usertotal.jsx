import {
  Button,
  Card,
  CardActions,
  CardContent,
  Typography,
} from "@mui/material";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../../config";

export default function UserTotal() {
  const [count, setcount] = useState(0);
  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_user_count", {
        secret_code: localStorage.getItem("secretCode"),
      })
      .then((res) => {
        setcount(res.data.count);
      });
  }, []);
  return (
    <Card>
      <CardContent>
        <Typography variant="h6" component="div">
          Total User Count
        </Typography>
        <span>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            Since Begin
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
            {count} Users
          </Typography>
        </span>
      </CardContent>
      <CardActions>
        <Link to="/users">
          <Button size="small">Learn More</Button>
        </Link>
      </CardActions>
    </Card>
  );
}
